# Proof of Concept API Template

> [!NOTE] 
> Not intended for production use. Use for rapind prototyping and experementation, with minimalistic dependencies and generic structure.


## Structure

File tree:

```
.
├── README.md
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── dependencies.py
│   │   ├── main.py
│   │   └── v1
│   │       ├── __init__.py
│   │       ├── health.py
│   │       └── schema.py
│   ├── cmd
│   │   └── main.py
│   ├── config.py
│   ├── infra
│   │   └── db
│   │       ├── __init__.py
│   │       └── conn.py
│   ├── models
│   ├── repositories
│   ├── services
│   └── tests
├── docker-compose.yml
├── poetry.lock
└── pyproject.toml
```

65 lines of Python code, half in `app/infra/db/conn.py` and another half split between `app/api/main.py` and `app/api/v1/health.py` health endpoint.

```
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                           7             31              0             65
Markdown                         1              2              0             30
TOML                             1              4              0             19
YAML                             1              0              0             13
```


## Commands

```shell
# Install the app and its dependencies
poetry install

# Run
poetry run app
```


## Dependencies

Minimalistic set of dependencies.

* FastAPI
* Asyncpg
* Pydantic
* Uvicorn
