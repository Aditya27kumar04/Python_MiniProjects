import random
from art import logo
from art import vs
print(logo)
#Making overall function
def overall_function():
    #Making A part
    def asking_question_a():
        from Question_lists import data

        print("Compare A:", random.choice(data))


    asking_question_a()

    print(vs)

    def asking_question_b():
        from Question_lists import data

        print("Compare B:", random.choice(data))

    asking_question_b()



overall_function()

