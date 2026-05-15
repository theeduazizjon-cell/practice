"""
M-TASK

Masalaning sharti: 
Shunday function yozing, u string qabul qilsin va string palindrom yani togri oqilganda ham,
 orqasidan oqilganda ham bir hil oqiladigan soz ekanligini aniqlab boolean qiymat qaytarsin.


MASALAN: palindrom_check("dad") return True;  palindrom_check("son") return False;

Masalaning yechimi:

"""


def palindrom_check(text):
    cleaned_text = text.replace(" ", "").lower()
    return cleaned_text == cleaned_text[::-1]


print(palindrom_check("dad"))
print(palindrom_check("son"))


"""
K - Task 

Masalaning sharti:

Shunday function yozing, u string qabul qilsin 
va string ichidagi eng uzun sozni qaytarsin.

MASALAN: find_longest("I come from Uzbekistan") 
return "Uzbekistan"

Masalaning yechimi:

def find_longest(text):
    words = text.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


print(find_longest("I come from Uzbekistan"))

I - Task

Masalaning  sharti: Shunday function tuzing, unga string argument pass bolsin.
Function ushbu argumentdagi digitlarni yangi stringda return qilsin.

Masalan: get_digits("m14ii1t")
return qiladi "141"

Masalaning yechimi:

def get_digits(text):
    result = ""

    for char in text:
        if '0' <= char <= '9':
            result += char

    return result


print(get_digits("m14ii1t"))


"""
