import os
import sys
from src.data_config import createEnv, createDatabase

def init_environment():
    # Create .env file from template if it doesn't exist
    createEnv()

    # Create database.json file from template if it doesn't exist
    createDatabase()

    # Load environment variables from .env file
    if os.path.exists(".env"):
        with open(".env") as f:
            for line in f:
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split("=", 1)
                    os.environ[key] = value
    else:
        print("Error: .env file not found. Please ensure the environment is set up correctly.")
        sys.exit(1)

def main():
    # Actual application code goes here
    key = os.getenv("CANVAS_KEY")
    print(key)


if __name__ == "__main__":
    # Ensure environment is set up FIRST
    init_environment()
    
    # Run the application ONLY if setup succeeded
    main()