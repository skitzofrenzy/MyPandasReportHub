import os

def list_scripts(scripts_dir):
    scripts = [f for f in os.listdir(scripts_dir) if f.endswith('.py')]
    if not scripts:
        print("No scripts available in the scripts directory.")
        return []
    return scripts

def select_script(scripts_dir):
    scripts = list_scripts(scripts_dir)
    if not scripts:
        return None

    print("Select a script to run:")
    for i, script in enumerate(scripts, 1):
        print(f"{i}. {script}")

    try:
        choice = int(input("Enter the number of the script to run: "))
        if 1 <= choice <= len(scripts):
            return scripts[choice - 1]
        else:
            print("Invalid choice.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
