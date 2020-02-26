while True:
    print("Калькулятор выгоды при покупке:")
    print("Введите '1' чтобы сравнить два товара")
    print("Введите '0' чтобы выйти из программы")


    user_input = input("Ввод:   ")

    if user_input == "0":
        break

    elif user_input == "1":
        cost1 = float(input("Введите стоимость первого товара в рублях: "))
        cost2 = float(input("Введите стоимость второго товара в рублях: "))
        weight1 = float(input("Введите вес первого товара в граммах: "))
        weight2 = float(input("Введите вес второго товара в граммах: "))
        result1 = str((cost1/weight1)*1000)
        result2 = str((cost2/weight2)*1000)
        print("Стоимость первого товара:" + " " + result1 + " " + "рублей за килограмм")
        print("Стоимость второго товара:" + " " + result2 + " " + "рублей за килограмм")
        if result1 > result2:
            print("Второй товар дешевле")
        elif result1 < result2:
            print("Первый товар дешевле")
        else:
            print("Они одинаково выгодны))")

    print("Завершено")
