# import third-party libraries
from colorama import init as coloramaInit
from colorama import Fore as F

# import local python files
from hotel_record import HotelDatabase, NUM_REGEX
from functions import read_db_file, save_db_file, check_if_db_file_exists, get_input, shutdown, S_reset, preintialise_data

# import standard libraries
import re, platform, pathlib
from random import randint, uniform
from sys import exit as sysExit
from sys import exc_info

def main():
    """
    This program helps to generate nth number of records for testing purposes!
    """
    hotelDB = HotelDatabase()
    if (check_if_db_file_exists()):
        loadExisting = get_input(prompt="Load existing records? (y/n): ", command=("y", "n"))
        if (loadExisting == "y"):
            hotelDB = read_db_file(preintialiseData=False)
            print()
            if (len(hotelDB) == 0):
                print(f"{F.LIGHTRED_EX}No records found in the database!")
                S_reset(nl=True)
            else:
                print(f"{F.LIGHTGREEN_EX}Loaded {len(hotelDB)} records from the database!")
                S_reset(nl=True)
    else:
        print(f"{F.LIGHTRED_EX}No database file found. Creating new database file.")
        S_reset(nl=True)

    numOfRecords = 0
    while (1):
        numOfRecords = input("Enter the number of records to generate (x to cancel): ").strip()
        if (numOfRecords.lower() == "x"):
            print(f"{F.LIGHTRED_EX}Notice: No records generated!")
            S_reset()
            numOfRecords = 0
            break
        elif (re.fullmatch(NUM_REGEX, numOfRecords)):
            numOfRecords = int(numOfRecords)
            if (numOfRecords > 2000):
                # more than that might hit the recursion depth limit
                print(f"{F.LIGHTRED_EX}Notice: Number of records to generate must be smaller than or equal to 2000!")
                S_reset(nl=True)
            else:
                break
        else:
            print(f"{F.LIGHTRED_EX}Invalid input. Please enter a number.")
            S_reset(nl=True)

    addedFlag = False
    for _ in range(numOfRecords):
        if (len(hotelDB) >= 2000):
            if (not addedFlag):
                print(f"{F.LIGHTRED_EX}Notice: Stopping addition of records to prevent recursion depth limit error.\nPlease remove some records to be less than 2000 records and try again!")
                return

            print(f"{F.LIGHTRED_EX}Notice: Some records has been added to the database. However, this program will stop adding records to prevent recursion depth limit error.\nPlease remove some records from the database to be less than 2000 records if you wish to use this program again.", end="\n\n")
            break

        randPackage, randCust = preintialise_data()
        hotelDB.add_record(randPackage, randCust, randint(1,9), uniform(50,1000))
        addedFlag = True

    save_db_file(hotelDB)
    return 0

if (__name__ == "__main__"):
    if (platform.system() == "Windows"):
        # colorama to escape the ANSI escape sequences for Windows systems
        coloramaInit(autoreset=False, convert=True)

    try:
        print(f"{F.LIGHTYELLOW_EX}Welcome to the Hotel Records Generator meant for development use!")
        S_reset()
        print()
        main()
    except (KeyboardInterrupt, EOFError):
        pass
    except:
        print(f"{F.LIGHTRED_EX}Unexpected error caught: {exc_info()}")
        S_reset()
    finally:
        shutdown(nl=False, program=pathlib.Path(__file__).resolve().stem)
        sysExit(0)