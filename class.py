

class creditCard():
    
    def __init__(self,customer, bank, acnt,limit):
        
        self.customer = customer
        self.bank = bank
        self.acnt =acnt
        self.limit = limit
        self.balance = 0
    
    def get_customer(self):
        return self.customer
    
    def get_bank(self):
        return self.bank
    
    def get_acnt(self):
        return self.acnt
    
    def get_limit(self):
        return self.limit
    
    def get_balance(self):
        return self.balance
    
    def charge(self,price):
        if price + self.balance > self.limit:
            return False
        
        else:
            self.balance +=price
            return True
    def make_payment(self,amount):
        self.balance -= amount
    
    
cc =creditCard( 'John Doe', '1st Bank' , '5391 0375 9387 5309' , 1000)

print(cc.get_acnt())