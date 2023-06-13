int_lists = [
    [3, 1, 2, 3, 2, 1],  # 0, 3
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # 1, -1 
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],  # 2, 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],  # 3, 2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],  # 4, 8
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],  # 5, 8
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],  #6, 2
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],  #7, 2
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],  #8, 1
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],  #9, 1
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],  #10, 2
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],  #11, 5
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],  #12, -1
]

def return_first_repeated_value():
    """iterate list and seeks for first repeated number occurence

    Returns:
        int: return first repeated occurence
    """
    number_ocurrence_set = set()
    repeated_number = -1

    for number in sub_list:
        if number in number_ocurrence_set:
            repeated_number = number
            break

        number_ocurrence_set.add(number)

    return repeated_number


for sub_list in int_lists:
    print(return_first_repeated_value())