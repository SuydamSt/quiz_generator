def check_answer(user_answer, correct_answer):
    """check if the users answer matches the correct answer"""
    try:
        return float(user_answer) == float(correct_answer)
    except ValueError:
        return False