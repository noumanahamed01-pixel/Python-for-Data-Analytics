#String : A string is a Sequence of character encloseed within single quotes ' ' and double quotes " " or Triple Quotes ''' '''.
# Strings Practice

# Creating strings
name = "Python"
sentence = "Learning OOP and Data Structures"

# Accessing characters
print("First character:", name[0])
print("Last character:", name[-1])

# Slicing
print("First three letters:", name[0:3])
print("From index 2 onwards:", name[2:])

# String methods
print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Split words:", sentence.split())
print("Replace:", sentence.replace("OOP", "Functions"))
word='programming'
print(word.find('g'))
print(word.find('z')) #if not found it print -1
fruits='banana'
print(fruits.count('a'))

# Checking substrings
print("Does sentence contain 'Data'?", "Data" in sentence)
print("Does sentence contain 'Java'?", "Java" in sentence)

# Concatenation
course = "BCA"
year = "Final"
print("Course Info:", course + " - " + year)

# Formatting with f-string
print(f"{name} is powerful for {course} students in {year} year.")


# join() does the opposite to split 
# it joins list into a string.
words=['python','sql','excel']
print(" ".join(words))

# startswith() check whether a string start with a given text.
#endswith() check whether a string ends with a given text.
course='python programming.'
print(course.startswith('py'))
print(course.endswith('in'))
print(course.endswith('ing.'))

#f-string
#They’re faster and more readable than .format() or concatenation.
#You can embed expressions directly inside {}.
name='numan'
print(f"Welcome,{name}!")
