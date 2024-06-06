# """CLI application for a prefix-notation calculator."""
# """
# repeat forever:
#     read input
#     tokenize input
#         if the first token is "q":
#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens

#             (...etc.)
          
# """


from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
#
while True:
#
    user_input=input("Type your equation here.> ")
#
    tokenize_input=user_input.split(" ")
    command=tokenize_input[0]
#
    if command == "q":
        break
    elif command == "add":
        add(int(tokenize_input[1]), int(tokenize_input[2]))
    elif command == "subtract":
        subtract(int(tokenize_input[1]), int(tokenize_input[2]))
    elif command == "multiply":
        multiply(int(tokenize_input[1]), int(tokenize_input[2]))
    elif command == "divide":
        divide(int(tokenize_input[1]), int(tokenize_input[2]))
    elif command == "square": 
        square(int(tokenize_input[1]))
    elif command == "cube":
        cube(int(tokenize_input[1]))
    elif command == "power":
        power(int(tokenize_input[1]), int(tokenize_input[2]))
    elif command == "mod":
        mod(int(tokenize_input[1]), int(tokenize_input[2]))
        