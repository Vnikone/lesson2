print('Привет! Пожалуйста, введи 2 строки:')
a = (input())
a = str(a)
b = (input())
b = str(b)
c = 'learn'
c = str(c)


def main(a,b,c):   
    if a == b:
        print(1)
    elif a != b and a > b:
        print(2)
    elif a != b and c == b:
        print (3) 
    elif (a,b) != (str()):
        print (0)
    


if __name__ == "__main__":
    main(a,b,c)
