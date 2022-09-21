# Pawan Kumar
# ID: 2046222
from decimal import Decimal

user_Lemon = float(input('Enter amount of lemon juice (in cups):\n'))
user_Water = float(input('Enter amount of water (in cups):\n'))
user_Agave = float(input('Enter amount of agave nectar (in cups):\n'))
user_servings = float(input('How many servings does this make?\n'))
print ('\nLemonade ingredients - yields',f"{user_servings:.2f}",'servings',)
print (f'{user_Lemon:.2f}','cup(s) lemon juice')
print (f'{user_Water:.2f}','cup(s) water')
print (f'{user_Agave:.2f}','cup(s) agave nectar')
serve_amt = float(input('\nHow many servings would you like to make?\n'))
calcServeAmt = (serve_amt / user_servings)
calcLemon = (calcServeAmt * user_Lemon)
calcWater = (calcServeAmt * user_Water)
calcAgave = (calcServeAmt * user_Agave)
print ('\nLemonade ingredients - yields',f'{serve_amt:.2f}','servings',)
print (f'{calcLemon:.2f}','cup(s) lemon juice',)
print (f'{calcWater:.2f}','cup(s) water',)
print (f'{calcAgave:.2f}','cup(s) agave nectar',)
Gal = 16.0
calcLemonGal = (calcLemon / Gal)
calcWaterGal = (calcWater / Gal)
calcAgaveGal = (calcAgave / Gal)
print ('\nLemonade ingredients - yields',f'{serve_amt:.2f}','servings',)
print (f'{calcLemonGal:.2f}','gallon(s) lemon juice')
print (f'{calcWaterGal:.2f}','gallon(s) water')
print (f'{calcAgaveGal:.2f}','gallon(s) agave nectar')