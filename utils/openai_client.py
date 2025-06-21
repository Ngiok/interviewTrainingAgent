import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def evaluate_answer(question, ideal_answer, user_answer):
    prompt = (
        "You are an expert in software engineering helping a junior programmer prepare for future technical interviews.\n\n"
        f"Question: {question}\n"
        f"Ideal answer: {ideal_answer}\n"
        f"Candidate's answer: {user_answer}\n\n"
        "Evaluate the candidate's answer. Assign a score from 0 to 10, and give a brief explanation to the junior programmer about why the answer is good, incomplete, or incorrect.\n"
        "Respond in strict JSON format like: {\"score\": <int>, \"feedback\": \"<brief explanation>\"}. Do not include anything else."
    )


    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        raw = response.choices[0].message.content.strip()

        # very basic JSON-safe eval
        if raw.startswith("{") and raw.endswith("}"):
            return eval(raw)  # replace later with `json.loads`
        else:
            return {"score": None, "feedback": raw}

    except Exception as e:
        print(f"[ERROR] Failed to evaluate answer: {e}")
        return {"score": None, "feedback": "Evaluation failed."}
