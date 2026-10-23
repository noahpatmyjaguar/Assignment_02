
#This code was done by Maria Mihalka (MM)
#Exercise2

#Part1
animals = ['cat', 'dog', 'cow', 'pig', 'sheep', 'horse', 'raven', 'fish', 'monkey', 'bear']   #all string values
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     #all integers
floating_points= [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2]      #all floating points
mixed= ['cat', 6, 3.2, 'sheep', 9, 10.2, 'raven', 7, 9.2, 'fish']     #mixing the three lists
combined = [animals, integers, floating_points]        #combines the three lists, storing each list as a variable

#Part2

print(animals[3])       #prints the fourth item of the list
print(integers[3])      #prints the fourth item of the list
print(floating_points[3])     #prints the fourth item of the list
print(combined[0])       #print the whole first list
print(combined[0][0])    #prints the first word on the first list

#Part3
animals[0] = "bull"           #replaces the first item on the list      
animals.append("turtle")      #adds an item to the end of the list        
animals.insert(6, "rabbit")   #adds an item to a specific position on the list  
print(animals)                #print the updated list

combined[0] = "word"          #changes the whole first list with the word "word"    
print(combined)                  


