import datetime

class FitnessTracker:
    def __init__(self):
        self.workouts = []
        self.meals = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def add_meal(self, meal):
        self.meals.append(meal)

    def view_workouts(self):
        print("Today's Workouts:")
        for workout in self.workouts:
            print(workout)

    def view_meals(self):
        print("Today's Meals:")
        for meal in self.meals:
            print(meal)

def main():
    tracker = FitnessTracker()
    while True:
        print("\nFitness and Wellness Tracker")
        print("1. Add Workout")
        print("2. Add Meal")
        print("3. View Workouts")
        print("4. View Meals")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            workout = input("Enter workout details: ")
            tracker.add_workout(workout)
            print("Workout added successfully.")
        elif choice == '2':
            meal = input("Enter meal details: ")
            tracker.add_meal(meal)
            print("Meal added successfully.")
        elif choice == '3':
            tracker.view_workouts()
        elif choice == '4':
            tracker.view_meals()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
