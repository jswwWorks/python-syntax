def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    # YOUR CODE HERE
    current_number = start
    while current_number <= stop:
        print(current_number)
        current_number += 1


count_up(5, 7)
