def reverse_string(input):
    """ Return reversed input string"""

    if len(input) == 0:
        return ""

    else:
        first_char = input[0]
        the_rest = slice(1, None)
        sub_string = input[the_rest]
        reversed_string = reverse_string(sub_string)
        return reverse_string + first_char
