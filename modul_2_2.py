first=int(input("введите число" ))
second=int(input("введите число" ))
third=int(input("введите число" ))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
elif first != second and second != third:
    print(0)
