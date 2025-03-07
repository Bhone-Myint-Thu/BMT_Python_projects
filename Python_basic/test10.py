#need to learn this code
if __name__ == '__main__':
    n = int(input())  # Number of students
    student_marks = {}
    
    # Read student data
    for _ in range(n):
        line = input().split()
        name = line[0]  # First element is the student's name
        scores = list(map(float, line[1:]))  # Remaining elements are their scores (as floats)
        student_marks[name] = scores
    
    # Query the student's name
    query_name = input()
    
    # Calculate the average of the queried student's scores
    scores = student_marks[query_name]
    average = sum(scores) / len(scores)
    
    # Print the result with 2 decimal places
    print(f"{average:.2f}")
