import sys
a,b,c = map(int,sys.stdin.readline().split())

# TODO
if (a>=c and a<=b) or (a>=b and a<=c):
    print(a)
elif (b>=c and b<=a) or (b>=a and b<=c):
    print(b)
else:
    print(c)

# if score>=90 and score<=100:
#     print("A")
# #else if
# elif score>=80 and score<90:
#     print("B")
# elif score>=70 and score<80:
#     print("C")
# elif score>=60 and score<70:
#     print("D")
# else:
#     print("F")

# print("a = ")
# a = int(sys.stdin.readline())
# print("b = ")
# b = int(sys.stdin.readline())
# print(a/b)

#a, b = map(int, sys.stdin.readline().split())

# print(a-b)
# print("Hello World!")
#
#
# print("testing\n...")
# 4 5
# print(
# """
# #include<stdio.h>
# main()
# {
#     printf("Hello World\\n");
# }
# """
# )
