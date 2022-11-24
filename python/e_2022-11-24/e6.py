import time


payments = dict()

while 1 == 1:
    pay = input("please input a payment (€), \"p\" to print or \"q\" to quit: ")
    if pay == "p":
        print(tuple(payments))
    elif pay == "q":
        quit()
    else:
        date = time.time()
        payments[pay] = [date]
