import random
import time
def generate_random_problem():
    """Generate a random math problem."""
    number1 = random.randint(1, 25)
    number2 = random.randint(1, 25)
    operator = random.choice(['+', '-'])
    if operator == '+':
        solution = number1 + number2
    else:
        solution = number1 - number2
    problem = f"What is {number1} {operator} {number2}?"
    return problem, solution

def main():
    print("Welcome to the Math Quiz! You will need to solve 10 math problems!")

    score = 0
    num_problems = 10

    for _ in range(num_problems):
        problem, solution = generate_random_problem()
        print(problem)

        user_answer = input("Your answer: ")
        if user_answer.isdigit() and int(user_answer) == solution:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")

    print(f"\nQuiz complete! Your score: {score}/{num_problems}") 

if __name__ == '__main__':
    main()
time.sleep(6) #End of the code, made by FireShark224.