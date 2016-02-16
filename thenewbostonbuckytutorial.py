# printing
print('hello world')

# variable name with data attached
the_num_two = 2
the_num_three = 3
# printing addition problem using variables
print(the_num_two + the_num_three)

# subtraction
print(5-3)
# multiplying
print(2 * 3)

# dividing
print(10/2)

# dividing with rounding down
print(10//2)

# modulo
print(11%2)

# exponentiation
print(10**2)

# order of operations
print((10+2)*5)

# strings
# single quotation marks
print('what is going on')

# double quotation marks
# print("what's up")

# escaping a character
print('what\'s up')

# single quote string with escaping a character and double quotes as well
print('he said "what\'s up"')

# \n means go to new line in programming
# so putting r in front of string means print out raw string with no special meanings
print(r'C:\user\desktop\new')

# add strings together
let = 'let it '
snow = 'snow'
print(let + snow)

# multiply strings
print('hello '*5)

# indexes
# computers start at 0 not 1 and spaces count
candle = 'pine tree scent'
print(candle[0])

# go from right to left by using negative numbers
print(candle[-1])

# select any portion of an index
# [0:5] or [1:9]
# [:9] selects from the start to 9 and [4:] selects from 4 to the end
# [:] selects the whole thing
print(candle[0:4])

# find out the length of a string
print(len(candle))

# lists
players = [1, 2, 3, 4, 5]

# get item through index number
print(players[2])

# change item to new value
players[2] = 30
print(players)

# add a item onto list
players.append(6)
print(players)

# slice items from a list
print(players[0:2])

# set the slice to new items
players[0:2] = [0,0]
print(players)

# remove items from a list
players[0:2] = []
print(players)

# delete entire list
players[:] = []
print(players)

# if statements
age = 27
if age >= 21:
    print('You can buy beer')

# if elif and else statements
name = 'Arnold'
if name is 'Tom':
    print('Hellow Tom!')

elif name is 'Arnold':
    print('Hello Arnold!')

elif name is 'Frank':
    print('Hello Frank')

else:
    print('Please sign up for this site!')

# for loops
# for loops allows you take take a list and treat each item individually
foods = ['apples', 'bananas', 'avocados']
# f is a place holder for each item
# each time f loops it is equal to one of the items in the list, so first apples, then bananas, then avocados.
for f in foods:
    print(f)
    print(len(f))
# can also do just a slice of the list by doing- for f in foods[0:2]:

# range
for x in range(3):
    print('I like pie')
# this made a for loop for something 3 times
# if we printed x, it would print 0 1 2 each number under the other

# starting and ending range from what ever numbers you want
for x in range(3,7):
    print(x)

# range with 3 numbers
# start, stop, step
for x in range(0, 20, 5):
    print(x)

# while loops, loop as long as a condition is true
# if you don't put the spoon += 1 it will be an infinite loop
spoon = 5
while spoon < 10:
    print('big spoon')
    spoon += 1
# again remember the spoon +=1 or you can crash your computer

# break is used to stop an action once some desired outcome is met
magic_number = 26
for n in range(101):
    if n is magic_number:
        print(n, 'is the magic number!')
        break
    else:
        print(n)

