# Input the number of scores
n = int(input("Enter:"))

# Input the scores and convert them to a list
scores = list(map(int, input("Enter:").split()))

# Find the maximum score
max_score = max(scores)

# Remove all occurrences of the maximum score
scores = [score for score in scores if score != max_score]

# Find the runner-up score (the new maximum)
runner_up_score = max(scores)

# Print the runner-up score
print(runner_up_score)
