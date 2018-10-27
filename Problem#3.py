# Problem: 3
# Takes the number of items bought by the user and returns the total bill according to the conditions based on number of items discount...

items = int(input("Number Of Items: "))
total_cost = 0

def Calc_Bill(items):
    if items >= 1 and items < 10:
        total_cost = items * 12
        return total_cost
    elif items >= 10 and items <= 99:
        total_cost = items * 10
        return total_cost
    elif items == 100 or items > 100:
        total_cost = items * 7
        return total_cost
    else:
        print("Invalid Number Of Items!, Try Again")


functionCall = Calc_Bill(items)
print("Total Bill:", str(functionCall) + "$")
