# import local python files
from hotel_record import HotelDatabase, NUM_REGEX
from functions import read_db_file, save_db_file, check_if_db_file_exists, get_input, shutdown, S_reset, preintialise_data

# import third-party libraries
from colorama import init as coloramaInit
from colorama import Fore as F

# import standard libraries
import re
from random import randint, uniform
from sys import exit as sysExit
from sys import exc_info

def main():
    hotelDB = HotelDatabase()
    if (check_if_db_file_exists()):
        loadExisting = get_input(prompt="Load existing records? (y/n): ", command=("y", "n"))
        if (loadExisting == "y"):
            hotelDB = read_db_file()
    else:
        print(f"{F.LIGHTRED_EX}No database file found. Creating new database file.")
        S_reset(nl=True)

    numOfRecords = 0
    while (1):
        numOfRecords = input("Enter the number of records to generate: ")
        if (re.fullmatch(NUM_REGEX, numOfRecords)):
            numOfRecords = int(numOfRecords)
            break
        else:
            print("Invalid input. Please enter a number.")
    
    for _ in range(numOfRecords):
        randPackage, randCust = preintialise_data()
        hotelDB.add_record(randPackage, randCust, randint(1,9), uniform(50,10000))

    save_db_file(hotelDB)
    return 0

if (__name__ == "__main__"):
    coloramaInit(autoreset=False, convert=True)
    try:
        print(f"{F.LIGHTGREEN_EX}Welcome to the Hotel Records Generator meant for development use!")
        S_reset()
        print()
        main()
    except (KeyboardInterrupt):
        pass
    except:
        print()
        print(f"{F.LIGHTRED_EX}Unexpected error caught: {exc_info()}")
        S_reset()
    finally:
        shutdown(nl=True, program="create_records.py")
        sysExit(0)