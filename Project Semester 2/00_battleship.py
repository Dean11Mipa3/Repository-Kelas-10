# https://www.w3schools.com/python/ref_string_join.asp
lists = [ [0,1,2], [3,4,5]]
for list in lists:
	for item in list:
		print(item, end=" ")
	print()

texts = ["YYY", "YYY", "YYY"]
for text in texts:
	for char in text:
		print(char, end="")
	print()

# texts = []
# text = "X" * 3
# for i in range(3):
# 	texts.append(text)