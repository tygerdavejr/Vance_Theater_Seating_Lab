# THEATER SEATING LAB
#
# David Vance
# Professor Kevin Chang
# CIS129 - Programming and Problemsolving I
# 18 October 2024
"""This program asks the user to input the number of tickets sold for each
section of the theater, conducts some entry validation on the values, and 
then calculates all the required sales totals."""


# INITIALIZING
# Import libraries, set constant values, and define functions

SECTION_A = 'A'
SEATS_AVAILABLE_A = 300
TICKET_COST_A = 20.00

SECTION_B = 'B'
SEATS_AVAILABLE_B = 500
TICKET_COST_B = 15.00

SECTION_C = 'C'
SEATS_AVAILABLE_C = 200
TICKET_COST_C = 10.00

section_tuple = (SECTION_A, SECTION_B, SECTION_C)
seating_tuple = (SEATS_AVAILABLE_A, SEATS_AVAILABLE_B, SEATS_AVAILABLE_C)
tickets_tuple = (TICKET_COST_A, TICKET_COST_B, TICKET_COST_C)

# Future expansion is made easy.  First, you simply need to declare constants
# in the same manner as above for section name, total number of seats
# available, and the cost per seat.  Next, expand each tuple with the  
# new section names.  For example:
#
# section_tuple = (SECTION_A, SECTION_B, SECTION_C, SECTION_D)
# 
# There is no need to alter any other code; everything else processes as a
# loop.


# MAIN FUNCTION
def main():
    """This program displays theater information, receives the number of
       ticket sales for each theater section, calculates ticket sales for
       each section, and then prints out a total of ticket sales."""

    # Display the greeting banner
    banner()

    # Initiate lists to receive back seats and tickets sold per section.
    seats_sold_per = []
    ticket_sales_per = []

    # Prime our ticket sales with 0.00 and execute for each section in the tuple
    total_ticket_sales = 0.00
     
    # While I could pass this information via repeated lines of constants, it 
    # just looks cleaner to put the constants in tuples and then manage 
    # processing as loops.
    # Future programmers never have to edit code outside of setting new 
    # constants and ensurint those are built into the tuple as discussed above.
    for section in range(len(section_tuple)):
        seats_sold, ticket_sales = (input_tickets_sold(section_tuple[section], \
                                                       seating_tuple[section], \
                                                       tickets_tuple[section]))
    
        # Append each section's seats and tickets sold to the respective list
        seats_sold_per.append(seats_sold)
        ticket_sales_per.append(ticket_sales)

        # Display a running total per each section which then becomes our total 
        # cumulative sales.
        total_ticket_sales += ticket_sales
        print(f'The cumulative ticket sales so far are ${total_ticket_sales:.2f}')

    
    display_final_totals(seats_sold_per, ticket_sales_per, total_ticket_sales)   
    
    return 

# Display banner and welcome message
def banner():
    """This module displays the welcome message and all the constant values.
       it neither receives or returns values."""

    print('*' * 71)
    print(" " * 24 + 'WELCOME TO STAGEMASTER')
    print('*' * 71)
    print('  STAGEMASTER IS YOUR ALL-SOURCE SYSTEM FOR DETERMINING TICKET SALES.')
    
    for section in range(len(section_tuple)):
        print(f'Section {section_tuple[section]} has a total of {seating_tuple[section]} seats at ${tickets_tuple[section]:.2f} per ticket.')

          
# Calculate ticket revenue
def calculate_ticket_sales(ticket_price, seats_sold):
    """This function receives the ticket price and total seats sold per section
       and does the actual math to determinine actual ticket sales.  It will
       then return the ticket sales for the single section.""" 
    # While it is a small module, keeping the calculations separate allows 
    # for future expandability, such as incorporating tax, costs, or other 
    # financial calculations as needed.
    ticket_sales = ticket_price * seats_sold
    
    return ticket_sales


# Input and validate entry of ticket sales
def input_tickets_sold(section_name, seats_available, ticket_price):
    """This module receives the section name, the total number of seats
    available for that section, and the price per tickets for that section.
    It then prompts the user for the number of tickets sold.  If the entry 
    is not a number, or if the value falls out of the expected range of 
    number of seats abailable it will display an error message and re-prompt
    the user for another entry.  When a correct value is entered, it will 
    dispay the total sales for that section and return the seats sold and
    the total ticket sales value."""
    # I input seats_sold as a string, which allows me to not worry about a 
    # non-integer breaking the program.  This also parses out floats, 
    # exponentials, expressions, and negatives.
    seats_sold = str(input(f'\nPlease enter the number of seats sold for Section {section_name} from 0 to {seats_available}: '))

    while not seats_sold.isnumeric() or int(seats_sold) > seats_available:
        print(f'{seats_sold} is either not a whole number or falls outside of expected range.')
        seats_sold = str(input(f'Please enter the number of seats sold for Section {section_name} from 0 to {seats_available}: '))
    
    # Convert seats_sold from string to integer
    seats_sold = int(seats_sold)

    # Call calculate_ticket_sales to determine amount of ticket sales
    ticket_sales = calculate_ticket_sales(ticket_price, seats_sold)
     
    return seats_sold, ticket_sales


# Display final results
def display_final_totals(seats_sold_per, ticket_sales_per, total_ticket_sales):
    """This module receives seats sold per section, ticket sales per section and
    total ticket sales.  It will then display the summary information, to 
    include information per section along with the cumulative total sales."""
        
    print('\n' + '-' * 71)
    print('The total breakdown for each section is as follows:')

    for section in range(len(seats_sold_per)):
        print(f'For Section {section_tuple[section]}, a total of {seats_sold_per[section]} tickets were sold for a total of $', end = '')
        print(f'{ticket_sales_per[section]:.2f}')
    
    print('\n' + '-' * 71)
    print(f'\nYOUR FINAL TOTAL TICKET SALES: ${total_ticket_sales:.2f}')
    print('\n' + '=' * 71)

    return


main()