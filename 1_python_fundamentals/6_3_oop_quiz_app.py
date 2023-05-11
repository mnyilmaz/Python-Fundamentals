# BTK Academy
# Advanced Python Programming From Zero
# Lecture 6.3: Object Oriented Programming in Python - Quiz Applicaiton
# python 6_3_oop_quiz_app.py
blank = "----------------------"

# Form Question and Quiz classes for the application

# Question Class
class Question:
    def __init__(self, question, choice, answer):
        self.question = question
        self.choice = choice
        self.answer = answer
    
    def check_answer(self, answer):
        return self.answer == answer

# Quiz Class
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0  # means getting first element from q_list
    
    def get_question(self):
        return self.questions[self.question_index]
    
    def display_question(self):
        q = self.get_question()
        print(f"Question {self.question_index + 1}: {q.question}")

        for i in q.choice:
            print("-" + i)
        
        answer = input("Answer: ")
        self.guess(answer)
        self.load_question()

    def guess(self, answer):
        q = self.get_question()

        if q.check_answer(answer):
            self.score += 50

        self.question_index += 1
    
    def load_question(self):
        if len(self.questions) == self.question_index:
            self.display_score()
        else:
            print(blank)
            self.display_progress()
            self.display_question()
    
    def display_progress(self):
        total_q = len(self.questions)
        q_number = self.question_index 

        if q_number > total_q:
            print("Quiz has ended.")
        else:
            print(f"You've answered {q_number} of {total_q}")
            print(blank)

    def display_score(self):
        print(blank)
        print(f"Your score is: {self.score}\nQuiz has ended.")


question_1 = Question("Who is more mad than others?", ["Alice", "Mad Hatter", "Absolem", "Chess"], "Mad Hatter")
question_2 = Question("Who is the most bravest?", ["Alice", "Mad Hatter", "Absolem", "Chess"], "Alice")
question_3 = Question("Who has the best smile among them?", ["Alice", "Mad Hatter", "Absolem", "Chess"], "Chess")
q_list = [question_1, question_2, question_3]

quiz = Quiz(q_list)
q = quiz.get_question()
quiz.display_question()

# print(q.question) #second question comes from Question class
print(blank)

# print(question_1.check_answer("Chess")) # False
# print(question_2.check_answer("Alice")) # True
# print(question_3.check_answer("Absolem")) # False
# print(blank)
