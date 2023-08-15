# 3 Design a password strength checker that evaluates a password based on factors such as length, character types, and randomness.


# min 8 character(worse), moderate 10 character(good), max 15 character(best) password. -----> length.

# only number(worse), 
# latters with out upper case and lower case plus number(good), 
# latters with upper and lower case plus numbers(better),
# latters with out upper case and lower case plus number and special character(best), 
# latters with upper and lower case plus numbers and special character(great),

# using random ness test.

import string

def calculate_randomness_score(input_string):
    unique_chars = len(set(input_string))
    char_diversity_score = min(1.0, unique_chars / len(input_string))
    
    letter_ratio = sum(c.isalpha() for c in input_string) / len(input_string)
    digit_ratio = sum(c.isdigit() for c in input_string) / len(input_string)
    special_ratio = sum(not c.isalnum() for c in input_string) / len(input_string)
    
    distribution_score = max(letter_ratio, digit_ratio, special_ratio)
    
    pattern_count = 0
    for length in range(2, min(5, len(input_string))):
        patterns = set()
        for i in range(len(input_string) - length + 1):
            pattern = input_string[i:i+length]
            if pattern in patterns:
                pattern_count += 1
                break
            patterns.add(pattern)
    
    pattern_score = min(1.0, pattern_count / len(input_string))
    
    overall_score = (char_diversity_score + distribution_score + pattern_score) / 3.0
    randomness_score = round(overall_score * 10)
    
    return randomness_score

input_string = input("Please enter your password: ")
length_score = 0
char_score = 0

#length
if len(input_string) <= 8:
    length_score = 3
elif len(input_string) <= 10:
    length_score =  6
else:
   length_score = 9

#chartype
if input_string.isalnum():
    char_score = 9 
elif input_string.isnumeric():
    char_score = 3
elif input_string.isalpha():
    char_score = 6               
else:
    char_score = 10

# randomness check
randomness_score = calculate_randomness_score(input_string)

result = length_score + char_score + randomness_score

if result <= 21:
    print("bad password! :(")
elif result > 25:
    print("good! but needs more improvement :/ ")
else:
    print("great password! you are safe now :)")    


