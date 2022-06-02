# import third-party libraries
from colorama import Fore as F
from colorama import Style as S

# import standard libraries
import re, pathlib, logging, sqlite3
from datetime import datetime
from time import sleep
from random import randint, uniform, choice

# String to indicate that the records are not sorted
NOT_SORTED = "Not Sorted"

# Welcome header message
HEADER = "Welcome to Waffle Hotel's Staycation Booking"

# regex for handling user inputs
RANGE_INPUT_REGEX = re.compile(r"^\d+(\.\d+)?(-)\d+(\.\d+)?$|^\d+(\.\d+)?$")

# to get the path of the directory that the python is being executed from
# used for to get the path of the sqlite3 database file and the error log files
FILE_PATH = pathlib.Path(__file__).parent.resolve()

# for persistent storage of the records (using sqlite3 to store the records ONLY)
DB_FILE_PATH = FILE_PATH.joinpath("staycation_records.db")

# used for the table name in sqlite3 database file
STAYCATION_RECORDS_TABLE = "StaycationRecords"
HOTEL_DATABASE_CONFIG_TABLE = "HotelDatabaseConfig"

# a tuple of strings that indicates True used in this project
USED_TRUE_CONDITIONS = ("y", "Y", "d") 

# presets used in preinitialising the database with records
# by randomly selecting one element from each presets
PACKAGE_NAME_PRESETS = ("Budget Package", "Standard Package", "Premium Package", "Deluxe Package", "Luxury Package", "Ultimate Package")
CUSTOMER_NAME_PRESETS = ("John Smith", "Jane Doe", "Jack Black", "Jill Jackson", "Juanita Jones", "Eden Lai", "Calvin Goh", "Mr Waffles")

def S_reset(nl=False):
    """
    Function to reset colorama foreground, background colors and styles.
    
    Requires one argument:
    - nl (bool): If True, will print a new line after resetting colorama. Defaults to False.
    """
    end = ""
    if (nl): 
        end = "\n"

    print(f"{S.RESET_ALL}", end=end)

def check_if_db_file_exists():
    """
    Check if the db pickle file exists...
    
    Used in this python script and in create_records.py
    """
    return DB_FILE_PATH.is_file()

def preintialise_data():
    """
    Randomly picks a package name and customer name from the list of packages and customers predefined in this function and returns them in a tuple.
    """
    return choice(PACKAGE_NAME_PRESETS), choice(CUSTOMER_NAME_PRESETS)

def read_db_file(preintialiseData=False):
    """
    Function to load the database file
    
    Requires one argument:
    - preintialiseData (bool): to preinitialise the database with 10 records 
                               if pickle file doesn't exist, defaults to False
    """
    from hotel_record import HotelDatabase # import here to avoid circular imports
    db = HotelDatabase()

    if (check_if_db_file_exists()):
        try:
            con = sqlite3.connect(DB_FILE_PATH)
            cur = con.cursor()
            cur.execute(f"SELECT * FROM {STAYCATION_RECORDS_TABLE}")
            records = cur.fetchall()
            # load the HotelDatabase object's configuration from the sqlite3 database file
            configTuple = cur.execute(f"SELECT * FROM {HOTEL_DATABASE_CONFIG_TABLE}").fetchone()

            # load all sqlite3 database records into the HotelDatabase object
            for record in records:
                customerName = record[0]
                packageName = record[1]
                paxNum = record[2]
                costPerPax = record[3] / 100 # since the cost is stored as an INTEGER
                db.add_record(packageName, customerName, paxNum, costPerPax)

            # set the config here since the HoteLDatabase object will reset the 
            # sort order to NOT_SORTED when each record is added to the object.
            # (if the config data is saved/exists)
            if (configTuple[0] is not None):
                db.sort_order = configTuple[0]

            if (configTuple[1] is not None):
                db.descending_flag = bool(configTuple[1])

            return db
        except (sqlite3.Error, sqlite3.IntegrityError, sqlite3.OperationalError):
            # if the sqlite3 database file is empty (no tables) or has some errors, 
            # delete it and call itself (the function) again
            newFileName = datetime.now().strftime("corrupted-%d-%m-%Y_%H-%M-%S") + ".db"
            newFilePath = FILE_PATH.joinpath(newFileName)

            # in the event if the file already exists, delete it
            if (newFilePath.is_file()):
                newFilePath.unlink()

            DB_FILE_PATH.rename(newFilePath) # rename the file to newFileName
            print(f"{F.LIGHTRED_EX}Error: SQLite3 database file is empty or has some errors.")
            print(f"Old sqlite3 database file will be renamed to {newFileName} (delete at your own risk and will)")
            print(f"and a new one will be created with {'10 pre-initialised records' if (preintialiseData) else 'no records pre-initialised'}.")
            S_reset()
            return read_db_file(preintialiseData=preintialiseData)

    numOfRecords = 0
    if (preintialiseData):
        numOfRecords = 10

    # pre-initialize the database with 10 records to satisfy basic function b
    for _ in range(numOfRecords):
        randPackage, randCust = preintialise_data()
        db.add_record(randPackage, randCust, randint(1,9), uniform(50,1000))
    return db

