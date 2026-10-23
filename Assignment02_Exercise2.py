
#Exercise2

#Part1
animals = ['cat', 'dog', 'cow', 'pig', 'sheep', 'horse', 'raven', 'fish', 'monkey', 'bear']
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
floating_points= [1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2, 10.2]
mixed= ['cat', 6, 3.2, 'sheep', 9, 10.2, 'raven', 7, 9.2, 'fish']
combined = [animals, integers, floating_points]

#Part2
print(animals[3])       
print(integers[3])    
print(floating_points[3])     
print(combined[0])    
print(combined[0][0]) 

#Part3
animals[0] = "bull"                  
animals.append("turtle")               
animals.insert(6, "rabbit")          
print(animals)

combined[0] = "word"              
print(combined)                  


