# from ipdb import set_trace
from prettycli import red, bold
from simple_term_menu import TerminalMenu
from models import Base, Workout, Exercise, association_table 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


# Boilerplate for SQL Alchemy
engine = create_engine('sqlite:///fitness_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Cli():
    def start(self):
        os.system("clear")
        print(bold("Welcome to the Fitness Planner! 💪"))
        options = ["Create a new workout", "View existing workouts", "Add exercise to workout", "Delete exercise from workout","Select workout", "exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        selection = options[menu_entry_index]
        return selection
# Selection is a string. simple_term_menu alwas uses the index of a list of strings to return a value. 
# Consider options for keeping the CLI clean 
 
# Consider refactoring 
def handle_selection(selection):
    if selection == "Create a new workout":
        create_workout()
    elif selection == "View existing workouts":
        view_workouts()
    elif selection == "Add exercise to workout":
        add_exercise_to_workout()
    elif selection == "Delete exercise from workout":
        delete_exercise()
    elif selection == "Select workout":
        workouts = session.query(Workout).all()
        select_workout(workouts)
    else:
        exit_program()


# CRUD Functions 
def create_workout():
    print('Creating workout...')
def view_workouts():
    workouts = session.query(Workout).all()
    print(workouts)
def select_workout(workouts):
    os.system("clear")
    print(bold("Please choose an option"))
    options = [str(workout) for workout in workouts]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")
    selection = options[menu_entry_index]
    # selection == <class 'str'>
    # The join method does not accept a string argument representing the table name. It needs a table object. 
    
    exercises = session.query(Exercise).join(association_table).filter(association_table.c.workout_id == selection)
    print(exercises)
    # selected_workout_id = int(selection.split(" ")[1])
    # print(int(selection.split(' ')[1]))
    # print(exercises)
# SQLAL:Alechemy turns results into Python objects. 
def add_exercise_to_workout():
    print("Adding exercise...")
def delete_exercise():
    print('deleting exercise...')
def exit_program():
    print('Bye! 👋')




app = Cli()
selection = app.start()
handle_selection(selection)


