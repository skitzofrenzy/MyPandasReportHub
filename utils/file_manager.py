import os
from datetime import datetime

def create_output_directory(output_dir):
    # Create subdirectories based on current year and month
    year_month = datetime.now().strftime('%Y%m')
    sub_dir = os.path.join(output_dir, year_month)
    os.makedirs(sub_dir, exist_ok=True)
    return sub_dir

def generate_file_name(script_name, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return f"{script_name}_{timestamp}.xlsx"

def get_full_output_path(output_dir, file_name):
    sub_dir = create_output_directory(output_dir)
    return os.path.join(sub_dir, file_name)
