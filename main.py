#len(1234)

#Data Type convestion

#Data Type as String
print(len("Hello"))

print(len("1234"))

#Data Type Find out

print(type(1234))

print(type("abc"))

print(type(3.14))

print(type(True))

#Type Casting  In python
print(int("123") + int("456"))

#Invalid Literal Error
#print(int("abc") + int("456"))

int()
float()
str()
bool()
#can oly concatenate str not Integer
#print("Number of letters in your name: " + len(input("Enter your name")))

Data = input("Enter your name")
Data2 = len(Data)

print(type("Number of letters in your name: "))  #String

print(type(Data2))  #Int

print("Number of letters in your name: " + str(Data2))
