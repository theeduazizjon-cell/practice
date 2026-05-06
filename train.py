"""
I - Task 

Masalaning  sharti: Shunday function tuzing, unga string argument pass bolsin. 
Function ushbu argumentdagi digitlarni yangi stringda return qilsin. 

Masalan: get_digits("m14ii1t")
return qiladi "141"

Masalaning yechimi: 
"""


def get_digits(text):
    result = ""

    for char in text:
        if '0' <= char <= '9':
            result += char

    return result


print(get_digits("m14ii1t"))


"""
G - Task 

Masalaning sharti: Shunday function tuzingki unga integralardan iborat array pass bolsin va function bizga 
osha arrayning eng katta qiymatiga tegishli indexni qaytarsin. 

Masalan: get_highest_index([5, 21, 12, 21, 8])
return qiladi 1 sonini

Masalaning yechimi:

def get_highest_index(arr):
    max_value = arr[0]
    max_index = 0

    for i in range(len(arr)):
        if arr[i] > max_value:
            max_value = arr[i]
            max_index = i

    return max_index


print(get_highest_index([5, 21, 12, 21, 8]))


"""
