def arithmetic_arranger(*problems):
    display_answers = False
    if len(problems) == 2 and problems[1] is True:
        display_answers = True
    
    instructions = problems[0]
    if len(instructions) > 5:
        return 'Error: Too many problems.'
    arranged_problems = ""
    for problem in instructions:
        operands = problem.split(' ')
        if len(operands) != 3:
            return 'Error: Invalid problem.'

        first_operand, operator, second_operand = operands
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'
        if (len(first_operand) > 1 and first_operand[0] == '0') or (len(second_operand) > 1 and second_operand[0] == '0'):
            return 'Error: Numbers cannot start with 0.'
        if operator != '+' and operator != '-':
            return 'Error: Operator must be \'+\' or \'-\'.'

    for i in range(len(instructions)):
        first_operand, operator, second_operand = instructions[i].split(' ')
        
        len_longest_operand = max(len(first_operand), len(second_operand))
        arranged_problems += ' ' * (len_longest_operand - len(first_operand) + 2) + first_operand
        
        if i < len(instructions) - 1:
            arranged_problems += ' ' * 4
    
    arranged_problems += '\n'
    
    for i in range(len(instructions)):
        first_operand, operator, second_operand = instructions[i].split(' ')

        len_longest_operand = max(len(first_operand), len(second_operand))
        arranged_problems += operator + ' ' + ' ' * (len_longest_operand - len(second_operand)) + second_operand

        if i < len(instructions) - 1:
            arranged_problems += ' ' * 4
            
    arranged_problems += '\n'

    for i in range(len(instructions)):
        first_operand, operator, second_operand = instructions[i].split(
            ' ')

        len_longest_operand = max(len(first_operand), len(second_operand))
        arranged_problems += '-' * (len_longest_operand + 2)

        if i < len(instructions) - 1:
            arranged_problems += ' ' * 4

    if display_answers:
        arranged_problems += '\n'

        for i in range(len(instructions)):
            first_operand, operator, second_operand = instructions[i].split(' ')

            len_longest_operand = max(len(first_operand), len(second_operand))
            if operator == '+':
                res = int(first_operand) + int(second_operand)
                arranged_problems += ' ' * \
                    (len_longest_operand - len(str(res)) + 2) + str(res)

            if operator == '-':
                res = int(first_operand) - int(second_operand)
                arranged_problems += ' ' * \
                    (len_longest_operand - len(str(res)) + 2) + str(res)

            if i < len(instructions) - 1:
                arranged_problems += ' ' * 4
            
    return arranged_problems
