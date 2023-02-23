import string

vowels = {'A', 'E', 'I', 'O', 'U'}

alphabet = set(string.ascii_uppercase)

digits = set(string.digits)

print(digits.isdisjoint(alphabet))

print(alphabet)



#loop through vowels
#membership test
#if letter in alphabet, set flag to true
# else change to false, break loop

# is_related = None

for letter in vowels:
    if letter in alphabet:
        is_related = True
    else:
        is_related = False
        break

if is_related is True:
    print("it's related!")


#isdisjoint() - True if two sets have a null intersection (ie. no members in common).

#issubset() / <= - True if another set contains this set.

# issuperset() / >= True if this set contains another set.