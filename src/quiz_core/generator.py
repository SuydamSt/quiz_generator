import random

def generate_question() -> dict:
    """generate a random maths question"""
    var_a, var_b = random.randint(1,10), random.randint(1,10)
    operator = random.choice(["+","-"])

    if operator == "+":
        answer=var_a+var_b
    elif operator == "-":
        answer=var_a-var_b

    question = f"what is {var_a} {operator} {var_b}"
    return {"question": question, "answer": answer}
