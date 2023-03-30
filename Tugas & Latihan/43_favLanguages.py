favorite_languages ={
	'jen' : 'python',
	'sarah' : 'c++',
	'edward' : 'ruby',
	'alex' : 'lua',
	'mike' : 'python'
}

print(favorite_languages.items())

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thankyou for taking the poll")

my_list = ['a', 'b', 'c', 'a', 'd', 'd', 'a']
print(set(my_list))

for language in sorted(set(favorite_languages.values())):
	print(f"{language}")