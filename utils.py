def load_example():
    with open('./example.dat', 'r') as f:
        lines = f.readlines()
        return ''.join(lines)
