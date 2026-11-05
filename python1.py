#1
# N = int(input("Enter a number: "))
# for i in range(1, N+1):
#     print(i, end="")
#     print()


#2
# N = int(input("Enter a number: "))
# for i in range(N, 0, - 1):
#     print(i, end="")
#     print()
                                                                                                


#3
# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1, num + 1):
#     sum = sum + i
# print("Sum of first", num, "Number is sum:", sum)    



#4
# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1, num + 1):
#     if i % 2 == 0:
#         sum = sum + i
# print("sum of all even number from 1 to", num, "is", sum)        



#5
# n = int(input("Enter a number: "))
# for i in range(0, 10):
#     print(n * (i + 1))


#6
# n = 54321
# count = 0
# while n > 0:
#     n = n // 10
#     count += 1
# print(count)    


#7
# num = input()
# sum = 0
# for digit in num:
#     sum += int(digit)
# print("sum: ", sum)    



#8
# num = int(input("Enter a number: "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print("Reverse is", reverse)    




#9
# num = input("Enter a number: ")
# palindrome = num[::-1]
# if num == palindrome:
#     print("true")
# else:
#     print("false")    


#11
# base = 2
# exp = 4
# sq = base ** exp
# print(sq)


#12
# num = int(input("Enter a number: "))
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i 
# print(fact)    




#13
# a = 12
# b = 18
# gcd = 1
# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i
# print(gcd)


#14
# a = 4
# b = 6
# lcm = max(a, b)
# while True:
#     if lcm % a == 0 and lcm % b == 0:
#         break
#     lcm += 1
# print(lcm)



#15
# n = 17
# is_prime = True
# if n <= 1:
#     is_prime = False
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
# if is_prime:
#     print("Prime")
# else:
#     print("Not Prime")


#16
# n = 15
# for num in range(2, n + 1):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num)


#17
# n = 123
# original = n
# sum = 0
# digits = len(str(n))
# while n > 0:
#     digit = n % 10
#     sum = sum + digit ** digits
#     n = n // 10
# if sum == original:
#     print("True")
# else:
#     print("False")


#18
# n = 6
# total = 0
# for i in range(1, n):
#     if n % i == 0:
#         total = total + i
# print(total)        


#19
# binary = "1101"
# decimal = 0
# for digit in binary:
#     decimal = decimal * 2 + int(digit)
# print(decimal)


#20
# n = 13
# binary = ""
# while n > 0:
#     remainder = n % 2
#     binary = str(remainder) + binary

#     n = n // 2
# print(binary)    