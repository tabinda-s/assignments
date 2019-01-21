with open('name.txt') as f:
    name = f.read()

print(name)


#

with open('hello.txt', 'w') as f:
    f.write('Hello, my name is ' + name + '.')
    f.write('\n')