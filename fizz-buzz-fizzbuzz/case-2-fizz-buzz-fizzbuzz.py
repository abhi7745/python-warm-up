
'''
problem :-
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz
'''

num = int(input('Enter your limit : '))

for i in range(1, num+1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        continue
    if i % 3 == 0:
        print('Fizz')
        continue
    if i % 5 == 0:
        print('Buzz')
        continue
    print(i)