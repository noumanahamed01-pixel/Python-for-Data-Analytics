#class is a blueprint or template that defines the properties and behavior of objects
#create a class student
class student:
   pass  #do nothing — it’s just a placeholder. So the class has no attributes or methods initially.
#object is an instance of class, it contains actual data and can perform actions defines in the class.
#create an object 
student1=student()
print(student)
# we can add attributes to the objects
student1.name='alice'
student1.age=20
print(student1.name)
print(student1.age)

class book:
    pass
book1=book()
book2=book()
book1.title='first time to practice oop'  
book1.author='numan'
#Even though the class didn’t define title or author, 
#Python lets you add attributes directly to an object.
#So now book1 has its own title and author
book2.title='second time to practice oop'
book2.author='numan'
print(book1.title)
print(book1.author)
print(book2.title)
print(book2.author)

#constructor is a special method that runs automatically when obe=ject is created.
#Create a class called Book.

# Constructor should store: title,author,Create two books,Print both.
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
book1=book("this is my first oop program",'alice')
print(book1.title)
print(book1.author)
