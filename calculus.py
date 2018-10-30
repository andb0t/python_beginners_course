import sys
import time


print('Counting the numbers of beers I can still buy!')
credit = int(sys.argv[1])


def get_amount(money, price):
    result = money / price
    return str(int(result))


print('Hm, that\'s a difficult calculation ...')
time.sleep(2)
print('I got it! I can buy:')
print(' - ' + get_amount(credit, 1.5) + ' beers!')
print(' - ' + get_amount(credit, 1.3) + ' spezis!')
print(' - ' + get_amount(credit, 1.7) + ' weissbiers!')
