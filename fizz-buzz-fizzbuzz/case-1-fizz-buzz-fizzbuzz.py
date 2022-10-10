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
c3 = 0
c5 = 0
text = ''
for i in range(1 , num+1):
    c3 += 1
    c5 += 1

    if c3 == 3 and c5 == 5:
        text = 'FizzBuzz'
        print(text)
        c3=0
        c5=0
        continue

    if c3 == 3:
        text = 'Fizz'
        print(text)
        c3 = 0
        continue

    if c5 == 5:
        text = 'Buzz'
        print(text)
        c5=0
        continue    
    
    print(i)
