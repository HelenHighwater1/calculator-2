"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

while True:
# repeat forever:
    user_input=input("Type your equation here.> ")
#     read input
    tokenize_input=user_input.split(" ")
    command=tokenize_input[0]
#    tokenize input
    if command == "q":
        break
#         if the first token is "q":
#             quit
    elif command == "add":
        add(tokenize_input[1], tokenize_input[2])

#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)
# 
