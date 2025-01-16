# a = open("text.txt", "r")

# print(a.read())
# print(a.readline())
# a.close()

# # f = open("text.txt", "a")
# # f.write("Now the file has more content!")
# # f.close()

# # #open and read the file after the appending:
# # f = open("text.txt", "r")
# # print(f.read())

# f = open("text.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()

# #open and read the file after the overwriting:
# f = open("text.txt", "r")
# print(f.read())

# import os
# if os.path.exists("text.txt"):
#   os.remove("text.txt")
# else:
#   print("The file does not exist")