import os
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
    os.system("cls")

def parameter_input():

    is_correct_input = False

    while is_correct_input == False:
        try:
            fabricator = input("введите производителя:")
            CPU = input("введите название процессора:")
            GPU = int(input("введите количество видеопамяти графического процессора:"))
            RAM = int(input("введите количество оперативной памяти:"))
            SSD = int(input("введите количество внутренней памяти:"))
            weight = int(input("введите вес компьютера:"))
            price = int(input("введите стоимость компьютера:"))
            count = int(input("введите количество товара на складе:"))

            return GamePC(0, fabricator, CPU, GPU, RAM, SSD, weight, price, count)
            
        except:
            os.system("cls")
            print(f"ошибка ввода. Попробуйте ввести ещё раз")
            is_correct_input = False
            
def print_PC(PCs):
    os.system("cls")
    print(f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}")

    for i in range(len(PCs)):
        print(f"{PCs[i].id:<8}{PCs[i].fabricator:<15}{PCs[i].CPU:<15}{PCs[i].GPU:<15}{PCs[i].RAM:<15}{PCs[i].SSD:<15}{PCs[i].weight:<7}{PCs[i].price:<10}{PCs[i].count:<15}")

def print_best_bat(PCs):
    best = 0
    bad = PCs[0].price
    ind_best = 0
    ind_bad = 0
    for best_price in range(len(PCs)):
        if PCs[best_price].price > best:
            best = PCs[best_price].price
            ind_best = best_price
    for bad_price in range(len(PCs)):
        if PCs[bad_price].price < bad:
            bad = PCs[bad_price].price
            ind_bad = bad_price
    
    os.system("cls")

    print(f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}")
    print("Самый дорогой:")
    print(f"{PCs[ind_best].id:<8}{PCs[ind_best].fabricator:<15}{PCs[ind_best].CPU:<15}{PCs[ind_best].GPU:<15}{PCs[ind_best].RAM:<15}{PCs[ind_best].SSD:<15}{PCs[ind_best].weight:<7}{PCs[ind_best].price:<10}{PCs[ind_best].count:<15}")
    print("Самый дешёвый:")
    print(f"{PCs[ind_bad].id:<8}{PCs[ind_bad].fabricator:<15}{PCs[ind_bad].CPU:<15}{PCs[ind_bad].GPU:<15}{PCs[ind_bad].RAM:<15}{PCs[ind_bad].SSD:<15}{PCs[ind_bad].weight:<7}{PCs[ind_bad].price:<10}{PCs[ind_bad].count:<15}")        

def up_RAM(PCs, id, up):
    os.system("cls")
    for i in range(len(PCs)):
        if PCs[i].id == id:
            PCs[i].RAM += up
        print(f"Изменение памяти компьютера с id {id} успешно завершено")
        break
    else:
        print(f"компьютера с id {id} не существует")

def sale(PCs, id):
    os.system("cls")
    for ind in range(len(PCs)):
        if PCs[ind].id == id:
            PCs[ind].price -= PCs[ind].price * 0.1
            print(f"Компьютер с id {id} выстовлен на распрадажу")
            break
    else:
        print(f"компьютера с id {id} не существует")

def del_PC_id(PCs, id):
    os.system("cls")
    for ind in range(len(PCs)):
        if PCs[ind].id == id:
            PCs.pop(ind)
            print(f"Компьютер с id {id} успешно удален")
            break
    else:
        print(f"компьютера с id {id} не существует")

def del_PC_ind(PCs, ind):
    os.system("cls")
    try:
        PCs.pop(ind)
    except:
        print(f"Компьютера с индексом {ind} не существует")

def print_ind_PC(PCs, ind):
    os.system("cls")
    try:
        print(f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}")
        print(f"{PCs[ind].id:<8}{PCs[ind].fabricator:<15}{PCs[ind].CPU:<15}{PCs[ind].GPU:<15}{PCs[ind].RAM:<15}{PCs[ind].SSD:<15}{PCs[ind].weight:<7}{PCs[ind].price:<10}{PCs[ind].count:<15}")
    except:
        print(f"Компьютера с индексом {ind} не существует")

def compare_GPU(PCs, min_har):
    print_only_heading()
    for ind in range(len(PCs)):
        if PCs[ind].GPU > min_har:
            print_ind_PC(PCs, ind)

def print_only_heading():
    print(f"{'ID':<8}{'Изготовитель':<15}{'CPU':<15}{'GPU':<15}{'RAM':<15}{'SSD':<15}{'вес':<7}{'цена':<10}{'количество товаров':<15}")

def print_1_pc(PC):
    print(f"{PC.id:<8}{PC.fabricator:<15}{PC.CPU:<15}{PC.GPU:<15}{PC.RAM:<15}{PC.SSD:<15}{PC.weight:<7}{PC.price:<10}{PC.count:<15}")

