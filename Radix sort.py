def radix_sort(s):
    "" "Базовая сортировка" ""
    i=0  # Запись в данный момент занимает одну цифру, самая низкая цифра - 1
    max_num = max(s)  # Максимум
    j=len(str(max_num))  # Записываем максимальное количество цифр
    while i<j:
        bucket_list=[[] for _ in range(10)]  # Инициализировать массив сегментов
        for x in s:
            bucket_list[int(x/(10**i))%10].append(x)  # Находим позицию и помещаем ее в массив bucket
        print(bucket_list)
        s.clear()
        for x in bucket_list:  # Заменить исходную последовательность
            for y in x:
                s.append(y)
        i+=1


if __name__ == '__main__':
    a = [334, 5, 67, 345, 7, 345345, 99, 4, 23, 78, 45, 1, 3453, 23424]
    radix_sort(a)
    print(a)