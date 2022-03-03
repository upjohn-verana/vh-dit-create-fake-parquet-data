import pathlib

import faker
import pandas as pd
import yaml

_ = pathlib.Path("data").mkdir(parents=True, exist_ok=True)

fake = faker.Faker()

size = 500

with open("src/tables.yml") as test_data_file:
    table_config = yaml.load(test_data_file, Loader=yaml.Loader)


for table, columns in table_config.items():
    print(f"Creating table: {table}")

    folder_path = "data"

    # os.makedirs(folder_path)

    test_data = {}
    column_dtypes = {}

    for column_name, column_info in columns.items():
        column_faker = column_info["faker"]
        column_dtypes[column_name] = column_info["dtype"]

        test_data_values = []
        for _ in range(size):
            test_data_values.append(faker.Generator.format(fake, column_faker))
        test_data[column_name] = test_data_values

    df = pd.DataFrame(test_data)
    df = df.astype(column_dtypes)

    df.to_parquet(f"{folder_path}/{table}.snap.parquet", compression="snappy", index=False)
