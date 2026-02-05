from dataclasses import dataclass
ID = 4

@dataclass
class GamePC:
    id: int
    fabricator: str
    CPU: str
    GPU: str
    RAM: int
    SSD: int
    weight: int
    price: int
    count: int

PCs = []

def add_PC(PCs, PC):
    global ID

    ID += 1

    PC.id = ID

    PCs.append(PC)

def parameter_input():
    fabricator = input("введите производителя:")
    CPU = input("введите название процессора:")
    GPU = input("введите количество видеопамяти графического процессора:")
    RAM = int(input("введите количество оперативной памяти:"))
    SSD = int(input("введите количество внутренней памяти:"))
    weight = int(input("введите вес компьютера:"))
    price = int(input("введите стоимость компьютера:"))
    count = int(input("введите количество товара на складе:"))

    return GamePC(0, fabricator, CPU, GPU, RAM, SSD, weight, price, count)

def print_PC(PCs):
    print(f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}")

    for i in range(len(PCs)):
        print(f"{PCs[i].id:<8}{PCs[i].fabricator:<15}{PCs[i].CPU:<15}{PCs[i].GPU:<15}{PCs[i].RAM:<15}{PCs[i].SSD:<15}{PCs[i].weight:<7}{PCs[i].price:<10}{PCs[i].count:<15}")

def print_best_bat(PCs):
    best = 0
    bat = 10000000000000000000000
    ind_best = 0
    ind_bat = 0
    for i in range(len(PCs)):
        if PCs[i].price > best:
            best = PCs[i].price
            ind_best = i
    for j in range(len(PCs)):
        if PCs[j].price < bat:
            bat = PCs[j].price
            ind_bat = j

    print(f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}")
    print("Самый дорогой:")
    print(f"{PCs[ind_best].id:<8}{PCs[ind_best].fabricator:<15}{PCs[ind_best].CPU:<15}{PCs[ind_best].GPU:<15}{PCs[ind_best].RAM:<15}{PCs[ind_best].SSD:<15}{PCs[ind_best].weight:<7}{PCs[ind_best].price:<10}{PCs[ind_best].count:<15}")
    print("Самый дешёвый:")
    print(f"{PCs[ind_bat].id:<8}{PCs[ind_bat].fabricator:<15}{PCs[ind_bat].CPU:<15}{PCs[ind_bat].GPU:<15}{PCs[ind_bat].RAM:<15}{PCs[ind_bat].SSD:<15}{PCs[ind_bat].weight:<7}{PCs[ind_bat].price:<10}{PCs[ind_bat].count:<15}")        

def up_RAM(PCs, id, up):
    for i in range(len(PCs)):
        if PCs[i].id == id:
            PCs[i].RAM += up
    else:
        print(f"компьютера с id {id} не существует")

def sale(PCs, id):
    for i in range(len(PCs)):
        if PCs[i].id == id:
            PCs[i].price -= PCs[i].price * 0.1
            break
    else:
        print(f"компьютера с id {id} не существует")

def del_PC_id(PCs, id):
    for i in range(len(PCs)):
        if PCs[i].id == id:
            PCs.pop(i - 1)
            break
    else:
        print(f"компьютера с id {id} не существует")

def del_PC_ind(PCs, ind):
    PCs.pop(ind)

def print_ind_PC(PCs, ind):
    print(f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}")
    print(f"{PCs[ind].id:<8}{PCs[ind].fabricator:<15}{PCs[ind].CPU:<15}{PCs[ind].GPU:<15}{PCs[ind].RAM:<15}{PCs[ind].SSD:<15}{PCs[ind].weight:<7}{PCs[ind].price:<10}{PCs[ind].count:<15}")

def compare_GPU(PCs, min_har):
    for i in range(len(PCs)):
        if PCs[i].GPU > min_har:
            print_ind_PC(PCs, i)

def sorted_PC_price(PCs):
    j = 1
    mid_glass = 0
    while True:
        if j == 0:
            break
        j = 0
        for i in range(len(PCs) - 1):
            if PCs[i].price > PCs[i + 1].price:
                mid_glass = PCs[i + 1].price
                PCs[i + 1].price = PCs[i].price
                PCs[i].price = mid_glass
                j += 1
    PCs.reverse()
    print_PC(PCs)

def searc_PC(PCs):
    print("\nПОИСК ПО ОЗУ И ЦЕНЕ")
    
    try:
        min_ram = int(input("Минимальное ОЗУ (ГБ): "))
        max_price = int(input("Максимальная цена: "))
        
        results = []
        for pc in PCs:
            if pc.RAM >= min_ram and pc.price <= max_price:
                results.append(pc)
        
        if results:
            print(f"\nНайдено {len(results)} компьютеров с ОЗУ ≥ {min_ram}ГБ и ценой ≤ {max_price}:")
            print_PC(results)
        else:
            print(f"\nНет компьютеров с ОЗУ ≥ {min_ram}ГБ и ценой ≤ {max_price}")
            
    except ValueError:
        print("Ошибка ввода! Введите целые числа.")

def menu():
    global GAME_RUN
    print("=== МЕНЮ ===")
    print("1) Добавить компьютер")
    print("2) Показать все компьютеры")
    print("3) Поиск компьютеров")
    print("4) Сортировка по цене")
    print("5) Самый дорогой/дешевый")
    print("6) увеличить оперативную память ПК")
    print("7) удалить ПК")
    print("8) поставить на распродажу")
    print("9) поиск GPU п оего минимальным характеристикам")
    print("0) Выход")
    result = int(input("сделай выбор:"))

    if result == 1:
        add_PC(PCs, parameter_input())
    elif result == 2:
        print_PC(PCs)
    elif result == 3:
        searc_PC(PCs)
    elif result == 4:
        sorted_PC_price(PCs)
    elif result == 5:
        print_best_bat(PCs)
    elif result == 6:
        print("введите ID ПК:")
        id = int(input())
        print("введите количество оперативной памяти которую вы хотите добавить:")
        up_ram = int(input())
        up_RAM(PCs, id, up_ram)
    elif result == 7:
        print("как вы хотите удалить пк (1 - по ID, 2 - по индексу)")
        result_7 = int(input())
        if result_7 == 1:
            ID_PC = int(input("введите ID ПК:"))
            del_PC_id(PCs, ID_PC)
        else:
            IND_PC = int(input("введите INDEX ПК:"))
            del_PC_ind(PCs, IND_PC)
    elif result == 8:
        print("введте ID ПК которому вы хотите сделать скидку:")
        sale_id = int(input())
        sale(PCs, sale_id)
    elif result == 9:
        print("введите минимальную характеристику видеокарте (ГБ видеопамяти):")
        har = int(input())
        compare_GPU(PCs, har)
    else:
        GAME_RUN = False
        return GAME_RUN

        


PCs.append(GamePC(1, 1, 1, 16, 1, 1, 1, 180000, 1))
PCs.append(GamePC(2, 2, 2, 32, 2, 2, 2, 120000, 2))
PCs.append(GamePC(3, 1, 1, 16, 1, 1, 1, 200000, 1))
PCs.append(GamePC(4, 2, 2, 32, 2, 2, 2, 300000, 2))
GAME_RUN = True
while GAME_RUN:
    menu()
