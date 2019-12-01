
# kantor

answer= input("Hello people!\nDo you want buy some dollars? (Y/N): ")

while answer not in ['Y', 'y','N', 'n'] :
      answer= input("Please use Y or N\nDo you want buy some dollars? (Y/N): ")

if answer in ['N', 'n'] :
  print ('Thanks!!!')          
if answer in ['Y', 'y'] :
   sumUAH= float(input("Please input the sum (in UAH): "))
   courseUS = float(input("Please input course USD/UAH: "))
   cash = sumUAH//courseUS
   rest = round(sumUAH%courseUS,2)
   print('Your money: '+str(cash)+' USD')
   print('Your rest: '+str(rest)+' UAH')
   
print ('Bye!!!')


 