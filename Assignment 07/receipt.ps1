$me="Luis Morales"
# Heading
$storeName = "       Affordable Daily Needs"
$storeAddress1 = "       4715 San Pedro Avenue"
$storeAddress2 = "        San Antonio TX 78217"
$storePhone = "        Phone: 210-128-1919"
$description = "This Program will prompt for 10 items.
Enter quantities of each item purchased"

# Prices
$lvBread = 1.95
$galMilk = 4.29
$bgChips = 4.89
$lbPotatoes = 1.69
$lbBananas = 0.69
$lbBeef = 6.39
$lbTomatoes = 1.29
$lbApples = 1.69
$aaBatteries = 3.99
$btlVitamin = 5.29
$taxRate = .0825

# Start of receipt
"==================================="
"$storeName"
"$description"
# Input Prompts
$qntBread = Read-Host "How many loaves of Bread (`$$lvBread each)   "
$qntMilk = Read-Host "How many Gallons of Milk (`$$galMilk each)   "
$qntChips = Read-Host "How many Bags of Chips (`$$bgChips each)     "
$qntPotatoes = Read-Host "How many pounds of Potatoes (`$$lbPotatoes each)"
$qntBananas = Read-Host "How many pounds of Bananas (`$$lbBananas each) "
$qntBeef = Read-Host "How many pounds of Beef (`$$lbBeef each)    "
$qntTomatoes = Read-Host "How many pounds of Tomatoes (`$$lbTomatoes each)"
$qntApples = Read-Host "How many pounds of Apples (`$$lbApples each)  "
$qntBatteries = Read-Host "How many 2-pack AA batteries(`$$aaBatteries each)"
$qntVitamins = Read-Host "How many Bottles of Vitamin(`$$btlVitamin each) "
# ------------- Calculations ------------
# $subBread = $lvBread * $qntBread
$subBread = [math]::Round(($lvBread * $qntBread),2)
$subMilk = [math]::Round(($galMilk * $qntMilk),2)
$subChips = [math]::Round(($bgChips * $qntChips),2)
$subPotatoes = [math]::Round(($lbPotatoes * $qntPotatoes),2)
$subBananas = [math]::Round(($lbBananas * $qntBananas),2)
$subBeef = [math]::Round(($lbBeef * $qntBeef),2)
$subTomatoes = [math]::Round(($lbTomatoes * $qntTomatoes),2)
$subApples = [math]::Round(($lbApples * $qntApples),2)
$subBatteries = [math]::Round(($aaBatteries * $qntBatteries),2)
$subVitamin = [math]::Round(($btlVitamin * $qntVitamins),2)
$subTotal = [math]::Round(($subBread + $subMilk + $subChips + $subPotatoes + $subBananas + $subBeef + $subTomatoes + $subApples + $subBatteries + $subVitamin),2)
$tax = [math]::Round((($subVitamin + $subBatteries) * $taxRate),2)
$total = [math]::Round(($subTotal + $tax),2)
# ---------------------------------------
"==================================="

#Formatted heading
"$storeName"
"$storeAddress1"
"$storeAddress2"
"$storePhone"
"-----------------------------------"
# Category Title
$("{0,-10} {1,4} {2,13} {3,5}" -f "Item","Qty","Price/Unit","Cost")
"-----------------------------------"

# Formatted columns
$("{0,-10} {1,4} {2,10} {3,8}" -f "Bread",$qntBread,"`$$lvBread","$subBread") 
$("{0,-10} {1,4} {2,10} {3,8}" -f "Milk",$qntMilk,"`$$galMilk","$subMilk") 
$("{0,-10} {1,4} {2,10} {3,8}" -f "Chips",$qntChips,"`$$bgChips","$subChips")
$("{0,-10} {1,4} {2,10} {3,8}" -f "Potatoes",$qntPotatoes,"`$$lbPotatoes","$subPotatoes") 
$("{0,-10} {1,4} {2,10} {3,8}" -f "Bananas",$qntBananas,"`$$lbBananas","$subBananas") 
$("{0,-10} {1,4} {2,10} {3,8}" -f "Beef",$qntBeef,"`$$lbBeef","$subBeef") 
$("{0,-10} {1,4} {2,10} {3,8}" -f "Tomatoes",$qntTomatoes,"`$$lbTomatoes","$subTomatoes") 
$("{0,-10} {1,4} {2,10} {3,8}" -f "Apples",$qntApples,"`$$lbApples","$subApples") 
$("{0,-10} {1,4} {2,10} {3,8}" -f "Batteries",$qntBatteries,"`$$aaBatteries","$subBatteries")
$("{0,-10} {1,4} {2,10} {3,8}" -f "Vitamins",$qntVitamins,"`$$btlVitamin","$subVitamin")  
"-----------------------------------"
$("{0,-10} {1,24:n2}" -f "Subtotal","`$$subTotal")
$("{0,-10} {1,23:n2}" -f "Tax @ 8.25%","`$$tax")
"-----------------------------------"
$("{0,-10} {1,24:n2}" -f "Total","`$$total")
"-----------------------------------"
"Sales Clerk: $me"
"Counter#: 10"
Write-Host "Date: " $(Get-Date)