if __name__ == '__main__':
    my_list = []  # Start with an empty list
    N = int(input())  # Read the number of commands

    for _ in range(N):
        command = input().split()  # Read the command
        action = command[0]  # First part is the action (e.g., "insert", "print")
        
        if action == "insert":
            # insert i e
            i, e = int(command[1]), int(command[2])
            my_list.insert(i, e)
        elif action == "print":
            print(my_list)  # Print the list
        elif action == "remove":
            # remove e
            e = int(command[1])
            my_list.remove(e)
        elif action == "append":
            # append e
            e = int(command[1])
            my_list.append(e)
        elif action == "sort":
            my_list.sort()  # Sort the list
        elif action == "pop":
            my_list.pop()  # Remove the last element
        elif action == "reverse":
            my_list.reverse()  # Reverse the list
