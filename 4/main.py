from hashlib import md5

def solve_part_1(inp):
    # Logic here.

    num = 0
    bool = True
    while (bool):
        numstr = inp + str(num)
        hashed = md5(numstr.encode()).hexdigest()
        if (hashed[:5] == "00000"):
            bool = False
        else:
            num += 1
    return num

def solve_part_2(inp):
    # Logic here.

    num = 0
    bool = True
    while (bool):
        numstr = inp + "{:05d}".format(num)
        hashed = md5(numstr.encode()).hexdigest()
        if (hashed[:6] == "000000"):
            bool = False
        else:
            num += 1
    return num

def ingest(name):
    # Edit parse process here.

    text_input = (open("./" + name)).read()
    inp = text_input.split("\n")[:-1]
    return inp[0]

def main():
    #Main function.

    sample_inp = ingest("sample_input.txt")
    problem_inp = ingest("problem_input.txt")

    sample_outp = solve_part_1(sample_inp)
    problem_outp = solve_part_1(problem_inp)

    print("---PART 1---")
    print("Sample Input Answer:", sample_outp)
    print("Problem Input Answer:", problem_outp)


    sample_outp = solve_part_2(sample_inp)
    problem_outp = solve_part_2(problem_inp)

    print("---PART 2---")
    print("Sample Input Answer:", sample_outp)
    print("Problem Input Answer:", problem_outp)

if __name__ == '__main__':
    main()
