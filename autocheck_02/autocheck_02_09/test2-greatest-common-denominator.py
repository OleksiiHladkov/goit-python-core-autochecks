# На співбесідах часто люблять запитувати про алгоритми.
# Наприклад, розрахуйте найбільший спільний дільник (НД) двох додатних чисел.
# НСД — це найбільше число, на яке без залишку діляться обидва числа.

first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

# обираємо найменьше з двох чисел та назначаємо у gcd
gcd = first if first < second else second
while True:
    if not first % gcd and not second % gcd:
        break
    else:
        gcd -= 1

print(gcd)
