def solve_part_1(inp):
    # Logic here.
    
    return 0

def solve_part_2(inp):
    # Logic here.

    return 0

def ingest(name):
    # Edit parse process here.

    text_input = (open("./" + name)).read()
    inp = text_input.split("\n")[:-1]
    return [int(num) for num in inp]

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
