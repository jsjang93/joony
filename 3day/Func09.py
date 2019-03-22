# Func09.py


CountLogin = 0
Log_list = []
def Login(name) :
    global CountLogin, Log_list
    CountLogin = CountLogin + 1
    Log_list += [name]
    print(name+"이 로그인")



def Logout(name):
    global CountLogin
    if name in Log_list:
        CountLogin = CountLogin - 1
        print(name + "이 로그아웃")
    else:
        print("잘못된 호출")



def Log_output():
    global Log_list
    print(Log_list)


Login('Jane')
print(CountLogin)
Log_output()
Login('Tom')
print(CountLogin)
Log_output()
Login('Alice')
print(CountLogin)
Log_output()
Logout('Tom')
print(CountLogin)
Log_output()
Logout('Timmy')


















