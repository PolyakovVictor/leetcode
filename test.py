def count(list):
    if list == []:
        return 0
    max_num = list[0]
    if list[1:] > max_num:
        max_num = list[1:]
    return


print(count(list=[1, 2, 3, 4]))
