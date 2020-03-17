import os
import datetime
print('Программа выключит Ваш ПК')
print('Для выключения по таймеру введите "1"\nДля выключению по времени введите "2"')
choise = int
while choise == 1 or 2:
    choise = int(input('Сделайте выбор: '))
    if choise == 2:
        now = datetime.datetime.now()
        print('Выключение в заданное время')
        a = int(input('Введите часы: '))
        b = int(input('Введите минуты: '))
        h = datetime.datetime.today().strftime("%H")
        m = datetime.datetime.today().strftime("%M")
        h1 = int(h) % 24
        m1 = int(m) % 59
        b1 = b % 60
        a1 = a % 24
        if b1 < m1:
            c = (((a1 - h1)-1) % 24) * 60 * 60
            d = ((b1 - m1) % 59) * 60
        else:
            c = ((a1 - h1) % 24) * 60 * 60
            d = ((b1 - m1) % 59) * 60
        sum = c+d
        print('Компьютер выключится через {} часов, {} минут'.format(int(c/60/60), int(d/60)))
        cmd = 'shutdown -s -t ' + str(sum)
        os.system(cmd)
        break
    elif choise == 1:
        print('Выключение по таймеру')
        h = int(input('Количество часов: '))
        m = int(input('Количество минут: '))
        c = h*60*60+m*60
        cmd = 'shutdown -s -t ' + str(c)
        os.system(cmd)
        break
input()


