from mymodule import *
login_list=["vlad","vlad2"]
password_list=["Parol1!","Parol2!"]
while True:
    a=int(input("1 - авторизаиця\n2 - регистрация\n3 - закончить работу\nВыберите действие:   "))
    if a==1:
        auth(login_list,password_list)
    elif a==2:
        a=int(input("Выберите действие:   \n1 - автоматическое созднаие пароля\n2 - создать пароль самостоятельно"))
        if a==1:
            auto_registration(login_list,password_list)
            print(login_list,password_list) #проверка, в конечном варианте данной строки не должно быть
        elif a==2:
            manual_registration(login_list,password_list)
    elif a==3:
        break