#!/usr/bin/python3

class Checkbook:
    """
    A simple Checkbook class to simulate deposit and withdrawal operations.
    The class maintains the current balance and allows users to deposit, withdraw, and check the balance.

    Attributes:
        balance (float): The current balance in the checkbook.
    """

    def __init__(self):
        """
        Initializes a new Checkbook object with a starting balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook.

        Parameters:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook, if there are sufficient funds.

        Parameters:
            amount (float): The amount to withdraw.

        Returns:
            None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance in the checkbook.

        Returns:
            None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main function to simulate a checkbook management system where the user can deposit, withdraw, or check the balance.
    The user input is validated and appropriate error handling is implemented for invalid input.

    Returns:
        None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")

        if action.lower() == 'exit':
            print("Exiting the program.")
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount cannot be negative. Please enter a valid amount.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a valid number for the deposit.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount cannot be negative. Please enter a valid amount.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a valid number for the withdrawal.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
