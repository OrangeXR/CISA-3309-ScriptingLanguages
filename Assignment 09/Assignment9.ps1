$me = "Luis Morales"
$coName = "XYZ Auto Dealership"

# Fill the arrays from file
$file = Get-Content "C:\Users\luise\OneDrive\School\CISA 3309 - Scripting Languages\Assignments\posh\automobileInfo.dat"
$line = $null;
[String[]] $modelName = @();
[float[]] $price = @();
[int[]] $onHand = @();

             $line = $null;
             foreach ($line in $file)
                {
                 #Split fields into values
                 $line = $line -split (",")
                 $modelName += $line[0];
                 $price += $line[1];
                 $onHand += $line[2];
                }


# === Menu ===
do {
    # === Title === 
    Write-Host "`n---------------------------"
    Write-Host $coName
    Write-Host "By: $me"
    Write-Host "--------------------------"
    Write-Host "1. Search by Automobile"
    Write-Host "2. List All"
    # =============

    # === User Input ===
    $choice = Read-Host "Enter an option (0 to quit)"
    # ==================

    switch ($choice) {
        # === Option 1 ===
        "1" {
             $model = Read-Host "Enter Automobile Model"

            
             $result = [array]::indexof($modelName, $model);
             if ($result -gt -1)
              {
               Write-Host "`n---------------------------------------  "    
               Write-Host "Details for Auto Model:  $model"
               Write-Host "--------------------------------------- "
               Write-Host "Automobile Model   Price   Qty-In-Hand  " 
               Write-Host $("{0,0} {1,-14} {2,-12:n2} {3,2}" -f " ",$modelName[$result],$price[$result],$onHand[$result])
               
               For ($nextItem = 0 ; $nextItem -lt $modelName.length; $nextItem++)
                {
                 for ($modelName -eq $model)
                  {
                   break;
                  }
                }
             }
              else
               {
                "`nSorry, $model was not found.`n"
               }
            }
        # ================
        # === Option 2 ===
        "2" {
            Write-Host "`n---------------------------------------"       
            Write-Host $("{0,5} {1, 0}" -f  " ","Details for all Auto Models")
            Write-Host "---------------------------------------"
            Write-Host $("{0, 16} {1,7} {2,13}" -f "Automobile Model","Price","Qty-in-Hand")
            for ($nextItem =0 ; $nextItem -lt $modelName.length; $nextItem++)
                {
                 $val1n = $modelName[$nextItem]
                 $val2n = $price[$nextItem]
                 $val3n = $onhand[$nextItem]
     
                 Write-Host $("{0,0} {1,-14} {2,-12:n2} {3,2}" -f " ",$val1n,$val2n,$val3n)

                }
            Write-Host "---------------------------------------"
            }
        # ================
        # === Option 3 ===
        "0" {
            Write-Host "Thank You. Bye!"
            exit
            }
        # ================
        # === Option 4 ===
        default {
            Write-Host "Invalid choice. Please try again."
                }
        # =================
    }
} while ($true)

