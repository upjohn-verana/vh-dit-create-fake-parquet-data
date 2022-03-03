precommit-install:
    pre-commit install

create-data:
    poetry run python src/create_fake_tables.py
