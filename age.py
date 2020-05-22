print("Привет! Введите ваш возраст: ")
age = int(input())
not_born = int(0)
child = int(7)
teenager = int(17)
human = int(27)
work_Human = int(60)


def main(not_born,age,child,teenager,human,work_Human):
    if age <= not_born:
        print (str('Что вы тут делаете? Вы еще не родились...'))
    elif age <= child:
        print(str('Пора в сад!'))
    elif age <= teenager:
        print(str('О, пора учиться!'))
    elif age <= human:
        print (str('Пора на пары!'))
    elif age <= work_Human:
        print (str('Пора на работу..'))
    else:
        print (str('Пора отдохнуть...'))

if __name__ == "__main__":
    main(not_born,age,child,teenager,human,work_Human)
