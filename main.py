class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
#printing string
    def __str__(self):
        cat_line = self.category.center(30, "*") + "\n"
        line = ""
        for i in self.ledger:
            line += i['description'].ljust(23)[:23] + "{:.2f}".format(i['amount']).rjust(7)[:7] + "\n"
        total = "Total: " + str(self.get_balance())
            
        return cat_line + line + total
        

#deposit function
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

#get current account balance
    def get_balance(self):
        return sum([i["amount"] for i in self.ledger])

#check_funds
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else: 
            return True

#withdraw function
    def withdraw (self, amount, description=""):
        if self.check_funds(amount): 
            self.ledger.append({"amount": (-amount), "description": description})
            return True
        else:
            return False

#transfer amount
    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        #Withdraw from current category
        self.ledger.append({"amount": (amount*-1), "description": f"Transfer to {category.category}"})
        #transfert toward destination category
        category.ledger.append({"amount": amount, "description": f"Transfer from {self.category}"})
        return True

#Check_funds method
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else: 
            return True

# Creation d'une visualisation par graphe
def create_spend_chart(categories):
    total_amount = 0
    for category in categories:
        for i in category.ledger:
            if i['amount'] < 0:
                total_amount += i['amount']
    #percentages = dictionnaire: category : %
    percentages = dict.fromkeys([x.category for x in categories])
    #calculate all percentages and store it into dict
    for category in categories:
        cat_expenses = 0
        for i in category.ledger:
            if i['amount']<0:
                cat_expenses += i['amount']
        percentages[category.category] = (cat_expenses / total_amount) * 100

    # printing graph 
    print("Percentage spent by category")
    for i in range(100, -10, -10): 
        line = str(i).rjust(3)+"|"
        for key in percentages:
            if percentages[key] >= i:
                line += "o".center(3)
            else:
                line += "   "
        print(line)
    print("    " + ("---"*(len(percentages)) + "-"))

    for i in range(max([len(key) for key in percentages])):
        line2 = "    "
        for key in percentages:
            if i < len(key):
                line2 += key[i].center(3)
            else:
                line2 += "   "
        print(line2)    

    


#testing part
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
clothing.deposit(500)
clothing.withdraw(30)
auto = Category("Auto")
auto.deposit(400)
auto.withdraw(60)

print(food, end = "\n\n\n")

create_spend_chart([food, clothing, auto])


