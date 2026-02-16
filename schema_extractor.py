import psycopg2
from typing import Dict, List

class SchemaExtractor:
    def __init__(self, connection_params: Dict):
        self.conn = psycopg2.connect(**connection_params)
        self.cursor = self.conn.cursor()
    
    def get_tables(self) -> List[str]:
        """Get all table names in the database."""
        query = """
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """
        self.cursor.execute(query)
        return [row[0] for row in self.cursor.fetchall()]
    
    def get_table_schema(self, table_name: str) -> Dict:
        """Get detailed schema for a specific table."""
        query = """
            SELECT 
                column_name,
                data_type,
                is_nullable,
                column_default
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position;
        """
        self.cursor.execute(query, (table_name,))
        columns = []
        
        for row in self.cursor.fetchall():
            columns.append({
                'name': row[0],
                'type': row[1],
                'nullable': row[2] == 'YES',
                'default': row[3]
            })
        
        # Get primary keys
        pk_query = """
            SELECT a.attname
            FROM pg_index i
            JOIN pg_attribute a ON a.attrelid = i.indrelid 
                AND a.attnum = ANY(i.indkey)
            WHERE i.indrelid = %s::regclass
            AND i.indisprimary;
        """
        self.cursor.execute(pk_query, (table_name,))
        primary_keys = [row[0] for row in self.cursor.fetchall()]
        
        return {
            'table_name': table_name,
            'columns': columns,
            'primary_keys': primary_keys
        }
    
    def get_foreign_keys(self, table_name: str) -> List[Dict]:
        """Get foreign key relationships."""
        query = """
            SELECT
                kcu.column_name,
                ccu.table_name AS foreign_table_name,
                ccu.column_name AS foreign_column_name
            FROM information_schema.table_constraints AS tc
            JOIN information_schema.key_column_usage AS kcu
                ON tc.constraint_name = kcu.constraint_name
            JOIN information_schema.constraint_column_usage AS ccu
                ON ccu.constraint_name = tc.constraint_name
            WHERE tc.constraint_type = 'FOREIGN KEY'
                AND tc.table_name = %s;
        """
        self.cursor.execute(query, (table_name,))
        
        return [{
            'column': row[0],
            'references_table': row[1],
            'references_column': row[2]
        } for row in self.cursor.fetchall()]
    
    def format_schema_for_llm(self) -> str:
        """Format the entire schema in a way the LLM can understand."""
        tables = self.get_tables()
        schema_description = "# Database Schema\n\n"
        
        for table in tables:
            schema = self.get_table_schema(table)
            fks = self.get_foreign_keys(table)
            
            schema_description += f"## Table: {table}\n"
            schema_description += "Columns:\n"
            
            for col in schema['columns']:
                pk_marker = " (PRIMARY KEY)" if col['name'] in schema['primary_keys'] else ""
                nullable = "NULL" if col['nullable'] else "NOT NULL"
                schema_description += f"- {col['name']}: {col['type']} {nullable}{pk_marker}\n"
            
            if fks:
                schema_description += "\nForeign Keys:\n"
                for fk in fks:
                    schema_description += f"- {fk['column']} → {fk['references_table']}.{fk['references_column']}\n"
            
            schema_description += "\n"
        
        return schema_description
    
    def close(self):
        """Close database connection."""
        self.cursor.close()
        self.conn.close()