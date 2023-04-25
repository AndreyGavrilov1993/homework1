list1=[1,2,3,4,5,6,7,8,9,7,5,3,8,4,1]

def sum_min(list, n, minimum=0, min_index=0, index=0, flag=True):
    summ=0
    if(flag):
        for i in range(n):
            summ+=list[i]
        index=0
        minimum=summ
    else:
        try:
            for i in range(index, n+index,):
                summ+=list[i]
        except:
            return min_index
        if(minimum>summ):
            minimum=summ
            min_index=index
    return (sum_min(list, n, minimum, min_index, index+1, False))
print(sum_min(list1,3))

# Задача о шахматном коне
def knightsTour(x0, y0, done, size=5):
    # создаем шахматную доску в виде 2го списка
    h = [[0 for j in range(size)] for i in range(size)]
    # начальная координата(1го хода)
    h[x0][y0] = 1

    # Возможные ходы
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    def CanBeDone(u, v, i):
        h[u][v] = i
        done = tryNextMove(u, v, i)
        if not done:
            h[u][v] = 0
        return done

    def tryNextMove(x, y, i):

        # eos - показывает все ли варианты возможных 8ми ходов мы рассмотрели
        # done - показывает удачна ли данная ветка решения
        # k - порядковый номер рассмотренной попытки из 8 допустимых
        env = {'done': False, 'eos': False, 'u': x, 'v': y, 'k': -1}

        def next():
            x = env['u']
            y = env['v']
            while env['k'] < 8:
                env['k'] += 1;
                if env['k'] < 8:
                    env['u'] = x + dx[env['k']]
                    env['v'] = y + dy[env['k']]
                if (env['u'] >= 0 and env['u'] < size) and (env['v'] >= 0 and env['v'] < size) and h[env['u']][
                    env['v']] == 0:
                    break
            env['eos'] = (env['k'] == 8)

        if i < size ** 2:  # если доска не заполнена
            next()
            while not env['eos'] and not CanBeDone(env['u'], env['v'], i + 1):
                next()
            done = not env['eos']
        else:
            done = True
        return done

    tryNextMove(x0, y0, 1)
    print(h)

knightsTour(0, 0, True)