import random

def generate_task():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    op = random.choice(['+', '-', '*'])
    str_a, str_b = a, b
    if a < 0:
        str_a = f'({a})'
    if b < 0:
        str_b = f'({b})'
    task = f'{str_a} {op} {str_b}'
    answer = calculate_task(a, b, op)

    return [task, answer]

def calculate_task(a, b, operator):
    if operator == '+':
        answer = a + b
    elif operator == '-':
        answer = a - b
    else:
        answer = a * b
    
    return answer

def get_answers(answer):
    answers = [num for num in range(answer - 5, answer + 5)]
    answers.remove(answer)
    random.shuffle(answers)
    answers = answers[0:3]
    answers.append(answer)
    random.shuffle(answers)

    return answers
