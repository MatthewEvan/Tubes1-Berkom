# Tugas Besar 1 - WI1102 Berpikir Komputasional
# Kelas K34 - Kelompok 3

# 19625098 - Matthew Evan Kurniawan
# 19625190 - Muhammad Fakhriyan Rizki M
# 19625210 - Dhean Zhafirkalis Mudtiza
# 19625214 - Muhammad Rafi Insyan Syiham A
# 19625218 - Ni Ketut Kayika Silayukti Sadu

# Program Sistem AutoGate untuk Lahan Parkir bagi Mahasiswa ITB

# KAMUS - BAGIAN PENGENDARA MASUK KE TEMPAT PARKIR
# checker = boolean - mengecek input dari user, ketika "STOP", maka program akan berhenti menerima input Masuk/Keluar
# jumlah_parkir_mobil = jumlah tempat parkir yang tersedia untuk mobil
# jumlah_parkir_motor = jumlah tempat parkir yang tersedia untuk motor
# entranceAutoGate = menerima input dari pengendara untuk masuk atau keluar dari tempat parkir
# jenisKendaraan = untuk menentukan pengaturan mesin terhadap jenis kendaraan pengendara
# platNomor = menerima input dari pengendara berupa plat nomor kendarannya sebagai identitas per kendaraan dalam Array
# jamMasukParkir = menerima input berupa jam saat ini untuk mengetahui kapan pengendara masuk ke tempat parkir
# menitMasukParkir = menerima input berupa menit saat ini untuk mengetahui kapan pengendara masuk ke tempat parkir
# jenisPembayaran = menerima input dari user berupa jenis pembayaran mereka nanti, baik menggunakan karcis parkir, atau kartu uang elektronik (E-Money)
# listKarcisParkir = sebuah array berisikan karcis yang akan dikeluarkan oleh mesin pada pengendara yang memilih tombol Karcis
# kartuEMoney = menerima input berupa kode unik dari kartu E-Money pengendara, sebagai proses tapping kartu pada mesin
# saldoEMoney = menerima input dari pengendara tentang saldo E-Money mereka, untuk merepresentasikan proses tap kartu pada mesin biasanya
# dataSatuan = array yang berisi "satu" identitas untuk pengendara, kendaraan, dan cara pembayarannya
# dataPengendara = gabungan dari beberapa array dataSatuan sebagai pembanding untuk proses pembayaran biaya parkir
# i = variable counter untuk list jenis atau kode karcis parkir yang didapatkan oleh pengendara
# j = variable counter untuk mememasukkan identitas kendaraan ke dalam array yang dituju
# n = integer untuk menjumlahkan 

# KAMUS - BAGIAN PENGENDARA KELUAR DARI TEMPAT PARKIR
# k = counter yang akan di while loop untuk menemukan identitas kendaraan pengendara dalam dataPengendara
# sisaSaldoEMoney = sisa saldo yang dimiliki oleh E-Money pengendara untuk diberikan informasinya kepada pengendara
# totalBiayaParkir = berisi total biaya yang akan dikenakan pada pengendara berdasarkan jenis kendaraannya
# identitasDitemukan = sebuah boolean untuk memberhentikan whileloop ketika identitas pengendara sudah ditemukan
# identitasKendaraan = bagian dimana user bisa menginput Karcis Parkir mereka atau Id kartu E-Money untuk dicari oleh mesin
# jamKeluarParkir = menerima input berupa jam saat ini untuk mengetahui kapan pengendara keluar ke tempat parkir
# menitKeluarParkir = menerima input berupa menit saat ini untuk mengetahui kapan pengendara keluar ke tempat parkir
# biaya_parkir_mobil = int yang merupakan jumlah biaya parkir mobil per jam
# biaya_parkir_motor = int yang merupakan jumlah biaya parkir motor per jam
# maks_biaya_parkir_mobil = int yang berisi biaya maks yang akan dikenakan pada mobil ketika ia sedang parkir
# maks biaya_parkir_motor = int yang berisi biaya maks yang akan dikenakan pada motor ketika ia seadng parkir

# Inisialisasi Jumlah Tempat Parkir:
jumlah_parkir_mobil = 1 # User yang mengubah isinya
jumlah_parkir_motor = 2 # User yang mengubah isinya
n = jumlah_parkir_mobil + jumlah_parkir_motor

