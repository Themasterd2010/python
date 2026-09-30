#inputs and varibles

def clac_costs():
    bathroom_total_cost = BATHROOM_COST * number_of_bathrooms
    other_room_total_cost = OTHER_ROOM_COST * number_of_other_rooms
    total_cost = SERCIVE_CHARGE + bathroom_total_cost + other_room_total_cost
    return total_cost

SERCIVE_CHARGE = 40.00
BATHROOM_COST = 15.00
OTHER_ROOM_COST = 10.00

name = input("what is your last name: ")
#think about what numerical values we need to convert to.. because we are going to have to ask the user for number of bathrooms and other rooms
#both of these things are whole numebers

number_of_bathrooms = int(input("How many bathrooms do you need cleaned? "))
number_of_other_rooms = int(input("How many other rooms do you need cleaned? "))

#processing and calculations
overall_total_cost = clac_costs()

#output
print("Hello, " + name)
print("Your overall cost including the service charge is:", overall_total_cost)
print("Thank you for using the best Indiana housekeeping service, " + name + "!")