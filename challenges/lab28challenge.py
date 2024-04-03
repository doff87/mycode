#!/usr/bin/env python3

import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

def main():

    answer = input(trivia["question"] + "\n A) " + html.unescape(trivia["incorrect_answers"][0]) + "\n B) " + html.unescape(trivia["incorrect_answers"][1]) + "\n C) " + html.unescape(trivia["correct_answer"]) + "\n D) " + html.unescape(trivia["incorrect_answers"][2]) + "\n")

    answer = answer.upper()

    if answer=="C":
        print("Congratulations, your answer was correct!")

    else:
        print("I'm sorry, your answer was incorrect")

if __name__ == "__main__":

    main()
    


