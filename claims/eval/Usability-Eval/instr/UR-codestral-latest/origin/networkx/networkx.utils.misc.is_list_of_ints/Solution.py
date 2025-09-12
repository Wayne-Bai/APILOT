def is_list_of_ints(lst):
    return all(isinstance(x, int) for x in lst)
