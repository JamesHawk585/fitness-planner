# from ipdb import set_trace
from prettycli import red, bold
from simple_term_menu import TerminalMenu


class Cli():
    def start(self):
        print(bold("Welcome to the Fitness Planner! 💪"))
        options = ["Create a new workout", "View existing workouts", "Add exercise to workout", "Delete exercise from workout", "exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
        selection = options[menu_entry_index]
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
    print('Showing workouts...')
def add_exercise_to_workout():
    print("Adding exercise...")
def delete_exercise():
    print('deleting exercise...')
def exit_program():
    print('Bye! 👋')




app = Cli()
selection = app.start()
handle_selection(selection)


