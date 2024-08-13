my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i <= len(my_list):
    number_i = my_list[i]
    if number_i > 0:
        print(number_i)
    elif number_i < 0:
        break
    i = i + 1


