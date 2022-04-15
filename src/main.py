from sys import exit as sysExit

try:
    from colorama import init as coloramaInit
except (ModuleNotFoundError, ImportError):
    print("Error importing third-party libraries needed for this program to work properly...")
    print("Please press ENTER to exit...")
    input()
    sysExit(1)

try:
    from functions import *
except (ModuleNotFoundError, ImportError):
    print("Error importing python files needed for this program to work properly... ")
    print("Please press ENTER to exit...")
    input()
    sysExit(1)
except SystemExit:
    sysExit(1)

def main():
    hotelDB = read_db_file()
    uInput = ""
    while (uInput != "x"):
        print_main_menu()
        uInput = get_input(prompt="Enter command: ", command=("1", "2", "3", "4", "x"), warning="Invalid command input, please enter a valid command from the menu above...")
        
        if (uInput == "x"): 
            shutdown()
        elif (uInput == "1"):
            # display options
            print_sub_menu(1)
            subInput = ""
            while (subInput != "f"):
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                if (subInput == "1"):
                    # display all records
                    pass
                elif (subInput == "2"):
                    # display records range from $X to $Y. e.g $100-200
                    pass
                
        elif (uInput == "2"):
            # add new record
            pass
        
        elif (uInput == "3"):
            # edit options
            print_sub_menu(3)
            subInput = ""
            while (subInput != "f"):
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                if (subInput == "1"):
                    # Search record by Customer Name using Linear Search and update record
                    pass
                elif (subInput == "2"):
                    # Search record by Package Name using Binary Search and update record
                    pass
                
        elif (uInput == "4"):
            # sort options
            print_sub_menu(4)
            subInput = ""
            while (subInput != "f"):
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "3", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                if (subInput == "1"):
                    # sort by customer name using bubble sort
                    pass
                elif (subInput == "2"):
                    # sort by package name using selection sort
                    pass
                elif (subInput == "3"):
                    # sort by package cost using insertion sort
                    pass
                
        elif (uInput == "5"):
            # delete options
            print_sub_menu(5)
            subInput = ""
            while (subInput != "f"):
                subInput = get_input(prompt="Enter option: ", command=("1", "2", "f"), warning="Invalid command input, please enter a valid option from the sub-menu above...")
                if (subInput == "1"):
                    # Delete record by customer name
                    pass
                elif (subInput == "2"):
                    # Delete record by package name
                    pass

if __name__ == "__main__":
    coloramaInit(autoreset=0, convert=1)
    try:
        main()
    except KeyboardInterrupt:
        # shutdown(1)
        pass
    except SystemExit:
        shutdown(1)
    finally:
        sysExit(0)