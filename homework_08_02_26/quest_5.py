from dataclasses import dataclass

ID = 0

@dataclass 
class SportEqup:
    id: int
    name: str
    sport: str
    material: str
    weight: int
    size: str
    price: int
    status: int
    count: int
    request_fix: str

def add_equp(Equpments, equp):
    global ID

    ID += 1

    equp.id = ID

    Equpments.append(equp)

def input_equp():
    name = input("введите название оборудования:")
    sport = input("введите вид спорта где это оборудование используется:")
    material = input("введите материал из которого сделано оборудование:")
    weight = int(input("введите вес оборудования:"))
    size = input("введите размер оборудования:")
    price = int(input("введите стоимость товара:"))
    status = int(input("введите статус оборудования (1 - новый, 2 - использованный, 3 - сломанный):"))
    count = int(input("введите количество товара на складе:"))
    request_fix = "-"
    return SportEqup(0, name, sport, material, weight, size, price, status, count, request_fix)

def del_equp_count_0(Equpments):
    for i in range(len(Equpments)):
        if Equpments[i].count == 0:
            Equpments.pop(i)

def find_max_weight_equp(Equpments):
    while True:
        if j == 0:
            break
        j = 0
        mid_glass = 0

        for i in range(len(Equpments) - 1):
            if Equpments[i].weight > Equpments[i + 1].weight:
                mid_glass = Equpments[i + 1]
                Equpments[i + 1] = Equpments[i]
                Equpments[i] = mid_glass

    Equpments.reverse()
    if len(Equpments) - 1 > 0:
        print_only_heading()
        print_1_equp(Equpments[0])

def print_only_heading():
    print(f"{'id':<15}{'название':<20}{'Вид спорта':<15}{'Материал':<15}{'Вес':<15}{'Размер':<15}{'Цена':<15}{'Состояние':<15}{'Количество на складе':<23}{'Требуется ремонт':<10}")

def print_1_equp(equp):
    print(f"{equp.id:<15}{equp.name:<20}{equp.sport:<15}{equp.maretial:<15}{equp.weight:<15}{equp.size:<15}{equp.price:<15}{equp.status:<15}{equp.count:<23}{equp.request_fix:<10}")

def print_all_equp(Equpment):
    for i in range(len(Equpment)):
        print_only_heading()
        print(f"{Equpment[i].id:<15}{Equpment[i].name:<20}{Equpment[i].sport:<15}{Equpment[i].maretial:<15}{Equpment[i].weight:<15}{Equpment[i].size:<15}{Equpment[i].price:<15}{Equpment[i].status:<15}{Equpment[i].count:<23}{Equpment[i].request_fix:<10}")

def request_fix(Equpments):
    for i in range(len(Equpments)):
        if Equpments[i].status != 1:
            Equpments[i].request_fix = "+"

def print_only_new_equp(Equpments):
    print_only_heading()
    for i in range(len(Equpments)):
        if Equpments[i].status == 1:
            print_1_equp(Equpments[i])

def print_all_price_equp(Equpments):
    all_price = 0
    for i in range(len(Equpments)):
        all_price += Equpments[i].price * Equpments[i].count
    
    print(f"стоимость всего склада равна {all_price}")

def under_count_by_id(Equpments, id, under):
    for i in range(len(Equpments)):
        if Equpments[i].id == id:
            Equpments[i].count -= under
            break
    else:
        print(f"товара с id {id} не сушествует")

def sorted_by_price(Equpments):
    while True:
        if j == 0:
            break
        j = 0
        mid_glass = 0

        for i in range(len(Equpments) - 1):
            if Equpments[i].price > Equpments[i + 1].price:
                mid_glass = Equpments[i + 1]
                Equpments[i + 1] = Equpments[i]
                Equpments[i] = mid_glass

    Equpments.reverse()
    print_all_equp(Equpments)

def sorted_by_count(Equpments):
    while True:
        if j == 0:
            break
        j = 0
        mid_glass = 0

        for i in range(len(Equpments) - 1):
            if Equpments[i].count > Equpments[i + 1].count:
                mid_glass = Equpments[i + 1]
                Equpments[i + 1] = Equpments[i]
                Equpments[i] = mid_glass
    Equpments.reverse()
    print_all_equp(Equpments)

def search_sport(Equpments, sport):
    print_only_heading()
    for i in range(len(Equpments)):
        if Equpments[i].sport == sport:
            print_1_equp(Equpments[i])

def search_weight_up(Equpments, weight):
    print_only_heading()
    for i in range(len(Equpments)):
        if Equpments[i].weight > weight:
            print_1_equp(Equpments[i])

def search_weight_down(Equpments, weight):
    print_only_heading()
    for i in range(len(Equpments)):
        if Equpments[i].weight < weight:
            print_1_equp(Equpments[i])

GAME_RUN = True

Equpments =[]

def menu():
    global GAME_RUN

    print("======= МЕНЮ =======")
    print("== ВЫБОР ДЕЙСТВИЙ ==")
    print("1) Добавить оборудование")
    print("2) удалить инвентарь с количеством на складе равным 0")
    print("3) найти самый тяжёлый инвентарь")
    print("4) пометить инвентарь как «требует ремонта», если состояние не равно «новый»")
    print("5) вывести инвентарь в состоянии «новый»")
    print("6) подсчитать общую стоимость склада")
    print("7) списать инвентарь, уменьшить количество на складе на указанное число")
    print("8) сортировка инвентаря")
    print("9) поиск инвентаря по виду спорта или диапазону веса")
    print("10) вывести все оборудование")
    print("0) выход")

    result = int(input("сделай свой выбор:"))
    
    if result == 1:
        add_equp(Equpments, input_equp())
    elif result == 2:
        del_equp_count_0(Equpments)
    elif result == 3:
        find_max_weight_equp(Equpments)
    elif result == 4:
        request_fix(Equpments)
    elif result == 5:
        print_only_new_equp(Equpments)
    elif result == 6:
        print_all_price_equp(Equpments)
    elif result == 7:
        id = int(input("Введите id оборудования:"))
        under = int(input("введите на сколько вы хотите понизить количество позиций:"))
        under_count_by_id(Equpments, id, under)
    elif result == 8:
        sort = int(input("введите как вы хотите отсортировать спортивного инвентаря(1 - по количеству, 2 - по цене)"))

        if sort == 1:
            sorted_by_count(Equpments)
        else:
            sorted_by_price(Equpments)
    elif result == 9:
        search = int(input("введите как вы хотите найти оборудование(1 - по виду спорта, 2 - по диапозону веса):"))

        if search == 1:
            sport = input("введите вид спорта:")
            search_sport(Equpments, sport)
        else:
            weight = int(input("введите вес:"))
            up_down = int(input("1 - больше, 2 - меньше:"))

            if up_down == 1:
                search_weight_up(Equpments, weight)
            else:
                search_weight_down(Equpments, weight)
    elif result == 10:
        print_all_equp(Equpments)
    else:
        GAME_RUN = False

        return GAME_RUN

while GAME_RUN:
    menu()     




#ИД — целое уникальное число
#Название — строка (макс 20 символов)
#Вид спорта — строка (макс 15 символов)
#Материал — строка (макс 15 символов)
#Вес — целое число
#Размер — строка (макс 10 символов)
#Цена — целое число
#Состояние — строка (макс 10 символов)
#Количество на складе — целое число