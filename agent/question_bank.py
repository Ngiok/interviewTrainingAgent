import json

class QuestionBank:
    def __init__(self, filepath="data/questions.json"):
        self.questions = []
        self.index = 0
        self.load_questions(filepath)

    def load_questions(self, filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                self.questions = json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load questions: {e}")
            self.questions = []

    def get_next_question(self):
        if self.index >= len(self.questions):
            return None
        question = self.questions[self.index]
        self.index += 1
        return question

    def reset(self):
        self.index = 0
