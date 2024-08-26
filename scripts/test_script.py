import pandas as pd

name = "Month_Schedule"

def generate_file(output_path):
    # Create some data (this should be replaced with your actual logic)
    data = {'Time': ['8:00 AM', '9:00 AM'], 'Task': ['Task 1', 'Task 2']}
    df = pd.DataFrame(data)

    # Save the data to the provided output path
    df.to_excel(output_path, index=False)
