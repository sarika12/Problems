import random
# Guess the number  I have chosen between 1 and 100 asks as many yes/no questions,do not
# repeat a question.
from random import randint

# def random1():
# #
# #     for i in range(1,10):
# #         a=str(randint(1,10))
# #     # a=[str(randint(1,10)) for i in range(1,10)]
# #
# #
# #         return a
# # # a=random()
# #
# # for i in range(1,10):
# #     if random1() in str(i):
# #         print("yes")
# #     else:
# #         print("No")


def guess_number():
    number=random.randint(1,100)
    low,high=1,100
    ask_question=set()

    while True:
        mid=low+high//2
        question=f"is this greater then {mid}"
        if question in ask_question:
            print("u already ask the question try differnt")


guess_number()