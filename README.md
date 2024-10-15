# Blog API

This project is a RESTful API for a blogging platform built using **FastAPI**. The API allows users to register, log in, create blog posts, and view posts. It also includes authentication using JWT (JSON Web Tokens) for securing certain endpoints.

## Features

- **User Registration**: Create new user accounts.
- **User Login**: Authenticate users with JWT.
- **Post Creation**: Authenticated users can create blog posts.
- **Post Listing**: Fetch and list all posts with pagination.
- **Protected Endpoints**: Some endpoints require user authentication via JWT tokens.

---

## Table of Contents

- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Environment Variables](#environment-variables)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [License](#license)

---

## Installation

To get started with the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/blog-api.git
   cd blog-api

2. **Create Virtual Environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Setup Database:**
    - You need to configure the database connection URL in the .env file
    - Run the following to create the necessary database tables
    ```bash
    alembic upgrade head  # If you are using Alembic for migrations
5. **Run the Application**
    ```bash
    uvicorn app.main:app --reload

6. **Project Structure**
    ```
    blog-api/
    │
    ├── app/
    │   ├── __init__.py
    │   ├── models.py         # SQLAlchemy models
    │   ├── main.py           # Main FastAPI app
    │   ├── schemas.py        # Pydantic schemas
    │   ├── crud.py           # CRUD operations
    │   ├── auth.py           # Authentication utilities
    │   ├── database.py       # Database session management
    │
    ├── .env                  # Environment variables
    ├── alembic/              # Migrations folder (if using Alembic)
    ├── README.md             # Project readme
    ├── requirements.txt      # Python dependencies
    └── .venv/                # Virtual environment folder

