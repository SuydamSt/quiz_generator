from quiz_core.generator import generate_question
from quiz_core.evaluator import check_answer

class QuizManager:
    """handles quiz logics"""

    def __init__(self):
        self.score = 0
        self.total = 0
        self.current_question = generate_question()

    def get_question(self):
        return self.current_question

    def submit_answer(self, user_answer):
        """check answer | update score | load next q"""
        correct = check_answer(user_answer, self.current_question["answer"])
        if correct:
            self.score+=1
        self.total+=1
        self.current_question = generate_question()
        return correct
    
    def get_score(self):
        return {"score": self.score, "total": self.total}
    
    def reset(self):
        self.score = 0
        self.total = 0
        self.current_question = generate_question()