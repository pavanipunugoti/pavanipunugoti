#problem2

a = int(input("Enter a number: "))

series = [str(2*i - 1) for i in range(1, a+1)]
print(", ".join(series))