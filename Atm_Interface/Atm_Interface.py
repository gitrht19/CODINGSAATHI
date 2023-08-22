class account:
    def __init__(self,user_id,user_pin,balance=0):
        self.user_id=user_id
        self.user_pin=user_pin
        self.balance=balance
        self.transiction_history=[]
    
    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        self.balance += amount
        self.transiction_history.append(f"deposited: {amount}")
    
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transiction_history.append(f"withdraw : {amount}")
        else:
            print("jaa ke kama")
    def transfer(self,amount,target_amount):
        if amount <= self.balance:
            self.balance -= amount
            target_amount.balance += amount
            self.transiction_history.append(f"Transfred :{amount} to account {target_amount.user_id}")
        else:
            print("Phle paise kama le fir vejna")
        
    def get_transiction_history(self):
        return self.transiction_history
    
class ATM:
    def __init__(self):
        self.accounts = {} 
    
    def create_account(self,user_id, user_pin):
        if user_id not in self.accounts:
            self.accounts[user_id] = account(user_id,user_pin)
            print("account created successfully.")
        else:
            print("User id already exists. please choose diffrent id.")
    
    def login(self):
        user_id = input("Enter user id : ")
        user_pin = input("Enter user pin : ")
        
        if user_id in self.accounts and self.accounts[user_id].user_pin == user_pin:
            print("Login sucessful")
            return self.accounts[user_id]
        else:
            print("Invalid user id or pin")
            return None
        
    def atm_menu(self,account):
        while True:
            print("\nATM Functionalities : ")
            print("1. View Balance.")
            print("2. Deposit.")
            print("3. withdraw.")
            print("4. Transfer.")
            print("5. Transiction history.")
            print("6. Quit.")
            
            choice = input("Entet your choice...")
            
            if choice == "1":
                print(f"Balance: {account.get_balance()}")
                
            elif choice == "2":
                amount = float(input("Enter deposite amount : "))
                account.deposite(amount)
                
            elif choice == "3":
                amount = float(input("Enter withdraw amount : "))
                account.withdraw(amount)
                
            elif choice == "4":
                target_user_id = input("Enter target user id for transfer : ")
                if target_user_id in self.accounts:
                    target_account = self.accounts[target_user_id]
                    amount = float(input("Enter Transfer amount : "))
                    account.transfer(amount,target_account)
                else:
                    print("Target user id not found.")
                    
            elif choice == "5":
                print("transiction history")
                for transiction in account.get_transiction_history():
                    print(transiction)
                    
            elif choice == "6":
                print("Thank you for for using ATM . Good Bye!")
                break
            
            else:
                print("Invalid choice . Please try again.")
                
if __name__=="__main__":
    atm = ATM()
    
    while True:
        print("\nWelcome to the ATM ")
        print("1. Create Account")
        print("2. Login")
        print("3. Quit")
        
        main_choice = input("Ente your choice : ")
        
        if main_choice == "1":
            user_id = input("Enter user id : ")
            user_pin = input("Enter user pin : ")
            atm.create_account(user_id,user_pin)
        elif main_choice == "2":
            account = atm.login()
            if account:
                atm.atm_menu(account)
            else:
                print("Login failed. please try again.")
        elif main_choice == "3":
            print("Thank you for using ATM.")
            break
        else:
            print("Invalid choice, please try again.")