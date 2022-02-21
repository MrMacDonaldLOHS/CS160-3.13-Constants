#Read through this code, and see how we use these constant values to make
#the code more understandable
PENNIES_PER_DOLLAR = 100
FEET_PER_MILE = 5280
INCHES_PER_FOOT = 12

pennies = int(input("How many pennies do you have? "))

dollars = pennies/PENNIES_PER_DOLLAR

print("You have $", dollars, sep='')

miles = float(input("How many miles do you live from school? "))

feet = FEET_PER_MILE * miles
inches = INCHES_PER_FOOT * feet


print("That means you live", feet, "away, or", inches,"inches" )
