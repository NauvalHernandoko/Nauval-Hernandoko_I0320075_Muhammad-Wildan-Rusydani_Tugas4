print("=============Program seleksi kursus online============")
masukkan_usia = int(input("Berapa usia kamu:"))
print(masukkan_usia >= 21)
ujian= input("Apakah Anda sudah lulus ujian kualifikasi(Ya/Tidak?):")
if masukkan_usia >= 21 and ujian == "ya":
    print('Anda dapat mendaftar kursus')
else:
    print('Anda tidak dapat mendaftar kursus')




