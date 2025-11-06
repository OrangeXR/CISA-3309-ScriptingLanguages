# Luis Morales
# CISA 3309
# April 6, 2023

#'''
# Question 4
import time;


# Prices
brePri = 2.19
milPri = 4.09
chiPri = 4.39
potPri = 1.49
banPri = 0.58
beePri = 5.39
tomPri = 1.09
appPri = 1.49
batPri = 3.89
vitPri = 5.39

print("          Affordable Daily Needs")
print("This program will prompt for 10 items.")
breQty = float(input("How many loaves of Bread ($2.19 each): "))
milQty = float(input("How many gallons of Milk ($4.09 each): "))
chiQty = float(input("How many bags of Chips ($4.39 each): "))
potQty = float(input("How many pounds of Potatoes ($1.49/lb): "))
banQty = float(input("How many pounds of Bananas ($0.58/lb): "))
beeQty = float(input("How many pounds of Beef ($4.25/lb): "))
tomQty = float(input("How many pounds of Tomatoes ($1.09/lb): "))
appQty = float(input("How many pounds of Apples ($1.49/lb): "))
batQty = float(input("How many 2-packs AA batteries ($3.89 each): "))
vitQty = float(input("How many Vitamin bottles ($5.39 each): "))
# Math
breCos = breQty * brePri
milCos = milQty * milPri
chiCos = chiQty * chiPri
potCos = potQty * potPri
banCos = banQty * banPri
beeCos = beeQty * beePri
tomCos = tomQty * tomPri
appCos = appQty * appPri
batCos = batQty * batPri
vitCos = vitQty * vitPri

# More Math
subTotal = float(breCos) + float(milCos) + float(chiCos) + float(potCos) + float(banCos) + float(beeCos) + float(tomCos) + float(appCos) + float(batCos) + float(vitCos)
taxable = float(batCos) + float(vitCos)
tax = float(taxable) * .0825
total = float(subTotal) + float(tax)

# Receipt
print("===================================")
print("  Affordable Daily Needs")
print("   2300 N. Loop 1604 E")
print("   San Antonio TX 78258")
print("-----------------------------------")
print("Item        Qty  price/unit  cost")
print("-----------------------------------")
print("Bread     %5.1f    %3.2f    %6.2f" % (float(breQty),float(brePri),float(breCos)))
print("Milk      %5.1f    %3.2f    %6.2f" % (float(milQty),float(milPri),float(milCos)))
print("Chips     %5.1f    %3.2f    %6.2f" % (float(chiQty),float(chiPri),float(chiCos)))
print("Potatoes  %5.1f    %3.2f    %6.2f" % (float(potQty),float(potPri),float(potCos)))
print("Bananas   %5.1f    %3.2f    %6.2f" % (float(banQty),float(banPri),float(banCos)))
print("Beef      %5.1f    %3.2f    %6.2f" % (float(beeQty),float(beePri),float(beeCos)))
print("Tomatoes  %5.1f    %3.2f    %6.2f" % (float(tomQty),float(tomPri),float(tomCos)))
print("Apples    %5.1f    %3.2f    %6.2f" % (float(appQty),float(appPri),float(appCos)))
print("Batteries %5.1f    %3.2f    %6.2f" % (float(batQty),float(batPri),float(batCos)))
print("Vitamins  %5.1f    %3.2f    %6.2f" % (float(vitQty),float(vitPri),float(vitCos)))
print("...................................")
print("Sub Total %23.2f" % (float(subTotal))) # Sub Total
taxChar = "Tax @8.25%"
print("Tax @ 8.25%% %21.2f" % (float(tax))) # Tax
print("-----------------------------------")
print("TOTAL %27.2f" % (float(total)))
print("===================================")
print("Sales Clerk: Luis Morales")
print("Date:%s" % (time.strftime('%m/%d/%Y %H:%M:%S')))
#'''