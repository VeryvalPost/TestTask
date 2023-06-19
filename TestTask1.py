#   1.  Даны:
#   размер ипотечного кредита — 2 млн. руб,
#   процентная ставка — 10%,
#   кол-во лет— 5.
#   Найти переплату по кредиту


# Данное решение подразумевает выбор между аннуитентным платежом и дифференцированным платежом.
def overpayment(creditSize, rateYear, periodYear): 
    typeOfCredit = input("Выберите тип платежа: \n 1. Аннуитентный \n 2. Дифферинцированный\n")
    match typeOfCredit:
        case '1':
            rateMonth = rateYear / 12 / 100
            periodMonth = periodYear * 12
            paymentPerMonth = creditSize * (rateMonth * ((1+rateMonth)**periodMonth))/   (((1+rateMonth)**periodMonth)-1) # Формула аннуитентного платежа (приблизительная... Из Интернетов).
            payment = paymentPerMonth*12 * periodYear - creditSize 
        case '2':
            payment= rateYear/100 * creditSize * (periodYear + 1)/2     # Формула дифференцированного платежа (приблизительная... Из Википедии).
        case _: 
            print(" Введены некорректные данные ")                            
    return payment

creditSize = 2000000
rateYear = 10
periodYear = 5

print(" Переплата составит: ",round(overpayment(creditSize, rateYear, periodYear),2))