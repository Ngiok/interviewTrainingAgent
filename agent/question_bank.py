import json

class QuestionBank:
    def __init__(self, filepath, category=None, difficulty=None):
        self.questions = []
        self.index = 0
        self.load_questions(filepath, category, difficulty)

    def load_questions(self, filepath, category, difficulty):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                all_questions = json.load(f)

            self.questions = [
                q for q in all_questions
                if (not category or q["category"] == category) and
                   (not difficulty or q["difficulty"] == difficulty)
            ]
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
