## COUNT LETTER ##

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
word = "mississippi"

# solution with letters string 
# def unique_english_letters(word):
# 	count = 0
# 	for letter in letters:
# 		if letter in word:
# 			count += 1
# 	return count

# soltuion without letters string
def unique_english_letters(word):
	my_list = []
	for letter in word:
		if letter in my_list:
			continue
		else: 
			my_list.append(letter)
	return(len(my_list))

# Uncomment these function calls to test your function:
# print(unique_english_letters("mississippi"))
# should print 4
# print(unique_english_letters("Apple"))
# should print 4

##COUNT X ##

# Write your count_char_x function here:
def count_char_x(word, letter):
	my_dict = {}
	for character in word:
		if character in my_dict.keys():
			my_dict[character] += 1
		else:
			my_dict[character] = 1
	return my_dict[letter]

# Uncomment these function calls to test your tip function:
# print(count_char_x("mississippi", "s"))
# should print 4
# print(count_char_x("mississippi", "m"))
# should print 1


## COUNT MULTI X ##
# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):

# Uncomment these function calls to test your function:
#print(count_multi_char_x("mississippi", "iss"))
# should print 2
#print(count_multi_char_x("apple", "pp"))
# should print 1

## SUBSTRING BETWEEN ##

# Write your substring_between_letters function here:

# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"