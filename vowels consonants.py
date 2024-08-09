def count_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    
    for char in input_string:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return {'vowels': vowel_count, 'consonants': consonant_count}


result = count_vowels_consonants("hello world")
print(result)  
