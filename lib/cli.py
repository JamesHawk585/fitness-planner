# from ipdb import set_trace
import os

def start():
    print("Welcome to the Fitness Planner! 💪")
    print('1. Create a new workout')
    print('2. View existing workouts')
    print('3. Add exercise to workout')
    print('4. Delete exercise from workout')
    print('5. Exit')
    user_input = input('What would you like to do?')
    handle_user_input(user_input)

def handle_user_input(input):
    # import ipdb; ipdb.set_trace()
    if input == '1':
        print('Creating workout...')
        # Returns the next workout in a rotation of push_day, pull_day, and abs_and_legs_day.
    elif input == '2':
        print('Showing existing workouts...')
        #  Return the exercises for each of the three workouts.
    elif input == '3':
        print('Adding exercise to workout...')
        # Add new exercise to a specified workout. 
            #  User will have to enter a valid value for each of the columns in the exercise table and append that exercise to an existing workout. 
    elif input == '4':
        print('Deleting exercise from workout...')
        # Delete a specified instance of the Exercise class by refrencing exercise_name.
    elif input == '5': 
        print('Quitting app..')
        # Quit the application 
    else: 
        os.system('clear')
        print('Please enetr a valid number (1-5).')
        start()



start()

    





