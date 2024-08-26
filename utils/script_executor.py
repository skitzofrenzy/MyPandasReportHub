import os
import sys
import importlib.util
from utils.file_manager import generate_file_name, get_full_output_path

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

    # Generate file name using the script's name variable
    generated_name = generate_file_name(script_module.name)

    # Get the full output path
    output_path = get_full_output_path(output_dir, generated_name)

    # Ensure the script has a 'generate_file' function
    if not hasattr(script_module, 'generate_file'):
        print(f"The script {script_name} does not define a 'generate_file' function.")
        sys.exit(1)

    # Generate the file using the script's generate_file function
    script_module.generate_file(output_path)

    print(f"File generated: {output_path}")
