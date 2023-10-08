def cost_delivery(quantity: int, *_, discount: float = 0):
    """Функція повертає суму за доставлення замовлення.

     Перший параметр &mdash; кількість товарів в замовленні.
     Параметр знижки discount, який передається лише як ключовий, за замовчуванням має значення 0."""
    if quantity <= 0:
        return 0
    else:
        return (5 + 2 * (quantity - 1)) * (1 - discount)


print(cost_delivery(2, 1, 2, 3))
print(cost_delivery(3, 3))
print(cost_delivery(1))
print(cost_delivery(2, 1, 2, 3, discount=0.5))