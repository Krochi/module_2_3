my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
empty_current = 0

while empty_current < len(my_list):
    new_list = my_list[empty_current]
    if new_list > 0:
        print(new_list)
        empty_current += 1
    elif new_list <= 0:
        empty_current += 1
    else:
        break


my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0
while index < len(my_list):
    number = my_list[index]
    if number < 0:
        break
    if number > 0:
        print(number)
    index += 1

