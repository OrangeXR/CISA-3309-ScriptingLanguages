'''
Luis Morales
CSCI 3309
April 19,2023
'''
'''===================================== Constants ========================================'''
tax1 = .10;
tax2 = .12;
tax3 = .22;
tax4 = .24;
tax5 = .32;
tax6 = .35;
tax7 = .37;
'''========================================================================================'''
print('====================================================================================')
print('Personal Income Tax Calculator')
print('Developed By: Luis Morales')
print('====================================================================================')
print('Valid Filing Statuses (1 = Unmarried Filer, 2 = Married Filing Jointly, 3 = Head of Household)\n')
print('Personal Income Tax Calculator')
'''====================================== Inputs ======================================'''
status = int(input('Enter the Filing status: '))
income = float(input('Enter your taxable income: '))
'''=================================== Number Magic ==================================='''
''' Single Individual '''
if (status == 1):
    if (income <= 10276):
        incomeTax = (income * tax1)
    elif (income <= 41776):
        incomeTax = ((10276 * tax1) + ((income - 10276) * tax2))
    elif (income <= 89076):
        incomeTax = ((10276 * tax1) + ((41776 - 10276) * tax2) + ((income - 41776) * tax3))
    elif (income <= 170051):
        incomeTax = ((10276 * tax1) + ((41776 - 10276) * tax2) + ((89076 - 41776) * tax3) + ((income - 89076) * tax4))
    elif (income <= 215951):
        incomeTax = ((10276 * tax1) + ((41776 - 10276) * tax2) + ((89076 - 41776) * tax3) + ((170051 - 89076) * tax4) + ((income - 170051) * tax5))
    elif (income <= 539901):
        incomeTax = ((10276 * tax1) + ((41776 - 10276) * tax2) + ((89076 - 41776) * tax3) + ((170051 - 89076) * tax4) + ((215951 - 170051) * tax5) + ((income - 215951) * tax6))
    elif (income > 539901):
        incomeTax = ((10276 * tax1) + ((41776 - 10276) * tax2) + ((89076 - 41776) * tax3) + ((170051 - 89076) * tax4) + ((215951 - 170051) * tax5) + ((539901 - 215951) * tax6) + ((income - 539901) * tax7))
''' Married Individuals Filing Joint Returns '''
if (status == 2):
    if (income <= 20551):
        incomeTax = (income * tax1)
    elif (income <= 83551):
        incomeTax = ((20551 * tax1) + ((income - 20551) * tax2))
    elif (income <= 178151):
        incomeTax = ((20551 * tax1) + ((83551 - 20551) * tax2) + ((income - 83551) * tax3))
    elif (income <= 340101):
        incomeTax = ((20551 * tax1) + ((83551 - 20551) * tax2) + ((178151 - 83551) * tax3) + ((income - 178151) * tax4))
    elif (income <= 431901):
        incomeTax = ((20551 * tax1) + ((83551 - 20551) * tax2) + ((178151 - 83551) * tax3) + ((340101 - 178151) * tax4) + ((income - 340101) * tax5))
    elif (income <= 647851):
        incomeTax = ((20551 * tax1) + ((83551 - 20551) * tax2) + ((178151 - 83551) * tax3) + ((340101 - 178151) * tax4) + ((431901 - 340101) * tax5) + ((income - 431901) * tax6))
    elif (income > 647851):
        incomeTax = ((20551 * tax1) + ((83551 - 20551) * tax2) + ((178151 - 83551) * tax3) + ((340101 - 178151) * tax4) + ((431901 - 340101) * tax5) + ((647851 - 431901) * tax6) + ((income - 647851) * tax7))
''' Heads of Households '''
if (status == 3):
    if (income <= 14651):
        incomeTax = (income * tax1)
    elif (income <= 55901):
        incomeTax = ((14651 * tax1) + ((income - 14651) * tax2))
    elif (income <= 89051):
        incomeTax = ((14651 * tax1) + ((55901 - 14651) * tax2) + ((income - 539901) * tax3))
    elif (income <= 170051):
        incomeTax = ((14651 * tax1) + ((55901 - 14651) * tax2) + ((89051 - 55901) * tax3) + ((income - 89051) * tax4))
    elif (income <= 215951):
        incomeTax = ((14651 * tax1) + ((55901 - 14651) * tax2) + ((89051 - 55901) * tax3) + ((170051 - 89051) * tax4) + ((income - 170051) * tax5))
    elif (income <= 539901):
        incomeTax = ((14651 * tax1) + ((55901 - 14651) * tax2) + ((89051 - 55901) * tax3) + ((170051 - 89051) * tax4) + ((215951 - 170051) * tax5) + ((income - 215951) * tax6))
    elif (income > 539901):
        incomeTax = ((14651 * tax1) + ((55901 - 14651) * tax2) + ((89051 - 55901) * tax3) + ((170051 - 89051) * tax4) + ((215951 - 170051) * tax5) + ((539901 - 215951) * tax6) + ((income - 539901) * tax7))
if (status != 1 and status != 2 and status != 3):
    print("Input error in filing Status or income.  Processing stopped")
    exit()
'''===================================== Results ======================================'''
print("Your income tax for 2022 will be: $  %1.2f" % (float(incomeTax)))

