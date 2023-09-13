with open('excelformula.txt', 'w') as f:
   for i in range(33):
      f.write('IF(DAY(B48)=\'Major Monthly Bills\'!$D$'+str(i+4)+',\'Major Monthly Bills\'!$C$'+str(i+4)+',0)+')