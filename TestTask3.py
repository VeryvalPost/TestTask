#Напишите функцию, которая в зависимости от переданного в нее целочисленного аргумента, будет выводить слово «товар» в нужной форме («12 товаров», но «22 товара»).

# 1- товар
# 2-3-4- товара
# 5-20 - товаров
# 21 - товар
# 22-23-24 - товара
# 2.....


def endings ():
    number = input("Вводите число: ")
    char = list(number)
    
    if int(number) < 0:
        print("некорректный ввод")
    elif  0<=int(number)<10:
        print(number,lastChar(char[-1]))      
    else:
        print(number,lastChar(char[-1], char[-2]))
          
# В зависимости от двух последних символов любого числа будет получено нужное окончание. Соблюдена проверка на 11, 12, 13, 14   
def lastChar(charLast,charPrev = '0'):
    if charLast=='1' and charPrev != '1':
        return " - товар"
    if (charLast=='2' or charLast=='3' or charLast=='4') and charPrev != '1' :
        return " - товара"
    else:
        return " - товаров"   
  
    
endings()