import time

run = True
run_time = False
run_pd = False
run_sec = False

name = input('Введите пользователя --> ')


def userName():
    global name
    name = input('Введите пользователя --> ')


def inputUser():
    realtime = time.strftime('%H:%M:%S', time.localtime())
    return input(f'{realtime} {name} ~ $ ')


def helpMes():
    print('exit - выход\nhelp - выведет это сообщение еще раз\ntime - часы\npd - таймер для работы\nsec - секундамер\n'
          'user - сменить пользователя')


print('help - помощь по командам')
while run:

    action = inputUser()
    # if action == '':
    #     action = inputUser()
    #     continue
    if action == 'exit':
        exit()
    elif action == 'help':
        helpMes()
    elif action == 'user':
        userName()
    elif action == 'time':
        run_time = True
    elif action == 'pd':
        run_pd = True
    elif action == 'sec':
        run_sec = True

    while run_pd:
        pass
    while run_time:
        pass
    while run_sec:
        pass
