from dataclasses import dataclass

ID = 0

@dataclass
class OnlineCourse:
    id: int
    name: str
    platform: str
    language: str
    time: int
    lvl_hard: int
    price: int
    rate: float
    count_stud: int

Courses = []

def add_course(Courses, cours):
    global ID

    ID += 1

    cours.id = ID

    Courses.append(cours)

def import_course():
    name = input("введите название курса:")
    platform = input("введите название платформы:")
    language = input("введите язык курса:")
    time = int(input("введите длительность курса (часы):"))
    lvl_hard = int(input("введите уровень сложносли (1 - легко, 2 - средне, 3 - продвинутый):"))
    price = int(input("введите стоимость курса:"))
    rate = float(input("введите рейтинг курса:"))
    count_stud = int(input("введите количество студентов:"))
    return OnlineCourse(0, name, platform, language, time, lvl_hard, price, rate, count_stud)

def course_time(Courses, max_time):
    for i in range(len(Courses)):
        if Courses[i] <= max_time:
            print_1_cours(Courses[i])

def print_1_cours(Cours):
    print(f"{'ID':<15}{'название':<15}{'Платформа':<15}{'Язык':<15}{'Длительность':<15}{'Уровень сложности':<20}{'Цена':<15}{'Рейтинг':<15}{'Количество учеников':<20}")
    print(f"{Cours.id:<15}{Cours.name:<15}{Cours.platform:<15}{Cours.language:<15}{Cours.time:<15}{Cours.lvl_hard:<20}{Cours.price:<15}{Cours.rate:<15}{Cours.count_stud:<20}")

def all_income(Courses):
    all_income = 0
    for i in range(len(Courses)):
        all_income += Courses[i].price * Courses[i].count_stud
    
    print(f"доход равен {all_income}")

def up_price(Courses):
    j = 0
    for i in range(len(Courses)):
        if Courses[i].lvl_hard == 3:
            Courses[i].price *= 1.15
            j += 1 
    print(f"успешно изменена стоимость {j} курсов")
    
def print_up_time(Courses, min_time):
    for i in range(len(Courses)):
        if Courses[i].time >= min_time:
            print_1_cours(Courses[i])

def find_min_rate(Courses):
    min_rate = 10
    min_course = 0
    for i in range(len(Courses)):
        if Courses[i].rate < min_rate:
            min_rate = Courses[i].rate
            min_course = Courses[i]
    print_1_cours(min_course)

def del_cour_under_4(Courses):
    j = 0
    for i in range(len(Courses)):
        if Courses[i].rate < 4:
            Courses.pop(i)
            j += 1
    print(f"успешно удалено {j} курсов")

def sort_time(Courses):
    j = 1
    while True:
        if j == 0:
            break
        j = 0
        mid_glass = 0

        for i in range(len(Courses) - 1):
            if Courses[i].time > Courses[i + 1].time:
                mid_glass = Courses[i + 1].time
                Courses[i + 1] = Courses[i].time
                Courses[i] = mid_glass
    Courses.reverse()
    print_all_courses(Courses)

def print_all_courses(Courses):
    print(f"{'ID':<15}{'название':<15}{'Платформа':<15}{'Язык':<15}{'Длительность':<15}{'Уровень сложности':<20}{'Цена':<15}{'Рейтинг':<15}{'Количество учеников':<20}")
    for i in range(len(Courses)):
        print(f"{Courses[i].id:<15}{Courses[i].name:<15}{Courses[i].platform:<15}{Courses[i].language:<20}{Courses[i].time:<15}{Courses[i].lvl_hard:<15}{Courses[i].price:<15}{Courses[i].rate:<15}{Courses[i].count_stud:<20}")

def sort_stud(Courses):
    j = 1
    while True:
        if j == 0:
            break
        j = 0
        mid_glass = 0

        for i in range(len(Courses) - 1):
            if Courses[i].studs > Courses[i + 1].studs:
                mid_glass = Courses[i + 1]
                Courses[i + 1] = Courses[i]
                Courses[i] = mid_glass
    Courses.reverse()
    print_all_courses(Courses)

def search_platform(Courses, platform):
    for i in range(len(Courses)):
        if Courses[i] == platform:
            print_1_cours(Courses[i])

def search_lvl_hard(Courses, lvl):
    for i in range(len(Courses)):
        if Courses[i].lvl_hard == lvl:
            print_1_cours(Courses[i])

def egit_all_platform(Courses, platform):
    for i in range(len(Courses)):
        Courses[i].platform = platform


GAME_RUN = True


def menu():
    global GAME_RUN

    print("======= МЕНЮ =======")
    print("== ВЫБОР ДЕЙСТВИЙ ==")
    print("1) Добавить курс")
    print("2) найти курс с минимальным рейтингом")
    print("3) сортировка курсов")
    print("4) подсчитать общий доход")
    print("5) увеличить цену курсов уровня «продвинутый» на 15%")
    print("6) вывести курсы длительностью больше указанной")
    print("7) удалить курсы с рейтингом ниже 4.0")
    print("8) поиск курсов по платформе или уровню сложности")
    print("9) изменить названия платформы всем курсам")
    print("0) выход")

    inpud = int(input("введите что вы хотите:"))

    if inpud == 1:
        add_course(Courses, import_course())
    elif inpud == 2:
        find_min_rate(Courses)
    elif inpud == 3:
        inpud_3 = int(input("что вы хотите отсортировать (1 - по длительности, 2 - по количеству студентов):"))

        if inpud_3 == 1:
            sort_time(Courses)
        else:
            sort_stud(Courses)
    elif inpud == 4:
        all_income(Courses)
    elif inpud == 5:
        up_price(Courses)
    elif inpud == 6:
        min_time = int(input("введите минимальное время для курса:"))
        print_up_time(Courses, min_time)
    elif inpud == 7:
        del_cour_under_4(Courses)
    elif inpud == 8:
        inpud_8 = int(input("введите с помошью чего вы хотите найти курсы (1 - по платформе, 2- по уровню сложности):"))
        if inpud_8 == 1:
            platform = input("введите платформу:")
            search_platform(Courses, platform)
        else:
            lvl = int(input("введите уровень сложности (1 - легко, 2 - средне, 3 - продвинутый):"))
            search_lvl_hard(Courses, lvl)
    elif inpud == 9:
        platform = input("ведите название платформы:")
        egit_all_platform(Courses, platform)
    else:
        GAME_RUN = False
        return GAME_RUN
    

while GAME_RUN:
    menu()