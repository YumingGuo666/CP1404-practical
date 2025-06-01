"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
import random
def main():
  score = float(input("Enter score: "))
  result = get_result(score)
  print(result)
  random_score = random.uniform(0, 100)
  print(f"\nRandom score: {random_score:.2f}")
  print(get_result(random_score))
def get_result(score):
  if score < 0:
    return"Invalid score"
  else:
    if score > 100:
        return"Invalid score"
    elif score >=90:
        return"Excellent"
    elif score >=50:
        return"Passable"
    elif score < 50:
        return"Bad"
main()
