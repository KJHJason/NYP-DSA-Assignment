# import local python files
from data import HotelDatabase
from functions import read_db_file, save_db_file, check_if_db_file_exists, get_input, shutdown, S_reset

# import third-party libraries
from colorama import init as coloramaInit
from colorama import Fore as F

# import standard libraries
import re
from random import randint, uniform
from sys import exit as sysExit
from sys import exc_info

numRegex = re.compile(r"^\d+$")
packageRegex = re.compile(r"^Package \d+$")
customerRegex = re.compile(r"^Customer \d+$")

def main():
    hotelDB = HotelDatabase()
    currentPackageInt = currentCustomerInt = 0
    if (check_if_db_file_exists()):
        loadExisting = get_input(prompt="Load existing records? (y/n): ", command=("y", "n"))
        if (loadExisting == "y"):
            hotelDB = read_db_file()
            
            # get the highest package and customer number if exists to avoid duplicated package and customer name
            db = hotelDB.get_array()
            for record in db:
                packageName = record.get_package_name()
                if (re.fullmatch(packageRegex, packageName)):
                    packageInt = int(packageName.split(" ")[-1])
                    if (packageInt > currentPackageInt):
                        currentPackageInt = packageInt + 1

                customerName = record.get_customer_name()
                if (re.fullmatch(customerRegex, customerName)):
                    customerInt = int(customerName.split(" ")[-1])
                    if (customerInt > currentCustomerInt):
                        currentCustomerInt = customerInt + 1
    else:
        print(f"{F.LIGHTRED_EX}No database file found. Creating new database file.")
        S_reset(nl=1)

    numOfRecords = 0
    while (1):
        numOfRecords = input("Enter the number of records to generate: ")
        if (re.fullmatch(numRegex, numOfRecords)):
            numOfRecords = int(numOfRecords)
            break
        else:
            print("Invalid input. Please enter a number.")
    
    for i in range(numOfRecords):
        hotelDB.add_record(f"Package {currentPackageInt}", f"Customer {currentCustomerInt}", randint(1,9), uniform(50,10000))
        currentPackageInt += 1
        currentCustomerInt += 1

    save_db_file(hotelDB)
    return 0

if (__name__ == "__main__"):
    coloramaInit(autoreset=0, convert=1)
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
        shutdown(nl=1, program="create_records.py")
        sysExit(0)