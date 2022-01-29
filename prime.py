print('Enter an integer: ')

x = input()
x = int(x)
prime = []
for i in range(x):
    try:
        if x % int(i + 1) == 0:
            prime.append(i + 1)
            print(x +  + int(i))
    except:
        pass
        if len(prime) > 2:
            print(prime[1:-1])

            for x in range(-5, 6):
                y = x * x * 8 + 1
                print('When x is ' + str(x) + ', y is ' + str(y))
