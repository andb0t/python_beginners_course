import sys


print('Counting the numbers of beers I can still buy!')
credit = int(sys.argv[1])

print('I can buy:')
print(' - ' + str(int(credit / 1.5)) + ' beers!')
print(' - ' + str(int(credit / 1.3)) + ' spezis!')
print(' - ' + str(int(credit / 1.7)) + ' weissbiers!')
