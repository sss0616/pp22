import re

def snake_to_camel(snake_case):
    words = snake_case.split("_")
    camel_case = ''.join([words[0]] + [word.title() for word in words[1:]])
    return camel_case

snake_case_str = "this_is_snake_case"
camel_case_str = snake_to_camel(snake_case_str)
print(camel_case_str)

