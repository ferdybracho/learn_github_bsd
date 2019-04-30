# x = 5;
# y = '5';
# z = 6;
# print(x==int(y) and int(y)<z);
# print(x==int(y) or int(y)<z);
# print(not(x==int(y) or int(y)<z));


# and 

# True and True -> true
# True and False -> False
# False and True -> False

# or

# True or True -> True
# True or False -> True
# False or True -> True
# False or False -> False


# x = int(input("Masukkan Angka : "));
# if (x%2==0):
#     print("Angka " + str(x) + " tergolong bilangan GENAP!");
# else:
#     print("Angka " + str(x) + " tergolong bilangan GANJIL!");



# # IMT = massa(kg) /  tinggi(meter)^2
# x = int(input("Masukan Berat Badan Anda"));
# y = int(input("masukan Tinggi Badan Anda"));
# z = y/100;
# Index = (x /(z**2));
# if (Index < 18.5):
#     print("Berat Badan Kurang Ideal")
# elif (Index >= 18.5 and Index <= 25):
#     print("Berat Badan Ideal")
# elif (Index > 25.0 and Index <= 30):
#     print("BB Berlebih")
# elif (Index > 30 and Index <= 39.9):
#     print ("BB Sangat berlebih")
# else:
#     print('Obesitas')

#MODUL_3

# angka = 1;
# while(angka <= 10):
#    print(angka);
#    angka += 2;

# listItem = list(range(1,11,2));
# print(listItem);

# for item in range(1,11,2):
# 	print(item);


# y = "nomor urut"
# for item in range(1,11,1):
#      print(y  +  str(item));

# y = 1;
# while(y <=10):
#     print ("nomor urut", (y));
#     y +=1;

#For Loop Drawing 
z='';
for item in range(0,10):
   z += ' * '
   print(z);

