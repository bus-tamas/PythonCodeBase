import json

config_data = {

    "database": {
    "host": "localhost",
    "port": 5432,
    "settings": {
        "setting1": "val1",
        "setting2": "val2",
    },
    "features": ["feature1", "feature2"]
}
}

config_file_path = r"C:\Users\Tamás\Desktop\Minden fájl\MS\Code\PythonCodeBase\src\2ndweek\secondday\config2.json"


with open(config_file_path, "w") as config_file:
    json.dump(config_data, config_file, indent=4)

print(f"Configuration data saved to {config_file_path}")
