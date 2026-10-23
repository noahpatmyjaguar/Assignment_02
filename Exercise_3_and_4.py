#Exercise 3 - AJ
#part 1 - Basic for loops, make a list with all five senses
senses=['smell', 'taste', 'touch', 'vision', 'hearing']
for sense in senses:
    print(senses)

#part 2 - Using counter variables, list the senses one by one
sense_number=0
for sense in senses:
    print(f'The sense is {sense}')
    sense_number += 1

#part 3 - For loops by list indexing, list it from first to tenth
numeric_order=['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 
                'eigth', 'ninth', 'tenth']
len(numeric_order)
len_order=len(numeric_order)
order_range=range(len_order)
print(order_range)
for index in order_range:
    print(numeric_order[index])

#part 4 - While loops, count the age by two until the age 30 is hit
counter=0
while counter<30:
    print(f'I am {counter}, not yet 30')
    counter +=2

#extra - Nested for loop, fruit list
fruits=['apple', 'banana', 'pear', 'grapes']
length=len(fruits)
order=range(length)
for fruit in fruits:
    for letter in fruit:
        print(letter)

#Exercise 4 - AJ
#part 1 - Defining simple functions 
def function():
    print('This is my first function')
function()

#part 2 - Relational operators, input
def function(relation_to_greeted_person):
    teacher='may be your teacher'
    no_teacher='is not your teacher'

    if relation_to_greeted_person=='anna':
        print(teacher)
        return teacher
    else:
        print(no_teacher)
        return no_teacher

function('anna')
function('amalie')

#part 3 - Relational operators, output
def new_function(teach):
    if teach=='anna':
        teacher='True'
        print('May be your teacher')
    else:
        teacher='False'
        print('Is not your teacher')
    
    return teacher


output=new_function('anna')
print(output)       
#I don't think teacher could've been reached, if "return" hadn't been used, 
# not where it's defined like this at least

#You could've gone like this:
def new_funct(teach):
    true='True'
    false='False'
    if teach=='anna':
        print(true)
    else:
        print(false)

new_funct('anna')
#And then written it like this being the answer of whether or not it was the teacher

#part 4 - Function stored in module - Made in a different document (My_Module)
import My_Module

professor=My_Module.new_function('anna')
print(professor)

#part 5 - Different functions stored in my module - they are in the module
