import json
from datetime import date

file = "sales.json"

def add_sales():
    item =input("enter item sold: ")
    quantity = int(input("enter quantity sold: "))
    amount = float(input("enter amount for items: "))
    totalamount = quantity * amount
    today = str(date.today())


    sale = {
        "item":item,
        "quantity":quantity,
        "amount":amount,
        "totalamount":totalamount,
        "today":today
        }
    try:
        with open(file,"r") as f:
            data = json.load(f)
            data.append(sale)
    except  FileNotFoundError:
        data = [sale]
    with open(file, "w")as f:
        json.dump(data, f, indent=4)

    print("sale record added succesful")
    
add_sales()    