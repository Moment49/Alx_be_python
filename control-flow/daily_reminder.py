task_description = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match task_priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a {task_priority} priority task that requires immediate attention today!")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a {task_priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
                print(f"Reminder: '{task_description}' is a {task_priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a {task_priority} priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Reminder: '{task_description}' is a {task_priority} priority task. Consider completing it when you have free time.")