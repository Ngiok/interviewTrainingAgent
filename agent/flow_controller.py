from agent.question_bank import QuestionBank
from agent.memory import SessionMemory
from utils.openai_client import evaluate_answer

class FlowController:
    def __init__(self, language="en", difficulty="junior", category="fundamentals"):
        self.language = language
        self.memory = SessionMemory()
        self.qbank = QuestionBank(
            filepath="data/questions.json",
            category=category,
            difficulty=difficulty
        )

    def start_interview(self):
        print("\n=== Welcome to your technical interview practice ===")
        print("You will be asked a series of programming questions.\n")

        question_number = 1
        print("-------------------------------------------------")
        while True:
            question = self.qbank.get_next_question()
            if not question:
                print("\nInterview session complete.")
                break
                
            question_text = question["text"].get(self.language, question["text"]["en"])
            print(f"\nQuestion {question_number}: {question_text}")

            user_answer = input("Your answer: ").strip()

            eval_result = evaluate_answer(
                question=question["text"],
                ideal_answer=question["ideal_answer"],
                user_answer=user_answer,
                language=self.language
            )

            self.memory.record(
                question_id=question["id"],
                question_text=question["text"],
                user_answer=user_answer,
                score=eval_result.get("score"),
                feedback=eval_result.get("feedback")
            )

            print(f"\nScore: {eval_result.get('score')}/10")
            print(f"Feedback: {eval_result.get('feedback')}")
            print("\n-------------------------------------------------")
            question_number += 1

        print("\nSession Summary:")
        self.memory.print_history()
