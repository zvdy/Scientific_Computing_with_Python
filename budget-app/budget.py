"""
Final Project for FreeCodeCamp's Python Scientific Computinc course
Author: @zvdy
"""
def create_spend_chart(categories):
    title = 'Percentage spent by category'+ '\n'
    total = 0 
    counts = {} 
    percentage = {} 
    name_length = 0   
   

    for category in categories:
        countkey = category.wd_count() 
        counts[category.name] = countkey 
        total += countkey 


    for name, count in counts.items():
        percent = count / total * 100
        percentage[name] = percent
 
    """Y axis"""
    x = 100 
    for number in range(11):
        row = f"{x}".rjust(3) + "| "
        for name, percent in percentage.items():
            if percent >= (x):
                row += "o  "
            else:
                row += "   "
        title += row + '\n'
        x -= 10
   
    """X axis"""
    x_axis = "    -" 
    for category in categories:
        x_axis += ("---")
    title += x_axis + "\n"


    for category in categories:
        if len(category.name) > name_length:
            name_length = len(category.name)
 
    
    y = 0
    while y <= name_length:
        rows = "     "
        for key, value in percentage.items():
            category_name = key
            try:    
                rows +=  category_name[y] + "  "
            except: 
                rows += "   "
        
        if y <= name_length -1:
            title += rows + '\n' 
        else:
            title += rows.strip(" ")
           
        y = y + 1
    title = title.rstrip("\n")
    return title

class Category:

    def __init__(self, category):
        """Initialize the category."""
        self.name = category
        self.ledger = []

    def deposit(self, amount, description=""):
        """Add an amount to the ledger."""
        self.ledger.append({"amount": amount, "description": description})
        
    
    def withdraw(self, amount, description=""):
        """Withdraw an amount from the ledger."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    
    def get_balance(self):
        """Return the current balance of the ledger."""
        return sum([x["amount"] for x in self.ledger])

    
    def transfer(self, amount, category):
        """Transfer an amount to another category."""
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False


    def check_funds(self, amount):
        """Return True if there are enough funds."""
        if(self.get_balance() >= amount):
            return True
        return False

    def wd_count(self):
        """Return the total amount of withdrawals."""
        return sum([x["amount"] for x in self.ledger if x["amount"] < 0])

    def __str__(self):
        """Return the category in a string."""
        output = self.name.center(30, "*") + "\n"
        for item in self.ledger:
            output += item["description"][:23].ljust(23) + str("{:.2f}".format(item["amount"])).rjust(7) + "\n"
        output += "Total: " + str(self.get_balance())
        return output
