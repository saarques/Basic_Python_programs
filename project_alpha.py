#What am i doing?
#Well, i am creating a game in which a random jumbled word would be printed and one will need to answer it correctly,
#i am going to use two players in it, so that they can compete and winnere will be decided by their scores.
#If a player answers incorrect or don't answer, then the othe player will be rewarded half the score.


#importing random module
import random
import time
from threading import Timer

def input_correct():
	timeout=10
	t=Timer(timeout, print, ['Sorry, times up']) #put a default value other than None, if no input is given, so that upper() can work
	t.start()
	prompt="You got 10 seconds to answer \n"
	answer=input(prompt)
	t.cancel()
	if answer==None:
		answer=-9999
	return answer

#function to choose random word
def choose():
	#list of words
	words=['total', 'ping', 'pitch', 'telephone', 'drone', 'sunrise', 'evening', 'prompt', 'sophisticated', 'synergy', 'tesla', 'developer',
	      'latest', 'greed', 'amsterdam', 'hornbill', 'locker', 'triumph', 'withstand', 'understand', 'mistake', 'prejudice', 'docker', 'eel',
	      'doctrine', 'awesome', 'super', 'exclaim', 'prevalent', 'distinct', 'dope', 'suggest', 'cooler', 'heater', 'scene', 'watch', 'clock',
	      'decoration', 'light', 'mug', 'starting', 'groan', 'dream', 'choice', 'jumble', 'decision', 'environment', 'speaker', 'tower', 'sun']
	#choice() chooses randomly
	my_word=random.choice(words)
	return my_word.upper()

# print(choose())

#Now we need to jumble the characters of the word choosen from the choose() function
#For this we will need to use sample() function
def shuffle(my_word):
    random_word=random.sample(my_word, len(my_word)) 
    # print(random_word)
    # Now as we saw that the output is a unordered list of characters of the word, so we need to join them now
    jumble_word=''.join(random_word)
    return jumble_word 


def result(p1, p2, p1s, p2s):
	print(p1, " your score is: ", p1s)
	print(p2, " your score is: ", p2s)
	print("Thank you both for playing the game")


def start_game():
	p1=input("Player 1, tell us your Name:")
	p2=input("Player 2, tell us your Name:")

	# variable for counting individual score. 
	p1s, p2s = 0.0,0.0
	# variable for counting  number of turns
	turn = 0
	# infinite looping
	while True:
		# choose() function calling
		random_word = choose()
		# shuffle() fucntion calling
		jumble_word = shuffle(random_word)
		print("jumbled word is :", jumble_word) 
		# checking turn 
		if turn % 2 == 0:
			# if turn no. is even 
			# player1 turn 
			print(p1, "Your Turn.\nWhat's in your mind? ") 
			answer = input_correct()
			# checking answer is equal to random_word or not 
			if answer.upper() == random_word:
				# incremented by 1 
				p1s += 1
				print("Correct")
				turn += 1
			else: 
				print("Better luck next time ...")
				p2s += 0.5
				# player 2 turn
				print(p2, "Your Turn.\nWhat's in your mind? ") 
				answer = input_correct()
				if answer.upper() == random_word:
					p2s += 1
					print("Correct") 
				else: 
					print("Better luck next time...correct word is :", random_word)
					p1s += 0.5
					c = int(input("press 1 to continue and 0 to quit :"))
					# checking the c is equal to 0 or not 
					# if c is equal to 0 then break out 
					# of the while loop o/w keep looping. 
					if c == 0: 
						# result() function calling 
						result(p1, p2, p1s, p2s) 
						break
		else: 
			# if turn no. is odd 
			# player2 turn 
			print(p2, "Your Turn.\nWhat's in your mind? ") 
			answer = input_correct()
			if answer.upper() == random_word: 
				p2s += 1
				print("Correct") 
				turn += 1
			else: 
				print("Better luck next time...") 
				p1s += 0.5
				print(p1, "Your Turn.\nWhat's in your mind? ") 
				answer = input_correct()
				if answer.upper() == random_word: 
					p1s += 1
					
					print("Correct")
				else: 
					print("Better luck next time...correct word is :", random_word)
					p2s += 0.5
					c = int(input("press 1 to continue and 0 to quit :"))
					if c == 0:
						# result() function calling 
						result(p1, p2, p1s, p2s) 
						break
			c = int(input("press 1 to continue and 0 to quit :")) 
			if c == 0: 
				# result() function calling 
				result(p1, p2, p1s, p2s)
				break
#starting of the program
if __name__ == '__main__':
	start_game()