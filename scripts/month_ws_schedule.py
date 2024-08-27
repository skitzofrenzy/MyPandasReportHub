import pandas as pd

# This Schedule is to help track, manage, and focus my time spent daily for a full month
name = "Month_Schedule"

class ScheduleTimes:
    """Handles the timeslots for the schedule."""
    def __init__(self):
        self.times = [
            '7:00 AM - 7:20 AM', '7:20 AM - 7:40 AM', '7:40 AM - 8:00 AM',
            '8:00 AM - 9:00 AM', '9:00 AM - 10:00 AM', '10:00 AM - 11:00 AM', 
            '11:00 AM - 12:00 PM', '12:00 PM - 1:00 PM', '1:00 PM - 2:00 PM', 
            '2:00 PM - 3:00 PM', '3:00 PM - 4:00 PM', '4:00 PM - 5:00 PM', 
            '5:00 PM - 6:00 PM', '6:00 PM - 8:00 PM'
        ]

    def get_times(self, limit=None):
        return self.times[:limit] if limit else self.times

class ScheduleActivities:
    """Handles the activities for each time slot."""
    def __init__(self):
        self.names = {
            'wake_up': 'Wakeup time',
            'interview_prep': 'Interview prep/coding questions',
            'mental_prep': 'Mental preparation for workday',
            'work_hours': 'Work hours',
            'lunch_hour': 'Lunch hour',
            'rest': 'Rest and unwind',
            'project_work': 'Portfolio Project Work',
            'networking': 'Networking',
            'tech_writing': 'Technical writing for cybersecurity',
            'cloud_security': 'Cloud security',
            'incident_response': 'Incident response planning',
            'hands_on_practice': 'Hands-on practice with Wireshark and Metasploit',
            'crypto_principles': 'Cryptography principles',
            'cyber_hacking': 'Ethical hacking mini-project',
            'cyber_questions': 'Cybersecurity interview questions review',
            'cyber_mini_project': 'Cybersecurity mini-project or case study',
            'public_speaking': 'Public speaking practice',
            'resume_enhancement': 'Resume enhancement',
            'finalize_portfolio': 'Finalize Portfolio Project',
            'advanced_study': 'Advanced cybersecurity study',
            'review_projects': 'Review cybersecurity projects',
            'finalize_linkedin': 'Finalize LinkedIn profile',
            'finalize_resume': 'Finalize resume',
            'cert_prep': 'Certification exam prep',
            'plan_steps': 'Plan next steps',
            'reflect_progress': 'Reflect on progress',
            'recharge': 'Rest and recharge'
        }

    def get_activity(self, key):
        return self.names.get(key, 'Undefined Activity')

