'''
Luis Morales
CSCI 3309
April 27,2023
'''
import datetime;

'''==================================== List Code ===================================='''
# Open file stream
fo = open("dailyWages.dat","r")
'''===================================================================================='''


'''===================================== Variables ========================================'''

''' Skill Levels '''
U =  8.15
M = 12.55
S = 18.60
# print('U =',U,' M =',M,' S =',S)
# Any worker(U/M/S) receives 1.5 times the rate per hour for hours worked over 8 per day.
# However, by regulation any worker cannot work more than 12 hours per day.
''' ============= '''
now = datetime.datetime.now()
rate = 0.00
wage = 0.00
totHours = 0.00
totPay = 0.00

while True:

    '''======================================= Menu ======================================'''
    print("=============================")
    print("   Daily Wage Calculator")
    print("   By: Luis Morales")
    print("-----------------------------")
    print("1. Display by Employee Number")
    print("2. Display All")
    option = int(input("Enter Option. 0 to Exit:"))
    '''=============='''
    '''==================================================================================='''

    if (option == 1):
        '''================================= Single Employee ================================='''
        fo = open("dailyWages.dat", "r")
        searchEmp = str(input("Enter Employee Number:"))
        count = 0
        found = False

        # Code for printing individual employee
        while True:
            count += 1
            line = fo.readline()
            if not line:
                break
            splittedLine = line.split ("|")
            if (splittedLine[0] == searchEmp):
                found = True
                if (splittedLine[2] == "U" ):
                    rate = float(U)
                elif (splittedLine[2] == "M"):
                    rate = float(M)
                elif (splittedLine[2] == "S"):
                    rate = float(S)
                if (float(splittedLine[3]) < float(8)):
                    wage = float(splittedLine[3]) * float(rate)
                if (float(splittedLine[3]) == float(8)):
                    wage = float(splittedLine[3]) * float(rate)
                if (float(splittedLine[3]) > float(8)):
                    wage1 = 8.00 * float(rate)
                    overT = float(splittedLine[3]) - 8  # Overtime worked
                    overP = float(rate * 1.5)           # Overtime pay
                    overW = overT * overP               # Overtime Wage
                    wage = (wage1 + overW)
                print('===================== Employee Daily Wage Record ======================')
                print('{0:15} {1:17} {2:5} {3:8} {4:7} {5:15}'.format('Employee Number', 'Employee Name', 'Skill Level', 'Hrs Worked', 'Rate', 'Wage'))
                print('-----------------------------------------------------------------------')
                print("      ""{0:10} {1:21} {2:5} {3:8.2f} {4:7.2f} {5:8.2f}".format(splittedLine [0], splittedLine [1], splittedLine [2], float(splittedLine [3]), float(rate), float(wage)))#
                print('-----------------------------------------------------------------------')
            else:
                continue
        if (found == False):
             print("\n*** Employee Number not found. Try again.")

        fo.close()
        '''===================================================================================='''
    if (option == 2):
        '''================================== All Employees =================================='''
        fo = open("dailyWages.dat","r")
        count = 0
        print('========================  Daily Wage Record ==========================')
        print('         Report Generated on : ' + now.strftime("%Y-%m-%d @ %H:%M:%S"))
        print('{0:15} {1:17} {2:5} {3:8} {4:7} {5:15}'.format('Employee Number', 'Employee Name', 'Skill Level', 'Hrs Worked', 'Rate', 'Wage'))
        print('----------------------------------------------------------------------')
        # Code for printing all employees
        while True:
            count += 1
            line = fo.readline()
            if not line:
                break
            splittedLine = line.split ("|")

            if (splittedLine[2] == "U" ):
                rate = float(U)
            elif (splittedLine[2] == "M"):
                rate = float(M)
            elif (splittedLine[2] == "S"):
                rate = float(S)
            if (float(splittedLine[3]) < float(8)):
                wage = float(splittedLine[3]) * float(rate)
            if (float(splittedLine[3]) == float(8)):
                wage = float(splittedLine[3]) * float(rate)
            if (float(splittedLine[3]) > float(8)):
                wage1 = 8.00 * float(rate)
                overT = float(splittedLine[3]) - 8  # Overtime worked
                overP = float(rate * 1.5)           # Overtime pay
                overW = overT * overP               # Overtime Wage
                wage = (wage1 + overW)
            totHours += float(splittedLine[3])
            totPay += float(wage)
            print("      ""{0:10} {1:21} {2:5} {3:8.2f} {4:7.2f} {5:8.2f}".format(splittedLine [0], splittedLine [1], splittedLine [2], float(splittedLine [3]), float(rate), float(wage)))
        print('----------------------------------------------------------------------')
        print("{0:1} {1:46.2f}         ${2:1.2f}".format('Totals',totHours, totPay))
        fo.close()
        print('======================================================================')
        exit()
        '''===================================================================================='''
    if (option == 0):
        print("Good Bye!")
        exit()