def save_db_file(db, printSuccessMsg=True):
    """
    Function to save the database file for future runs
    
    Requires two arguments:
    - db (HotelDatabase)
    - printSuccessMsg (bool): to print a success message if True, defaults to True
    """
    con = sqlite3.connect(DB_FILE_PATH)
    cur = con.cursor()

    # saving the records to the sqlite3 database
    # remove old table
    cur.execute(f"DROP TABLE IF EXISTS {STAYCATION_RECORDS_TABLE}")
    con.commit()

    # create new table
    cur.execute(f"""CREATE TABLE {STAYCATION_RECORDS_TABLE} (
        customerName TEXT NOT NULL, 
        packageName TEXT NOT NULL, 
        paxNum INTEGER NOT NULL, 
        costPerPax INTEGER NOT NULL -- Using INTEGER since REAL is not the best way to store price data
                                    -- https://dba.stackexchange.com/questions/15729/storing-prices-in-sqlite-what-data-type-to-use
        )""")
    con.commit()

    # add tuples to the new table
    for record in db.get_array():
        dataTuple = (
                record.get_customer_name(), record.get_package_name(), 
                record.get_pax_num(), int(record.get_cost_per_pax() * 100) # times 100 since it is in 2dp
            )
        cur.execute(f"INSERT INTO {STAYCATION_RECORDS_TABLE} VALUES (?, ?, ?, ?)", dataTuple)
    con.commit()

    # save the HotelDatabase object's configuration to the sqlite3 database file
    # delete old HotelDatabase saved configuration (sorting order and descending flag)
    cur.execute(f"DROP TABLE IF EXISTS {HOTEL_DATABASE_CONFIG_TABLE}")
    con.commit()

    # update the HotelDatabase saved configuration (sorting order and descending flag)
    cur.execute(f"CREATE TABLE {HOTEL_DATABASE_CONFIG_TABLE} (sortingOrder TEXT, descendingFlag BOOLEAN)")
    cur.execute(f"INSERT INTO {HOTEL_DATABASE_CONFIG_TABLE} VALUES (?, ?)", (db.sort_order, \
                                                                             db.descending_flag))
    con.commit()
    con.close()

    if (printSuccessMsg):
        print(f"{F.LIGHTGREEN_EX}Database file saved successfully!")
        S_reset()