def sorted_PC_price(PCs):
    j = 1
    mid_glass = 0
    while True:
        if j == 0:
            break
        j = 0
        for i in range(len(PCs) - 1):
            if PCs[i].price < PCs[i + 1].price:
                mid_glass = PCs[i + 1]
                PCs[i + 1] = PCs[i]
                PCs[i] = mid_glass
                j += 1
    print_PC(PCs)

def searc_PC(PCs, min_ram, max_price):
    os.system("cls")
    print("\nПОИСК ПО ОЗУ И ЦЕНЕ")
    
    results = []
    for pc in PCs:
        if pc.RAM >= min_ram and pc.price <= max_price:
            results.append(pc)
    
    if results:
        print(f"\nНайдено {len(results)} компьютеров с ОЗУ ≥ {min_ram}ГБ и ценой ≤ {max_price}:")
        print_PC(results)
    else:
        print(f"\nНет компьютеров с ОЗУ ≥ {min_ram}ГБ и ценой ≤ {max_price}")
            
def menu():
    global GAME_RUN
    print("======= МЕНЮ =======")
    print("== ВЫБОР ДЕЙСТВИЙ ==")
    print("1) Добавить компьютер")
    print("2) Показать все компьютеры")
    print("3) Поиск компьютеров")
    print("4) Сортировка по цене")
    print("5) Самый дорогой/дешевый")
    print("6) увеличить оперативную память ПК")
    print("7) удалить ПК")
    print("8) поставить на распродажу")
    print("9) поиск GPU по его минимальным характеристикам")
    print("0) Выход")
    result = int(input("сделай выбор:"))

    if result == 1:
        os.system("cls")
        add_PC(PCs, parameter_input())
    elif result == 2:
        os.system("cls")
        print_PC(PCs)
    elif result == 3:
        os.system("cls")
        is_correct_input = False
        while is_correct_input == False:
            try:
                min_ram = int(input("введите минимальное количество оперативной памяти в пк (ГБ):"))
                max_price = int(input("введите максимальную стоимость компьютера:")) 
                is_correct_input = True
            except:
                is_correct_input = False
                print("Ошибка ввода попробуйте ещё раз")

        searc_PC(PCs, min_ram, max_price)
    elif result == 4:
        os.system("cls")
        sorted_PC_price(PCs)
    elif result == 5:
        os.system("cls")
        print_best_bat(PCs)
    elif result == 6:
        os.system("cls")
        is_correct_input = False
        while is_correct_input == False:
            os.system("cls")
            try:
                id = int(input("введите ID ПК:"))
                up_ram = int(input("введите количество оперативной памяти которую вы хотите добавить:"))
                is_correct_input = True
            except:
                is_correct_input = False
                print("ошибка ввода попробуйте ещё раз")
        up_RAM(PCs, id, up_ram)
    elif result == 7:
        os.system("cls")
        is_correct_input = False
        while is_correct_input == False:
            try:
                result_7 = int(input("как вы хотите удалить пк (1 - по ID, 2 - по индексу)"))
                is_correct_input = True
            except:
                is_correct_input = False
                os.system("cls")
                print("Ошибка ввода попробуйте ещё раз")
        if result_7 == 1:
            id_PC = 0
            os.system("cls")
            is_correct_input = False
            while is_correct_input == False:
                try:
                    id_PC = int(input("введите ID ПК:"))
                    is_correct_input = True
                except:
                    os.system("cls")
                    is_correct_input = False
                    print("Ошибка ввода попробуйте ещё раз")
            del_PC_id(PCs, id_PC)
        else:
            os.system("cls")
            is_correct_input = False
            while is_correct_input == False:
                try:
                    ind_PC = int(input("введите INDEX ПК:"))
                    is_correct_input = True
                except:
                    os.system("cls")
                    is_correct_input = False
                    print("Ошибка ввода попробуйте ещё раз")
            del_PC_ind(PCs, ind_PC)
    elif result == 8:
        os.system("cls")
        is_correct_input = False
        while is_correct_input == False:
            try:
                sale_id = int(input("введте ID ПК которому вы хотите сделать скидку:"))
                is_correct_input = True
            except:
                os.system("cls")
                is_correct_input = False
                print("Ошибка ввода попробуйте ещё раз")
        sale(PCs, sale_id)
    elif result == 9:
        os.system("cls")
        is_correct_input = False
        while is_correct_input == False:
            try:
                har = int(input("введите минимальную характеристику видеокарте (ГБ видеопамяти):"))
                is_correct_input = True
            except:
                is_correct_input = False
                print("Ошибка ввода попробуйте ещё раз")
        compare_GPU(PCs, har)
    else:
        os.system("cls")
        GAME_RUN = False
        return GAME_RUN

PCs.append(GamePC(1, 1, 1, 16, 1, 1, 1, 180000, 1))
PCs.append(GamePC(2, 2, 2, 32, 2, 2, 2, 120000, 2))
PCs.append(GamePC(3, 1, 1, 16, 1, 1, 1, 200000, 1))
PCs.append(GamePC(4, 2, 2, 32, 2, 2, 2, 300000, 2))
GAME_RUN = True
while GAME_RUN:
    menu()
