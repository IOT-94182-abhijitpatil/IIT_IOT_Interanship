
def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count


def count_consonants(s):
    count = 0
    for ch in s.lower():
        if ch.isalpha() and ch not in "aeiou":
            count += 1
    return count


def vowel_consonant_ratio(s):
    v = count_vowels(s)
    c = count_consonants(s)

    if c == 0:
        return "Consonants count is zero, ratio not possible"
    else:
        return v / c

# Main program
s = input("Enter a string: ")
ratio = vowel_consonant_ratio(s)
print("Ratio of vowels to consonants:", ratio)

