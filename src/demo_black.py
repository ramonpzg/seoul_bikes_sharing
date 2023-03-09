def this_func(string1, string2):

    """I don't know what this does, but oh 🐋"""

    to_lower = string1.lower()

    to_upper = string2.upper()

    a_list_of_strings = list(to_lower, to_upper)

    a_dict_of_strings = {
        "item1": to_lower, "item2": to_upper, "item3": a_list_of_strings,
    }
    return a_dict_of_strings
