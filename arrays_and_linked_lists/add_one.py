def add_one(arr):
    """
    :param: arr - list of digits representing some number x
    return a list with digits represengint (x + 1)
    """

    output = 1

    for i in range(len(arr), 0, -1):
        output = output + arr[i-1]
        borrow = output // 10
        if borrow == 0:
            arr[i-1] = output
            break
        else:  # borrow == 1
            arr[i-1] = borrow % 10
            output = borrow

    arr = [borrow] + arr  # either [0] or [1]
    index = 0
    while arr[index] == 0:
        index += 1
    return arr[index:]
