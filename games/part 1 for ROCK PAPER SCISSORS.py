# # by @shreyash joshi
# import random

# while True: 
# 	print('Make your choice:')
# 	choice = str(input())
# 	choice = choice.lower()

# 	print("My choice is", choice)

# 	choices = ['rock', 'paper', 'scissors']

# 	computer_choice = random.choice(choices)

# 	print("Computer choice is", computer_choice)
# 	if choice in choices:
# 		if choice == computer_choice:
# 			print('it is a tie')
# 		if choice == 'rock':
# 			if computer_choice == 'paper':
# 				print('you lose, sorry :(')
# 			elif computer_choice == 'scissors':
# 				print('You win!!!!! congrats :)')
# 		if choice == 'paper':
# 			if computer_choice == 'scissors':
# 				print('you lose, sorry :(')
# 			elif computer_choice == 'rock':
# 				print('You win!!!!! congrats :)')
# 		if choice == 'scissors':
# 			if computer_choice == 'rock':
# 				print('you lose, sorry :(')
# 			elif computer_choice == 'paper':
# 				print('You win!!!!! congrats :)')
# 	else:
# 		print('invalid choice, try again')

# 	print()

# # by @shreyash joshi
# # USING MATRIXES

# import random

# random.seed(42)

# while True:
# 	print("Make your guess:", end=" ")
# 	guess = str(input())
# 	guess = guess.lower()
# 	print("you guessed", guess)
# 	choices = ['rock', 'paper', 'scissors']
# 	computer_guess = random.choice(choices)
# 	print("computer guessed", computer_guess)
# 	guess_dict = {'rock': 0, 'paper': 1, 'scissors': 2}
# 	guess_idx = guess_dict.get(guess, 3)
# 	computer_idx = guess_dict.get(computer_guess)
# 	result_matrix = [[0,2,1],
# 					 [1,0,2],
# 					 [2,1,0],
# 					 [3,3,3]]
# 	result_idx = result_matrix[guess_idx][computer_idx]
# 	result_messages = ["it is a tie", "You win!!! Congrats", 'the computer wins :(', 'invalid guess']
# 	result = result_messages[result_idx]
# 	print(result)
# 	print()