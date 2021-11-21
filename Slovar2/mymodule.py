def auth(x,y):
    #функция, которая проверяет наличие вашего имя пользователя на наличие в списках. Если такое есть, то дает возможность залогиниться.
    a=input("Введите имя пользователя:   ")
    if a in x:
        b=input("Введите пароль для данного имя пользователя:   ")
        if b in y and y.index(b)==x.index(a):
            print("Авторизация успешно завершена!")
        else:
            print("Неверный пароль!")
    else:
        print("Данного имя пользователя нет")
        pass
    return
def auto_registration(x,y):
    #функция позволяет создать имя пользователя, проверяет есть ли уже такое или нет. если нет, то создает пароль автомаатически. Заносит имя и пароль в списки.
    a=input("Придумайте имя пользователя:   ")
    if a not in x:
        print("Данное имя пользователя свободно!")
        x.append(a)
        print("Создаем пароль...")
        import random
        str0=".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
        str4 = str0+str1+str2+str3
        print(str4)
        ls = list(str4)
        print(ls)
        random.shuffle(ls)
        print(ls)
        # Извлекаем из списка 12 произвольных значений
        psword = ''.join([random.choice(ls) for x in range(12)])
        # Пароль готов
        print("Ваш пароль - ",psword)
        y.append(psword)
    else:
        print("Данное имя пользователя занято!")
    return
def manual_registration(x,y):
    a=input("Придумайте имя пользователя:   ")
    p=0
    o=0
    if a not in x:
        print("Данное имя пользователя свободно!")
        x.append(a)
        b=(input("Пароль должен содержать буквы верхнего,нижнего регистра и минимум одну цифру.\nПридумайте пароль:   "))
        z=b.lower()
        g=list(b)
        if b==z:
            print("Не хватает хотя бы одной заглавной буквы!")
        else:
            for t in g:
                if t.isdigit()==True:
                    p+=1
                    if p==0:
                        print("Пароль должен содержать цифры!")
                    else:
                        for t in g:
                            if t.isupper()==True:
                                o+=1
                                if o==0:
                                    print("В пароле нужна заглавная буква")
                                else:
                                    print("Отличный пароль!")
                                    x.append(a)
                                    y.append(b)
            print(x,y) #в конечном варианте даной строки не должно быть, она только для проверки
    else:
        print("Данное имя пользователя занято!")

    return