# Inisialisasi List Karcis Parkir
listKarcisParkir = [f"Karcis{i:02d}" for i in range(1, n + 1)]
i = 0
j = 0

# Variable tetap mengenai biaya parkir mobil dan motor
biaya_parkir_mobil = 2000
biaya_parkir_motor = 1000
maks_biaya_parkir_mobil = 10000
maks_biaya_parkir_motor = 5000

dataPengendara = []
checker = True

while checker == True:
    entranceAutoGate = str(input("Masuk/Keluar dari tempat parkir: "))
    if entranceAutoGate == "Masuk":
        if jumlah_parkir_mobil > 0 or jumlah_parkir_motor > 0 :
            # Dialog awal untuk menyambut pengendara dan memberikan informasi mengenai ketersediaan tempat parkir
            print("==========================================")
            print("=    Selamat datang di ITB Jatinangor    =")
            print("=       Parkiran kosong saat ini:        =")
            print(f"=        Tempat Parkir Motor: {jumlah_parkir_motor}          =")
            print(f"=        Tempat Parkir Mobil: {jumlah_parkir_mobil}          =")
            print("==========================================")
            print()
            # Mengecek jenis kendaraan yang digunakan pengendara
            print("Masukkan jenis kendaraan Anda:")
            print("    1. Mobil     2. Motor     ")
            jenisKendaraan = int(input("Ketik (1/2): "))
            if jenisKendaraan == 1:    # Ketika jenis kendaraan adalah mobil
                jumlah_parkir_mobil -= 1
            elif jenisKendaraan == 2:  # Ketika jenis kendaraan adalah motor
                jumlah_parkir_motor -= 1
            else:                      
                print("Jenis kendaraan Anda tidak valid")
            # Mengecek Plat Nomor Kendaraan yang digunakan sebagai identitas per kendaraan
            platNomor = str(input("Masukkan plat nomor kendaraan Anda: ")) # OPSIONALL
            # Mengecek waktu ketika pengendara masuk ke tempat parkir
            jamMasukParkir = int(input("Masukkan jam saat ini (masuk parkir): "))
            menitMasukParkir = int(input("Masukkan menit saat ini (masuk parkir): "))
            # Mengecek jenis pembayaran yang akan digunakan oleh pengendara
            print("Pilihlah bagaimana Anda akan membayar nanti: ")
            print("        1. Karcis       2. E-Money")
            jenisPembayaran = int(input("Ketik (1/2):"))
            # Ketika jenis pembayaran adalah karcis parkir, maka sistem akan memberikan sebuah karcis
            if jenisPembayaran == 1:
                print("========================")
                print("=                      =")
                print(f"=      {listKarcisParkir[i]}      =")
                print("=                      =")
                print("========================")
                # Inisialisasi data per pengendara dengan kendaraannya
                dataSatuan = [jenisKendaraan, platNomor, jamMasukParkir, menitMasukParkir, jenisPembayaran, listKarcisParkir[i]]
                i += 1  # Untuk berpindah item dalam array, agar pengendara selanjutnya tidak mendapatkan karcis yang sma
            # Ketika jenis pembayaran adalah kartu uang elektronik (E-Money), mesin akan meminta id kartu dan jumlah saldonya (simulasi proses tap kartu)
            elif jenisPembayaran == 2:
                kartuEMoney = int(input("Masukkan id kartu E-Money Anda (16 digit): "))
                saldoEMoney = int(input("Masukkan jumlah saldo dalam E-Money Anda: "))
                # Inisialisasi data per pengendara dengan kendaraannya
                dataSatuan = [jenisKendaraan, platNomor, jamMasukParkir, menitMasukParkir, jenisPembayaran, kartuEMoney, saldoEMoney]
            else:
                print("Jenis pembayaran yang anda lakukan tidak valid.")
            # Memasukkan data per pengendara ke dalam kumpulan data beberapa pengendara
            dataPengendara.append(dataSatuan)
            print(dataPengendara[j]) # Opsional
            j += 1                   # Opsional
        else:
            print("Parkir sudah penuh, Anda bisa mencari parkir di luar atau tempat lain")
    elif entranceAutoGate == "Keluar":
        # Reset variable setiap ada kendaraan yang ingin keluar dari tempat parkir
        k = 0
        sisaSaldoEMoney = 0
        totalBiayaParkir = 0
        identitasDitemukan = False
        # Meminta input berupa waktu saat ini untuk menghitung biaya parkir
        jamKeluarParkir = int(input("Masukkan jam saat ini (keluar parkir): "))
        menitKeluarParkir = int(input("Masukkan menit saat ini (keluar parkir): "))
        # Memilih jenis pembayaran seperti proses saat masuk ke tempat parkir
        print("Pilihlah jenis pembayaran Anda:")
        print(" 1. Karcis Parkir   2. E-Money")
        jenisPembayaran = int(input("Ketik (1/2):"))
        # Ketika jenis pembayaran adalah parkir, maka mesin akan meminta kode karcis parkir, sama seperti pengendara memberikan karcis parkir pada penjaga
        if jenisPembayaran == 1:
            identitasKendaraan = str(input("Masukkan Kode Karcis Parkir Anda: "))
            # Looping identitas per pengendara hingga ditemukan k, yaitu item ke berapa identitas pengendara ada dalam array dataPengendara
            while identitasDitemukan == False:
                if identitasKendaraan == dataPengendara[k][5]:
                    identitasDitemukan = True
                else:
                    k += 1
            # Ketika pengendara menggunakan mobil
            if dataPengendara[k][0] == 1:
                totalBiayaParkir = min((5000 + (jamKeluarParkir - jamMasukParkir - 1) * biaya_parkir_mobil + (abs(menitKeluarParkir - menitMasukParkir) > 0) * biaya_parkir_mobil), 20000)
                print(f"Biaya parkir Anda adalah: {totalBiayaParkir}")
                jumlah_parkir_mobil += 1
            # Ketika pengendara menggunakan motor
            elif dataPengendara[k][0] == 2:
                totalBiayaParkir = min((2000 + (jamKeluarParkir - jamMasukParkir - 1) * biaya_parkir_motor + (abs(menitKeluarParkir - menitMasukParkir) > 0) * biaya_parkir_motor), 10000)
                print(f"Biaya parkir Anda adalah: {totalBiayaParkir}")
                jumlah_parkir_motor += 1
        elif jenisPembayaran == 2:
            identitasKendaraan = int(input("Masukkan Id Kartu EMoney Anda: "))
            # Looping identitas per pengendara hingga ditemukan k, yaitu item ke berapa identitas pengendara ada dalam array dataPengendara
            while identitasDitemukan == False:
                if identitasKendaraan == dataPengendara[k][5]:
                    identitasDitemukan = True
                else:
                    k += 1
            # Ketika pengendara menggunakan mobil
            if dataPengendara[k][0] == 1:
                totalBiayaParkir = min((3000 + (jamKeluarParkir - jamMasukParkir - 1) * biaya_parkir_mobil + (abs(menitKeluarParkir - menitMasukParkir) > 0) * biaya_parkir_mobil), maks_biaya_parkir_mobil)
                jumlah_parkir_mobil += 1
            # Ketika pengendara menggunakan motor
            elif dataPengendara[k][0] == 2:
                totalBiayaParkir = min((2000 + (jamKeluarParkir - jamMasukParkir - 1) * biaya_parkir_motor + (abs(menitKeluarParkir - menitMasukParkir) > 0) * biaya_parkir_motor), maks_biaya_parkir_motor)
                jumlah_parkir_motor += 1
            # Mengecek apabila pengendara memiliki saldo E-Money yang cukup untuk membayar parkir
            if dataPengendara[k][6] >= totalBiayaParkir:
                sisaSaldoEMoney = dataPengendara[k][6] - totalBiayaParkir
                print(f"Sisa saldo E Money Anda adalah: {sisaSaldoEMoney}")
            else:
                print(f"Biaya parkir Anda adalah: {totalBiayaParkir}")
                print("Saldo EMoney Anda tidak cukup. Mohon bayar menggunakan cara lain!")
    elif entranceAutoGate == "STOP": # Menghentikan Program agar user tidak perlu terus menerus menginput
        checker = False
    else:
        print("Input yang Anda masukkan tidak valid. Mohon memilih antara masuk atau keluar!")

