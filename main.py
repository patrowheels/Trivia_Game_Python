question_level = 0
score = 0

class Question:
    def __init__(self, prompt, a, b, c, d, answer):
        self.prompt = prompt
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.answer = answer
        
question_list = [
    Question(
        prompt = "Which of these countries borders Romania?",
        a = "Poland",
        b = "Moldova",
        c = "Turkiye",
        d = "Tanzania",
        answer = "Moldova",
    ),
    Question(
        prompt = "How many subspecies of tigers are there?",
        a = "9",
        b = "250",
        c = "3",
        d = "17",
        answer = "9",
    ),
    Question(
        prompt = "Which college owns scratch?",
        a = "Yale",
        b = "Texas Tech",
        c = "Stanford",
        d = "MIT",
        answer = "MIT",
    ),
]



def display_quiz(question_level):
    global score
    print(" ")
    print(question_list[question_level].prompt)
    print("a. " + question_list[question_level].a)
    print("b. " + question_list[question_level].b)
    print("c. " + question_list[question_level].c)
    print("d. " + question_list[question_level].d)
    choice = input()
    if question_level == 0 and choice == question_list[question_level].answer.lower() or choice == question_list[question_level].answer.upper() or choice == "b" :
        print("well done")
        score += 1
    elif question_level == 0:
        print("wrong")
    if question_level == 1 and choice == question_list[question_level].answer.lower() or choice == question_list[question_level].answer.upper() or choice == "a" :
        print("well done")
        score += 1
    elif question_level == 1:
            print("wrong")
    if question_level == 2 and choice == question_list[question_level].answer.lower() or choice == question_list[question_level].answer.upper() or choice == "d" :
        print("well done")
        score += 1
    elif question_level == 2:
            print("wrong")
    
    question_level += 1
    if question_level < 3:
        display_quiz(question_level)
    else:
        print(" ")
        print( "you scored " + str(score) + " out of"+ " 3")
display_quiz(question_level)
