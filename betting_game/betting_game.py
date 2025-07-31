# global constants: 
# all CAP for constants we can just call function from the constants file.
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
# to get the amount of money the user wants to deposit
    while True:
        amount = input("What would you like to deposit? $")
        # check if the input is a valid number
        if amount.isdigit():
            #convert the input to an integer
            amount = int(amount)
            #check if the amount is greater than 0
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        # The + symbol is used to join (concatenate(1-3)) strings and variables.
        #str(MAX_LINES) converts the number into a string so it can be combined with other text.
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            #check if the number of lines is between 1 and 3
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                # f-string is used to format the string with a variable.
                print(f"Amount must be between {MIN_BET} - {MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


#call the functions
def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        if bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        
    #calculate the total bet
    total_bet = bet * lines
    print(f"You are betting ${bet} on {lines}. Total bet is equal to: ${total_bet}")

main()
