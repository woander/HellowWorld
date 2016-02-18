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

# bucky's test
# make a program to loop through the numbers 1 to 100 and
# print out any number that is a multiple of 4
for n in range(101):
    if n%4 is 0:
        print(n)

# continue
# continue skips whatever is underneath it only when if statement is met
# and starts the next item in a loop
numbers_taken = [2, 5, 12, 13, 17]
print('Here are the numbers still available:')
for n in range(1, 20):
    if n in numbers_taken:
        continue
    print(n)

# functions
# functions break up the program into manageable chunks and help organize your program better
# functions can be reused
def banana():
    print('I like bananas')

banana()

def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)

bitcoin_to_usd(3.75)

# return
# return allows you to save a value for later use
def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age

my_dating_age = allowed_dating_age(27)
print('I can date girls', my_dating_age, 'years old or older')

# buckys age table test
for x in range(15, 61):
    print('a person at the age of', x, 'is allowed to date a person as young as', allowed_dating_age(x))

# default arguments
# arguments are the things inside () in functions
def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)

get_gender('m')
get_gender('f')
get_gender()

# variable scope
# a variable created outside a function will work for any function that comes after it
# a variable created inside a function, will only work for that function

# keyword arguments
def pizza_maker(who='Joe', type='plain', when='Friday'):
    print(who, type, when)

pizza_maker()
pizza_maker('doug', 'extra cheese', 'Saturday')

# it doesn't matter what order you type the arguments in
# and it will fill in the defaults if you leave any out
pizza_maker(when='Sunday', type='avocado')

# how to make a function that takes any amount of arguments
# it's common among python programmers to name the flexible argument args
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(5, 10)

# unpacking arguments
def health_calculator(age, healthy_foods_eaten, junk_foods_eaten):
    answer = (100-age) + (healthy_foods_eaten*3) - (junk_foods_eaten*2)
    print(answer)

kyles_data = [27, 10, 1]

# the old way to add this data in to the function would be
health_calculator(kyles_data[0], kyles_data[1], kyles_data[2])

# quicker way to do the above would be to unpack the argument list
# like so
health_calculator(*kyles_data)

# set
# sets are like a collection of items but can't have any duplicates like a list can
groceries = {'bananas', 'apples', 'avocados', 'apples', 'tea'}
print(groceries)

if 'apples' in groceries:
    print('You already have apples')
else:
    print('Apples are a great idea')

# dictionary
# in a real life dictionary we have words and definitions
# but in a python dictionary we have keys and values
beer = {'blue point': ' blueberry', 'budweiser': ' bud light', 'blue moon': ' belgian white'}
print(beer)
print(beer['blue point'])

# .items() makes it recognized as a set or a collection of stuff not just a variabe
for k, v in beer.items():
    print(k + v)

# modules
# modules are a file that you store code in,
# such as a function, and you can import it into another file,
# so that you don't have to re-write it
import testmoduletutorial

import random

testmoduletutorial.my_first_module()

x = random.randrange(1, 1000)
print(x)

# downloading an image from the web
# import random was already done above, but if not you would need to
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url, full_name)

# the image we download will be in a tab under our projects
# IF YOU REMOVE THE NUMBER SIGN BELOW AND RUN THE PROGRAM, IT WILL DOWNLOAD THE IMAGE EVERY TIME YOU RUN IT
# I BELIEVE BECAUSE IT SAVES IT AS A RANDOM NUMBER NAME AND IT ONLY WON'T IF IT TRIES TO SAVE AS THAT NUMBER NAME AGAIN
# download_web_image('https://thenewboston.com/photos/users/2/resized/23471ba4417d650505928a0b1f1fd8b1.jpg')

# how to read and write files
fw = open('sample.txt', 'w')
fw.write('writing some stuff in my text file\n')
fw.write('here is more text\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

# downloading files from the web
# make url smaller and cleaner by storing it in a variable if you want
from urllib import request

goog_url = 'http://real-chart.finance.yahoo.com/table.csv?s=GOOG&a=07&b=19&c=2004&d=01&e=18&f=2016&g=m&ignore=.csv'

def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split('\\n')
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close()

download_stock_data(goog_url)