
# Напишите программу, удаляющую из текста все слова, содержащие "абв".





list = input('Введите текст :').split(' ')

for i in range (len(list)-1,-1, -1):
    if 'абв' in list[i]:
        print(list[i])
        list.remove(list[i])

print(list)