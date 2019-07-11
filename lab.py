# Global code labe 1 & 2 code
#Code to check assessment
#
x=int(input("Please enter your grade for class exercise \n"))
if x<=30:
    print("You entered: ",x," as your class assesment")
else:
    print("Please enter a number less than 30")

y=int(input("Please enter your grade for exams \n"))
if y<=70:
    print("You entered: ",y," as your exams score")
else:
    print("Please enter a number less than 70")

result = x + y
print("You had a total score of: ",result)

if result >= 70:
    print("You had an A")
elif result >= 60:
    print("You had an B")
elif result >= 50:
  print("You had an C")
elif result >=40:
  print("You had an D")
elif result < 40:
  print("You had an F")
