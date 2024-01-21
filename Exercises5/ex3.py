def find_num[number_list]
    for iterate_number in number_list:
        if iterate_number % 2 == 0:
            return True
        else:
            return False

result = find_num(1,2,3,4,5,6,7,8)
print(result)