print("Welcome To Finance Helper")

balancefile = open("balance.txt", "r")
current_balance = balancefile.read()
print("Your bank balance is:",current_balance)
bank_balance = float(current_balance)
balancefile.close()
print("You have", bank_balance, "dollars")
products = {}
while True:
  print("1 - Check your current balance ")
  print("2 - Add money into account ")
  print("3 - Spend Money ")
  print("4 - Get Advice")
  print("5 - See your products")
  print("6 - Exit ")
  choice = int(input("Enter your choice:"))
  if choice == 1:
    print(bank_balance)
  elif choice == 2:
    balancefile = open("balance.txt", "w")
    amount_of_money = int(input("How much money do you want to add"))
    source = input("Where is the money coming from?")
    balancefile.write(str(amount_of_money))
    balancefile.close()
  elif choice == 3:
    productsfile = open("products.txt", "w")
    balancefile = open("balance.txt", "w")
    thing = input("What do you spend your money on?")
    money = int(input("How much do you spend on it?"))
    balancefile.write(str(bank_balance-money))
    balancefile.close()
    print("I have added",thing,"to your list of products")
    products[thing] = money
    productsfile.write(str(products))
    productsfile.close()
  elif choice == 4:
    if income <= money:
      print("Your income is not enough to buy", thing, "try to stop buying",
            thing)
    print(products)
  elif choice == 5:
    print(products)
  else:
    break
