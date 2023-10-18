import json

config_file_path = r"C:\Users\Tamás\Desktop\Minden fájl\MS\Code\PythonCodeBase\src\2ndweek\secondday\config.json"

try:
    with open(config_file_path, "r") as config_file:
        config_data = json.load(config_file)
    
    database_setting = config_data.get("database",{})
    api_key = config_data.get("api_key","")
    debug_mode = config_data.get("debug mode",False)

    config_data["new_setting"] = "new value"
    with open(config_file_path, "w") as config_file:
        json.dump(config_data, config_file, indent=4)

    print(database_setting.get("host","N/A"))
    print(api_key)
    print(debug_mode)

except FileNotFoundError:
    print(f"config file not found {config_file_path}")
except json.JSONDecodeError as e:
    print(f"Error parsing JSON")
except Exception as e:
    print(e)