def separate_elements(mixed_list):
    integers, floats, strings = [], [], []
    for item in mixed_list:
        if isinstance(item, int):
            integers.append(item)
        elif isinstance(item, float):
            floats.append(item)
        elif isinstance(item, str):
            strings.append(item)
    return integers, floats, strings

mixed_list = [1, 2.5, 'hello', 3, 'world', 4.0]

integers, floats, strings = separate_elements(mixed_list)
print("Integers:", integers)
print("Floats:", floats)
print("Strings:", strings)