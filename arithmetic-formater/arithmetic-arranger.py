def arithmetic_arranger(problems, solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_value = []
    second_value = []
    operator = []

    for problem in problems:
        pieces = problem.split()
        first_value.append(pieces[0])
        operator.append(pieces[1])
        second_value.append(pieces[2])

    if "*" in operator or "/" in operator:
        return "Error: Operator must be '+' or '-'."


    for i in range(len(first_value)):
        if not (first_value[i].isdigit() and second_value[i].isdigit()):
            return "Error: Numbers must only contain digits."

    for i in range(len(first_value)):
        if len(first_value[i]) > 4 or len(second_value[i]) > 4:
            return "Error: Numbers cannot be more than four digits."

    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    for i in range(len(first_value)):
        if len(first_value[i]) > len(second_value[i]):
            first_line.append(" "*2 + first_value[i])
        else:
            first_line.append(" "*(len(second_value[i]) - len(first_value[i]) + 2) + first_value[i])

    for i in range(len(second_value)):
        if len(second_value[i]) > len(first_value[i]):
            second_line.append(operator[i] + " " + second_value[i])
        else:
            second_line.append(operator[i] + " "*(len(first_value[i]) - len(second_value[i]) + 1) + second_value[i])

    for i in range(len(first_value)):
        third_line.append("-"*(max(len(first_value[i]), len(second_value[i])) + 2))

    if solution:
        for i in range(len(first_value)):
            if operator[i] == "+":
                ans = str(int(first_value[i]) + int(second_value[i]))
            else:
                ans = str(int(first_value[i]) - int(second_value[i]))
            if len(ans) > max(len(first_value[i]), len(second_value[i])):
                fourth_line.append(" " + ans)
            else:
                fourth_line.append(" "*(max(len(first_value[i]), len(second_value[i])) - len(ans) + 2) + ans)
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
    else:
        arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
    return arranged_problems