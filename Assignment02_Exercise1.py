#Exercise1

# Part 1
#my favorite tea
tea = 'spearmint'
print(tea)
type(tea)

#Part2
print ("Null hypothesis: Eating ice cream does not improve mood")
null_hypothesis = "Null hypothesis: Eating ice cream does not improve mood"
print(null_hypothesis [0:4])
print(null_hypothesis [-4:])

#Part3
split_var = null_hypothesis.split()
print(split_var[1])            
print(split_var[1][1])         
split_by_colon = null_hypothesis.split(":")
hypothesis_word = split_var[1]                    
hypothesis_word_upper = hypothesis_word.upper()   
print(null_hypothesis.replace("hypothesis", hypothesis_word_upper))
print(hypothesis_word_upper.startswith("H"))     
print(len(null_hypothesis))      

#Part4
integer= 20
float = 0.6
print(type(integer), type(float))
print(integer + float)   
print(integer - float)
print(integer / float)
product = integer * float
print(product)

#Part5
subject_id = "s_01"
reaction_time = 0.48
print(f"The current subject is {subject_id}")
print(f"The current subject is {subject_id} and their reaction time is {reaction_time:.2f}")