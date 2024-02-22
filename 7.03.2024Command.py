## Задание 1 Паттерн Command
import logging
from abc import ABC, abstractmethod
from typing import List, Deque

class ICommand(ABC):
    @abstractmethod
    def positive(self):
        pass
    @abstractmethod
    def negative(self):
        pass

class Conveyor:
    def on(self):
        print('Конвеер запущен')

    def off(self):
        print('Конвеер остановлен')

    def speed_increase(self):
        print('Увеличена скорость конвеера')

    def speed_decrease(self):
        print('Снижена скорость конвеера')

class ConveyorWorkCommand(ICommand):
    def __init__(self, conveyor: Conveyor):
        self.conveyor: Conveyor = conveyor

    def positive(self):
        self.conveyor.on()

    def negative(self):
        self.conveyor.off()

class ConveyorAdjustCommand(ICommand):
    def __init__(self, conveyor: Conveyor):
        self.conveyor: Conveyor = conveyor

    def positive(self):
        self.conveyor.speed_increase()

    def negative(self):
        self.conveyor.speed_decrease()

class Multipult:
    def __init__(self):
        self.__commands: List[ICommand] = [None, None]
        self.__history: Deque[ICommand] = []

    def set_command(self, button: int, command: ICommand):
        self.__commands[button] = command

    def press_on(self, button: int):
        self.__commands[button].positive()
        self.__history.append(self.__commands[button])

    def press_cancel(self):
        self.__history.pop().negative()

if __name__ == '__main__':
    conveyor = Conveyor()

    multipult = Multipult()
    multipult.set_command(0, ConveyorWorkCommand(conveyor))
    multipult.set_command(1, ConveyorAdjustCommand(conveyor))

    multipult.press_on(0)
    multipult.press_on(1)
    multipult.press_cancel()
    multipult.press_cancel()

### Задание 2
# Есть класс, предоставляющий доступ к набору чисел.
# Источником этого набора чисел является некоторый
# файл. С определенной периодичностью данные в файле
# меняются (надо реализовать механизм обновления).
# Приложение должно получать доступ к этим данным и
# выполнять набор операций над ними (сумма, максимум,
# минимум и т.д.). При каждой попытке доступа к этому
# набору необходимо вносить запись в лог-файл. При реализации используйте паттерн Proxy (для логгирования)
# и другие необходимые паттерны.

import _random
import logging

class NumList:
    def __init__(self):
        pass
class Change:
    def __init__(self, change: str):
        self.change: str = change

with open("NumList.txt", "r", encoding = "utf-8") as f:
    file = open('NumList.txt', 'a')
    file.write('9 8 7 6 5 4 3 2 11')
    file.readlines()
    file.close()

    smallest_number = min("NumList.txt")
    print("The smallest number is: ", smallest_number)
    largest_number = max("NumList.txt")
    print("The largest number is: ", largest_number)
    summ_number = sum("NumList.txt")
    print("The summ number is: ", summ_number)

# запись в лог-файл
logging.basicConfig(filename = "py_log.log",
                    filemode = 'a',
                    format = '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt = '%H:%M:%S',
                    level = logging.DEBUG)
logging.debug("A DEBUG Message")
logging.info("An INFO")
logging.warning("A WARNING")
logging.error("An ERROR")
logging.critical("A message of CRITICAL severity")

logging.info("Running Urban Planning")
logger = logging.getLogger("urbanGUI")

# Поведение может зависеть от платформы, но можно просто периодически пытаться дальше файл прочитать после EOF (или в худшем случае запоминать последнюю позицию и вызывать file.seek(last_position) на переоткрытом файле), предполагая что в файл новые строки добавляются только в конце (как в лог-файле)—нет других изменений. Например, чтобы показывать в GUI последнюю строчку в файле, которая соответствует заданному регулярному выражению (аналог tail -f file | grep -Pe regex):
#
# #!/usr/bin/env python3
# """Usage: grep-tail <regex> <file>"""
# import collections
# import functools
# import re
# import sys
# import tkinter.messagebox
#
# def filter_lastline(file, predicate):
#     """Find the last line in *file* that satisfies *predicate*."""
#     lines = collections.deque(filter(predicate, file), maxlen=1)
#     try:
#         return lines.pop().rstrip('\n')
#     except IndexError:
#         return ''  # not found
#
# def update_label(root, label, last_line):
#     current = label['text']
#     new = last_line()
#     if new and current != new:
#         label['text'] = new  # update label
#     root.after(1000, update_label, root, label, last_line)  # poll in a second
#
# def main():
#     root = tkinter.Tk()
#     root.withdraw()  # hide the main window
#     try:  # handle command-line arguments
#         regex_string, path = sys.argv[1:]
#         found = re.compile(regex_string).search
#         file = open(path)
#     except Exception as e:
#         tkinter.messagebox.showerror('wrong command-line arguments',
#                                      'error: %s\n%s' % (e, __doc__),
#                                      parent=root)
#         sys.exit(__doc__)
#
#     last_line = functools.partial(filter_lastline, file, found)
#     label = tkinter.Label(root, text=last_line()
#                           or '<nothing matched %r>' % regex_string)
#     label.pack()
#
#     update_label(root, label, last_line)  # start polling
#
#     # center window
#     root.eval('tk::PlaceWindow %s center' %
#               root.winfo_pathname(root.winfo_id()))
#     root.mainloop()
#
# main()
# Пример:
#
# $ ./grep-tail 'python[23]' /var/log/syslog
# Комментарии к реализации
# файл является итератором над строками в Питоне, поэтому filter(predicate, file) генерирует строки в файле, которые удовлетворяют predicate(line) критерию (регулярному выражению в данном случае).
#
# deque(it, maxlen=1) поглощает итератор, оставляя самое большее только последний элемент.
#
# При повторном вызове filter_lastline(file, predicate), file читается с последней позиции (EOF—с предыдущего конца файла). Можно ли не переоткрывая файл прочитать новые строки таким способом, может зависеть от платформы
#
# root.after(1000, f, *args) вызывает f(*args) через секунду, поэтому:
#
# def f(*args):
#     # do something
#     # continue loop
#     root.after(1000, f, *args)
# создаёт цикл, не блокируя GUI. Нельзя написать:
#
# def loop():
#     while True:
#         f(*args)
#         time.sleep(1)
# так как loop() заблокирует GUI и придётся вызов в отдельный поток/процесс помещать. root.after() позволяет f(*args) в GUI потоке вызывать и модифицировать label без проблем.
#!/usr/bin/env python3

