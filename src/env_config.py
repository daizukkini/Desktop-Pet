import os
from dotenv import load_dotenv, set_key

""" Environment setup functions: """

# Creates a new .env file from the template if it doesn't exist
def createEnv(template_path= ".env.template", output_path= ".env"):
    # Check if the template exists
    if not os.path.exists(template_path):
        print(f"Error: Template file '{template_path}' not found.")
        return

    # Read the template and write to the new .env file
    with open(template_path, "r") as template, open(output_path, "w") as env_file:
        env_file.write(template.read())
        
    print(f"Successfully created '{output_path}' from '{template_path}'.")

# Loads environment variables from the .env file as long as it exists (true), otherwise returns False
def loadEnv(): 
    if os.path.exists(".env"):
        load_dotenv(".env")
    else:
        print("Error: .env file not found. Please ensure the environment is set up correctly.")
        return False
    return True

# Checks if the environment is set up, creates it if not, and returns True if successful
def startupEnv():
    if not loadEnv():
        createEnv()
    return loadEnv()  # Load again after creating .env

if __name__ == "__main__":
    createEnv()
    loadEnv()