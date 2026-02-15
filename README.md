# SQL Query Generator using LLMs

> Transform natural language into SQL queries with the power of Large Language Models

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LLM: Claude/GPT](https://img.shields.io/badge/LLM-Claude%20%7C%20GPT-green.svg)](https://www.anthropic.com)

## Overview

A production-ready SQL query generator that converts natural language questions into accurate, safe SQL queries. Built with schema awareness, safety validation, and support for multiple LLM providers.

**Live Demo:** [Coming Soon]  
**Medium Article:** [Building a Simple SQL Query Generator Using LLMs](your-medium-link)

## Features

✅ **Natural Language to SQL** - Ask questions in plain English  
✅ **Schema-Aware** - Understands your database structure  
✅ **Safety First** - Validates queries before execution  
✅ **Multi-Provider** - Works with OpenAI, Anthropic, or local LLMs  
✅ **Multiple Dialects** - Supports PostgreSQL, MySQL, SQL Server  
✅ **Web Interface** - Simple Flask UI included  
✅ **Conversation Context** - Handles follow-up questions  

## Quick Start

### Prerequisites

- Python 3.8+
- PostgreSQL/MySQL/SQL Server database
- API key from OpenAI or Anthropic

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/sql-query-generator.git
cd sql-query-generator

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys and database credentials
```
