T=5

#1
for i in range(1,T+1):
    print('*' * i)

print('------------------')

#2
for i in range(1, T+1):
    print(' ' * (T-i)  + '*' * i)

print('------------------')

#3
for i in range(T,0,-1):
    print('*' * i)

print('------------------')

#4
for i in range(1, T+1):
    print(' ' * (T-i) + '*' * (2*i-1) + ' '* (T-1))

print('------------------')

#5
for i in range(T,0,-1):
    print(' ' * (T-i) + '*' * (2*i-1) + ' '* (T-i))

print('------------------')

#6
for i in range(1, T):
    print(' ' * (T-i) + '*' * (2*i-1) + ' '* (T-1))

print('*' * (2*T-1))

#7
for i in range(T-1,0,-1):
    print(' ' * (T-i) + '*' * (2*i-1) + ' '* (T-1))

print('------------------')

#8
for i in range(1, T):
    print('*' * i + ' ' * 2*(T-i) + '*' * i)

print('*' * (2*T))

for i in range(T-1,0,-1):
    print('*' * i + ' ' * 2*(T-i) + '*' * i)

print('------------------')

for i in range(T,1,-1):
    print(' ' * (T-i) + '*' * (2*i-1) + ' '* (T-1))

print(' ' * (T-1) + '*' * (2*1-1) + ' '* (T-1))

for i in range(2, T+1):
    print(' ' * (T-i) + '*' * (2*i-1) + ' '* (T-1))
