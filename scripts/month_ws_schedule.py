import pandas as pd

# This Schedule is to help track manage and focus my time spent daily for a full month
name = "Month_Schedule"

# Function to generate the Excel file
def generate_file(output_path):
    # Data for each week
    week1_data = {
        'Time': ['7:00 AM - 7:20 AM', '7:20 AM - 7:40 AM', '7:40 AM - 8:00 AM', '8:00 AM - 1:00 PM', '1:00 PM - 2:00 PM', '2:00 PM - 5:00 PM', '5:00 PM - 6:00 PM', '6:00 PM - 8:00 PM'],
        'Monday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Network security basics'],
        'Tuesday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Hands-on practice with Wireshark and Metasploit'],
        'Wednesday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Cryptography principles'],
        'Thursday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Ethical hacking mini-project'],
        'Friday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Cybersecurity interview questions review'],
        'Saturday': ['9:00 AM - 12:00 PM', '', '', 'Portfolio Project Work', '', '', '', ''],
        'Sunday': ['9:00 AM - 11:00 AM', '', '', 'Networking', '', '', '', 'GitHub/Portfolio Website Updates']
    }

    week2_data = {
        'Time': ['7:00 AM - 7:20 AM', '7:20 AM - 7:40 AM', '7:40 AM - 8:00 AM', '8:00 AM - 1:00 PM', '1:00 PM - 2:00 PM', '2:00 PM - 5:00 PM', '5:00 PM - 6:00 PM', '6:00 PM - 8:00 PM'],
        'Monday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Cloud security'],
        'Tuesday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Practice with Burp Suite, Nessus'],
        'Wednesday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Incident response planning'],
        'Thursday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Cybersecurity mini-project or case study'],
        'Friday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Cybersecurity scenarios review'],
        'Saturday': ['9:00 AM - 12:00 PM', '', '', 'Portfolio Project Work', '', '', '', ''],
        'Sunday': ['9:00 AM - 11:00 AM', '', '', 'Mock Interview Practice', '', '', '', 'Advanced cybersecurity study']
    }

    week3_data = {
        'Time': ['7:00 AM - 7:20 AM', '7:20 AM - 7:40 AM', '7:40 AM - 8:00 AM', '8:00 AM - 1:00 PM', '1:00 PM - 2:00 PM', '2:00 PM - 5:00 PM', '5:00 PM - 6:00 PM', '6:00 PM - 8:00 PM'],
        'Monday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Technical writing for cybersecurity'],
        'Tuesday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Cybersecurity team project or collaboration'],
        'Wednesday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Public speaking practice'],
        'Thursday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Best practices in cybersecurity'],
        'Friday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Resume enhancement'],
        'Saturday': ['9:00 AM - 12:00 PM', '', '', 'Finalize Portfolio Project', '', '', '', ''],
        'Sunday': ['9:00 AM - 11:00 AM', '', '', 'Advanced cybersecurity study', '', '', '', 'Mock Interview Practice']
    }

    week4_data = {
        'Time': ['7:00 AM - 7:20 AM', '7:20 AM - 7:40 AM', '7:40 AM - 8:00 AM', '8:00 AM - 1:00 PM', '1:00 PM - 2:00 PM', '2:00 PM - 5:00 PM', '5:00 PM - 6:00 PM', '6:00 PM - 8:00 PM'],
        'Monday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Review cybersecurity projects'],
        'Tuesday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Finalize LinkedIn profile'],
        'Wednesday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Finalize resume'],
        'Thursday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Certification exam prep'],
        'Friday': ['Wakeup time', 'Interview prep/coding questions', 'Mental preparation for workday', 'Work hours', 'Lunch hour', 'Work hours', 'Rest and unwind', 'Plan next steps'],
        'Saturday': ['9:00 AM - 12:00 PM', '', '', 'Complete certification prep', '', '', '', ''],
        'Sunday': ['9:00 AM - 11:00 AM', '', '', 'Reflect on progress', '', '', '', 'Rest and recharge']
    }

    # Create a DataFrame for each week
    week1_df = pd.DataFrame(week1_data)
    week2_df = pd.DataFrame(week2_data)
    week3_df = pd.DataFrame(week3_data)
    week4_df = pd.DataFrame(week4_data)

    # Save the data to an Excel file with each week as a separate sheet
    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        week1_df.to_excel(writer, sheet_name='Week 1', index=False)
        week2_df.to_excel(writer, sheet_name='Week 2', index=False)
        week3_df.to_excel(writer, sheet_name='Week 3', index=False)
        week4_df.to_excel(writer, sheet_name='Week 4', index=False)

    print(f"Excel file created successfully at: {output_path}")
