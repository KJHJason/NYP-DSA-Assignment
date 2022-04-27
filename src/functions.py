# import third-party libraries
from colorama import Fore as F
from colorama import Style as S
import dill

# import standard libraries
import re, pathlib, logging
from datetime import datetime
from time import sleep

def S_reset(nl=0):
    """
    Function to reset colorama foreground, background colors and styles.
    
    Param:
    - nl (bool): If True, will print a new line after resetting colorama. Defaults to False.
    """
    if (nl): end = "\n"
    else: end = ""
    print(f"{S.RESET_ALL}", end=end)

filePath = pathlib.Path(__file__).parent.resolve().joinpath("hotel_records.pickle")
def check_if_db_file_exists():
    """
    Check if the db pickle file exists
    """
    return filePath.is_file()

def read_db_file():
    """
    Function to load the database file
    """
    from data import HotelDatabase

    db = HotelDatabase()
    if (check_if_db_file_exists()):
        with open(filePath, "rb") as f:
            db = dill.load(f)
    return db

def save_db_file(db):
    """
    Function to save the database file for future runs
    """
    with open(filePath, "wb") as f:
        dill.dump(db, f)
    print(f"{F.LIGHTGREEN_EX}Database file saved successfully!")
    S_reset()

def print_main_menu(numOfRecords):
    """
    Print the menu for user to choose their next action
    """
    print()
    print("-" * 13, "Menu Options", "-" * 13)
    print()
    print(f"> Number of records: {numOfRecords}")
    print()
    print("1. Display records options")
    print("2. Add a new record")
    print("3. Edit records options")
    print("4. Sort records options")
    print("5. Delete records options")
    print("X. Exit application and save database")
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
        print("-" * 8, "Display Options", "-" * 8)
        print()
        print("1. Display all records")
        print("2. List records by cost (linear search/binary search + radix sort)")
        print("F. Back to main menu")
        print()
        print("-" * 33)
    elif (typeOfMenu == 3):
        print()
        print("-" * 13, "Edit Options", "-" * 13)
        print()
        print("1. Edit record by customer name (linear search)")
        print("2. Edit record by package name (linear search/binary search + 3way quicksort)")
        print("F. Back to main menu")
        print()
        print("-" * 40)
    elif (typeOfMenu == 4):
        print()
        print("-" * 15, "Sort Options", "-" * 15)
        print()
        print("1. Sort records by customer name (bubble sort)")
        print("2. Sort records by package name (selection sort)")
        print("3. Sort records by package cost (insertion sort)")
        print("4. Sort records by package's number of pax (merge sort)")
        print("F. Back to main menu")
        print()
        print("-" * 40)
    elif (typeOfMenu == 5):
        print()
        print("-" * 13, "Delete Options", "-" * 13)
        print()
        print("1. Delete record by customer name (linear search)")
        print("2. Delete record by package name (linear search/binary search + 3way quicksort)")
        print("F. Back to main menu")
        print()
        print("-" * 42)
    else:
        raise Exception(f"Unknown type of sub-menu argument, {typeOfMenu}...")

def get_input(prints=None, prompt=None, command=None, warning=None):
    """
    Returns user's input based on the defined command paramater without 
    letting the user enter anything else besides the defined command parameter.
    
    Args:
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
    if (not prompt): 
        prompt = ""

    if (not command): 
        raise Exception("command keyword argument must be defined in the function, get_input")

    if (prints):
        print()
        if (isinstance(prints, tuple)):
            for line in prints:
                print(line)
        else: 
            print(prints)
        print()

    while (1):
        userInput = input(prompt).lower().strip()
        if (userInput in command): 
            return userInput
        else: 
            if (warning): 
                print(f"{F.LIGHTRED_EX}Error: {warning}")
            else: 
                commandToPrint = (s for s in command if s != "")
                
                instruction = "enter"
                if ("" in command):
                    instruction = "press Enter or"

                print(f"{F.LIGHTRED_EX}Error: Invalid input. Please {instruction} {' or '.join(commandToPrint)}.")
            print(f"{S.RESET_ALL}")

def log_error():
    """
    Logs an error message to the error log file
    """
    logFolderPath = pathlib.Path(__file__).parent.resolve().joinpath("logs")
    logFolderPath.mkdir(exist_ok=1, parents=1)
    
    fileName = "".join(["error-details-", datetime.now().strftime("%d-%m-%Y"), ".log"])
    logFilePath = logFolderPath.joinpath(fileName)

    if (logFilePath.is_file()):
        with open(logFilePath, "a") as f:
            f.write("\n\n")
    else:
        with open(logFilePath, "w") as f:
            f.write("Waffle Hotel's Booking Records System Error Log\n\n")

    logging.basicConfig(filename=logFilePath, filemode="a", format="%(asctime)s - %(message)s")
    logging.error("Error Details: ", exc_info=True)

def countdown():
    """
    Prints a countdown message to the user before closing the application
    """
    print("Please press ENTER to exit...")
    input()
    for i in range(3, -1, -1):
        print(f"\rAutomatically shutting down in {i} seconds...", end="")
        if (i != 0): 
            sleep(1)

def shutdown(nl=0, program="Main"):
    """
    Print some messages before shutting down the program

    Args:
    - nl (int/bool, optional): Whether to print a newline before the shutdown messages. Defaults to 0/False.
    - program (str, optional): Print the corresponding program shutdown messages. Defaults to "Main".
    """
    if (nl): print()
    if (program.title() == "Main"): 
        print(f"\n{F.LIGHTYELLOW_EX}Thank you for using Waffle Hotel's Booking Records System!")
    else:
        print(f"\n{F.LIGHTRED_EX}Exiting program...")
    S_reset()
    countdown()

rangeInputRegex = re.compile(r"^\d+(-)\d+|\d+$")
def get_range(userInput):
    """
    Used for retreiving a range from the user's input.
    
    Note: It uses the regex, "\d+(-)\d+|\d+" to check for input validity such as "1-2", or "1" which are valid.
    
    Requires one argument to be defined:
    - The user's URL input (string or list)
    """
    userInput = userInput.replace(" ", "")
    if re.fullmatch(rangeInputRegex, userInput):
        if ("-" not in userInput):
            return int(userInput)
        userInput = userInput.split("-")
        rangeList = [int(i) for i in userInput]
        rangeList.sort() # Sort the list in ascending order to make sure the range is valid
        return rangeList
        
    else:
        return "error"