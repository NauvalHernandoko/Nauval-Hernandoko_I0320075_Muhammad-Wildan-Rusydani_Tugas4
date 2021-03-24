x = 99
y = 7

print('x + y:',x+y)
print('x - y:',x-y)
print('x * y:',x*y)
print('x / y:',x/y)
print('x ** y:',x ** y)
print('x // y:',x // y)
print('x % y:',x % y)

print('x > y:', x>y)
print('x < y:', x<y)
print('x != y:', x!=y)
print('x >= y:', x>=y)
print('x <= y:', x<=y)

x = True
y = False
print('x and y is',x and y)
print ('x or y is',x or y)
print('not x is',not x)

str1 = "dia"
str2 = "cantik"
result = str1 + " " + str2
print(result)

str = 'banget'
result = str * 3
print(result)

bagian = 'can'
utuh = 'cantik'
if bagian in utuh:
    print(bagian, 'adalah bagian dari',utuh)
else:
    print('not found')
bagian2 = 'cin'
if bagian2 in utuh:
    print(bagian2, 'adalah bagian dari',utuh)
else:
    print('not found')

ch = str[3]
print(ch)

sub = str[1:]
print(sub)

new = str[0::6]
print(new)

hasil = str[::-2]
print(hasil)
