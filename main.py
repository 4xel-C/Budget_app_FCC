class Category:
    withdraws = 0

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
            self.withdraws += amount
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
    total_withdraw = 0
    for category in categories:
        total_withdraw += category.withdraws
    #percentages = dictionnaire: category : %
    percentages = dict.fromkeys([x.category for x in categories])
    #calculate all percentages and store it into dict
    for category in categories:
        percentages[category.category] = (category.withdraws / total_withdraw) * 100

    # printing graph 
    graph = ""
    graph += "Percentage spent by category" + "\n"
    for i in range(100, -10, -10): 
        graph += str(i).rjust(3)+"|"
        for key in percentages:
            if percentages[key] >= i:
                graph += "o".center(3)
            else:
                graph += "   "
        graph += "\n"
    graph += "    " + ("---"*(len(percentages)) + "-" + "\n")

    for i in range(max([len(key) for key in percentages])):
        graph += "    "
        for key in percentages:
            if i < len(key):
                graph += key[i].center(3)
            else:
                graph += "   "
        if i < max([len(key) for key in percentages])-1:
            graph += "\n"
    return graph   

    


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

print(create_spend_chart([food, clothing, auto]))


