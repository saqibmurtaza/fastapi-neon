How to Start a New Project with Python Poetry

1   poetry new project-name
2   cd project-name
3   poetry install
***Note:***
This create pyproject.toml & poetry.lock file. **Note-it** that it not install all dependencies. The easiest way is to cut & paste all necessary dependencies in pyproject.toml

**********************************************************
[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.110"
uvicorn = {extras = ["standard"], version = "^0.27.1"}
sqlmodel = "^0.0.16"
psycopg = {extras = ["binary"], version = "^3.1.18"}
pytest = "^8.0.2"
httpx = "^0.27.0"
*********************************************************
or from pyproject.toml of SirZia repository 05_microservices_all_in_one_platform/11_microservice_db
After cut & paste run the following command which installed all cut & paste dependencies and lock it in poetry.lock automatically

4   poetry update
5   Add poetry virtualenv interpreter in VSCode
***Note***
virtualenv interpreter: Remommended, Poetry, Global
select Poetry- which have your project name & unique hashtag
***************
Now start your project in virtualenv interpreter

6   Sign up for Neon DB and create a new project
    copy the connection string & paste it in .env file (must put .env file in gitignore)
    create Test Branch & copy the connection string & paste it in .env file

7   Files in Project folder   
        1   main.py
            Code steps:
                create todo class
                create connection string
                create engine
                crete function to create db & tables
                create decorator function 
                    @asynccontextmanager
            Main Part of the Code
                create instance of Fastapi class and assign it to variable app
                create function session
                create decorator functions for CURD (create,update,read,delete)
                    @app.get for root
                    @app.post
                    @app.get
                    @app.put
                    @app.delete
        2   settings.py
                - the file in which we describe connection url
poetry run pytest
poetry run uvicorn fastapi_neon.main:app
            
