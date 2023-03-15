def oxford_comma(items):
    if len(items) == 1:
        return  f"{items[0]}"
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else: 
        last = items.pop()
        first = f"{', '.join(items)},"
        return f'{first} and {last}'


