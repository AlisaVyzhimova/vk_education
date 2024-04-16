#задание 1
a=input("Введите имя")
print("Hello,",a)

#2
город=input('Введите название города:')
время=input('введите время:')
print("Current location is", город, 'and time is', время)
#задание

#3
a1 = input()
a2 = input()
a3 = input()
while a3 !="":
    a3 = input ()
if a1 <= a3 >= a2:
    print (True)
else:
    print (False)
  #4
def a(s):
    return ('a' in s or 'o' in s) and ('i' not in s) and ('e' not in s)

if __name__ == "__main__":
    letter = input().strip()
    print(a(letter))
