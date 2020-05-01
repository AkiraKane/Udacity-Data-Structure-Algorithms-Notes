def nth_row_pascal(n):
    """
    :param: - n - index (0 based)
    return - list() representing nth row of Pascal's triangle
    """

    if n = 0:
        return [1]

    current_row = [1]
    for i in range(1, n):
        previous_row = current_row
        current_row = [1]

        for j in range(1, i):
            next_number = previous_row[j] + previous_row[j-1]
            current_row.append(next_number)
        current_row.append(1)

    return current_row
