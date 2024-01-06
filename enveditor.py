#!/usr/bin/env python3

import os, json, logging

logging.basicConfig(filename="enveditor.log", format='%(asctime)s - %(levelname)s:%(message)s', datefmt= '%m/%d/%y %I:%M:%S %p', level=logging.DEBUG)

class enveditor:
    # Variables
    PATH = {
        "ENV_GLOBAL_PATH" : "/etc/environment"
    }

    def enveditor(self):
        pass

    # Getter for path
    def return_path(key: str, self) -> str:
        return self.PATH[key]
    
    # ADD or EDIT path
    def edit_path(self, key: str, path: str) -> None:
        self.PATH[key.upper()] = path

        logging.info(f"Path edited, KEY: {key} VALUE: {path}")
    
    # SAVE dict to JSON
    def commit_config(self) -> None:
        stream = open("config.json", "w")
        
        json.dump(self.PATH, stream, indent=4)

        stream.close()

        logging.info("Configuration saved")
    
    # LOAD configuration
    def load_config(self) -> None:
        try:
            stream = open("config.json", "r")

            self.PATH = json.load(stream)

            stream.close()

            logging.info("Config loaded")
        except FileNotFoundError:
            logging.warning("There's no config file, loading default configuration")
    
    # Get file content
    def read_file(self, key: str) -> str:
        stream = open(self.PATH[key], "r")

        lines = stream.read()

        stream.close()

        return lines

def main():
    logging.debug("Debug mode enabled")
    
    editor = enveditor()
    editor.load_config()

    while True:
        print("Environment Editor | Debug Mode\n0 - Stop Debug\n1 - Add/Edit Path\n2 - Read File\n3 - Edit File")
        prompt = int(input("Enter a number [0-3]: "))

        match prompt:
            case 0:
                break
            case 1:
                print("\nSelected Add/Edit Path:\n")
                key = str(input("Key: "))
                value = str(input("Path: "))

                editor.edit_path(key, value)
                editor.commit_config()
            case 2:
                print("\nSelected Read File:\n")
                print(f"Which path to read?\n{json.dumps(editor.PATH, indent=4)}\n")
                selection = str(input("Type the key value: ")).upper()

                lines = editor.read_file(selection)

                print(f"\n{lines}\n")
            case 3:
                print("\nSelected Edit File:\n")

main()