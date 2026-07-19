# path=r"C:\Users\nouma\OneDrive\Documents\Daily Note\internship.txt"
# file=open(path,'w')
# file.write('welcome to file handling in python')
# file=open(path,'r')
# #file.write('nouman')
# print(file.read())
# file.close()
newpath=r"C:\Users\nouma\OneDrive\Documents\Daily Note\file_handling.txt"
#files=open(newpath,'x')
files=open(newpath,'w')
files.write('hello!, This is my new file created using file handling.')

print('\t')

# append this is ayesha to files
files=open(newpath,'a')
files.write('\nThis is Ayesha')

# read the entire file and read it.
files=open(newpath,'r')
print(files.read())
files.close()

# create a file course.txt  write python, sql, excel.
cors=r"C:\Users\nouma\OneDrive\Documents\Daily Note\course.txt"
#course=open(cors,'x')
course=open(cors,'w')
course.write('python \nSQl \nExcel')
course=open(cors,'r')
print(course.read())
course.close()

#mini challenge 
s=r"C:\Users\nouma\OneDrive\Documents\Daily Note\skill.txt"
#skill=open(s,'x')
skill=open(s,'w')
skill.write('python,\nSQl,\nExcel,\nPowerBI')
skill=open(s,'r')
print(skill.read())
print('\n')
skill=open(s,'a')
skill.write("\nGIt")
skill=open(s,'r')
print(skill.read())
print('\n')

#readline() reads only one line at a time.
skill=open(s,'r')
print(skill.readline())

#readlines() reads all lines and stored them in a list.
skill=open(s,'r')
print(skill.readlines())
print('\n')
# accessing individual lines
skill=open(s,'r')
data=skill.readlines()
print(data[1])
print(data[2])
print(data[0])
skill.close()

#with open() is a professional way in which we don't have to close the files
with open(s,'r') as skill:
    print(skill.read())


