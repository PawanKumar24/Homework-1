# Pawan Kumar
# ID: 2046222

import math

paintColors = {
   'red': 35,
   'blue': 25,
   'green': 23
}

wallHeight = float(input('Enter wall height (feet):\n'))
wallWidth = float(input('Enter wall width (feet):\n'))
wallArea = float(wallHeight * wallWidth)
print('Wall area:', int(wallArea), 'square feet')

area_per_gallon = float(1 / 350)
amt_paint = wallArea * area_per_gallon
print('Paint needed:', f'{amt_paint:.2f}', 'gallons')


paintCans = math.ceil(amt_paint)
print('Cans needed: %d can(s)' % (paintCans))

userColor = input('\nChoose a color to paint the wall:\n')
if userColor in paintColors:
  price = paintColors[userColor]
  totalPrice = int(price) * paintCans
  print('Cost of purchasing %s paint: $%d' % (userColor, totalPrice))
else:
  print('Invalid Color Choice!')