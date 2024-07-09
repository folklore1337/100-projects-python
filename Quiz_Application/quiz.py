import random
import psycopg2
from string import ascii_lowercase

DB_CONFIG = {
    'dbname': 'quizdb',
    'user': 'postgres',
    'password': '1234',
    'host': '127.0.0.1',
    'port': '5432'
}


NUM_QUESTIONS_PER_QUIZ = 5

def get_questions_from_db():
    conn = psycopg2.connect(**DB_CONFIG)
    questions = []
    with conn.cursor() as cur:
        cur.execute("""
            SELECT q.id, q.text, a.text, a.is_correct 
            FROM question q 
            JOIN answer a ON q.id = a.question_id
        """)
        rows = cur.fetchall()
    
    questions_dict = {}
    for row in rows:
        question_id, question_text, answer_text, is_correct = row
        if question_id not in questions_dict:
            questions_dict[question_id] = {"question": question_text, "answers": [], "alternatives": []}
        if is_correct:
            questions_dict[question_id]["answers"].append(answer_text)
        else:
            questions_dict[question_id]["alternatives"].append(answer_text)
    
    for question in questions_dict.values():
        questions.append(question)
    
    conn.close()
    return questions

def ask_question(question):
    correct_answers = question["answers"]
    alternatives = question["answers"] + question["alternatives"]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = get_answers(
        question=question["question"],
        alternatives=ordered_alternatives,
        num_choices=len(correct_answers),
    )
    if set(answers) == set(correct_answers):
        print("⭐ Correct! ⭐")
        return 1
    else:
        is_or_are = " is" if len(correct_answers) == 1 else "s are"
        print("\n- ".join([f"No, the correct answer{is_or_are}:"] + correct_answers))
        return 0

def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nChoice? ")) not in labeled_alternatives:
        print(f"Please answer one of {', '.join(labeled_alternatives)}")

    return labeled_alternatives[answer_label]

def get_answers(question, alternatives, num_choices=1):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while True:
        plural_s = "" if num_choices == 1 else f"s (choose {num_choices})"
        answer = input(f"\nChoice{plural_s}? ")
        answers = set(answer.replace(",", " ").split())

        # Handle invalid answers
        if len(answers) != num_choices:
            plural_s = "" if num_choices == 1 else "s, separated by comma"
            print(f"Please answer {num_choices} alternative{plural_s}")
            continue

        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers
        ):
            print(
                f"{invalid!r} is not a valid choice. "
                f"Please use {', '.join(labeled_alternatives)}"
            )
            continue

        return [labeled_alternatives[answer] for answer in answers]

def run_quiz():
    questions = get_questions_from_db()

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    print(f"\nYou got {num_correct} correct out of {num} questions")

if __name__ == "__main__":
    run_quiz()