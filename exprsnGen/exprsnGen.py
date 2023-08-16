import random
import operator

# Define the operators and their corresponding functions
operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def generate_expression():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator_symbol = random.choice(list(operators.keys()))
    expression = f"{num1} {operator_symbol} {num2}"
    return expression

def evaluate_expression(expression):
    num1, operator_symbol, num2 = expression.split()
    num1 = int(num1)
    num2 = int(num2)
    operation = operators[operator_symbol]
    result = operation(num1, num2)
    return result

def main():
    num_questions = 5

    print("Welcome to the Math Quiz!")
    print("Solve the following expressions:")

    correct_answers = 0
    for _ in range(num_questions):
        expression = generate_expression()
        print(f"What is the result of {expression}?")
        user_answer = float(input("Your answer: "))
        correct_answer = evaluate_expression(expression)
        if user_answer == correct_answer:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")

    print(f"You answered {correct_answers} out of {num_questions} questions correctly.")

if __name__ == "__main__":
	main()
