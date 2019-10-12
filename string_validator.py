
def string_validator(string):
    print(any(element.isalnum() for element in string))
    print(any(element.isalpha() for element in string))
    print(any(element.isdigit() for element in string))
    print(any(element.islower() for element in string))
    print(any(element.isupper() for element in string))

string_validator('Ussherk03')