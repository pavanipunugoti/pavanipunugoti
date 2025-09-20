
#  Problem-3.py

a = int(input("Enter a number: "))

if a <= 2:
    series = [1]
else:
    n = a if a % 2 != 0 else a - 1
    series = [2*i - 1 for i in range(1, n+1)]

print(", ".join(map(str, series)))

