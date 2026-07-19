#String : A string is a Sequence of character encloseed within single quotes ' ' and double quotes " " or Triple Quotes ''' '''.
# language = 'Python Programming'
# print(type(language))
# print(language)
# #create a string data engineering print it using indexing.
# text = "Data Engineering"
# # print first character
# print("First character:", text[0])
# # print last character
# print("Last character:", text[-1])
# # create a string artificial intelligence.
# text = "Artificial Intelligence"
# print(text[:10])
# print(text[11:])
# ai = 'OpenAI'
# print(ai[::2])
# data = 'DataBase'
# print(data[::-1])

#String Methods
#1. upper()
# covert all letters to the uppercase.
# name = 'python'
# print(name.upper())
#2. lower() Convert all letters to the lowercase.
# name = "PYTHON PROGRAMMING"
# print(name.lower())
#3. strip() removes spaces from beginning and end.
# name = "  Python     "
# print(name.strip())
#4. replace() replaces one text from another.
# sentence='I love java'
# print(sentence.replace('java','python'))
# 5. find() Returns the index of first occurence.
# word='programming'
# print(word.find('g'))
# print(word.find('z')) #if not found it print -1
# 6. count() it counts how many times a character or word appears.
# fruits='banana'
# print(fruits.count('a'))
#mini Day 18 Challenge
# text='   Data Engineering with Python '
# print(text.upper())
# print(text.lower())
# print(text.strip())
# print(text.replace('Python','SQL'))
# print(text.find('Enginnering'))
# print(text.count('a'))

# split() converts strings into list 
# text = " welcome to Python "
# print(text.split())
# print(text.split(","))

# join() does the opposite to split 
#it joins list into a string.
# words=['python','sql','excel']
# print(" ".join(words))

# startswith() check whether a string start with a given text.
#endswith() check whether a string ends with a given text.
# course='python programming.'
# print(course.startswith('py'))
# print(course.endswith('in'))
# print(course.endswith('ing.'))

#f-string
#They’re faster and more readable than .format() or concatenation.
#You can embed expressions directly inside {}.
# name='numan'
# print(f"Welcome,{name}!")