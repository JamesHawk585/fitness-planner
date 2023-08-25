# from ipdb import set_trace
from prettycli import red, bold
from simple_term_menu import TerminalMenu
from models import Base, Workout
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Boilerplate for SQL Alchemy
engine = create_engine('sqlite:///fitness_data.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Cli():
    def start(self):
        print(bold("Welcome to the Fitness Planner! 💪"))
        options = ["Create a new workout", "View existing workouts", "Add exercise to workout", "Delete exercise from workout", "exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        selection = options[menu_entry_index]
        print(type(selection))
        return selection
# Consider options for keeping the CLI clean 

# 2023-08-11-SQLAlchemy/Alembic - Migrations Cont. Many-to-many, CLI build demo
# 2:05:30

# Routes selection from start() to CRUD functions. 
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
    else:
        exit()
# Goole Python Exit() function. May need to rename. 

# CRUD Functions 
def create_workout():
    print('Creating workout...')
def view_workouts():
    workouts = session.query(Workout).all()
    print(workouts)
    # Pulls a list from the DB
# Use session.query
# SQLAL:Alechemy truens results intop Python objects. 
    # Selects alls rows from the workout table. 
    # Isert logic to show three tables: 
    # 1. All exercises in push_day
    # 2. All exercises in pull_day
    # 3. All exercises in abs_and_legs_day
    # 4. Returns user to menu when done 
def add_exercise_to_workout():
    print("Adding exercise...")
def delete_exercise():
    print('deleting exercise...')
def exit_program():
    print('Bye! 👋')




app = Cli()
selection = app.start()
handle_selection(selection)


