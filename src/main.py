# import third-party libraries
from colorama import init as coloramaInit

# import standard libraries
from sys import exit as sysExit
from sys import exc_info
import re

# import local python files
from functions import *
from data import print_record_data

paxNumRegex = re.compile(r"^\d+$")
costRegex = re.compile(r"^\d+(\.\d+)?$")
DEBUG_FLAG = 1

def main():
    hotelDB = read_db_file()
    uInput = ""
    while (uInput != "x"):
        print_main_menu(len(hotelDB))
        uInput = get_input(prompt="Enter command: ", command=("1", "2", "3", "4", "5", "x"), warning="Invalid command input, please enter a valid command from the menu above...")
        
        if (uInput == "x"): 
            save_db_file(hotelDB)
            shutdown()

        elif (uInput == "1"):
            # display options
            subInput = ""
            while (subInput != "f"):
                print_sub_menu(1)
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "3", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                if (subInput == "1"):
                    # display all records
                    print(hotelDB)
                elif (subInput == "2"):
                    # display records range from $X to $Y. e.g $100-200
                    print()
                    if (len(hotelDB) > 0):
                        while (1):
                            print("Please enter the range of prices you want to display in the format, $100-200...")
                            rangeInput = input("Enter the range of prices you want to display (x to cancel): $").lower().strip()
                            if (rangeInput == "x"):
                                break
                            formattedRange = get_range(rangeInput)
                            if (formattedRange == "error"):
                                print(f"{F.LIGHTRED_EX}Invalid range input, please enter in a \"$10-100\" format...")
                                S_reset(nl=1)
                            else:
                                if (isinstance(formattedRange, int)):
                                    hotelDB.search_for_range_of_cost(formattedRange, formattedRange)
                                else:
                                    hotelDB.search_for_range_of_cost(formattedRange[0], formattedRange[1])

                                searchAgainPrompt = get_input(prompt="Would you like to search again? (y/n): ", command=("y", "n"))
                                if (searchAgainPrompt == "n"):
                                    break
                                else:
                                    print()
                    else:
                        print(f"{F.LIGHTRED_EX}Error: There is no records...")
                        S_reset(nl=1)
                        
                elif (subInput == "3"):
                    # search for records that matches the specified customer name
                    print()
                    searchAgainPrompt = ""
                    while (searchAgainPrompt != "x"):
                        custInp = input("Enter customer name (x to cancel): ").lower()

                        if (custInp != "x"):
                            hotelDB.search_for_customer(custInp, mode="Display")
                            searchAgainPrompt = get_input(prompt="Would you like to search again? (y/n): ", command=("y", "n"))
                        else:
                            searchAgainPrompt = "x"

        elif (uInput == "2"):
            # add new record
            continueFlag = 1
            while (continueFlag != 0):
                packageName = customerName = ""
                paxNum = costperPax = 0

                print()
                while (continueFlag):
                    customerNameInput = input("Enter the customer name (F to cancel): ").lower().strip()
                    if (customerNameInput == "f"):
                        continueFlag = 0
                        break
                    elif (customerNameInput == ""):
                        print(f"{F.LIGHTRED_EX}Customer name cannot be empty, please enter a valid customer name...")
                        S_reset()
                    else:
                        confirmInput = get_input(prompt=f"Please confirm the customer name, \"{customerNameInput}\" (y/n): ", command=("y", "n"))
                        if (confirmInput == "y"):
                            customerName = customerNameInput
                            print()
                            break
                    print()

                while (continueFlag):
                    packageNameInput = input("Enter the package name (F to cancel): ").lower().strip()
                    if (packageNameInput == "f"):
                        continueFlag = 0
                        break
                    elif (packageNameInput == ""):
                        print(f"{F.LIGHTRED_EX}Package name cannot be empty, please enter a valid package name...")
                        S_reset()
                    else:
                        confirmInput = get_input(prompt=f"Please confirm the package name, \"{packageNameInput}\" (y/n): ", command=("y", "n"))
                        if (confirmInput == "y"):
                            packageName = packageNameInput
                            print()
                            break
                    print()

                while (continueFlag):
                    paxNumInput = input("Enter the number of pax (F to cancel): ").lower().strip()
                    if (paxNumInput == "f"):
                        continueFlag = 0
                        break
                    elif (paxNumInput == ""):
                        print(f"{F.LIGHTRED_EX}Input cannot be empty, please enter a valid pax number of pax...")
                        S_reset()
                    elif (not re.fullmatch(paxNumRegex, paxNumInput)):
                        print(f"{F.LIGHTRED_EX}Invalid input, please enter a valid pax number of pax...")
                        S_reset()
                    else:
                        confirmInput = get_input(prompt=f"Please confirm the number of pax, \"{paxNumInput}\" (y/n): ", command=("y", "n"))
                        if (confirmInput == "y"):
                            paxNum = paxNumInput
                            print()
                            break
                    print()

                while (continueFlag):
                    costperPaxInput = input("Enter the package cost per pax (F to cancel): $").lower().strip()
                    if (costperPaxInput == "f"):
                        continueFlag = 0
                        break
                    elif (costperPaxInput == ""):
                        print(f"{F.LIGHTRED_EX}Package cost per pax cannot be empty, please enter a valid cost per pax...")
                        S_reset()
                    elif (not re.fullmatch(costRegex, costperPaxInput)):
                        print(f"{F.LIGHTRED_EX}Invalid package cost per pax, please enter a valid cost per pax...")
                        S_reset()
                    else:
                        confirmInput = get_input(prompt=f"Please confirm the package cost per pax, \"{costperPaxInput}\" (y/n): ", command=("y", "n"))
                        if (confirmInput == "y"):
                            costperPax = costperPaxInput
                            print()
                            break
                    print()

                if (continueFlag):
                    print(print_record_data(packageName, customerName, paxNum, costperPax))
                    addConfirmation = get_input(prompt="Is this information correct? (y/n): ", command=("y", "n"), warning="Invalid confirmation input, please enter a valid confirmation command...")
                    if (addConfirmation == "y"):
                        hotelDB.add_record(packageName, customerName, paxNum, costperPax)
                        print(f"{F.LIGHTGREEN_EX}Record added successfully...")
                        S_reset()
                else:
                    print(f"\n{F.LIGHTRED_EX}Adding of record cancelled...")
                    S_reset()

        elif (uInput == "3"):
            # edit options
            subInput = ""
            while (subInput != "f"):
                print_sub_menu(3)
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                if (subInput == "1"):
                    # Search record by Customer Name using Linear Search and update record
                    while (1):
                        customerName = input("Enter the customer name (F to cancel): ").lower().strip()
                        if (customerName == "f"):
                            break
                        elif (customerName == ""):
                            print(f"{F.LIGHTRED_EX}Customer name cannot be empty, please enter a valid customer name...")
                            S_reset()
                        else:
                            hotelDB.search_for_customer(customerName, mode="Edit")

                elif (subInput == "2"):
                    # Search record by Package Name using Binary Search and update record
                    while (1):
                        packageName = input("Enter the package name (F to cancel): ").lower().strip()
                        if (packageName == "f"):
                            break
                        elif (packageName == ""):
                            print(f"{F.LIGHTRED_EX}Package name cannot be empty, please enter a valid package name...")
                            S_reset()
                        else:
                            hotelDB.search_for_package(packageName, mode="Edit")

        elif (uInput == "4"):
            # sort options
            subInput = ""
            while (subInput != "f"):
                print_sub_menu(4)
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "3", "4", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                if (subInput == "1"):
                    # sort by customer name using bubble sort
                    sortConfirmation = get_input(prompt="Do you want to sort the records by customer name? (y/n): ", command=("y", "n"))
                    if (sortConfirmation == "y"):
                        descendingFlag = get_input(prompt="Do you want to sort in descending order? (y/n): ", command=("y", "n"))
                        hotelDB.sort_by_customer_name(descendingFlag)

                elif (subInput == "2"):
                    # sort by package name using selection sort
                    sortConfirmation = get_input(prompt="Do you want to sort the records by package name? (y/n): ", command=("y", "n"))
                    if (sortConfirmation == "y"):
                        descendingFlag = get_input(prompt="Do you want to sort in descending order? (y/n): ", command=("y", "n"))
                        hotelDB.sort_by_package_name(descendingFlag)

                elif (subInput == "3"):
                    # sort by package cost using insertion sort
                    sortConfirmation = get_input(prompt="Do you want to sort the records by package cost? (y/n): ", command=("y", "n"))
                    if (sortConfirmation == "y"):
                        descendingFlag = get_input(prompt="Do you want to sort in descending order? (y/n): ", command=("y", "n"))
                        hotelDB.sort_by_package_cost(descendingFlag)

                elif (subInput == "4"):
                    # sort by package's number of pax
                    sortConfirmation = get_input(prompt="Do you want to sort the records by pax number? (y/n): ", command=("y", "n"))
                    if (sortConfirmation == "y"):
                        descendingFlag = get_input(prompt="Do you want to sort in descending order? (y/n): ", command=("y", "n"))
                        hotelDB.sort_by_pax_num(descendingFlag)

        elif (uInput == "5"):
            # delete options
            subInput = ""
            while (subInput != "f"):
                print_sub_menu(5)
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                
                if (subInput == "1"):
                    # Delete record by customer name
                    while (1):
                        print()
                        customerName = input("Enter the customer name (F to cancel): ").lower().strip()
                        if (customerName == "f"):
                            break
                        elif (customerName == ""):
                            print(f"{F.LIGHTRED_EX}Customer name cannot be empty, please enter a valid customer name...")
                            S_reset()
                        else:
                            hotelDB.search_for_customer(customerName, mode="Delete")

                elif (subInput == "2"):
                    # Delete record by package name
                    while (1):
                        print()
                        packageName = input("Enter the package name (F to cancel): ").lower().strip()
                        if (packageName == "f"):
                            break
                        elif (packageName == ""):
                            print(f"{F.LIGHTRED_EX}Package name cannot be empty, please enter a valid package name...")
                            S_reset()
                        else:
                            hotelDB.search_for_package(packageName, mode="Delete")
    return 0

if (__name__ == "__main__"):
    coloramaInit(autoreset=0, convert=1)

    header = "Welcome to Waffle Hotel's Booking Records"
    print("*" * len(header))
    print(f"{F.LIGHTYELLOW_EX}{header}")
    print(" " * 16, "System", sep="")
    S_reset()
    print("*" * len(header))

    if (not DEBUG_FLAG):
        try:
            main()
        except (KeyboardInterrupt):
            shutdown(nl=1, program="Main")
        except:
            print()
            print(f"{F.LIGHTRED_EX}Unexpected error caught: {exc_info()}")
            print(f"Please refer to the generated error log file for more details...")
            S_reset()
            log_error()
            print()
            countdown()
        finally:
            sysExit(0)
    else:
        main()