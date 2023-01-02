#Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".   

#  Write a code that displays the sum of all the even numbers from the given list.
# numbers = [12, 75, 150, 180, 145, 525, 50]
# a=0
# for i in numbers:
#     if i%2==0:
#         a=a+i
#     else:
#         continue    
# print(a)  

#Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
# 
# x,y,z=input(" enter 3 no -").split(",")
# if x>y and x>z:
#     print(f"{x} is greater")
# elif y>x and y>z:
#     print(f"{y} is greator")
# else:

#     print(F"{z} is greater")        


# Q25. Write a program to display only those numbers from a list that satisfy the following conditions

# - The number must be divisible by five

# - If the number is greater than 150, then skip it and move to the next number

# - If the number is greater than 500, then stop the loop


list1= [12, 75, 150, 180, 145, 525, 50]

# lis=[]
# for i in list1:
#     if i >150:
#         if i > 500:
#              break
#     elif i%5==0:  
#        lis.append (i) 
# print(lis)  

lis=[]
for i in list1:
    if i%5==0:
    elif i>150:
        if i>500:
         break
    lis.append (i) 
print(lis)









