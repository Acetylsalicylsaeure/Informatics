# ask for suitcase weigth
weight = float(input("please enter your suitcase weight: "))

# evaluate weight
if weight > 23:
    # calculate cost
    cost = float((weight-23)*4)
    # print message and insert cost via modulo
    print("sorry, you need to pay %.2f €" % cost)
else:
    print("thank you for flying with us")
