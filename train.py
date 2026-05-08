"""
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
