from itertools import groupby

if __name__ == '__main__':
    output = []
    for a, b in groupby((raw_input()), int):
        output.append((len(list(b)), a))

    print
    " ".join(map(str, output))