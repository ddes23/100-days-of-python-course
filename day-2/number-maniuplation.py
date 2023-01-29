#python making rounding numbers easy. round()
print(round(8/3))

#Can round to a specific decimal place
print(8/3)
print(round(8/3, 3))

#floor division notation "//" will produce an int rather than a float

print( type( 8 // 3 ) )
print( type( 8 / 3 ) )

# use the += or (operator-equal) to manipulate a value based on it's previous value
score = 1
print (score)
score += 1
print (score)

#f-strings allow for mixing different data types, add 'f' to the beginning of your string, but must be outside your quotes

score = 0
height = 1.8
winning = True

print(f"your score is {score}, your height is {height}, you are winning is {winning}")