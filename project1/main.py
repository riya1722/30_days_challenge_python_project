import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3
symbols_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

symbols_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}
def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines



 
def auto_spin(balance):
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
        print("Not enough balance to start auto-spin.")
        return balance

    while True:
        spins_input = input("How many auto spins would you like to perform? ")
        if spins_input.isdigit():
            spins = int(spins_input)
            if spins > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        else:
            print("Please enter a valid number.")

    for spin_number in range(1, spins + 1):
        if balance < total_bet:
            print(f"\nSpin #{spin_number}: Insufficient balance to continue auto-spin.")
            break
        print(f"\nAuto Spin #{spin_number}")
        slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
        print_slot_machine(slots)
        winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
        balance += winnings - total_bet
        print(f"You won ${winnings}.")
        print("Winning lines:", *winning_lines)
        print(f"Current balance: ${balance}")
    return balance


def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,  symbols_count in symbols.items():
        for _ in range (symbols_count):
            all_symbols.append(symbol)
    columns=[]
    for col in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for row in range(rows):
            value=random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns) - 1:
               print(column[row], end=" | " )
               
            else:
               print(column[row],end="")
        print()
               
def deposit():
    while True:
        amount=input("What amount you want to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number .")
    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ") ?")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("Please enter valid number of lines.")
        else:
            print("Please enter a number .")
    return lines

def get_bet():
    while True:
        amount=input("What amount you want to bet? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number .")
    return amount
def spin(balance):
     lines=get_number_of_lines()
     while True:
      bet=get_bet()
      total_bet=bet*lines

      if total_bet > balance:
          print("You dont have enough balance. Your current balance is:  ${balance}")
      else:
          break

     print(f"You are betting ${bet} on {lines}. Total bet is equal to : ${total_bet}")
     slots=get_slot_machine_spin(ROWS,COLS ,symbols_count)
     print_slot_machine(slots)
     winnings,winning_lines=check_winnings(slots,lines,bet,symbols_value)
     print(f"You won ${winnings}.")
     print(f"You won on lines :",*winning_lines)
     return winnings-total_bet
def main():
  balance=deposit()
  while True:
      print(f"Current balance is ${balance}")
      answer = input("Press Enter to spin manually, type 'a' for auto-spin, or 'q' to quit: ")

      if answer == 'q':
        break
      elif answer == 'a':
       balance = auto_spin(balance)
      else:
        balance += spin(balance)
  print(f"You left with ${balance}")
main()