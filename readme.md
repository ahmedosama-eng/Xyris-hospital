# Project Xyris HIS

## Overview

Project Xyris HIS (Hospital Information System) is designed to manage various hospital operations such as document ingestion, vectorization, database management, and data retrieval. The system integrates with OpenAI's embeddings and FAISS vector storage for efficient document search capabilities.

## Features

- *Data Ingestion and Processing*: Converts raw data from databases into a structured format suitable for further processing.
- *Vectorization*: Splits text data into manageable chunks and converts them into vector embeddings.
- *Database Management*: Handles operations related to database setup, connection, and data insertion.
- *Data Retrieval*: Retrieves vectorized data from storage, allowing for efficient search and retrieval operations.

## Modules

### Ingestion

Handles the ingestion and initial processing of data.

- *File*: app/ingestion/vectorization.py
- *Main Functions*:
  - doc_loader: Converts data into document format.
  - text_spliter: Splits text into smaller chunks.
  - create_Embeddings_and_vectordb: Creates embeddings and stores them in a FAISS database.
  - retrive_vectordb: Retrieves the vector database.

### Data

Manages database interactions and schema definitions.

- *Files*:
  - app/data/db_setup.py: Sets up the database and inserts data.
  - app/data/db_model.py: Defines the database schema and connection methods.

### Retrieval

Facilitates the retrieval of vectorized data for querying.

- *File*: app/retrieval/retrieval.py
- *Main Function*:
  - retrive_the_vector: Determines whether to retrieve or create new embeddings based on file existence.

## Setup and Installation

### Requirements

- Python 3.8+
- OpenAI API key
- FAISS
- SQLite
- Pandas

### Environment Setup

1. Clone the repository.
2. Install dependencies:
   bash
   pip install -r requirements.txt
   
3. Set up environment variables:
   - Ensure your OpenAI API key is set in your environment variables.
