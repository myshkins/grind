with open('auth.txt', mode='r') as file:
    s = file.read()
    print(s == 'testingpoop')