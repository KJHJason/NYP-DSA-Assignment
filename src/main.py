# import standard libraries
from sys import exit as sysExit

# import third-party libraries
from colorama import init as coloramaInit

# import local python files
from functions import *
from data import print_record_data

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
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                if (subInput == "1"):
                    # display all records
                    print(hotelDB)
                elif (subInput == "2"):
                    # display records range from $X to $Y. e.g $100-200
                    while (1):
                        print()
                        print("Please enter the range of prices you want to display in the format, $100-200...")
                        rangeInput = input("Enter the range of prices you want to display (x to cancel): $").lower().strip()
                        if (rangeInput == "x"):
                            break
                        formattedRange = get_range(rangeInput)
                        if (formattedRange == 0):
                            print(f"{F.LIGHTRED_EX}Invalid range input, please enter in a \"$10-100\" format...")
                            reset_colour()
                        else:
                            if (isinstance(formattedRange, int)):
                                hotelDB.search_for_range_of_cost(formattedRange, formattedRange)
                            else:
                                hotelDB.search_for_range_of_cost(formattedRange[0], formattedRange[1])

        elif (uInput == "2"):
            # add new record
            while (1):
                packageName = customerName = ""
                paxNum = costperPax = 0
                continueFlag = 1

                while (continueFlag):
                    print()
                    packageNameInput = input("Enter the package name (F to cancel): ").lower().strip()
                    if (packageNameInput == "f"):
                        continueFlag = 0
                        break
                    elif (packageNameInput == ""):
                        print(f"{F.LIGHTRED_EX}Package name cannot be empty, please enter a valid package name...")
                        reset_colour()
                    else:
                        packageName = packageNameInput
                        break

                while (continueFlag):
                    customerNameInput = input("Enter the customer name (F to cancel): ").lower().strip()
                    if (customerNameInput == "f"):
                        continueFlag = 0
                        break
                    elif (customerNameInput == ""):
                        print(f"{F.LIGHTRED_EX}Customer name cannot be empty, please enter a valid customer name...")
                        reset_colour()
                    else:
                        customerName = customerNameInput
                        break

                while (continueFlag):
                    paxNumInput = input("Enter the number of pax (F to cancel): ").lower().strip()
                    if (paxNumInput == "f"):
                        continueFlag = 0
                        break
                    elif (paxNumInput == ""):
                        print(f"{F.LIGHTRED_EX}Input cannot be empty, please enter a valid pax number of pax...")
                        reset_colour()
                    elif (not re.fullmatch(r"^\d+$", paxNumInput)):
                        print(f"{F.LIGHTRED_EX}Invalid input, please enter a valid pax number of pax...")
                        reset_colour()
                    else:
                        paxNum = paxNumInput
                        break

                while (continueFlag):
                    costperPaxInput = input("Enter the package cost per pax (F to cancel): $").lower().strip()
                    if (costperPaxInput == "f"):
                        continueFlag = 0
                        break
                    elif (costperPaxInput == ""):
                        print(f"{F.LIGHTRED_EX}Package cost per pax cannot be empty, please enter a valid cost per pax...")
                        reset_colour()
                    elif (not re.fullmatch(r"^\d+\.?\d*$", costperPaxInput)):
                        print(f"{F.LIGHTRED_EX}Invalid package cost per pax, please enter a valid cost per pax...")
                        reset_colour()
                    else:
                        costperPax = costperPaxInput
                        break

                if (continueFlag):
                    print(print_record_data(packageName, customerName, paxNum, costperPax))
                    addConfirmation = get_input(prompt="Is this information correct? (y/n): ", command=("y", "n"), warning="Invalid confirmation input, please enter a valid confirmation command...")
                    if (addConfirmation == "y"):
                        hotelDB.add_record(packageName, customerName, paxNum, costperPax)
                        print(f"{F.LIGHTGREEN_EX}Record added successfully...")
                        reset_colour()
                else:
                    break

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
                            reset_colour()
                        else:
                            hotelDB.search_for_customer(customerName)
                elif (subInput == "2"):
                    # Search record by Package Name using Binary Search and update record
                    while (1):
                        packageName = input("Enter the package name (F to cancel): ").lower().strip()
                        if (packageName == "f"):
                            break
                        elif (packageName == ""):
                            print(f"{F.LIGHTRED_EX}Package name cannot be empty, please enter a valid package name...")
                            reset_colour()
                        else:
                            hotelDB.search_for_package(packageName)
                
        elif (uInput == "4"):
            # sort options
            subInput = ""
            while (subInput != "f"):
                print_sub_menu(4)
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "3", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
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

        elif (uInput == "5"):
            # delete options
            subInput = ""
            while (subInput != "f"):
                print_sub_menu(5)
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                if (subInput == "1"):
                    # Delete record by customer name
                    pass
                elif (subInput == "2"):
                    # Delete record by package name
                    pass

if __name__ == "__main__":
    coloramaInit(autoreset=0, convert=1)
    main()
    # try:
    #     main()
    # except KeyboardInterrupt:
    #     # shutdown(1)
    #     pass
    # except SystemExit:
    #     shutdown(1)
    # finally:
    #     sysExit(0)