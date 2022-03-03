# Create fake data for aws poc datalab

This code uses `just`, wich is like `make`. It holds the common commands, such as how to create the files.
You can install just with `brew install just`

## Usage

- Add your tables along with the column names and the desired faker type and data type to the `src/tables.yml` file.
- Run `just create-data`
- the data will be in the `data` directory.

