import os

def createEnv(template_path= ".env.template", output_path= ".env"):

    # Check if .env already exists to avoid overwriting existing data
    if os.path.exists(output_path):
        print(f"Aborting: '{output_path}' already exists.")
        return

    # Check if the template exists
    if not os.path.exists(template_path):
        print(f"Error: Template file '{template_path}' not found.")
        return

    # Read the template and write to the new .env file
    with open(template_path, "r") as template, open(output_path, "w") as env_file:
        env_file.write(template.read())
        
    print(f"Successfully created '{output_path}' from '{template_path}'.")

def createDatabase(template_path= "database.template.json", output_path= "database.json"):
    # Check if database.json already exists to avoid overwriting existing data
    if os.path.exists(output_path):
        print(f"Aborting: '{output_path}' already exists.")
        return

    # Check if the template exists
    if not os.path.exists(template_path):
        print(f"Error: Template file '{template_path}' not found.")
        return

    # Read the template and write to the new data.database.json file
    with open(template_path, "r") as template, open(output_path, "w") as db_file:
        db_file.write(template.read())
        
    print(f"Successfully created '{output_path}' from '{template_path}'.")


if __name__ == "__main__":
    createEnv()
    createDatabase()