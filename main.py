from agent.flow_controller import FlowController
from agent.language import SUPPORTED_LANGUAGES, DEFAULT_LANGUAGE

def main():
    print("Select language:")
    for code, name in SUPPORTED_LANGUAGES.items():
        print(f"{code}: {name}")
    choice = input("\nEnter language code (default is 'en'): ").strip().lower()
    language = choice if choice in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE

    print("\nSelect difficulty:")
    difficulties = ["junior", "mid", "senior"]
    for i, diff in enumerate(difficulties, 1):
        print(f"{i}. {diff}")
    diff_input = input("Choose a number (default is 1): ").strip()
    difficulty = difficulties[int(diff_input) - 1] if diff_input.isdigit() and 1 <= int(diff_input) <= 3 else "junior"

    print("\nSelect category:")
    categories = ["fundamentals", "concurrency", "data structures"]
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")
    cat_input = input("Choose a number (default is 1): ").strip()
    category = categories[int(cat_input) - 1] if cat_input.isdigit() and 1 <= int(cat_input) <= len(categories) else "fundamentals"

    controller = FlowController(language=language, difficulty=difficulty, category=category)
    controller.start_interview()

if __name__ == "__main__":
    main()
