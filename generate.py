import json
import os
import subprocess

def cmake_user_presets() -> str:
    presets =  {
            "version": 2,
            "configurePresets": [
                {
                    "name": "default",
                    "inherits": "vcpkg",
                    "environment": {
                        "VCPKG_ROOT": os.environ["VCPKG_ROOT"]
                        }
                    }
                ]
            }
    return json.dumps(presets, indent=4)

if __name__ == "__main__":
    with open("CMakeUserPresets.json", "w") as file: 
        file.write(cmake_user_presets())
    subprocess.run(["vcpkg", "new", "--application"])
