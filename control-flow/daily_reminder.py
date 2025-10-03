# daily_reminder.py

# Step 1: Prompt for inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Match Case for priority handling
match priority:
    case "high":
        reminder = f"'{task}' is a HIGH priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = f"'{task}' has an unknown priority."

# Step 3: Check if time-sensitive
if time_bound == "yes":
    reminder += " That task requires immediate attention today!"

# Step 4: Print the final customized reminder
print(reminder)
