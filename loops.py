# A code for loops
#
# x=2

# for x in range(2,20):
#     if x%2==0:
#         print(x)

# def even(x,y):
#     for x in range(x+1,y):
#         if x%2==0:
#            print (x)

# x=int(input("Please enter the first number \n"))
# y=int(input("Please enter the second number \n"))
# even(x,y)

# def even(x,y):
#     for y in range(y+1,x-1,-1):
#         if y%2==0:
#            print (y)

# y=int(input("Please enter the second number \n"))
# x=int(input("Please enter the first number \n"))

# even(x,y)\
# def star():
#     for i in range(0,4):
#         aster=" "
#         for j in range(0,4):
#            aster+="*"
#         print(aster)
# star()

# Descending star
# for i in range(0,4):
#     for j in range(0,i+1):
#         print("*", end=' ')
#     print("\r")

# for i in range(4,0,-1):
#     for j in range(0,i-1):
#         print("*", end=' ')
#     print("\r")

# for i in range(0,5):
#     print("*"*i)
# reversed= range(5,0,-1)
# for i in reversed:
#     print("*" * i)



def sentence(sent,char):
    for i in range(len(sent),0,-1):
        if sent[len(sent)-i]== char:
            return "true"
            break
        if i==1:
            return "false"


sent=input("Please enter a sentence: \n")
char=input("Please enter a character you want to find in the sentence: \n")
print(sentence(sent,char))
