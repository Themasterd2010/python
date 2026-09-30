def happy_birthday():
    print("Happy Birthday to You!")
    print("Happy Birthday to You!")
    print("Happy Birthday Dear " + name + "!")
    print("Happy Birthday to You!")


name = input("Please enter your name: ")
happy_birthday()
happy_birthday()
























total = 10.00
#we can also use functions for calculations
def calc_tax():
    Sales_TAX = 0.06
    total_with_tax = total +(total * Sales_TAX)
    print(total_with_tax)


#lets say instead of just printing the value, we went to store the result of our function calculation in a varible
#this is what tghe returen keyword does.. it returns the result of the calculation

def calc_tax_return():
    Sales_TAX = 0.06
    total_with_tax = total +(total * Sales_TAX)
    return total_with_tax

#run calc_tax
calc_tax()

#return functions have to have a varible to return dat into it
result = calc_tax_return()
print(result)


