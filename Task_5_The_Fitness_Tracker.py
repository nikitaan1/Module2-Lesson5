#Task1

activities = ["Dancing", "Swimming", "Biking"]
duration = [10, 20, 15]

def fitness_activities():
    for i in range(len(activities)):
        activity = activities[i]
        minutes = duration[i]
        print(f"{activity} - {minutes} mins")

fitness_activities()


#Task2

def calories_burned():
    for i in duration:
        total_calories += i * 3.5 
    print(f"{i} - {total_calories}")

calories_burned()