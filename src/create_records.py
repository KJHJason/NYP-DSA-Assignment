from data import HotelDatabase

import re
numRegex = re.compile(r"^\d+$")

def main():
    numOfRecords = 0
    while (1):
        numOfRecords = input("Enter the number of records to generate: ")
        if (re.fullmatch(numRegex, numOfRecords)):
            numOfRecords = int(numOfRecords)
            break
        else:
            print("Invalid input. Please enter a number.")
    
    hotelDB = HotelDatabase()
    for i in range(numOfRecords):
        # wip
        print()
        
    return 0

if __name__ == "__main__":
    main()
    