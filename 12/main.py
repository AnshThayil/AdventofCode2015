import re
from json import loads

def solve_part_1(inp):
    # Logic here.
    total = sum([int(num) for num in re.findall("\d+|-\d+", inp)])
    return total 

def solve_part_2(inp):
    # Logic here.
    return parse(loads(inp))

def parse(inp):
    if type(inp) == int:
        return inp
    if type(inp) == list:
        return sum([parse(inp) for inp in inp])
    if type(inp) != dict:
        return 0
    if 'red' in inp.values():
        return 0
    return parse(list(inp.values())) 

def ingest(name):
    # Edit parse process here.

    text_input = (open("./" + name)).read()
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
