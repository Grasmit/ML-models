

#Numbers from 10 to 20(included) that are odd
a1 = list(range(10,21))

a1 = [num for num in a1 if num%2 != 0] 

print("A1 : ",a1)

print("------------------------------------------------------------------------------------------------")

'''numbers from 100 to 0(included) that can be divided by 10 (use %, the
modulus operator and list comprehension)'''

a2 = list(range(100,-1,-1))

a2 = [num for num in a2 if num%10 == 0]

print("A2 : ",a2)

print("------------------------------------------------------------------------------------------------")

'''numbers from 15 to 1 (included) that can be divided by 3'''

a3 = list(range(15,0,-1))


a3 = [num for num in a3 if num%3 == 0]

print("A3 : ",a3)

print("------------------------------------------------------------------------------------------------")

''' string like “x”, “xx”, “xxx” repeated 10 times. Use the fact that, in
Python, a string s multiplied by an integer n results in s repeated n
times.'''

a4 = ["x"]*10

a4 = [a4[s-1]*s for s in range(1,11)]

print("A4 : ",a4)

print("------------------------------------------------------------------------------------------------")


''' the string ”stringX” repeated 5 times, where X goes from 5 to 0(excluded).
Use the builtin function str() to convert numbers to strings and the fact
that strings can be concatenated using the ”+” operator '''

a5 = ["string"+str(i) for i in range(5,0,-1)]

print("A5 : ",a5)


print("------------------------------------------------------------------------------------------------")

''' a list with the items ”1”, 1, 1.0, “one” '''

a6 = [str(1),int(1),float(1),str("one")]

print("A6 : ",a6)

print("------------------------------------------------------------------------------------------------")

'''  all the numbers from 0 to 99 that contain the digit ”5”. You may use
the method find() that all strings possess to look for a substring. If it is
found, the start index is returned, otherwise -1. '''

a7 = list(range(0,100))

a7 = [i if "5" in str(i) else -1 for i in a7]

print("A7 : ",a7)

print("------------------------------------------------------------------------------------------------")