class SessionMemory:
    def __init__(self):
        self.history = []

    def record(self, question_id, question_text, user_answer, score=None, feedback=None):
        self.history.append({
            "question_id": question_id,
            "question_text": question_text,
            "user_answer": user_answer,
            "score": score,
            "feedback": feedback
        })


    def get_history(self):
        return self.history

    def print_history(self):
        for i, entry in enumerate(self.history, start=1):
            print(f"\n--- Question {i} ---")
            print(f"Q: {entry['question_text']}")
            print(f"A: {entry['user_answer']}")
            if entry.get("score") is not None:
                print(f"Score: {entry['score']}/10")
            if entry.get("feedback"):
                print(f"Feedback: {entry['feedback']}")

