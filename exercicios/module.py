import sys



for i in range(len(sys.argv)):
    if i == 0:
        print(f'Função: {sys.argv[0]}')
    else:
        print(f'{i}. argumento: {sys.argv[i]}')

