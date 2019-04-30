##################### module_1 ############################

# # #solved_it_1
# nama = input("Nama kamu? : ");
# umur = input("Umur kamu? : ");
# kelamin = input("Kelamin kamu? : ");
# pekerjaan = input("Pekerjaan kamu? : ");

# print("Nama : " + nama);
# print("Umur : " + umur);
# print("Kelamin : " + kelamin);
# print("Pekerjaan : " + pekerjaan);

# # #solved_it_2
# import math
# x = 4;
# y = 3;
# z = 2;

# numerator = x+(y*z);
# denominator = x*y;
# w = (numerator/denominator)**2;

# print(w);

#solved_it_3
# number = int(input("Silahkan masukkan angka berapapun : "));
# print("Kuadrat dari " + str(number) + " adalah " + str(number**2));

# #solved_it_4
# import math

# awal_hari = 485;
# total_tahun = math.floor(awal_hari/360);
# sisa_hari = awal_hari - total_tahun * 360;
# total_bulan = math.floor(sisa_hari/30);
# sisa_hari -= total_bulan * 30;
# total_minggu = math.floor(sisa_hari/7);
# sisa_hari -= total_minggu * 7;
# print(str(awal_hari) + " hari sama dengan " 
#                      + str(total_tahun) + " tahun " 
#                      + str(total_bulan) + " bulan "
#                      + str(total_minggu) + " minggu " 
#                      + str(sisa_hari) + " hari.");

#solved_it_5

# """
#     jumlah_usia = 49
#     rasio_usia = 0.4
#     a + b = 49
#     a/b = 0.4
#     a = 0.4b
#     0.4b + b = 49
#     1.4b = 49
# """

# b = int(49/1.4);
# a = int(49 - b);
# print("Dua tahun lagi, usia Andi " + str(a+2) 
#                                    + " dan usia Budi " 
#                                    + str(b+2) 
#                                    + ".")

# # #solved_it_6
# x = "Halo Dunia";
# y = 'z';
# jumlah_char = len(x.split(y))-1;
# print("Jumlah karakter " + y 
#                          + " adalah " 
#                          + str(jumlah_char) 
#                          + " huruf.");