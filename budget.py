class ledgerObj():
    amount = float(0)
    description = ""

    def __init__ (self, amount, description):
        self.amount = float("{:.2f}".format(amount))
        self.description = description

class Category():

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        objStr = ""
        objStr = objStr + self.name.center(31, '*') + '\n'
        for elem in self.ledger:
            amount = format(elem.amount, '.2f')
            description = elem.description
            objStr = objStr + '{:<23} {:>7}'.format( str(description)[:23],  str(amount) ) + '\n'
        
        objStr = objStr + '{:<23} {:>7}'.format( "Total",  str(self.get_balance()) ) + '\n'
        return (objStr)
    
    def deposit(self, amount, description):
        obj = ledgerObj(amount, description)
        self.ledger.append(obj)

    def withdraw(self, amount, description):

        if self.check_funds(amount) :
            obj = ledgerObj(-amount, description)
            self.ledger.append(obj)
            return True
        else : return False


    def get_balance(self):
        balance = 0

        if len(self.ledger) < 1:
            return 0
        else:
            for elem in self.ledger:
                balance = balance + elem.amount
        
        return balance
    
    def check_funds(self, amount):
        balance = self.get_balance()

        if balance >= amount : return True
        else : return False

    def transfer(self, amount, category):
        if self.check_funds(amount) : 
            category.deposit(amount, "Transfer from " + self.name )
            self.withdraw(amount, "Transfer to " + category.name )
            return True
        else:
            return False
        
    def get_total_spences(self):
        
        total = 0

        if len(self.ledger) < 1:
            return 0
        else:
            for elem in self.ledger:
                if( elem.amount < 0):
                    total = total + elem.amount

        return round(total, 2)

def create_spend_chart(categories):
    
    print("Percentage spent by category")
    
    total = 0
    allPercentages = []
    names = []
    for category in categories:
        total = total + category.get_total_spences()
        names.append(category.name)

    for category in categories:
        allPercentages.append( ( (category.get_total_spences() / total * 100) // 10 ) * 10 )

    graph = ""
    for i in range(100, -1, -10):
        graph = graph + '{:>4}'.format((str(i) + "|"))
        for perc in allPercentages:
            if perc >= i:
                graph = graph + "\to"
            else:   
                graph = graph + "\t "
        graph = graph + "\n"

    graph = graph + "    "

    for i in names:
        graph = graph + "--------"

    graph = graph + "\n"

    print(graph)
    namesString = ""

    max_length = getMaxLen(names)

    for i in range(max_length):
        for w in names:
            w1 = w[i] if i < len(w) else " "
            namesString = namesString + '\t' + w1
        namesString = namesString + '\n'            

    print(namesString)
def getMaxLen(words):
    maxLen = 0

    for word in words:
        if maxLen < len(word):
            maxLen = len(word)
    return maxLen


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55, "")
clothing.withdraw(100, "")
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15, "")


print(food)
print(clothing)
print(auto)
create_spend_chart([food, clothing, auto])