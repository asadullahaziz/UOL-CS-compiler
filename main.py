from lex import Lex

def main():
    l = Lex()

    infile = "sc.txt"
    outfile = "tokens.txt"
    l.scan(infile)
    write_tokens(l.tokens, outfile)


def write_tokens(array, filename):
    with open(filename, 'w') as file:
        for token in array:
            file.write(token.__repr__() + "\n")

if __name__ == "__main__":
    main()