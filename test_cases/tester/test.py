import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

_filepath = 'hw6.py'

with open(_filepath, 'r') as f:
    _code = f.read()

_num = 300

for _i in range(0, _num):
    with open('tests/in' + str(_i) + ".txt", "r") as f:
        _inp = f.read()
    with open('tests/out' + str(_i) + "-1.txt", "r") as f:
        _ans1 = f.read()
    with open('tests/out' + str(_i) + "-2.txt", "r") as f:
        _ans2 = f.read()
    with open('tests/out' + str(_i) + "-3.txt", "r") as f:
        _ans3 = f.read()
    with open('crime_scene.txt', 'w') as f:
        f.write(_inp)

    try:
        exec(_code)
    except Exception as err:
        print('There was an error when trying the input: tests/in' + str(_i) + '.txt')
        print(err)
        exit()
    
    with open('solution_part1.txt', 'r') as f:
        _out1 = f.read()
    with open('solution_part2.txt', 'r') as f:
        _out2 = f.read()
    with open('solution_part3.txt', 'r') as f:
        _out3 = f.read()
    
    if(_ans1.strip() != _out1.strip()):
        print('Wrong answer on: tests/in' + str(_i) + '.txt')
        print('your code gave output in task 1')
        print(_out1)
        print('but the desired answer was')
        print(_ans1)
        # exit()

    if(_ans2.strip() != _out2.strip()):
        print('Wrong answer on: tests/in' + str(_i) + '.txt')
        print('your code gave output in task 2')
        print(_out2)
        print('but the desired answer was')
        print(_ans2)
        # exit()

    if(_ans3.strip() != _out3.strip()):
        print('Wrong answer on: tests/in' + str(_i) + '.txt')
        print('your code gave output in task 3')
        print(_out3)
        print('but the desired answer was')
        print(_ans3)
        # exit()


print('Accepted')
print('Your code passed all', _num, 'tests')