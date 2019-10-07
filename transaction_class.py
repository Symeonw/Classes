import datetime

#Transaction entry system
#Primary function is to take transactional details, create a transaction number
#and store it into a dictionary
input_1 = input("Please input transaction date as mm/dd/yy: ")
input_2 = input("Please input transaction amount: ")
input_3 = input("Please input name of transaction: ")
input_4 = input("Please input description for the transaction: ")
transaction_dict = {}
class Transaction:
    num_of_trans = 0
    def __init__(self,trans_num, date, amount, name, desc):
        self.trans_num = trans_num
        self.date = date
        self.amount = amount
        self.name = name
        self.desc = desc
        Transaction.num_of_trans += 1
    def full_details(self):
        return f"{self.date}, {self.amount}, {self.name}, {self.desc}."
    @classmethod
    def trans_number(cls):
        cls.trans_num = cls(f"{date}-{num_of_trans}")
    @staticmethod
    def store_in_dict():
        transaction_dict.update({Transaction.trans_number(trans):trans.full_details()})


        
trans = Transaction(None,1, 2, 3,4)
transactions_dict = {}
transactions_dict.update({Transaction.trans_number():trans_1.full_details()})
print(transactions_dict)

