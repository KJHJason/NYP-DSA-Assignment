try:
    from colorama import Fore as F
    from colorama import Style as S
    import dill, pathlib
except (ModuleNotFoundError, ImportError):
    print("Error importing third-party libraries needed for functions.py to work properly...")
    print("Please press ENTER to exit...")
    input()
    raise SystemExit

def read_db_file():
    """Function to load the database file"""
    try:
        import data
    except (ModuleNotFoundError, ImportError):
        print()
        print("Error importing data.py needed for functions.py to work properly... ")
        print("Please press ENTER to exit...")
        input()
        raise SystemExit

    filePath = pathlib.Path(__file__).parent.resolve().joinpath("hotel_records.db")
    db = data.HotelDatabase()
    if (filePath.is_file()):
        with open(filePath, "rb") as f:
            db = dill.load(f)
    return db

def save_db_file(db):
    """Function to save the database file for future runs"""
    filePath = pathlib.Path(__file__).parent.resolve().joinpath("hotel_records.db")
    with open(filePath, "wb") as f:
        dill.dump(db, f)

def reset_colour(*nl):
    """
    Function to reset colorama foreground, background colors and styles.
    
    Param:
    - nl (bool): If True, will print a new line after resetting colorama.
    """
    if (nl): end = "\n"
    else: end = ""
    print(f"{S.RESET_ALL}", end=end)

def print_main_menu():
    """Print the menu for user to choose their next action"""
    print()
    print(f"{F.LIGHTYELLOW_EX}Welcome to Waffle Hotel's Booking Records")
    print(" " * 16, "System", sep="")
    reset_colour(1)
    
    print("-" * 13, "Menu Options", "-" * 13)
    print()
    print(f"> Number of records: ")
    print()
    print(f"1. Display records options")
    print(f"2. Add a new record")
    print(f"3. Edit records options")
    print(f"4. Sort records options")
    print(f"5. Delete records options")
    
    print(f"{F.RED}X. Exit Application")
    reset_colour()
    
    print()
    print("-" * 40)

def print_sub_menu(typeOfMenu):
    """
    Print the sub-menu based on the main menu option chosen by the user
    
    Requires one argument:
    - typeOfMenu (int): The main menu option that the user chose
    """
    if (typeOfMenu == 1):
        print()
        print("-" * 16, "Display Options", "-" * 16)
        print()
        print("1. Display all records")
        print("2. List records by cost")
        print("F. Back to main menu")
        print()
        print("-" * 49)
    elif (typeOfMenu == 3):
        print()
        print("-" * 13, "Edit Options", "-" * 13)
        print()
        print("1. Edit record by customer name")
        print("2. Edit record by package name")
        print("F. Back to main menu")
        print()
        print("-" * 40)
    elif (typeOfMenu == 4):
        print()
        print("-" * 13, "Sort Options", "-" * 13)
        print()
        print("1. Sort records by customer name")
        print("2. Sort records by package name")
        print("3. Sort records by package cost")
        print("F. Back to main menu")
        print()
        print("-" * 40)
    elif (typeOfMenu == 5):
        print()
        print("-" * 13, "Delete Options", "-" * 13)
        print()
        print("1. Delete record by customer name")
        print("2. Delete record by package name")
        print("F. Back to main menu")
        print()
        print("-" * 42)
    else:
        raise Exception(f"Unknown type of sub-menu argument, {typeOfMenu}...")

def get_input(**options):
    """
    Returns user's input based on the defined command paramater without 
    letting the user enter anything else besides the defined command parameter.
    
    Params:
    - prompt: The prompt to be displayed to the user.
    - prints: The message to be printed to the user.
    - command: The input to be accepted by the program.
    - warning: Used for displaying a custom error message.
    
    Defaults:
    - command: None but must be defined at all time as it will raise an Exception if not defined
    - prompt: "", an input without any prompt
    - prints: None, will not print out any messages
    - warning: None, will not display any error messages
    """
    prints = options.get("prints")

    prompt = options.get("prompt")
    if (not prompt): 
        prompt = ""

    commands = options.get("command")
    if (not commands): 
        raise Exception("command parameter must be defined in the function, get_input_from_user")

    warning = options.get("warning")

    if (prints):
        print()
        if (isinstance(prints, tuple)):
            for line in prints:
                print(line)
        else: 
            print(prints)
        print()

    while True:
        userInput = input(prompt).lower().strip()
        if (userInput in commands): 
            return userInput
        else: 
            if (warning): 
                print(f"{F.LIGHTRED_EX}Error: {warning}")
            else: 
                commandToPrint = " or ".join(commands)
                print(f"{F.LIGHTRED_EX}Error: Invalid input. Please enter {commandToPrint}.")
            print(f"{S.RESET_ALL}")

def shutdown(*args):
    """Print some messages before shutting down the program"""
    if (args): print()
    print("\nThank you for using Waffle Hotel's Booking Records System!")
    reset_colour()
    print("Please press ENTER to exit...")
    input()