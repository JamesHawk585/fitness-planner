# from ipdb import set_trace
from prettycli import red, bold
from simple_term_menu import TerminalMenu

# Create simple-term-menu


class Cli():
    def start():
        print(bold("Welcome to the Fitness Planner! 💪"))
        options = ["Create a new workout", "View existing workouts", "Add exercise to workout", "Delete exercise from workout"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(f"You have selected {options[menu_entry_index]}!")
    # def handle_user_input(input):
    # # import ipdb; ipdb.set_trace()
    #     is_number = input.isdigit()
    #     if is_number:
    #         selection = int(input)
    #         if 1 <= selection <=5:
    #             handle_selection(selection)
    #     else: 
    #         print(red("Please enter a valid number (1-5)."))
    start()
    # handle_user_input()


def handle_selection():
    pass

def handle_user_input(input):
    # import ipdb; ipdb.set_trace()
    is_number = input.isdigit()
    if is_number:
        selection = int(input)
        if 1 <= selection <=5:
            handle_selection(selection)
    else: 
        print(red("Please enter a valid number (1-5)."))

    def create_workout():
        pass
    def view_workouts():
        pass
    def add_exercise_to_workout():
        pass
    def delete_exercise():
        pass






