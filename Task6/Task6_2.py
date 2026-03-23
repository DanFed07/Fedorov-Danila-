import string

def palindrome(s: str) -> bool:
    text = s.lower()
    for punctuation in string.punctuation + " ":
        text = text.replace(punctuation, "")
    return text == text[::-1]

assert palindrome("") == True
assert palindrome("a") == True
assert palindrome("aa") == True
assert palindrome("ab") == False

assert palindrome("12321") == True
assert palindrome("3.1413") == True
assert palindrome("12345") == False

assert palindrome("Лёша на полке клопа нашёл") == True
assert palindrome("А роза упала на лапу Азора") == True

assert palindrome("'Ура!', - вопите, дети, повару!") == True
assert palindrome("А за работу - дадут? - Оба раза!") == True
assert palindrome("Тестирование корректности работы со строками") == False