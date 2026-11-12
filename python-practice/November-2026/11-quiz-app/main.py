# Topic: Building a Multiple Choice Quiz
# Date: 11-11-2026

from question import Mcq

question_prompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Mcq(question_prompts[0], "a"),
    Mcq(question_prompts[1], "c"),
    Mcq(question_prompts[2], "b"),
]

def run_test(quest_list):
    score = 0
    for q in quest_list:
        user_answer = input(q.prompt)
        if user_answer == q.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(quest_list)) + " correct")

run_test(questions)