def first():
    print('Я главная функция')

    def second():
        print('Я вложенная функция')

    second()

first()