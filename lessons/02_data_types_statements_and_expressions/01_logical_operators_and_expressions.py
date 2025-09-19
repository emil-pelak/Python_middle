x, y = 1, 2

if x == y or x > y:
    print("True")
else:
    print("False")

a = x != y
b = x >= y
c = x <= y

print(a, b, c)

k = [1, 2, 3]
l = k
print(l is k)

m = [1, 2, 3]
print(m is k)
print(m == k)

# n = 2
# o = 2
# print(n == o)
# print(n is o)