y=3
try:
  print(x)
except:
  print("An exception occurred")
finally:
  print("The 'try except' is finished")


try:
  print(y)
except:
    print("An exception occurred")
else:
    print("No exception occurred")
