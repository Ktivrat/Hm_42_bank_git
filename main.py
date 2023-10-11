from tabulate import tabulate

class Bank:
    def __init__(self):
        self.users = []
        self.user_id_counter = 1

    def add_user(self, first_name, last_name, postal_code):
        user = {
            "User ID": self.user_id_counter,
            "First Name": first_name,
            "Last Name": last_name,
            "Postal Code": postal_code,
            "Accounts": []
        }
        self.users.append(user)
        self.user_id_counter += 1
        
    def open_account(self, user_id, currency, balance):
        currencies = {"Dollar": "$", "Pound": "£", "Rupee": "₨"}
        user = next((user for user in self.users if user["User ID"] == user_id), None)
        if user:
            user["Accounts"].append(f"{currencies[currency]} - Balance: {balance}")
            
    def view_accounts(self):
        data = []
        for user in self.users:
            data.append({
                "User": f"{user['First Name']} {user['Last Name']}",
                "User ID": user["User ID"],
                "Postal Code": user["Postal Code"],
                "Accounts": ", ".join(user["Accounts"])
            })
        print(tabulate(data, headers="keys", tablefmt="grid"))
        
# Использования
bank = Bank()
bank.add_user("dod", "dop", "33333")
bank.add_user("Pop", "gop", "22222")
bank.add_user("Bob", "mop", "11111")

# Cчета для разных пользователей
bank.open_account(1, "Dollar", 1000)
bank.open_account(1, "Pound", 500)
bank.open_account(2, "Dollar", 200)
bank.open_account(3, "Rupee", 300)

# Учетные записи
bank.view_accounts()