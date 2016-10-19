"""Reverse a given list."""


def reverse_list(input_list):
    """Input a list. Returns a reveresed list."""
    return input_list[::-1]

if __name__ == "__main__":
    input_list = list()
    val = True
    while val:
        val = raw_input("Enter list to be reversed"
                        ". Enter nothing to exit.")
        if val:
            input_list.append(
                int(val)) if val.isdigit() else input_list.append(val)
    print ''.join(["Input List: ", str(input_list)])
    print ''.join(["Output List: ", str(reverse_list(input_list))])
