# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

string_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
string_str = string_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in string_str:
	if char in count:
		count[char] +=1
print(count)