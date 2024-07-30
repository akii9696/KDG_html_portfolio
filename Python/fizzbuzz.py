i = 1
print("数を入力")
x = int(input())
y = int(input())
j=x*y
while i <= 100:
    if i% j ==0:
        print(str(i) + "FizzBuzz")
    elif i% x ==0:
        print(str(i) + "Fizz")
    elif i% y ==0:
        print(str(i) + "Buzz")
    else:
        print(i)
    i += 1