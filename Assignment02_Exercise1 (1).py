
#This code was done by Maria Mihalka (MM)
#Exercise1

# Part 1
#my favorite tea
tea = 'spearmint'
print(tea)     #prints the value stored in "tea"
type(tea)      #prints the name of the type of the variable

#Part2
print ("Null hypothesis: Eating ice cream does not improve mood")      
null_hypothesis = "Null hypothesis: Eating ice cream does not improve mood"
print(null_hypothesis [0:4])      #prints the first four characters
print(null_hypothesis [-4:])      #prints the last four characters

#Part3
split_var = null_hypothesis.split()  #splits the variable by spaces
print(split_var[1])                  #prints the second word 
print(split_var[1][1])               #prints the second character of the second word
split_by_colon = null_hypothesis.split(":")         #splits it by the colon (:)
hypothesis_word = split_var[1]                      #prints the second character of the word "hypothesis" with the colon 
hypothesis_word_upper = hypothesis_word.upper()      #changes "hypothesis" to uppercase 
print(null_hypothesis.replace("hypothesis", hypothesis_word_upper))      #replaces the lowercase "hypothesis" with the uppercase one
print(hypothesis_word_upper.startswith("H"))           #tests whether the variable starts with "H"  
print(len(null_hypothesis))                            #prints the length of the variable   

#Part4
integer= 20         
float = 0.6
print(type(integer), type(float))       #prints the integer and floating point
print(integer + float)                  #adds the floating point to the integer 
print(integer - float)                  #subtracts the integer by the floating point 
print(integer / float)                  #divides the integer by the floating point
product = integer * float               #multiplies the integer by the floating point
print(product)

#Part5
subject_id = "s_01"                         
reaction_time = 0.48
print(f"The current subject is {subject_id}")             #prints the sentence in the f string with the variable stored in subject_id
print(f"The current subject is {subject_id} and their reaction time is {reaction_time:.2f}")     #prints the sentence in the f string with the subject_id and the reaction time with exactly two decimals
