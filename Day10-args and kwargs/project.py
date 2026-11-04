#1. Shopping Bill Calculator
def shopping_bill(customer, *prices, discount=0, **details):
    total = sum(prices)

    final_amount = total - (total * discount / 100)

    print("\n----- SHOPPING BILL -----")
    print("Customer:", customer)

    for key, value in details.items():
        print(key, ":", value)

    print("Total:", total)
    print("Discount:", discount, "%")
    print("Final Amount:", final_amount)


shopping_bill(
    "Aaryal",
    100,
    200,
    300,
    discount=10,
    city="Bhaktapur",
    payment="Cash"
)


#2. Student Report Card System
def report_card(name, **marks):
    total = sum(marks.values())
    subjects = len(marks)
    average = total / subjects

    print("\n----- REPORT CARD -----")
    print("Student:", name)

    for subject, mark in marks.items():
        print(subject, ":", mark)

    print("Total Marks:", total)
    print("Average:", average)

    if average >= 40:
        print("Result: PASS")
    else:
        print("Result: FAIL")


report_card(
    "Aaryal",
    Python=85,
    Java=75,
    DBMS=80,
    AI=90
)


#. Momo Order Management System
def momo_order(customer, *items, **details):
    print("\n----- MOMO ORDER -----")

    print("Customer:", customer)

    print("Ordered Items:")
    for item in items:
        print("-", item)

    print("\nCustomer Details:")
    for key, value in details.items():
        print(key, ":", value)

    print("Order Confirmed!")


momo_items = ["Buff Momo", "Chicken Momo", "C-Momo"]

customer_details = {
    "address": "Bhaktapur",
    "payment": "Cash",
    "quantity": 3
}

momo_order(
    "Aaryal",
    *momo_items,
    **customer_details
)