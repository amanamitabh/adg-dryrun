class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []
        self.transactions = []
        self.loans = []

    def create_account(self, account_holder, initial_balance):
        pass

    def get_account(self, account_number):
        return account
        

    def list_accounts(self):
        pass

    def close_account(self, account_number):
        pass

    def transfer_funds(self, from_account, to_account, amount):
        pass

    def generate_account_statement(self, account_number):
        pass

    def calculate_total_assets(self):
        pass

    def process_loan_payments(self):
        pass


class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def get_balance(self):
        pass

    def get_transaction_history(self):
        pass

    def apply_interest(self, rate):
        pass

    def overdraft_protection(self, amount):
        pass

    def update_contact_information(self, new_contact_info):
        pass


class Transaction:
    def __init__(self, transaction_id, account_number, amount, transaction_type, timestamp):
        self.transaction_id = transaction_id
        self.account_number = account_number
        self.amount = amount
        self.transaction_type = transaction_type
        self.timestamp = timestamp

    def process_transaction(self):
        pass

    def validate_transaction(self):
        pass

    def reverse_transaction(self):
        pass


class BankEmployee:
    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = name
        self.role = role

    def approve_loan(self, account_number, amount):
        pass

    def view_account_details(self, account_number):
        pass

    def suspend_account(self, account_number):
        pass

    def generate_financial_report(self):
        pass


class Loan:
    def __init__(self, loan_id, account_number, amount, interest_rate, tenure):
        self.loan_id = loan_id
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate
        self.tenure = tenure
        self.remaining_balance = amount

    def make_payment(self, amount):
        pass

    def get_remaining_balance(self):
        pass

    def calculate_interest(self):
        pass

    def check_loan_eligibility(self, account_number, income, credit_score):
        pass

    def restructure_loan(self, new_terms):
        pass
        print("Hi")
