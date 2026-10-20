import os
import sys
from src.database_config import createDatabase
from src.env_config import startupEnv, loadEnv
from dotenv import set_key

def init_environment():
    if not startupEnv(): 
        print("Error: Failed to set up the environment. Exiting.")
        sys.exit(1)

    # Create database.json file from template if it doesn't exist
    createDatabase()

def main():
    # Actual application code goes here
    apiInput = input("Enter your Canvas API Key: ")
    set_key(".env", "CANVAS_KEY", apiInput)
    loadEnv()
    print(os.getenv("CANVAS_KEY"))


if __name__ == "__main__":
    # Ensure environment is set up FIRST
    init_environment()
    
    # Run the application ONLY if setup succeeded
    main()