import collections
import functools
import re
import sys
import tkinter.messagebox

def filter_lastline(file, predicate):
    """Find the last line in *file* that satisfies *predicate*."""
    lines = collections.deque(filter(predicate, file), maxlen=1)
    try:
        return lines.pop().rstrip('\n')
    except IndexError:
        return ''  # not found

def update_label(root, label, last_line):
    current = label['text']
    new = last_line()
    if new and current != new:
        label['text'] = new  # update label
    root.after(1000, update_label, root, label, last_line)  # poll in a second

def main():
    root = tkinter.Tk()
    root.withdraw()  # hide the main window
    try:  # handle command-line arguments
        regex_string, path = sys.argv[1:]
        found = re.compile(regex_string).search
        file = open(path)
    except Exception as e:
        tkinter.messagebox.showerror('wrong command-line arguments',
                                     'error: %s\n%s' % (e, __doc__),
                                     parent=root)
        sys.exit(__doc__)

    last_line = functools.partial(filter_lastline, file, found)
    label = tkinter.Label(root, text=last_line()
                          or '<nothing matched %r>' % regex_string)
    label.pack()

    update_label(root, label, last_line)  # start polling

    # center window
    root.eval('tk::PlaceWindow %s center' %
              root.winfo_pathname(root.winfo_id()))
    root.mainloop()

main()

### Если файл редко изменяется, то для эффективности можно watchdog модуль использовать, чтобы вызывать update_label() только когда файл действительно поменялся (в on_modified() обратном вызове). В данном случае (обновления через 5-15 секунд), использование watchdog было бы излишнем уcложнением (сторонняя зависимость + интеграция с циклом событий):
# В отличии от предыдущей версии, update_label() вызывается только, если входной файл был изменён: нет root.after() вызова. Предполагается, что полные строки пишутся—разумно для лог-файлов и строк меньших размера буфера, иначе следует update_label() подредактировать, чтобы накапливать данные при каждом вызове пока новая строка не встретится.



import collections
import functools
import os
import re
import sys
import tkinter.messagebox

from watchdog.observers import Observer # $ pip install watchdog
from watchdog.events import FileSystemEventHandler

def filter_lastline(file, predicate):
    """Find the last line in *file* that satisfies *predicate*."""
    lines = collections.deque(filter(predicate, file), maxlen=1)
    try:
        return lines.pop().rstrip('\n')
    except IndexError:
        return ''  # not found

def update_label(root, label, last_line):
    current = label['text']
    new = last_line()
    if new and current != new:
        label['text'] = new  # update label

def main():
    root = tkinter.Tk()
    root.withdraw()  # hide the main window
    try:  # handle command-line arguments
        regex_string, path = sys.argv[1:]
        found = re.compile(regex_string).search
        file = open(path)
    except Exception as e:
        tkinter.messagebox.showerror('wrong command-line arguments',
                                     'error: %s\n%s' % (e, __doc__),
                                     parent=root)
        sys.exit(__doc__)

    last_line = functools.partial(filter_lastline, file, found)
    label = tkinter.Label(root, text=last_line()
                          or '<nothing matched %r>' % regex_string)
    label.pack()

    class EventHandler(FileSystemEventHandler):
        def on_modified(self, event):
            if event.src_path == path:
                update_label(root, label, last_line)

    observer = Observer()
    observer.schedule(EventHandler(), os.path.dirname(path))
    observer.start()

    # center window
    root.eval('tk::PlaceWindow %s center' %
              root.winfo_pathname(root.winfo_id()))
    root.mainloop()
    observer.stop()
    observer.join()

main()