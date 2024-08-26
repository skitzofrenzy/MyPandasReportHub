import os
import sys
import argparse
from utils.script_selector import list_scripts, select_script
from utils.script_executor import execute_script

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
        script_name = select_script(scripts_dir)
        if script_name:
            execute_script(script_name, scripts_dir, output_dir)
        else:
            print("No valid script selected. Exiting.")
            sys.exit(1)

if __name__ == "__main__":
    main()
