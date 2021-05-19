if True:
    print('ok')
language='python'

if language=='python':
    print('language is python')
else:
    print('language is not python')



language='java'

if language=='python':
    print('language is python')
elif language=='java':
    print('language is java')
else:
    print('not')

#and or not

user='admin'
logged_in=True
if user =='admin' and logged_in:
    print('admin page')
else:
    print('Bad creds')

#object identity:is
a=[1,2,3,4,5]
b=[1,2,3,4,5]
print(a==b)
print(a is b) #flase bcz id is different of a and b
print(id(a))
print(id(b))


###loops
nums=[1,2,3,4,5]
for num in nums:
    print(num)

for num in nums:
    for letter in 'abc':
        print(num,letter)


for i in range(10):
    print(i)

for i in range(1,10):
    print(i)


x=0
while x<10:
    print(x)
    x+=1s

#infinite loops:ctrl+c for break loops:
x=0
while True:
    print(x)
    x+=1