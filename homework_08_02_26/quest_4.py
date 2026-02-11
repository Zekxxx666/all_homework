from dataclasses import dataclass

ID = 0

@dataclass
class Film:
    id: int
    name: str
    genr: int
    director: str
    year: int
    time: int
    rate: float
    price: int
    copy: int
    epic: str

def input_correct(text):
    is_correct_input = False
    while is_correct_input == False:
        try:
            result = int(input(text))
            is_correct_input = True
        except:
            print("Ошибка ввода, попробуй ещё раз")
            is_correct_input = False
    return result

def input_correct_float(text):
    is_correct_input = False
    while is_correct_input == False:
        try:
            result = float(input(text))
            is_correct_input = True
        except:
            print("Ошибка ввода, попробуй ещё раз")
            is_correct_input = False
    return result

def add_film(Films, film):
    global ID

    ID += 1

    film.id = ID

    Films.append(film)

def input_film():
    name = input("введите название фильма:")
    genr = input_correct("вветите жанр фильма (1 - Драма, 2 - Боевик, 3 - Комедия, 4 - Фантастика)")
    director = input("введите название режиссёра:")
    year = input_correct("введите год выпуска фильма:")
    time = input_correct("введите год выпуска фильма:")
    rate = input_correct_float("введите рейтинг фильма:")
    price = input_correct("введите стоимось фильма:")
    copy = input_correct("введите количество копий фильма:")
    epic = "-"
    return Film(0, name, genr, director, year, time, rate, price, copy, epic)

def del_film_rate_under_5_0(Films):
    for ind in range(len(Films)):
        if Films[ind].rate  < 5.0:
            Films.pop(ind)

def print_all_film(Films):
    print(
        f"{'ID':<15}{'название':<15}{'жанр':<15}"
        f"{'Режиссер':<20}{'год выпуска':<15}{'длительность':<15}"
        f"{'рейтинг':<15}{'цена':<20}{'количество копий':<15}"
        )
    for i in range(len(Films)):    
        print(
            f"{Films[i].id:<15}{Films[i].name:<15}{Films[i].genr:<15}"
            f"{Films[i].director:<20}{Films[i].year:<15}{Films[i].time:<15}"
            f"{Films[i].rate:<15}{Films[i].price:<20}{Films[i].copy:<15}"
            )

def sorted_ganr(Films):
    sort = False
    while sort == False:
        sort = True
        mid_glass = 0

        for ind in range(len(Films) - 1):
            if Films[ind].ganr > Films[ind + 1].ganr:
                mid_glass = Films[ind + 1]
                Films[ind + 1] = Films[ind]
                Films[ind] = mid_glass
                sort = False

    print_all_film(Films)

def film_grate_150_min_epic(Films):
    for ind in range(len(Films)):
        if Films[ind].time > 150:
            Films[ind].epic = "+"

def up_price_film_year_unser_2000(Films, up_price):
    for ind in range(len(Films)):
        if Films[ind].year < 2000:
            Films[ind].price *= 1 + up_price / 100

def print_only_heading():
    print(
        f"{'ID':<15}{'название':<15}{'жанр':<15}"
        f"{'Режиссер':<20}{'год выпуска':<15}{'длительность':<15}"
        f"{'рейтинг':<15}{'цена':<20}{'количество копий':<15}"
        )     

def print_1_film(film):
    print(
        f"{film.id:<15}{film.name:<15}{film.genr:<15}"
        f"{film.director:<20}{film.year:<15}{film.time:<15}"
        f"{film.rate:<15}{film.price:<20}{film.copy:<15}"
        )

def print_top_3_films(Films):
    print_film = []
    sort = False
    while sort == False:
        StopIteration = True
        mid_glass = 0

        for ind in range(len(Films) - 1):
            if Films[ind].rate < Films[ind + 1].rate:
                mid_glass = Films[ind + 1]
                Films[ind + 1] = Films[ind]
                Films[ind] = mid_glass
                sort = False

    print_film.append(Films[0])
    print_film.append(Films[1])
    print_film.append(Films[2])

    print_only_heading()
    for ind in range(len(print_film)):
        print_1_film(print_film[ind])

def mid_time_film(Films):
    mid_time = 0
    all_time = 0
    for ind in range(len(Films)):
        all_time += Films[ind].time
    mid_time = all_time / len(Films)
    print(f"среднее время фильмов равна {mid_time} минут")

def sorted_time(Films):
    sort = False
    while sort == False:
        sort = True
        mid_glass = 0

        for ind in range(len(Films) - 1):
            if Films[ind].time < Films[ind + 1].time:
                mid_glass = Films[ind + 1]
                Films[ind + 1] = Films[ind]
                Films[ind] = mid_glass
                sort = False
    
    print_all_film(Films)

def sorted_rate(Films):
    sort = False
    while sort == False:
        sort = True
        mid_glass = 0

        for ind in range(len(Films) - 1):
            if Films[ind].rate < Films[ind + 1].rate:
                mid_glass = Films[ind + 1]
                Films[ind + 1] = Films[ind]
                Films[ind] = mid_glass
                sort = False

    print_all_film(Films)

def find_film_time(Films, time):
    print_only_heading()
    for ind in range(len(Films)):
        if Films[ind].time >= time:
            print_1_film(Films[ind])
    
def find_film_ganr(Films, ganr):
    print_only_heading()
    for ind in range(len(Films)):
        if Films[ind].ganr == ganr:
            print_1_film(Films[ind])

GAME_RUN = True
Films = []

def menu():
    global GAME_RUN

    print("======= МЕНЮ =======")
    print("== ВЫБОР ДЕЙСТВИЙ ==")
    print("1) удалить фильмы с рейтингом ниже 5.0")
    print("2) сгруппировать фильмы по жанрам и вывести результат")
    print("3) пометить фильмы длительностью более 150 минут как «эпик»")
    print("4) увеличить цену фильмов, выпущенных до 2000 года")
    print("5) вывести топ-3 фильма по рейтингу")
    print("6) вывести все фильмы")
    print("7) добавить фильм")
    print("8) сортировка фильмов")
    print("9) поиск фильмов")
    print("0) выход")

    result = int(input("введите что вы хотите:"))

    if result == 1:
        del_film_rate_under_5_0(Films)
    elif result == 2:
        sorted_ganr(Films)
    elif result == 3:
        film_grate_150_min_epic(Films)
    elif result == 4:
        up_price = input_correct("введите на сколько процентов вы хотите повысить цену фильмов:")
        up_price_film_year_unser_2000(Films, up_price)
    elif result == 5:
        print_top_3_films(Films)
    elif result == 6:
        print_all_film(Films)
    elif result == 7:
        add_film(Films, input_film())
    elif result == 8:
        sort = input_correct("как вы хотите отсортировать фильмы (1 - по времени, 2 - по оценке):")
        if sort == 1:
            sorted_time(Films)
        else:
            sorted_rate(Films)
    elif result == 9:
        how_find = input_correct("введите как вы хотите найти фильм (1 - по времени, 2 - по жанру):")
        if how_find == 1:
            time = input_correct("введите минимальное количество времени для фильма:")
            find_film_time(Films, time)
        else:
            ganr = input_correct("введите жанр для фильма (1 - Драма, 2 - Боевик, 3 - Комедия, 4 - Фантастика):")

            find_film_ganr(Films, ganr)

    else:
        GAME_RUN = False

        return GAME_RUN
    
while GAME_RUN:
    menu()
       