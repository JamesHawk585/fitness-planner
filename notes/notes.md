# Phase 3 Python Command Line Project 


- [Project Requirements](https://my.learn.co/courses/653/pages/phase-3-project-cli?module_item_id=95439)


### Phase 3 Project Requirements

In this project, we're going to use these skills to create a CLI. You won't be able to fit everything in from phase 3, but the following are the minimum requirements:

1. [x] A CLI application that solves a real-world problem and adheres to best practices.
    - Fitness Planner... 
2. [] A database created with SQLAlchemy
    [] Modified with SQLAlchemy ORM
    [] 2+ related tables.
3. [] A well-maintained virtual environment using Pipenv.
4. [?] Proper package structure in your application.
5. [] Use of lists and dicts.
6. [14] At least 50+ cimmits 

### Phase 3 Project Stretch Goals 

7. [] A database created and modified with SQLAlchemy ORM with 3+ related tables.
8. [] Use of many-to-many relationships with SQLAlchemy ORM.
9. [] Use of additional data structures, such as ranges and tuples.

### Project Rubric 

### Virtual Environment Setup
1. [x] Create an empty directory:
    - mkdir fitness-planner
2. [x] Create a virtual environment using your current Python version 
    - pipenv --python <python-version> 
3. [x] Install dependencies
    - [x] pipenv install alembic sqlalchemy
    - [x] pip install ipdb
4. Launch Virtual Environment
    - [x] pipenv shell
5. [] Initialize Migrations: run **alembic init migrations**
    - [] In the top level of your project directory, run alembic init migrations. This will generate a folder named migrations., You can change migrations to something else if you would like. In the Alembic documentation, they use alembic init alembic.  

# Configuration
Before we can use SQLAlchemy or alembic to create a database, we need to configure a couple of things first:

1. [] In the alembic.ini configuration file, we need to define the connection string for the SQLAlchemy engine.
    - Find the line (around 58) that says sqlalchemy.url
    - Set the value to sqlite:///name_of_your_db.db
        - Change name_of_your_db to a name that best suits the kind of date that you will be storing.
        - This also defines the path to the directory in which we want our db to be created.
2. [] In the migrations/env.py file, we need to define the target_metadata variable. Find the following lines of code in the migrations/env.py file:

# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = None

And change it to this:

from models import Base
target_metadata = Base.metadata                                                                  

### Explanation
from models import Base

We have not defined models or Base yet but, we will add the following code to the models.py file next:

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
This code defined the Base class that all of our models will inherit from. This gives alembic a way to know about the state of our schemas (models) and compare it to the DB. If there is a difference, alembic will detect those differences and generate the necessary script in the migration files to bring the DB in sync with the schema.
target_metadata = Base.metadata

The line target_metadata = Base.metadata sets the variable target_metadata to hold information about the database tables and structure defined in the SQLAlchemy models.
The metadata attribute of the Base class is like a record keeper that stores all the information about the model classes (tables) and their columns. It keeps track of what tables exist in the application and how they are structured.
So, when you write Base.metadata, you are referring to this record-keeping tool, and by setting target_metadata to it, you can use this information to manage and compare the database structure during migrations with Alembic.                                                                                
# Create a schema
Defining a schema
In the main directory, create a [models.py](http://models.py) file and add the following code from the code example in the docs:
from sqlalchemy.orm import declarative_base

Base = declarative_base()
declaritive_base - function that when invoked, returns a base class that our Python classes will inherit from
By inheriting from this class, we are establishing a connection between SQLAlchemy and our Python classes.
The Base class will store data about each class that inherits from it (Base.metadata)
Code demo
Creating a schema
Generate and run migrations

2023-08-07-sqlalchemy-alembic-migrations-and-virtual-env 
    - 1:06 from start of lecture 