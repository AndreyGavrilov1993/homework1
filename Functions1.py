#1
# def show_list():
#     print('''
#     "Don't compare yourself wiith anyone in this world...
#     if you do so, you are insulting youlting yourself."
#     Bill Gates''')
#
# print(show_list())

#2
# def show_line(a,b):
#     return [i for i in range(a,b+1) if i%2==0]
#
# print(show_line(1,20))

#3
def show_rectangle(size,symbol,log):

  if log==False:
      for i in range(size):
          for j in range(size):
              if i==0 or j==0 or i==size-1 or j==size-1:
                  print(symbol, end=" ")
              else:
                  print(" ", end=" ")
          print(" ")
  elif log==True:
        for i in range(size):
          for j in range(size):
                  print(symbol, end=" ")
          print()

print(show_rectangle(4,"*",True))