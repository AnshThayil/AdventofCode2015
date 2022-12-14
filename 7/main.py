import re
def solve_part_1(inp):
    # Logic here.
    vals = {}
    for i in re.finditer("^(-\d+|\d+) -> (\w+)$", inp, flags = re.MULTILINE):
        vals[i.group(2)] = int(i.group(1))
    return vals

def solve_part_2(inp):
    # Logic here.

    return 0

def ingest(name):
    # Edit parse process here.
    text_input = (open("./" + name)).read()
    # inp = text_input.split("\n")[:-1]
    return text_input

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
