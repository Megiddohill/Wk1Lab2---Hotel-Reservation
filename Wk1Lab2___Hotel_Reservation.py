#David Prato
#CIS 376
#Lab Hotel Reservations

from datetime import datetime # This enables all the date and time functions
import locale #This enables world location information functions, currency, time zones, etc

run_again = 'y' #initially we want this to just be 'y' and we'll input the question later

while run_again.lower() == 'y': #The loop will run while this is "y"
    
    #-----ARRIVAL DATE SECTION ---------------------------#
    while True: # This loop will run while conditions are true
        date = input("Enter your arrival date in YYYY-MM-DD Format: ")
        try: #Try allows the following code to be tested while running the code. will return an error and try aain
            arrival_date = datetime.strptime(date, "%Y-%m-%d") #strips the inputted date of any time, and also reformats it based on our preference
        except ValueError: #the type of error we can expect and will return wht we code below
            print("Invalid date format")
            print()
            continue # continue will bring you back to the beginning of the loop you made


    #---- CHECKING THE INPUT DATE AGAINST TODAY SECTION --------#
        now = datetime.now() # Gets right now date and time
        today = datetime(now.year, now.month, now.day) # Takes "now" and strips it down to year, month, and date
        if arrival_date < today: #compares arrival date against "today"
            print("Date can't be earlier than today.")
            print()
        else:
            break  # break will simply end the loop and move on to the next line of code

    #------DEPARTURE DATE SECTION-----------------------------#
    while True:
        date = input("Enter your departure date in YYYY-MM-DD Format: ")
        try: 
            depart_date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Try again.")
            print()
            continue 
        
        if depart_date <= arrival_date: #can't leave on or before the day you arrive
            print("Departure Date must be at least one day after arrival date")
            print()
        else:
            break
    
    #---- CALCULATONS SECTION ---------------------------#
    rate = 85.0
    rate_message = ""
    if arrival_date.month == 8: #.month will be remembered thanks to "datetime"
        rate = 105.0
        rate_message = "(High Season)"
    total_nights = (depart_date - arrival_date).days #calculates from the .days function of "datetime" when we created these variables
    total_cost = rate * total_nights

    #----- FORMATTING RESULTS SECTION ------------------------#

    date_format = "%B %d, %Y" #again datetime allows this format to happen
    locale.setlocale(locale.LC_ALL, "en_US") #Sets the location...Here the LC_ALL overrides all other locations that might be in the code
    print(f"Arrival Date:    {arrival_date:{date_format}}")
    print(f"Departure Date:  {depart_date:{date_format}}")
    print(f"Nightly rate:    {locale.currency(rate)} {rate_message}")
    print(f"Total nights:    {total_nights}")
    print(f"Total price:     {locale.currency(total_cost)}")
    print()# This section was using various declarations (i.e. locale. rate_message}) to format the output of what we are printing

    #---- FINAL TOUCHES SECTION -------------------------------#
    run_again = input("Make another reservation? (y/n): ")
    print()

print("Thank you for using our Hotel!")
