'''
Luis Morales
CSCI 3309
April 24,2023
'''
import random;
import statistics;
import datetime;

'''==================================== List Code ===================================='''
randomList = []
i = 0
while (i < 1000):
    nextRand = random.randint (1,100);
    randomList.append(nextRand);
    i = i+1
'''===================================================================================='''


'''===================================== Variables ========================================'''
items = len(randomList);
listSum = sum(randomList);
maxi = max(randomList);
mini = min(randomList);
mean = statistics.mean (randomList);
median = statistics.median (randomList);
'''========== Evens =========='''
evens = 0
for element in randomList:
    if element % 2 == 0:
        evens += 1
'''==========================='''
'''========== Odds ==========='''
odds = 0
for element in randomList:
    if element % 2 != 0:
        odds += 1
'''==========================='''
evenSum = sum(num for num in randomList if not num%2);
oddSum  = sum(num for num in randomList if num%2);
'''=============== Range 1 (1-25) ==============='''
lower_bound = 1
upper_bound = 25
range1 = 0
for element in randomList:
    if lower_bound <= element <= upper_bound:
        range1 += 1
'''=============== Range 2 (26-50) =============='''
lower_bound = 26
upper_bound = 50
range2 = 0
for element in randomList:
    if lower_bound <= element <= upper_bound:
        range2 += 1
'''=============== Range 3 (51-75) =============='''
lower_bound = 51
upper_bound = 75
range3 = 0
for element in randomList:
    if lower_bound <= element <= upper_bound:
        range3 += 1
'''=============== Range 4 (76-100) ============='''
lower_bound = 76
upper_bound = 100
range4 = 0
for element in randomList:
    if lower_bound <= element <= upper_bound:
        range4 += 1
'''========================================================================================'''
now = datetime.datetime.now()
"============ Piece of Mind =================="
# I wanted to print the list for verification
#print(randomList)
'''==========================================='''

'''===================================== Printout ====================================='''
print('-------------------------------------------------')
print('Statistics of Randomly generated 1000 Number List')
print('             Developer: Luis Morales')
print('         Prepared on: ' + now.strftime("%Y-%m-%d %H:%M:%S"))
print('-------------------------------------------------')
print('List has', items, 'elements')
print('Sum of all elements in list is:', listSum)
print('List has a Maximum value of', maxi)
print('List has a Minimum value of', mini)
print('Mean of', items, 'elements in the list is: ', mean)
print('Median of', items, 'elements in the list is: ', median)
print('List has', evens, 'even elements')
print('List has', odds, 'odd elements')
print('Sum of even numbers in the list:', evenSum)
print('Sum of odd numbers in the list:', oddSum)
print('List has', range1, 'elements between 1 and 25.')
print('List has', range2, 'elements between 26 and 50.')
print('List has', range3, 'elements between 51 and 75.')
print('List has', range4, 'elements between 76 and 100.')
print('-------------------------------------------------')
'''===================================================================================='''