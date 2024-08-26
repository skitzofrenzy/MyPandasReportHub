import os
import sys
from datetime import datetime
import importlib.util
import argparse

# Function to list available scripts
def list_scripts(scripts_dir):
    scripts = [f for f in os.listdir(scripts_dir) if f.endswith('.py')]
    if not scripts:
        print("No scripts available in the scripts directory.")
        sys.exit(1)
    return scripts

# Function to dynamically import and execute a script
def execute_script(script_name, scripts_dir, output_dir):
    # Validate script file existence
    script_path = os.path.join(scripts_dir, script_name)
    if not os.path.exists(script_path):
        print(f"Script {script_name} does not exist in {scripts_dir}.")
        sys.exit(1)

    # Dynamically import and execute the script
    spec = importlib.util.spec_from_file_location("module.name", script_path)
    script_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(script_module)

    # Ensure the script has a 'name' variable
    if not hasattr(script_module, 'name'):
        print(f"The script {script_name} does not define a 'name' variable.")
        sys.exit(1)

    # Generate timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

    # Generate file name using the script's name variable
    generated_name = f"{script_module.name}_{timestamp}.xlsx"

    # Create subdirectories based on current year and month
    year_month = datetime.now().strftime('%Y%m')
    sub_dir = os.path.join(output_dir, year_month)
    os.makedirs(sub_dir, exist_ok=True)

    # Save file in the appropriate directory
    output_path = os.path.join(sub_dir, generated_name)

    # Ensure the script has a 'generate_file' function
    if not hasattr(script_module, 'generate_file'):
        print(f"The script {script_name} does not define a 'generate_file' function.")
        sys.exit(1)

    # Generate the file using the script's generate_file function
    script_module.generate_file(output_path)

    print(f"File generated: {output_path}")

# Main function to handle CLI and script execution
def main():
    # Define paths
    scripts_dir = os.path.join(os.getcwd(), 'scripts')
    output_dir = os.path.join(os.getcwd(), 'output')

    # Argument parser for command-line interface
    parser = argparse.ArgumentParser(
        description="Execute scripts from the scripts directory and generate output files.",
        epilog="Use this tool to run specific scripts, generate output files, and manage your script workflows efficiently."
    )
    parser.add_argument('-l', '--list', action='store_true', help="List all available scripts in the 'scripts' directory.")
    parser.add_argument('-s', '--script', type=str, help="Specify the script name to run from the 'scripts' directory.")
    args = parser.parse_args()

    # List available scripts
    if args.list:
        scripts = list_scripts(scripts_dir)
        print("Available scripts:")
        for i, script in enumerate(scripts, 1):
            print(f"{i}. {script}")
        sys.exit(0)

    # If a script is specified, execute it
    if args.script:
        execute_script(args.script, scripts_dir, output_dir)
    else:
        # If no script is specified, prompt the user to select one from the list
        scripts = list_scripts(scripts_dir)
        print("Select a script to run:")
        for i, script in enumerate(scripts, 1):
            print(f"{i}. {script}")

        try:
            choice = int(input("Enter the number of the script to run: "))
            if 1 <= choice <= len(scripts):
                execute_script(scripts[choice - 1], scripts_dir, output_dir)
            else:
                print("Invalid choice. Exiting.")
                sys.exit(1)
        except ValueError:
            print("Invalid input. Please enter a number.")
            sys.exit(1)

if __name__ == "__main__":
    main()
