# while

def search_while(x, lst):
    index = 0
    while index <= len(lst) - 1:
        if lst[index] == x:
            return f'True, {x}, index = {index}'
        index += 1
    return False


print(search_while(2, [123, 123, 2, 43, 534, 2]))

# for

def search_for(x, lst):
    for index in range(len(lst)):
        if lst[index] == x:
            return f'True, {x}, index = {index}'
    return False


print(search_for(2, [123, 123, 43, 534]))
