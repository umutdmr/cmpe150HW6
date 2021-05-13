def my_sort(lst, length):
    """recursive sort function"""
    if length == 0:
        return lst
    for i in range(len(lst) - 1):
        if int(lst[i]) > int(lst[i + 1]):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return my_sort(lst, length - 1)


crime_scene = open("crime_scene.TXT", "r")
line_1 = crime_scene.readline().split()
weight = int(line_1[0])
time = int(line_1[1])
crime_scene.readline()
evidence_ls_weight = []
evidence_ls_time = []
evidence_ls_weight_time = []
id_dict = dict()
for i in crime_scene.readlines():
    evidence_ls_weight.append((int(i.split()[1]), int(i.split()[-1])))
    evidence_ls_time.append((int(i.split()[2]), int(i.split()[-1])))
    evidence_ls_weight_time.append(([int(i.split()[1]), int(i.split()[2])], int(i.split()[-1])))
    id_dict[i.split()[0]] = int(i.split()[-1])
crime_scene.close()


def solve(parts):
    length = len(parts)
    if length == 0:
        return
    elif length == 3:
        # part1 only weights
        id_list = []
        value = 0
        my_lst = evidence_ls_weight
        length = len(my_lst)
        limit = weight

        def f(limit, i=0):
            if i == length:
                return 0, []
            if limit - my_lst[i][0] >= 0:
                total, id_lst = f(limit - my_lst[i][0], i + 1)
                total += my_lst[i][1]
                id_lst.append(list(id_dict.keys())[i])
            else:
                total = 0
                id_lst = list()
            dont_add, dont_add_lst = f(limit, i + 1)
            if total > dont_add:
                return total, my_sort(id_lst, len(id_lst))
            else:
                return dont_add, my_sort(dont_add_lst, len(dont_add_lst))

        to_write = f(limit)
        part1 = open(parts[0], "w")
        part1.write(str(to_write[0]) + "\n")
        part1.write(" ".join(to_write[1]))
        part1.close()


    elif length == 2:
        # part2 only time
        id_list = []
        value = 0
        my_lst = evidence_ls_time
        length = len(my_lst)
        limit = time

        def f(limit, i=0):
            if i == length:
                return 0, []
            if limit - my_lst[i][0] >= 0:
                total, id_lst = f(limit - my_lst[i][0], i + 1)
                total += my_lst[i][1]
                id_lst.append(list(id_dict.keys())[i])
            else:
                total = 0
                id_lst = list()
            dont_add, dont_add_lst = f(limit, i + 1)
            if total > dont_add:
                return total, my_sort(id_lst, len(id_lst))
            else:
                return dont_add, my_sort(dont_add_lst, len(dont_add_lst))

        to_write = f(limit)
        part2 = open(parts[0], "w")
        part2.write(str(to_write[0]) + "\n")
        part2.write(" ".join(to_write[1]))
        part2.close()

    elif length == 1:
        # part3 time and weight
        id_list = []
        value = 0
        my_lst = evidence_ls_weight_time
        length = len(my_lst)
        limit1 = weight
        limit2 = time

        def f(limit1, limit2, i=0):
            if i == length:
                return 0, []
            if limit1 - my_lst[i][0][0] >= 0 and limit2 - my_lst[i][0][1] >= 0:
                total, id_lst = f(limit1 - my_lst[i][0][0], limit2 - my_lst[i][0][1], i + 1)
                total += my_lst[i][1]
                id_lst.append(list(id_dict.keys())[i])
            else:
                total = 0
                id_lst = list()
            dont_add, dont_add_lst = f(limit1, limit2, i + 1)
            if total > dont_add:
                return total, my_sort(id_lst, len(id_lst))
            else:
                return dont_add, my_sort(dont_add_lst, len(dont_add_lst))

        to_write = f(limit1, limit2)
        part3 = open(parts[0], "w")
        part3.write(str(to_write[0]) + "\n")
        part3.write(" ".join(to_write[1]))
        part3.close()

    return solve(parts[1:])


solve(["solution_part1.txt", "solution_part2.txt", "solution_part3.txt"])