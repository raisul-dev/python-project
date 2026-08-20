#Bank account system use oop concept
class BankAccount :
  def __init__(self,id ,name,balance,):
    self.id = id
    self.name = name
    self.__balance = balance
#show accounts information
  def account_info(self):
    print(f"Name : {self.name}\nID : {self.id}")

#use gatter mathods and see blance
  def account_blance (self):
    print(f"Balance Is : {self.__balance}")

#use satter
  def deposit_balance(self,amount):
    if amount > 0 :
      self.__balance += amount
      print("Deposit Succesfull")

    else:
      print("Invalid Amount!")

  def withdraw_amount (self,amount):
    if amount<0 :
      print("Amount is Low")

    elif self.__balance <amount:
      print("insuffianc Balance")
    else:
      self.__balance -= amount
      print("Withdraw Succesfull")
      
#create object

acc1 = BankAccount(2343,'raisul Islam',2000)
#show Account information
acc1.account_info()
#show balance
acc1.account_blance()
acc1.withdraw_amount(200)
acc1.account_blance()
acc1.deposit_balance(1000)
acc1.account_blance()




