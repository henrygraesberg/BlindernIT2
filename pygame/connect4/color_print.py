def print_red(string, sep=" ", end="\n"):
    print(f'\033[91m{string}\033[00m', sep=sep, end=end)

def print_green(string, sep=" ", end="\n"):
    print(f'\033[92m{string}\033[00m', sep=sep, end=end)

def print_yellow(string, sep=" ", end="\n"):
    print(f'\033[93m{string}\033[00m', sep=sep, end=end)

def print_blue(string, sep=" ", end="\n"):
    print(f'\033[94m{string}\033[00m', sep=sep, end=end)