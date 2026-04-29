first_list = ["Py", " ", "awes"]
second_list = ["thon", "is ", "ome"]


def combine_lists(first_list, second_list):
    final_list = []
    for index in range(len(first_list)):
        combined = first_list[index] + second_list[index]
        final_list.append(combined)
    return ( "".join(final_list) )

print(combine_lists(first_list, second_list))