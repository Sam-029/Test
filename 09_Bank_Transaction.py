"""
I implemented the logic form mine real world Bank Management System Project

Record a transaction and update the balance accordingly.
transaction_type: 'credit' or 'debit'
amount: the amount to be credited or debited and than.
Display the transaction history and final balance.
"""
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.transactions = []

    def record_transaction(self, transaction_type, amount):
        if transaction_type == 'credit':
            self.balance += amount
            self.transactions.append(f"Credited ${amount}")
        elif transaction_type == 'debit':
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Debited ${amount}")
            else:
                print("Insufficient balance for this debit transaction.")
                return
        else:
            print("Invalid transaction type. Please use 'credit' or 'debit'.")
            return
        print(f"Balance after transaction: ${self.balance}")

    def show_summary(self):
        print("\nTransaction Summary:")
        for transaction in self.transactions:
            print(transaction)
        print(f"\nFinal Balance: ${self.balance}")

def main():
    initial_balance = float(input("Enter initial balance: $"))
    account = BankAccount(initial_balance)
    while True:
        transaction_type = input("\nEnter transaction type (credit/debit) or 'exit' to stop: ").lower()

        if transaction_type == 'exit':
            break
        elif transaction_type not in ('credit', 'debit'):
            print("Invalid transaction type. Use 'credit' or 'debit'.")
            continue
        try:
            amount = float(input(f"Enter the amount to {transaction_type}: $"))
            if amount <= 0:
                print("Amount must be positive.")
                continue
                
        except ValueError:
            print("Invalid amount. Please enter a numerical value.")
            continue
        # Record the transaction and display the balance
        account.record_transaction(transaction_type, amount)

    account.show_summary()
if __name__ == "__main__":
    main()