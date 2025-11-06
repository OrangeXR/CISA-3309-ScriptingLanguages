#/bin/bash
me="Luis Morales"
co="Global Traders Inc"
reportType="Business Performance Report by Location/Business Area"
reportDate="Report Date: `Date`"
file="business_performance.dat"
# Predetermined forcasted values
forMar=3000000.00 # forcasted Marketing
forAdv=2500000.00 # forcasted Advertising
forPro=400000.00  # forcasted Production
forITe=200000.00  # forcasted I Tech
forTot=7500000.00 # forcasted Total Revenue

# Heading
printf "%50s\n" "$co"
printf "%s\n\n" "                $reportType"
printf "%s\n" "                   $reportDate"
printf "%54s\n\n" "Prepared By: $me"
printf "%-20s  %-10s  %-10s  %-10s  %-10s  %-10s\n" "Location" "Marketing" "Advertising" "Production" "I. Tech" "Total Revenue"            # Column formatting/heading
printf "....................................................................................\n"                                            # print dotted line
 while IFS=, read -r "Location" "Marketing" "Advertising" "Production" "ITech";                                                            # Variable Spacing/formatting/naming
 do
 declare TotalRevenue=$(($Marketing+$Advertising+$Production+$ITech))                                                                      # Total Revenue calculation
  printf "%-20s  %10.2f  %10.2f  %10.2f  %10.2f  %10.2f\n" "$Location" "$Marketing" "$Advertising" "$Production" "$ITech" "$TotalRevenue"  # formatting and variable calls
  declare totMar=$(($totMar+$Marketing))     # location total for Marketing
  declare totAdv=$(($totAdv+$Advertising))   # location total for Advertising
  declare totPro=$(($totPro+$Production))    # location total for Production
  declare totITe=$(($totITe+$ITech))         # location total for I Tech
  declare totTot=$(($totTot+$TotalRevenue))  # location total for TotalRevenue
 done <"$file"

printf "....................................................................................\n"                                            # print dotted line
printf "%-20s  %10.2f  %10.2f  %10.2f  %10.2f  %10.2f\n" "Totals" "$totMar" "$totAdv" "$totPro" "$totITe" "$totTot"                        # formatting and variable calls
printf "....................................................................................\n"                                            # print dotted line
printf "%-20s  %10.2f  %10.2f  %10.2f  %10.2f  %10.2f\n" "Forcasted" "$forMar" "$forAdv" "$forPro" "$forITe" "$forTot"                     # formatting and variable calls
printf "....................................................................................\n"                                            # print dotted line
 declare plMar=`echo $totMar - $forMar | bc`   # Profit/Loss calculation for Marketing
 declare plAdv=`echo $totAdv - $forAdv | bc`   # Profit/Loss calculation for Advertising
 declare plPro=`echo $totPro - $forPro | bc`   # Profit/Loss calculation for Production
 declare plITe=`echo $totITe - $forITe | bc`   # Profit/Loss calculation for I Tech
 declare plTot=`echo $totTot - $forTot | bc`   # Profit/Loss calculation for Total Revenue
printf "%-20s  %10.2f  %10.2f  %10.2f  %10.2f  %10.2f\n" "Profit/Loss(-)" "$plMar" "$plAdv" "$plPro" "$plITe" "$plTot"                      # formatting and variable calls