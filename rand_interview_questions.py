import random
import sys


if __name__ == "__main__":

  question_file = sys.argv[-1]
  questions = []
  with open(question_file, "r") as f:
    questions = f.readlines()

  num_questions = len(questions)
  print(questions[random.randrange(num_questions)])
