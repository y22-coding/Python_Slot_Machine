import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 3,
    "C" : 4,
    "D" : 3
}

symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns ,lines ,bet , values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols =[]

    for symbol, symblo_count in symbols.items():
        for _ in range(symblo_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(colmuns):
    for row in range(len(colmuns[0])):
        for i,column in enumerate(colmuns):
            if i != len(colmuns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()



def deposite():
    while True:
        amount = input('what would you like to deposite ? $')
        if amount.isdigit() :
            amount = int(amount)
            if amount>0:
                break
            else:
                print('please enter amount grater than 0.')
        else:
            print('please enter a number')
    
    return amount

def get_num_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+ str(MAX_LINES)+ ")?")
        if lines.isdigit() :
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print('enter valid number of lines')
        else:
            print('please enter a number')
    
    return lines


def get_bet():
    while True:
        bet = input('what would you like to bet ? $')
        if bet.isdigit() :
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'please enter amount between ${MIN_BET}-${MAX_BET}')
        else:
            print('please enter a number')
    
    return bet

def spin(balance):
    lines = get_num_of_lines()
    

    while True:
        bet = get_bet()
        total = bet * lines

        if total > balance:
            print(f'you have not enough balance to bet.your current balace is: ${balance}')
        else:
            break
    
    print(f"you are betting ${bet} on {lines} lines. total bet is {total}")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    Winnings,winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"you won : ${Winnings}")
    print(f"you won on lines:", *winning_lines)

    return Winnings - total



def main():
    balance = deposite()
    while True:
        print(f"current balance is:{balance}")
        answer = input("press enter to spin(q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"you left with ${balance}")

    

   
main()

     