def print_main_menu(numOfRecords, sortOrder=NOT_SORTED):
    """
    Print the menu for user to choose their next action
    
    Requires one argument:
    - numOfRecords (int): to indicate the number of records in the database
    """
    print()
    print("*" * len(HEADER))
    print(f"{F.LIGHTYELLOW_EX}{HEADER}")
    print(f"{'Records System':^{len(HEADER)}}")
    S_reset()
    print("*" * len(HEADER))
    print()
    print("-" * 13, "Menu Options", "-" * 13)
    print()
    print(f"> Number of records: {numOfRecords}")
    print(f"> Sort Order: {sortOrder}")
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
        print("-" * 10, "Display Options", "-" * 10)
        print()
        print("1. Display all records")
        print("2. Display records by cost (binary search + radix sort)")
        print("3. Display records by customer name (binary search tree)")
        print("4. Display records by package name (fibonacci search + introsort)")
        print("F. Back to main menu")
        print()
        print("-" * 37)
    elif (typeOfMenu == 3):
        print()
        print("-" * 13, "Edit Options", "-" * 13)
        print()
        print("1. Edit record by customer name (linear search)")
        print("2. Edit record by package name (binary search + heap sort)")
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
        print("4. Sort records by package's number of pax (shellsort)")
        print("F. Back to main menu")
        print()
        print("Noob/Pancake. ???")
        print()
        print("-" * 44)
    elif (typeOfMenu == 5):
        print()
        print("-" * 13, "Delete Options", "-" * 13)
        print()
        print("1. Delete record by customer name (exponential search + tree sort)")
        print("2. Delete record by package name (binary search + heap sort)")
        print("F. Back to main menu")
        print()
        print("-" * 42)
    elif (typeOfMenu == 6):
        print()
        print("-" * 10, "Easter Egg Menu Options", "-" * 10)
        print()
        print("1. Sort records by customer name (stalin sort)")
        print("2. Sort records by package name (bogo sort)")
        print("3. Sort records by package name (bozo sort)")
        print("4. Sort records by package cost (slow sort)")
        print("5. Sort records by package's number of pax (sleep sort)")
        print("6. Sort records by package's number of pax (gnome sort)")
        print("Q. Back to sort menu")
        print()
        print("-" * 45)
    elif (typeOfMenu == 7):
        print()
        print("-" * 10, "Pancake Sort Menu Options", "-" * 10)
        print()
        print("1. Sort records by customer name")
        print("2. Sort records by package name")
        print("3. Sort records by package cost")
        print("4. Sort records by package's number of pax")
        print("Q. Back to sort menu")
        print()
        print("-" * 50)
    else:
        raise ValueError(f"Unknown type of sub-menu argument, {typeOfMenu}...")

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
        raise ValueError("command keyword argument must be defined in the function, get_input")

    if (prints):
        print()
        if (isinstance(prints, tuple)):
            for line in prints:
                print(line)
        else: 
            print(prints)
        S_reset(nl=True)

    while (1):
        userInput = input(prompt).lower().strip()
        if (isinstance(command, tuple) and userInput in command): 
            return userInput
        elif (userInput == command):
            return userInput
        else: 
            if (warning): 
                print(f"{F.LIGHTRED_EX}Input Error: {warning}")
            else:
                if (not isinstance(command, tuple)):
                    print(f"{F.LIGHTRED_EX}Input Error: Please enter {command}.")
                elif (len(command) == 2):
                    print(f"{F.LIGHTRED_EX}Input Error: Please enter {command[0]} or {command[1]}.")
                else:
                    print(f"{F.LIGHTRED_EX}Input Error: Please enter {', '.join(command[:-1])}, or {command[-1]}.")

            S_reset(nl=True)

def log_error():
    """
    Logs an error message to the error log file
    """
    logFolderPath = FILE_PATH.joinpath("logs")
    logFolderPath.mkdir(exist_ok=True, parents=True)
    
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

def shutdown(nl=False, program="Main"):
    """
    Print some messages before shutting down the program

    Requires two arguments:
    - nl (bool): Whether to print a newline before the shutdown messages. Defaults to False.
    - program (str): Print the corresponding program shutdown messages. Defaults to "Main".
    """
    if (nl): 
        print()

    if (program.title() == "Main"): 
        print(f"\n{F.LIGHTYELLOW_EX}Thank you for using Waffle Hotel's Booking Records System!")
    else:
        print(f"\n{F.LIGHTRED_EX}Exiting program...")

    S_reset()
    countdown()

