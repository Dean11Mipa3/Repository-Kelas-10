
def get_questions():
	
	return [
		["What color is the daytime sky on a clear day? ", "blue"],
		["What is the answer to life, the universe and everything? ", "42"],
		["What is a three letter word for mouse trap? ", "cat"],
		["What is the biggest mammals in world? ", "bluewhale"],
		["What animal is stongest in the world? ", "cockroach"],
		["What if fish climb the tree? ", "the fish will fall"],
		["What is the most handsome animal? ", "raccoon"]
	]

def check_question(row):
	q = row[0]
	a = row[1]

	user_answ = input(q)
	if user_answ == a:
		print("Correct!")
		return True
	else:
		print(f"Incorrect!, correct was : {a}")
		return False

def main(questionBank):

	if len(questionBank) == 0:
		print("No question were given")
		return

	index = 0
	right = 0 
	while index < len(questionBank):
		# print(questionBank[index])

		if check_question(questionBank[index]):
			right += 1

		index += 1
	print(f"your score is {right/len(questionBank)*100}")


main(get_questions())