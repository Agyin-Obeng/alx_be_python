# daily_reminder.py

# Step 1: Prompt for user input
task = input("Enter your task for today: ")
priority = input("Enter the priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Step 2: Use Match Case to handle priority
match priority:
    case "high":
        reminder = f"Reminder: Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Reminder: Your task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Reminder: Your task '{task}' is LOW priority."
    case _:
        reminder = f"Reminder: Your task '{task}' has an UNKNOWN priority."

# Step 3: Adjust message if task is time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Step 4: Print the final reminder
print(reminder)
