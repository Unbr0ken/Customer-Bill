#Customer Bill by Landon Weitenbeck
#This program will calculate a customer's bill from a resturant.

import sys

#Fixed Variables
BEEF_MEAL_COST = 15.95 #fixed cost for a single beef meal
CHICKEN_MEAL_COST = 13.95 #fixed cost for a single chicken meal
VEGAN_MEAL_COST = 10.95 #fixed cost for a single vegan meal
GRATUITY = 0.18 # fixed Amount of gratuity added to the whole meal cost
ROOM_TAX = 0.06 #fixed amount of tax taken from each room cost

#Asks for user input and  save it as a varible to be used later
#If input is over or under a certain amount print then exit
#Beef_meal input
beef_meal= int(input('Enter number of beef meals: '))        
if 0 > beef_meal > 200: 
    print('\nSorry, you have entered invaild data or entered a vaule over 200.\n')
    sys.exit()
#Chicken_meal Input
chicken_meal = int(input('\nEnter number of chicken meals: '))
if 0 > chicken_meal > 200:
    print('\nSorry, you have entered invaild data or entered a vaule over 200.')
    sys.exit() 
#Vegan_meal input
vegan_meal = int(input('\nEnter number of vegan meals: ')) 
if 0 > vegan_meal > 200:
    print('\nSorry, you have entered invaild data or entered a vaule over 200.')
    sys.exit()


#Varibles for meal
total_meals= beef_meal + chicken_meal + vegan_meal
beef_cost = beef_meal * BEEF_MEAL_COST 
chicken_cost = chicken_meal * CHICKEN_MEAL_COST 
vegan_cost = vegan_meal * VEGAN_MEAL_COST 
meals_cost = beef_cost + chicken_cost + vegan_cost
meals_gratuity = meals_cost * GRATUITY 
total_meals_cost = meals_gratuity + meals_cost 

#Varibles for room
#Checks to see if total_meals is within a certain amount and if so create a varible
if total_meals <= 0:
    print('\nYou must order something... Please come back later.')
    sys.exit()
elif total_meals > 0: 
    room_cost = 50
    room_tax_cost = room_cost * ROOM_TAX
elif total_meals > 30: 
    room_cost = 75
    room_tax_cost = room_cost * ROOM_TAX
elif total_meals >100: 
    room_cost = 200
    room_tax_cost = room_cost * ROOM_TAX
elif total_meals > 150: 
    room_cost = 250
    room_tax_cost = room_cost * ROOM_TAX
elif 200 < total_meals: 
    print('\n Unfortunately, our resturant does not have a large enough room to carter you. Have a nice day!')
    sys.exit()
total_room_cost = room_cost + room_tax_cost 

#Varibles for meal and room
total_cost = total_meals_cost + total_room_cost

#Print program (customer bill)
print('\n Catering Report by Landon Weitenbeck.\n')
print (f"{'Number in Party':<30s}{total_meals}")
print(f"{'Room Cost':<30s}${room_cost:.2f}") 
print(f"{'Room Tax':<30s}${room_tax_cost:.2f}\n")
if beef_meal != 0:
    print (f"{'Number of beef meal(s)':<30s}{beef_meal}")
    print(f"{'Cost of beef meal(s)':<30s}${beef_cost:.2f}")
if chicken_meal != 0:
    print (f"{'Number of chicken meal(s)':<30s}{chicken_meal}")
    print(f"{'Cost of chicken meal(s)':<30s}${chicken_cost:.2f}")
if vegan_meal != 0:
    print (f"{'Number of vegan meal(s)':<30s}{vegan_meal}")
    print(f"{'Cost of vegan meal':<30s}${vegan_cost:.2f}")
print(f"\n{'Total Cost':<30s}${total_cost:.2f}\n")
