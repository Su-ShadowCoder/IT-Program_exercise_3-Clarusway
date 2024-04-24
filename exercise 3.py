# # exercise 1
# user_input = input("Enter a letter: ")
# vowel = ["a", "o", "e", "i", "u"]
# if user_input in vowel:
#     print("This has a vowel!")
# else:
#     print("no vowel")

# # exercise 2
# user_input = int(input("number: "))
# if 1000 <= user_input <= 2000:
#     print("this numbers is between 1000 and 2000")
# elif user_input < 1000:
#     print("number lower than 1000")
# else:
#     print("number higher than 2000")

# # exercise 3
# user_input_1 = int(input("Enter 1st number: "))
# user_input_2 = int(input("Enter 2nd number: "))
# user_input_3 = int(input("Enter 3rd number: "))
# sum_of_numb = (user_input_1 + user_input_2 + user_input_3)
# if user_input_1 == user_input_2 == user_input_3:
#     total_X4 = sum_of_numb*4
#     print(f"These numbers are the same!\n"
#           f"The sum of these numbers is {sum_of_numb}\n"
#           f"Multiplied by 4 this becomes {total_X4}.")
# else:
#     print(f"The sum of these number is {sum_of_numb}.")

# # exercise 4
# user_input_1 = int(input("Enter 1st number: "))
# user_input_2 = int(input("Enter 2nd number: "))
# user_input_3 = int(input("Enter 3rd number: "))
# user_input_4 = int(input("Enter 4th number: "))
#
# if (user_input_1 > user_input_2 and user_input_1 > user_input_3 and
#         user_input_1 > user_input_4):
#     print(f"The largest number is {user_input_1}.")
# elif (user_input_2 > user_input_1 and user_input_2 > user_input_3 and
#       user_input_2 > user_input_4):
#     print(f"The largest number is {user_input_2}.")
# elif (user_input_3 > user_input_2 and user_input_3 > user_input_1 and
#       user_input_3 > user_input_4):
#     print(f"The largest number is {user_input_3}.")
# elif (user_input_4 > user_input_2 and user_input_4 > user_input_3 and
#       user_input_4 > user_input_1):
#     print(f"The largest number is {user_input_4}.")

# exercise 5
#
# user_input_1 = int(input("Enter your income: "))
#
# after_tax_box1 = user_input_1 - ((user_input_1/100)*24)
# after_tax_box2 = user_input_1 - ((user_input_1/100)*31)
# after_tax_box3 = user_input_1 - ((user_input_1/100)*34)
#
# if user_input_1 < 67000:
#     print(f"Your income after taxes is {after_tax_box1} euro’s")
# elif 67000 < user_input_1 < 97000:
#     print(f"Your income after taxes is {after_tax_box2} euro’s")
# elif user_input_1 >= 97000:
#     print(f"Your income after taxes is {after_tax_box3} euro’s")

# # exercise 6
#
# user_input = input("Enter a value of maximum of 5 letters: ")
# if len(user_input) == 1:
#     print(user_input*6)
# elif len(user_input) == 2:
#     result = user_input[-1:] + user_input[1:-1] + user_input[:1]
#     print(result)
# elif len(user_input) == 3:
#     result_2 = user_input[2] + user_input[:-1]
#     print(result_2)
# elif len(user_input) == 4:
#     print(user_input[::-1])
# elif len(user_input) == 5:
#     result_3 = (user_input[0] + "t" + user_input[1] + "t" + user_input[2] +
#                 "t" + user_input[3] + "t" + user_input[4])
#     print(result_3)

# # exercise 7
# user_input = int(input("what is 5*5?: "))
# if user_input == 25:
#     print(f"Good!, That is correct!")
#     user_input2 = int(input(f"Next question, what is 16/4?: "))
#     if user_input2 == 4:
#         print(f"Good!, That is correct!")
#         user_input3 = int(input(f"Next question, what is 3**2?: "))
#         if user_input3 == 9:
#             print(f"Good!, That is correct! congratulations you have "
#                   f"passed the test!")
#         else:
#             print("That is false, you failed the test!")
#     else:
#         print("That is false, you failed the test!")
# else:
#     print("That is false, you failed the test!")
