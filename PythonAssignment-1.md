## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?

Q2. Why is Python called a dynamically typed language?

Q3. List some pros and cons of Python programming language?

Q4. In what all domains can we use Python?

Q5. What are variable and how can we declare them?

Q6. How can we take an input from the user in Python?

Q7. What is the default datatype of the value that has been taken as an input using input() function?

Q8. What is type casting?

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?

Q10. What are keywords?

Q11. Can we use keywords as a variable? Support your answer with reason.

Q12. What is indentation? What's the use of indentaion in Python?

Q13. How can we throw some output in Python?

Q14. What are operators in Python?

Q15. What is difference between / and // operators?

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
ans-str="iNeuron"
print(str*4)

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.

ans-num=float(input("Enter the number:-"))
if num%2==0:
    print("no is even")
else:
    print("no is odd") 

Q18. What are boolean operator?

Q19. What will the output of the following?
```
1 or 0
ans-1
0 & 0
ans-0
True and False and True
ans-False
1 or 0 or 0
ans-1
```
Q20. What are conditional statements in Python?

Q21. What is use of 'if', 'elif' and 'else' keywords?

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
ans-
age=int(input("enter the age -"))
if age >= 18 :
    print("I can vote")
else:
    print("I can't vote")   

Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
numbers = [12, 75, 150, 180, 145, 525, 50]
a=0
for i in numbers:
    if i%2==0:
        a=a+i
    else:
        continue    
print(a)  
```


Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
ans-
x,y,z=input(" enter 3 no -").split(",")
if x>y and x>z:
    print(f"{x} is greater")
elif y>x and y>z:
    print(f"{y} is greator")
else:
    print(F"{z} is greater")   

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
ans-numbers = [12, 75, 150, 180, 145, 525, 50]
# lis=[]
# for i in list1:
#     if i >150:
#         if i > 500:
#              break
#     elif i%5==0:  
#        lis.append (i) 
# print(lis)  
```

```