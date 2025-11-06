$title = "----Number Summation----"
$scriptBy = "Luis Morales"

$Response=0;
do {
    "==============================="
    $title
    "This application will sum"
    "numbers divisible by 9 or"
    "numbers divisible by 13"
    "between 1 and 1000. "
    "Script Written By $scriptBy"
    "===============================`n"

    Write-Host "Select Option"
    Write-Host "1. Sum of numbers divisible by 9"
    Write-Host "2. Sum of numbers divisible by 13"
    Write-Host "0. Exit"
    $Response = Read-Host "Enter your selection here"
    
    switch($Response)
    {
      1 {
         $sum1 = 0
         for ($i = 1; $i -le 1000; $i++) 
              {
               if ($i % 9 -eq 0) 
               {
                $sum1 += $i
               }
              }

         Write-Host "`nSum of numbers divisible by 9 between 1 and 1000 = $sum1`n";
         }
      2 {
          $sum2 = 0
          for ($i = 1; $i -le 1000; $i++) 
              {
               if ($i % 13 -eq 0) 
                  {
                   $sum2 += $i
                  }
              }
         Write-Host "`nSum of numbers divisible by 13 between 1 and 1000 = $sum2`n";
        }
      0 {"`nThank You! Bye!";exit;}
      default {"`n---=== Please enter a valid option!===---`n`n";}
        }
   }
   while ($true)