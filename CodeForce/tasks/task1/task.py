def find_new_map(n: int, old_capital: int, new_capital: int,
                 old_map: list) -> list:
    new_road_map = list()
    # Почти придумал как избавиться от словаря, по памяти еще уменьшится
    dict_road_map = dict()
    for number in range(n): # O(n)
        if number < old_capital - 1:
            dict_road_map[number + 1] = old_map[number]
        elif number == old_capital - 1:
            dict_road_map[number + 1] = 0
        else:
            dict_road_map[number + 1] = old_map[number - 1]

    number_city = new_capital
    last_capital = new_capital
    while number_city != 0:
        # обращение к элементу словаря за константное время.
        # Сложность While - О(log(n)), зависит от расстояния между двумя столицами
        index = last_capital
        last_capital = number_city
        number_city = dict_road_map[last_capital]
        dict_road_map[last_capital] = index

    for key, value in dict_road_map.items(): # O(n)
        if key == new_capital:
            continue
        else:
            new_road_map.append(value)

    return new_road_map


n = 8
old_capital = 3
new_capital = 2
old_map = [6, 4, 7, 7, 3, 3, 6]
print(find_new_map(n, old_capital, new_capital, old_map))
