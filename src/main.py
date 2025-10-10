from quiz_core.generator import generate_question
from quiz_core.evaluator import check_answer

def main():
    print("quiz:")

    question = generate_question()
    print("Question:", question["question"])
    user_answer = input("answer: ")

    if check_answer(user_answer, question["answer"]):
        print("correct")
    else:
        print("wrong")

if __name__ == "__main__":
    main()