def get_range(userInput):
    """
    Used for retreiving a range from the user's input.
    
    Returns a list of integers
    
    Note: It uses the regex, "\d+(-)\d+|\d+" to check for input validity such as "1-2", or "1" which are valid.
    
    Requires one argument:
    - The user's URL input (string or list)
    """
    userInput = userInput.replace(" ", "")
    if (not re.fullmatch(RANGE_INPUT_REGEX, userInput)):
        return "error"

    if ("-" not in userInput):
        numRange = round(float(userInput), 2)
        return [numRange, numRange]
    userInput = userInput.split("-")
    rangeList = [round(float(i), 2) for i in userInput]

    # Check if the list in ascending order to make sure the range is valid
    if (rangeList[0] > rangeList[1]):
        # If not, swap the values
        rangeList = [rangeList[1], rangeList[0]]
        print(f"{F.LIGHTRED_EX}Alert: The minimum value is larger than the maximum value, the range will be reversed.", end=S_reset(nl=True))
    return rangeList

def format_price(price):
    """
    Format the price to 2 decimal places and return a string
    
    Requires one argument:
    - price (int/float)
    """
    return f"${round(float(price), 2):.2f}"

def print_record_data(packageNameInput, customerNameInput, paxNumInput, packageCostPerPaxInput):
    """
    Function to print the record data in a readable format.
    
    Requires 4 arguments:
    - packageNameInput (str): The package name
    - customerNameInput (str): The customer name
    - paxNumInput (int): The number of pax
    - packageCostPerPaxInput (int/float): The package cost per pax
    """
    header = "Record Data Displayed Below:"
    maxLen = len(header)

    packageName = f"Package Name: {packageNameInput}"
    if (len(packageName) > maxLen):
        maxLen = len(packageName)

    customerName = f"Customer Name: {customerNameInput}"
    if (len(customerName) > maxLen):
        maxLen = len(customerName)

    paxNum = f"Number of Pax: {paxNumInput}"
    if (len(paxNum) > maxLen):
        maxLen = len(paxNum)

    packageCostPerPax = f"Package Cost Per Pax: {format_price(packageCostPerPaxInput)}"
    if (len(packageCostPerPax) > maxLen):
        maxLen = len(packageCostPerPax)

    print()
    print("-" * maxLen)
    print(header)
    print()
    print(packageName)
    print(customerName)
    print(paxNum)
    print(packageCostPerPax)
    print("-" * maxLen)
    return ""

def convert_var_to_bool(var):
    """
    Convert a variable to a boolean
    
    Requires 1 argument:
    - var (str/int/float/bool): The variable to be converted
    """
    if (isinstance(var, bool)):
        return var

    if (isinstance(var, int)):
        return bool(var)

    if (isinstance(var, str) and var in USED_TRUE_CONDITIONS):
        return True

    return False

def get_descending_flag(msg=None, nl=False):
    """
    Asks the user if he/she wishes to sort in descending order...
    
    Optional argument:
    - msg (str): The message to be displayed to the user before prompting
    - nl (bool): Whether to print a newline before the prompt. Defaults to False.
    
    Returns True if the user wants to sort in descending order, False otherwise
    """
    if (nl):
        print() # print a newline

    if (msg):
        print(msg)

    print(f"{F.LIGHTYELLOW_EX}This program will proceed to sort in an ascending order...")
    S_reset()
    reverseOrder = get_input(prompt="Press ENTER to continue, or \"d\" to sort in descending order: ", command=("", "d"), warning="Please press ENTER to continue or \"d\" to sort in descending order!")

    return convert_var_to_bool(reverseOrder)