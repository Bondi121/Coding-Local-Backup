vowels = set()

vowels.add('A')


# print(vowels)

#is_member = "A" in vowels 

# print(is_member)

vowels.update('EIOU')

#print(vowels)

#example_1 = vowels.copy()
#example_1.clear() #removes elements from set
#print(example_1)


#example_2 = vowels.copy()
#example_2.remove ('E')
# example_2.remove ('F')
#print(example_2)


example_3 = vowels.copy()
example_3.discard('E')
example_3.discard('E') #no key error
print(example_3)

example_4 = vowels.copy()
vowel = example_4.pop()
print(example_4)
print(vowel)