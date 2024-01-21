def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass

result = find_num([1,2,3,4,5,6,7,8], 8)
print(result)
# The function loos to see if no 9 is in the list of numbers and its not so the code teminates with pass