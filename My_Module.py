#part 4:
def new_function(teach):
    if teach=='anna':
        teacher='True'
        print('May be your teacher')
    else:
        teacher='False'
        print('Is not your teacher')
    
    return teacher

#part 5

#First the concepts, then a function including all

#Variable types - there are 2 types, strings and numeric: float and integers
string='A string is a line of textual data'
print(string)

#floating numeric variable types are numbers with a decimal point, where integers are whole numbers
floats=2.56
integers=2

#Here we test that it's actually the expected variable type
type(floats)
type(integers)
type(string)

#Lists and loops
#Lists are a list with multiple variables stored
list_grocery=['bread', 'milk', 'eggs']
print(list_grocery)

#Loops are blocks of code that repeats the same block of code - there are two common: for loops and while loops
#For loops - can be used to say 'for every item in this list, do the following to them' 
#So for example if you want a list and you would like it written out:
for groceries in list_grocery:
    print(groceries)

#While loops - only repeats the code while a certain statement is true
#So for example if you would like to only list the first 2 groceries:
amount_of_groceries=0
while amount_of_groceries<2:
    print(f'the first 2 groceries are: {list_grocery[amount_of_groceries]}')
    amount_of_groceries+=1

#Logical / relational operators
#Relational operators compares the relationship between two values
1<3
4!=5
3>6
#And many more

#Logical operators are combinations of several relational operators - all statements must be true, or one must be true:
4<3 and 5<6       #Both sides has to be true
6==6 or 7<1       #One or both sides has to be true
(7>9) != (6<8)    #Exactly one side has to be true
4<=5 and 6==6 and 3>=3       #They can be combined to create longer operators - filter data

#Function inputs and outputs
#Inputs are the data or values fed into the function and outputs are the resulting data or value after the code has run with the input
#If we would like to say happy birthday if it's someones birthday, and otherwise say hello:
def greeting(birthday_or_not):
    birthday='Happy birthdayyyyy!!!'
    no_birthday='Hello, long time no see'

    if birthday_or_not=='True':
        print(birthday)
        return birthday
    else:
        print(no_birthday)
        return no_birthday

greeting('True')
greeting('false')

#Modules - A way of storing code in seperate files, to keep it more organized, modules are the seperate files
#This whole document is a module, that can be imported to a new file


#The second part - combining it all:

#I will make a list of animals, that i then create a function for that only calls on the words with fewer than 6 letters and contains 
#an e in the name

animals=['dog', 'rabbit', 'horse', 'mouse', 'cat', 'fish', 'cow', 'antelope', 'boar', 'pig', 'goat', 'sheep', 'hare', 'chicken', 'lion', 'monkey', 'ostrich', 'bat', 'owl']

#I start off defining the animals with 5 or fewer letters that also contains an 'e':
def animals_with_e_less_than_6(animal_list):
    result=[]                                     #This creates an empty list with all the animals that fit both criteria
    for animal in animal_list:
        animal=animal.strip()                     #This removes any spaces 
        if len(animal)<6 and 'e' in animal:
            result.append(animal)                 #This adds the animal to the result list, if both conditions are true
    return result

correct_animals=animals_with_e_less_than_6(animals)

for animal in correct_animals:
    print(animal)

#Now to add a module, you could store the list and the definiton in a different file and then import it, to keep it more clean 
