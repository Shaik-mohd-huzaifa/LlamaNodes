# LlamaNodes

## Overview

LlamaNodes is a Django-based project designed to handle AI workflows with various services integrated into a streamlined structure. The project includes multiple services like LLM (Language Model) service, Lambda service, and database interaction, all modularized under different directories. The project allows you to create, fetch, and manage workflows by interacting with APIs like Together Inference for AI-powered applications.

## Project Structure

```
LlamaNodes/
│
├── backend/                       # Backend directory for the Django app
│   ├── WorxAI/                # Main app directory for LlamaNodes
│   │   ├── migrations/            # Database migrations folder
│   │   ├── __init__.py            # Initialization file for the LlamaNodes app
│   │   ├── admin.py               # Django admin interface for models
│   │   ├── apps.py                # Configuration of the app
│   │   ├── models.py              # Database models for the LlamaNodes app
│   │   ├── views.py               # Views for handling requests
│   │   ├── serializers.py         # Serializers to convert data to/from JSON
│   │   ├── services/              # Contains all the service logic like LLM, Lambda, etc.
│   │   │   ├── llm_service.py     # LLM service logic
│   │   │   ├── lambda_service.py  # Lambda service logic
│   │   │   └── ...                # Other services as required
│   │   ├── db/                    # Contains database-related modules
│   │   │   ├── config.py          # Database connection configuration
│   │   │   ├── schema.py          # Schema files for DB models
│   │   │   ├── actions/           # DB action functions (e.g., create, fetch)
│   │   │   │   ├── create.py      # Create action for database
│   │   │   │   ├── fetch.py       # Fetch action for database
│   │   │   │   └── ...            # Other DB actions
│   │   ├── utils/                 # Utility functions
│   │   │   ├── sorting_nodes.py   # Sorting nodes logic
│   │   │   └── call_nodes.py      # Logic to call nodes in a row
│   ├── settings.py                # Django settings file for configuration
│   └── urls.py                    # URL routing for the LlamaNodes app
│
├── manage.py                      # Django manage.py file to manage the project
├── requirements.txt               # List of dependencies for the project
└── README.md                      # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.11.0 or higher
- Django 4.0.0 or higher
- Virtual environment (recommended)

### 1. Install Dependencies

Make sure you have a virtual environment set up and then install the dependencies using:

```bash
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

In your `.env` file, add the following environment variables:

```
TOGETHER_INFERENCE_ENDPOINT="https://api.together.xyz/v1"
TOGETHER_INFERENC_API_KEY=YOUR_API_KEY
AWS_RDS_USER = YOUR_DB_USER_NAME
AWS_RDS_PASSWORD = # AWS RDS MySQL password
AWS_RDS_ENDPOINT = # AWS RDS endpoint (e.g., example.abcdefghij.us-west-2.rds.amazonaws.com)
AWS_RDS_PORT = 3306                     # MySQL default port
AWS_RDS_DATABASE = # Name of your RDS database
```

### 3. Apply Migrations

Run the following command to apply the database migrations:

```bash
python manage.py migrate
```

### 4. Start the Development Server

Run the development server with:

```bash
python manage.py runserver
```

The server should now be running at `http://127.0.0.1:8000/`.

### 5. Access the Application

You can access the application through the browser at the local URL above, and interact with the API endpoints defined in the `views.py` file.

## App Structure

### LlamaNodes App

- **services/**: Contains all the core services like LLM and Lambda services that interact with external APIs.
- **db/**: Manages all database interactions. This includes:
  - `config.py`: Contains the database connection logic.
  - `schema.py`: Defines the database schema (tables, fields, etc.).
  - `actions/`: Contains actions such as create, fetch, and update database records.
- **utils/**: Contains utility functions to manage node operations like sorting and calling nodes in a sequence.

### Settings

- **settings.py**: This file contains the project configuration like database settings, installed apps, middleware, etc.
- **urls.py**: Routes for handling incoming HTTP requests.

## How It Works

LlamaNodes integrates with external services to run AI workflows. When a request is made, the relevant services (LLM service, Lambda service) are invoked to perform tasks like:
- Fetching or creating workflow data
- Triggering Lambda functions
- Interacting with AI models (e.g., Together Inference API)

Each workflow, once created, is provided with a production-ready API endpoint that can be accessed from anywhere without needing to worry about the underlying infrastructure.

## Services

### LLM Service

The LLM service handles interactions with language models, allowing you to generate AI responses based on input data. This service utilizes the **Together Inference API** to perform the inference tasks.

### Lambda Service

The Lambda service allows you to trigger AWS Lambda functions within workflows. This service integrates seamlessly with AWS Lambda functions, making it easy to invoke serverless functions as part of your workflow.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes.
4. Push your changes and open a pull request.
