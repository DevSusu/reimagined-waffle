import sys
n, x = map(int, sys.stdin.readline().split())
a = sys.stdin.readline().split()
ans = ""
for i in a:
    if int(i)<x:
        ans = ans + i + ' '
print(ans)
# for i in range(1,n+1):
#     print(" "*(i-1)+"*"*(n+1-i))

# for i in range(1,n+1):
#     print('*'*i)
    # Do something

# ans = 0
# for i in range(1,n+1):
#     ans = ans+i
# print(ans)

# for i in range(1,10):
#     print('{} * {} = {}'.format(n,i,n*i))

# for i in range(1,n+1):
#     print(n+1-i)
# range(1,n+1) = [1,2,3,4,5,6,..,n]
#
# for i in [1,2,3,4,5,6,..,n]:
#     print(i)