class WeeklySchedule:
    """Generates the schedule for each week."""
    def __init__(self, activities, times):
        self.activities = activities
        self.times = times
        self.num_slots = len(self.times.get_times())
        self.titles = self._generate_titles()

    def _common_daily_activities(self, late_activity=None):
        """Helper function to generate common activities for Monday to Friday."""
        common_activities = [
            self.activities.get_activity('wake_up'),             # 7:00 AM - 7:20 AM
            self.activities.get_activity('interview_prep'),      # 7:20 AM - 7:40 AM
            self.activities.get_activity('mental_prep'),         # 7:40 AM - 8:00 AM
            *([self.activities.get_activity('work_hours')] * 4), # 8:00 AM - 12:00 PM (4 slots for morning work)
            self.activities.get_activity('lunch_hour'),          # 12:00 PM - 1:00 PM
            *([self.activities.get_activity('work_hours')] * 3), # 1:00 PM - 4:00 PM (3 slots for afternoon work)
            self.activities.get_activity('rest'),                # 4:00 PM - 5:00 PM (1 slot for rest)
            "Free Time"
        ]
        if late_activity:
            common_activities.append(self.activities.get_activity(late_activity))
        return self._fill_slots(common_activities)

    def _multi_hour_task(self, task_key, hours):
        """Helper function to fill a task across multiple time slots."""
        task = [self.activities.get_activity(task_key)] * hours
        return self._fill_slots(task)

    def _weekend_task(self, task_key, hours, start_slot=4):
        """Helper function to fill a task for Saturday or Sunday, starting at 9 AM."""
        task_slots = [''] * start_slot + [self.activities.get_activity(task_key)] * hours
        return self._fill_slots(task_slots)

    def _fill_slots(self, activities, placeholder='Unscheduled'):
        """Ensure the number of activities matches the number of time slots."""
        filled_activities = activities + [placeholder] * (self.num_slots - len(activities))
        return filled_activities[:self.num_slots]  # Truncate if somehow longer than expected

    def _generate_titles(self):
        return {
            "week1": {
                "Monday": self._common_daily_activities('network_security_basics'),
                "Tuesday": self._common_daily_activities('hands_on_practice'),
                "Wednesday": self._common_daily_activities('crypto_principles'),
                "Thursday": self._common_daily_activities('cyber_hacking'),
                "Friday": self._common_daily_activities('cyber_questions'),
                "Saturday": self._weekend_task('project_work', hours=3),
                "Sunday": self._weekend_task('networking', hours=2, start_slot=4) + ['GitHub/Portfolio Website Updates']
            },
            "week2": {
                "Monday": self._common_daily_activities('cloud_security'),
                "Tuesday": self._common_daily_activities('burp_suite_nessus'),
                "Wednesday": self._common_daily_activities('incident_response'),
                "Thursday": self._common_daily_activities('cyber_mini_project'),
                "Friday": self._common_daily_activities('cyber_scenarios_review'),
                "Saturday": self._weekend_task('project_work', hours=3),
                "Sunday": self._weekend_task('advanced_study', hours=2, start_slot=4) + ['Mock Interview Practice']
            },
            "week3": {
                "Monday": self._common_daily_activities('tech_writing'),
                "Tuesday": self._common_daily_activities('cyber_team_project'),
                "Wednesday": self._common_daily_activities('public_speaking'),
                "Thursday": self._common_daily_activities('best_cyber_practices'),
                "Friday": self._common_daily_activities('resume_enhancement'),
                "Saturday": self._weekend_task('finalize_portfolio', hours=3),
                "Sunday": self._weekend_task('advanced_study', hours=2, start_slot=4) + ['Mock Interview Practice']
            },
            "week4": {
                "Monday": self._common_daily_activities('review_projects'),
                "Tuesday": self._common_daily_activities('finalize_linkedin'),
                "Wednesday": self._common_daily_activities('finalize_resume'),
                "Thursday": self._common_daily_activities('cert_prep'),
                "Friday": self._common_daily_activities('plan_steps'),
                "Saturday": self._weekend_task('cert_prep', hours=3),
                "Sunday": self._weekend_task('reflect_progress', hours=2, start_slot=4) + [self.activities.get_activity('recharge')]
            }
        }

    def to_dataframe(self, week):
        """Generates a DataFrame for the specified week."""
        data = {'Time': self.times.get_times(self.num_slots)}
        for day, activities in self.titles[week].items():
            data[day] = self._fill_slots(activities)
        return pd.DataFrame(data)

# Function to generate the Excel file
def generate_file(output_path):
    times = ScheduleTimes()
    activities = ScheduleActivities()
    weekly_schedules = {
        "week1": WeeklySchedule(activities, times),
        "week2": WeeklySchedule(activities, times),
        "week3": WeeklySchedule(activities, times),
        "week4": WeeklySchedule(activities, times)
    }

    with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
        for week_name, week_schedule in weekly_schedules.items():
            week_df = week_schedule.to_dataframe(week_name)
            week_df.to_excel(writer, sheet_name=week_name.replace('week', 'Week '), index=False)

    print(f"Excel file created successfully at: {output_path}")


# Example usage:
if __name__ == "__main__":
    output_file = "Month_Schedule.xlsx"
    generate_file(output_file)
