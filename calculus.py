import sys


print('Counting the numbers of beers I can still buy!')
credit = int(sys.argv[1])

print('I can buy:')
print(' - ' + str(int(credit / 1.5)) + ' beers!')
