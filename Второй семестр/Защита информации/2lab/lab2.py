A = ['111','111','111','111','111']
B = ['101','011','110','000','101']
C = ['001','100','001','101','110']
D = ['101','011','110','001','100']
E = ['011','110','000','001','011']
my = {"A": A, "B": B, "C": C, "D": D,"E": E}

boxes=[0,0,0,0,0]


def read(my):
    print("Выберите Пользователя")
    user=input()
    print("Выберите блок(1-5)")
    block=input()
    block=int(block)
    block=block-1
    if  my[user][block][0]=='1':
        print("Прочитано",boxes[block]+1)
    else:
        print("Ты не можешь!")


def write(my):
    print("Выберите Пользователя")
    user=input()
    print("Выберите блок(1-5)")
    block=input()
    block=int(block)
    block=block-1

    if my[user][block][1]=='1':
        print("Запишите:", end=" ")
        boxes[block]=input()
        print("Записано",boxes[block],"в",block+1,"ой контейнер")
    else:
        print("Ты не можешь!")


def grant(my):
    print("Выберите Пользователя")
    user=input()
    print("Выберите блок(1-5)")
    block=input()
    block=int(block)
    block=block-1

    if my[user][block][2]=='1':
        print("Какое право передаешь?")
        print("0:Читать / 1:Записать")
        what=input()
        what=int(what)
        print("Кому передаешь?")
        who=input()
        
        if what==0 and my[user][block][what]=='1':
            my[who][block] = "1" + my[who][block][1:]
            print("Все четко!")

        elif what==1 and my[user][block][what]=="1":
            my[who][block] = my[who][block][:1]+ "1" + my[who][block][2:]
            print("Все четко!")

        else:
             print("Ты не можешь!")

    else:
        print("Ты не можешь!")

p="999"
d="999"

while p!=0:
     print("Выберите действие\n1 Прочитать\n2 Записать\n3 Передать")
     p=input()
     if p=='1':
         print("----------------")
         read(my)
         print("----------------")
     elif p=='2':
         print("----------------")
         write(my)
         print("----------------")
     elif p=='3':
         print("----------------")
         grant(my)
         print("----------------")
