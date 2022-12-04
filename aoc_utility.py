def get_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    data = []
    for line in lines:
        line = line.strip('\n')
        if line:
            data += [line]
    return data


def replace_char(string, index, new_string):
    string = list(string)
    string[index] = new_string
    return "".join(string)