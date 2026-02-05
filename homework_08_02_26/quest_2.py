from dataclasses import dataclass

ID = 1

@dataclass
class Game:
    id: int
    name: str
    genre: int
    Platform: str
    age: int
    price: int
    rate: float
    state: str
    copy: int
    hit: str

Games = []
Games.append(Game(1, "bss", 4, "Boblox", 18, 0, 10, "good", 1000000, "-"))

def add_game(Games, game):
    global ID

    ID += 1

    game.id = ID

    Games.append(game)

def game_input():
    name = input("введите название игры:")
    genre = int(input("Введите жанр игры (1 - Шутеры, 2 - РПГ, 3 - Стратегии, 4 - приключения):"))
    Platform = input("введите платформу игры:")
    age = int(input("введите возрастное ограничение игры:"))
    price = int(input("введите стоимость игры:"))
    rate = int(input("введите оценку игроков:"))
    state = input("введите статус игры:")
    copy = int(input("введите количество копий:"))
    hit = "-"
    return Game(0, name, genre, Platform, age, price, rate, state, copy, hit)

def find_best_rate(Games):
    last_rate = 0
    ind = 0
    for i in range(len(Games)):
        if Games[i].rate > last_rate:
            last_rate = Games[i].rate
            ind = i
    print_1_game(Games[ind])
    

def print_1_game(Game):
    print(f"{'id':<13}{'название игры':<15}{'жанр':<15}{'Платформа':<15}{'возрастное ограничение':<25}{'цена':<13}{'оценка':<15}{'статус':<15}{'копий в наличии':<18}{'в Хите':<5}")
    print(f"{Game.id:<13}{Game.name:<15}{Game.genre:<15}{Game.Platform:<15}{Game.age:<25}{Game.price:<13}{Game.rate:<15}{Game.state:<15}{Game.copy:<18}{Game.hit:<5}")

def del_rate_dead(Games):
    del_game = 0
    for i in range(len(Games)):
        if Games[i].rate == 0:
            Games.pop(i)
            del_game += 1

    print(f"было удалено {del_game} игр")
    

def mid_price(Games):
    all_price = 0
    for i in range(len(Games)):
        all_price += Games[i].price
    mid_price = all_price / len(Games)

    print(f"средняя стоимоть игр {mid_price}")

def check_hit(Games):
    for i in range(len(Games)):
        if Games[i].rate >= 8.5:
            Games[i].hit = "+"
    
def sale_ganre(Games, ganre, sales):
    sale = 0
    for i in range(len(Games)):
        if Games[i].ganre == ganre:
            Games[i].price *= (100 - sales) / 100
            sale += 1
    print(f"успешно изменена стоимость {sale} игр")

def sorted_game_rate(Games):
    j = 0
    while True:
        if j == 0:
            break
        j = 0
        mid_glass = 0
        
        for i in range(len(Games) - 1):
            if Games[i].rate > Games[i + 1].rate:
                mid_glass = Games[i + 1]
                Games[i + 1] = Games[i]
                Games[i] = mid_glass
                j += 1
    
    Games.reverse()
    print_all_Game(Games)

def print_all_Game(Games):
    print(f"{'id':<13}{'название игры':<15}{'жанр':<15}{'Платформа':<15}{'возрастное ограничение':<25}{'цена':<13}{'оценка':<15}{'статус':<15}{'копий в наличии':<18}{'в Хите':<5}")
    for i in range(len(Games)):
        print(f"{Games[i].id:<13}{Games[i].name:<15}{Games[i].genre:<15}{Games[i].Platform:<15}{Games[i].age:<25}{Games[i].price:<13}{Games[i].rate:<15}{Games[i].state:<15}{Games[i].copy:<18}{Games[i].hit:<5}")

def sort_alphabet(Games):
    j = 1
    while True:
        if j == 0:
            break
        j = 0
        mid_glass = 0
        
        for i in range(len(Games) - 1):
            if ord(Games[i].name) > ord(Games[i + 1].name):
                mid_glass = Games[i + 1]
                Games[i + 1] = Games[i]
                Games[i] = mid_glass
                j += 1
    
    print_all_Game(Games)

def filter_game_age_up(Games,age):
    for i in range(len(Games)):
        if Games[i].age >= age:
            print_1_game(Games[i])
    
def filter_game_age_down(Games,age):
    for i in range(len(Games)):
        if Games[i].age <= age:
            print_1_game(Games[i])

def filter_game_platform(Games, platform):
    for i in range(len(Games)):
        if Games[i].Platform == platform:
            print(Games[i])

def find_game_id(Games, name):
    for i in range(len(Games)):
        if Games[i].name.find(name) != -1:
            print_1_game(Games[i])
            break
    else:
        print(f"игры с таким именем не существует не существует")

def menu():
    global GAME_RUN

    print("======= МЕНЮ =======")
    print("== ВЫБОР ДЕЙСТВИЙ ==")
    print("1) удалить все игры, у которых количество копий равно 0")
    print("2) найти игру с максимальной оценкой")
    print("3) подсчитать среднюю цену всех игр")
    print("4) изменить цену всех игр выбранного жанра")
    print("5) сортировка игр")
    print("6) фильтрация игр")
    print("7) поиск игр по части названия")
    print("8) добавить игру")
    print("9) вывести все игры")
    print("0) выход")

    inpud = int(input("введите что вы хотите:"))

    if inpud == 1:
        del_rate_dead(Games)
    elif inpud == 2:
        find_best_rate(Games)
    elif inpud == 3:
        mid_price(Games)
    elif inpud == 4:
        ganre = int(input("Введите жанр игры (1 - Шутеры, 2 - РПГ, 3 - Стратегии, 4 - приключения):"))
        sales = int(input("введите на сколько % вы хотите понизить стоимость:"))

        sale_ganre(Games, ganre, sales)
    elif inpud == 5:
        input_5 = int(input("введите как вы хотите отсортировать игры(1 - по рейтенгу, 2 - по алфавиту):"))

        if input_5 == 1:
            sorted_game_rate(Games)
        else:
            sort_alphabet(Games)
    elif inpud == 6:
        input_6 = int(input("введите как вы хотите отфильтровать игры (1 - по возрасту, 2 - по платформе):"))

        if input_6 == 1:
            up_down = int(input("отсортировать (1 - больше, 2 - меньше):"))
            age = int(input("введите возраст:"))
            if up_down == 1:
                filter_game_age_up(Games, age)
            else:
                filter_game_age_down(Games, age)
        else:
            platform = input("введите платформу:")
            filter_game_platform(Games, platform)
    elif inpud == 7:
        id = input("введите название игры игры:")
        find_game_id(Games, id)
    elif inpud == 8:
        add_game(Games)
    elif inpud == 9:
        print_all_Game(Games)
    else:
        GAME_RUN == False


GAME_RUN = True

while GAME_RUN:
    menu()
    check_hit(Games)


