
def start():
    print("Welcome to the Fitness Planner! 💪")
    print('1. Create a new workout')
    print('2. View existing workouts')
    print('3. Add exercise to workout')
    print('4. Delete exercise from workout')
    print('5. Exit')
    user_input = input('What would you like to do?')
    handle_user_input(user_input)

start()

def handle_user_input(user_input):
    if user_input == 1:
        pass
        # Returns the next workout in a rotation of push_day, pull_day, and abs_and_legs_day.
    elif user_input == 2:
        pass
        #  Return the exercises for each of the three workouts.
    elif user_input == 3:
        pass
        # Add new exercise to a specified workout. 
            #  User will have to enter a valid value for each of the columns in the exercise table and append that exercise to an existing workout. 
    elif user_input == 4:
        pass
        # Delete a specified instance of the Exercise class by refrencing exercise_name.
    elif user_input == 5: 
        pass
        # Quit the application 
    else: 
        print('Please enetr a valid input (1-5.)')





    





