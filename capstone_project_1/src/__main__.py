# Import module needed
from tabulate import tabulate
from utility import show_records, create_record, read_record, update_record, delete_record, get_input, show_data_pesanan, put_order

# Database to store data
car_data = {
    # "RS-MT-01" : {"Manufacturer": "Toyota", "Tipe" : "Rush", "Transmisi" : "MT", "Warna" : "Hitam", "Harga" : 300000000},
    # "HR-AT-01" : {"Manufacturer": "Honda", "Tipe" : "HRV", "Transmisi" : "AT", "Warna" : "Putih", "Harga" : 400000000},
    # "RK-AT-01" : {"Manufacturer": "Daihatsu", "Tipe" : "Rocky", "Transmisi" : "AT", "Warna" : "Merah", "Harga" : 200000000},
    # "TR-MT-01" : {"Manufacturer": "Mitsubishi", "Tipe" : "Triton", "Transmisi" : "MT", "Warna" : "Silver", "Harga" : 350000000},
    # "CR-AT-01" : {"Manufacturer": "Toyota", "Tipe" : "Camry", "Transmisi" : "AT", "Warna" : "Hitam Metalic", "Harga" : 700000000}
}

data_pesanan = {}


print("---------- Selamat datang di RentalMobilKu ----------")
print()
print("Login sebagai akun yang terdaftar: ")
print("""
> admin
> user-01
> user-02
""")
print("---------------------------------")
print("Tulis 'admin' jika sebagai admin.")
print("---------------------------------")

# validasi input user or admin
while True:
    try:
        user = input("Silahkan Login sebagai: ").replace(" ","").lower()
        if user.strip() == '':
            print("Input tidak boleh kosong, silahkan coba lagi")
            continue
        if user in ['admin', 'user-01', 'user-02']:
            break
        else:
            print("Akun tidak terdaftar, pastikan akun telah terdaftar")
            continue
    except:
        print("Invalid input, harap input ulang")
        continue

# the rest if login sucess
#-----------------------------------------------------------------------------------
# Start bagian admin
#-----------------------------------------------------------------------------------     
if user == 'admin':
    print()
    print("---------- Anda masuk sebagai admin ----------")
    # do all
    while True:
        try:
            print("---------- Anda berada di Main Menu ----------")
            print("""
Berikut hal yang dapat anda lakukan :
    
1.  (Read) Membaca/Melihat list mobil-mobil dalam daftar.
2.  (Create) Menambahkan mobil baru dalam daftar.
3.  (Update) Memperbaharui list mobil dalam daftar.
4.  (Delete) Menghapus mobil dalam daftar.
5.  (Exit) Keluar dari Program.
                """)
            user_input = input("Main Menu, masukkan pilihan nomer yang ingin dilakukan: '1'-'4' Menu dan '5' Exit: ")
            if user_input == '1':
                # implementasi read
                print("-----------------------")
                print(f"Anda berada di Menu : {user_input}")
                print("-----------------------")
                while True:
                    try:
                        print("""
Berikut hal yang dapat anda lakukan :
    
1.  Melihat seluruh daftar mobil.
2.  Melihat mobil tertentu.
3.  Kembali ke Main Menu.
                            """)
                        user_input = input("Menu 1, masukkan pilihan nomer yang ingin dilakukan: '1'-'2' Menu dan '3' kembali: ")
                        if user_input == '1':
                            # melihat semua
                            print()
                            if len(car_data) == 0:
                                print("Database kosong, mohon pastikan data tersedia. Silahkan exit dari program")
                                continue
                            print("Berikut daftar mobil yang tersedia: ")
                            show_records(car_data)
                            continue
                        elif user_input == '2':    
                            # melihat tertentu
                            if len(car_data) == 0:
                                print("Database kosong, mohon pastikan data tersedia. Silahkan exit dari program")
                                continue
                            nomer_reg_pattern = r'^[A-Za-z]{2}-[A-Za-z]{2}-\d{2}$'
                            user_input = get_input("Masukkan nomer registrasi mobil (contoh: 'TR-MT-01'): ", nomer_reg_pattern)
                            user_input = user_input.upper()   

                            if user_input in car_data:
                                print("Berikut mobil yang ingin anda lihat: ")# space setelah ini
                            read_record(car_data, user_input) # Baik ada atau tidak mobil, pesan akan muncul
                            continue
                        elif user_input == '3':    
                            # keluar dari pilihan 1 dan kembali ke Main Menu
                            print("-------------------------------")
                            print("Anda telah keluar dari Menu : 1")
                            print("-------------------------------")
                            break
                        else:
                            print("Input tidak valid, harap input ulang.")
                            continue    
                    except:
                        print("Input tidak valid, harap input ulang.")
                        continue
                continue
            elif user_input == '2':
                # implementasi create
                print("-----------------------")
                print(f"Anda berada di Menu : {user_input}")
                print("-----------------------")
                while True:
                    try:
                        print("""
Berikut hal yang dapat anda lakukan :
    
1.  Menambah unit baru ke dalam daftar.
2.  Kembali ke Main Menu.
                            """)
                        user_input = input("Menu 2, masukkan pilihan nomer yang ingin dilakukan: '1' Menu dan '2' kembali: ")
                        if user_input == '1':
                            # Menambah unit baru
                            while True:
                                try:
                                    # inputan
                                    print()
                                    print("Silahkan isi data mobil yang akan didaftarkan: ")

                                    # Definisi pattern untuk regular expression dan ambil input
                                    nomer_reg_pattern = r'^[A-Za-z]{2}-[A-Za-z]{2}-\d{2}$'
                                    nomer_reg = get_input("Buat nomer registrasi dengan format mobil 'Tipe-Transmisi-Urutan' (menjadi: 'RK-AT-01'): ", nomer_reg_pattern)
                                    nomer_reg = nomer_reg.upper()   
                                    # Jika nomer registrasi sudah ada tidak perlu isi kolom selanjutnya dan ulang.
                                    if nomer_reg in car_data: 
                                        print(f"Mobil dengan nomer registrasi '{nomer_reg}' sudah terdaftar.")
                                        continue

                                    # Definisi pattern untuk regular expression    
                                    manufacturer_pattern = r'^[A-Za-z\s]+$'
                                    tipe_pattern = r'^[A-Za-z0-9\s]+$'
                                    transmisi_pattern = r'^(AT|MT)$'
                                    warna_pattern = r'^[A-Za-z\s]+$'
                                    harga_pattern = r'^\d+$'

                                    # Validasi setiap input sesuai pattern
                                    manufacturer = get_input("Masukkan Manufacturer (contoh: 'Toyota') : ", manufacturer_pattern)
                                    tipe = get_input("Masukkan Tipe mobil (contoh: 'Inova'): ", tipe_pattern)
                                    transmisi = get_input("Masukkan jenis Transmisi mobil AT/MT (contoh: 'AT'): ", transmisi_pattern)
                                    warna = get_input("Masukkan warna mobil (contoh: 'Putih'): ", warna_pattern)
                                    harga = get_input("Masukkan Harga mobil (contoh: 400000000): ", harga_pattern)

                                    #--------------------------------
                                    is_saving = False
                                    while True:
                                        try:
                                            input_user = input("Apakah yakin ingin menambahkan data (y/n): ").lower()
                                            if input_user.strip() == '':
                                                print("Input tidak boleh kosong. Silakan coba lagi.")
                                                continue
                                            if input_user in ['y','yes']:
                                                is_saving = True
                                                break
                                            elif input_user in ['n','no']:
                                                is_saving = False
                                                break
                                            else:
                                                print("Format input tidak valid. Silakan coba lagi.")    
                                        except:
                                            print("Input tidak valid, harap input ulang.")
                                            continue 
                                    if is_saving:
                                        # Impementasi penambahan data baru ke database
                                        print()
                                        create_record(car_data, 
                                                    nomer_reg.upper(), 
                                                    manufacturer.capitalize(), 
                                                    tipe.capitalize(), 
                                                    transmisi.upper(),
                                                    warna.title(), 
                                                    int(harga)
                                                    )
                                        # Menampilkan semua mobil setelah penambahan mobil baru ke daftar.
                                        show_records(car_data)
                                        break
                                    else:
                                        print("Data tidak ditambahkan")
                                        break
                                except:
                                    print("Input tidak valid, harap input ulang.")
                                    continue
                            continue    
                        elif user_input == '2':    
                            # keluar dari pilihan 2 dan kembali ke Main Menu
                            print("-------------------------------")
                            print("Anda telah keluar dari Menu : 2")
                            print("-------------------------------")
                            break
                        else:
                            print("Input tidak valid, harap input ulang.")
                            continue    
                    except:
                        print("Input tidak valid, harap input ulang.")
                        continue
                continue
            elif user_input == '3':
                # implementasi update
                print("-----------------------")
                print(f"Anda berada di Menu : {user_input}")
                print("-----------------------")
                
                while True:
                    try:
                        print("""
Berikut hal yang dapat anda lakukan :
    
1.  Memperbaharui data unit dalam daftar.
2.  Kembali ke Main Menu.
                            """)
                        user_input = input("Menu 3, masukkan pilihan nomer yang ingin dilakukan: '1' Menu dan '2' Kembali ke Main Menu: ")
                        if user_input == '1':
                            # implementasi poin 1
                            if len(car_data) == 0:
                                print("Database kosong, mohon pastikan data tersedia. Silahkan exit dari program")
                                continue
                            while True: # Selama nomer registrasi tidak sesuai maka user input ulang
                                print()
                                # Definisi pattern untuk regular expression dan ambil input
                                nomer_reg_pattern = r'^[A-Za-z]{2}-[A-Za-z]{2}-\d{2}$'
                                nomer_registrasi = get_input("Silahkan masukkan nomer registrasi yang diinginkan (contoh: 'RS-MT-01'): ", nomer_reg_pattern)
                                nomer_registrasi = nomer_registrasi.upper()           
                                if nomer_registrasi not in car_data:
                                    print(f"Mobil dengan nomer registrasi '{nomer_registrasi}' tidak terdaftar, pastikan nomer registrasi benar")
                                    continue

                                print(f"Anda akan melakukan perubahan data mobil dengan nomer registrasi '{nomer_registrasi}'")
                                print("Beberapa pilihan yang dapat anda ubah: Manufacturer, Tipe, Transmisi, Warna dan Harga")
                                print()
                                user_input = input("Tuliskan yang ingin anda ubah (contoh: Tipe, Transmisi, dan harga): ").replace('dan','').replace(' ','')
                                user_input = [i.capitalize() for i in user_input.split(',')]

                                updated_features = {}
                                car_feature = ["Manufacturer", "Tipe", "Transmisi", "Warna", "Harga"]

                                # Definisi pattern untuk regular expression
                                patterns = {
                                    'Manufacturer' : r'^[A-Za-z\s]+$',
                                    'Tipe' : r'^[A-Za-z0-9\s]+$',
                                    'Transmisi' : r'^(AT|MT)$',
                                    'Warna' : r'^[A-Za-z\s]+$',
                                    'Harga' : r'^\d+$'
                                    }    

                                is_any_update = False
                                for i in range(len(user_input)):
                                    if user_input[i] in car_feature:

                                        is_any_update = True

                                        key = user_input[i]
                                        value = get_input(f"Masukkan '{user_input[i].capitalize()}' baru: ", patterns[key])
                                        if key == "Transmisi":
                                            updated_features[key] = value.upper().replace(' ','')
                                        if key == "Manufacturer" or key == "Warna" or key == "Tipe":
                                            updated_features[key] = value.title()
                                        if key == "Harga":
                                            updated_features[key] = int(value)

                                if is_any_update:
                                    # proses update data di databases             
                                    update_record(car_data, nomer_registrasi, **updated_features) 
                                    # tampilkan all records untuk cek perubahan pasca update
                                    show_records(car_data)
                                else:
                                    print("Input tidak sesuai, tidak ada data di-update")     

                                is_update_again = False

                                while True:
                                    try:
                                        user_input = input("Apakah ingin mengupdate lagi? (y/n): ").lower().replace(' ','')
                                        if user_input in ['y','yes']:
                                            is_update_again = True
                                            break
                                        elif user_input in ['n','no']:
                                            is_update_again = False
                                            break
                                        else:
                                            print("Input tidak valid, harap input ulang")
                                            continue
                                    except:
                                        print("Input tidak valid, harap input ulang")
                                        continue

                                if is_update_again:    
                                    continue
                                else:
                                    break
                                    
                        elif user_input == '2':
                            # keluar dari Menu 3 dan kembali ke Main Menu    
                            print("-------------------------------")
                            print("Anda telah keluar dari Menu : 3")
                            print("-------------------------------")
                            break
                        else:
                            print("Input tidak valid, harap input ulang.")
                            continue
                    except:
                        print("Input tidak valid, harap input ulang.")
                        continue    
                continue
            elif user_input == '4':
                # implementasi delete
                print("-----------------------")
                print(f"Anda berada di Menu : {user_input}")
                print("-----------------------")

                while True:
                    try:
                        print("""
Berikut hal yang dapat anda lakukan :
    
1.  Menghapus data unit dalam daftar.
2.  Kembali ke Main Menu.
                            """)
                        user_input = input("Menu 4, masukkan pilihan nomer yang ingin dilakukan: '1' Menu dan '2' Kembali ke Main Menu: ")
                        if user_input == '1':
                            # implementasi penghapusan
                            try:
                                if len(car_data) == 0:
                                    print("Database kosong, mohon pastikan data tersedia. Silahkan exit dari program")
                                    continue
                                while True:
                                    print()
                                    nomer_reg_pattern = r'^[A-Za-z]{2}-[A-Za-z]{2}-\d{2}$'
                                    nomer_registrasi = get_input("Silahkan masukkan nomer registrasi yang ingin dihapus (contoh: 'RS-MT-01'): ", nomer_reg_pattern)
                                    nomer_registrasi = nomer_registrasi.upper()   
                                    if nomer_registrasi not in car_data:
                                        print(f"Mobil dengan nomer registrasi '{nomer_registrasi}' tidak ditemukan")
                                        continue
                                    
                                    while True:        
                                        try:        
                                            user_input = input("Apakah yakin ingin menghapus data? (y/n): ").lower()
                                            if user_input in ['y','yes']:
                                                delete_record(car_data, nomer_registrasi)
                                                show_records(car_data)
                                                break
                                            elif user_input in ['n', 'no']:
                                                break
                                            else:
                                                print("Invalid input, harap input ulang")
                                                continue  
                                        except:
                                            print("Invalid input, harap input ulang")
                                            continue  

                                    is_delete_again = False

                                    while True:
                                        try:
                                            user_input = input("Apakah ingin menghapus lagi? (y/n): ").lower().replace(' ','')
                                            if len(car_data) == 0:
                                                print("Database kosong, mohon pastikan data tersedia. Silahkan exit dari program")
                                                break
                                            if user_input in ['y','yes']:
                                                is_delete_again = True
                                                break
                                            elif user_input in ['n','no']:
                                                is_delete_again = False
                                                break
                                            else:
                                                print("Input tidak valid, harap input ulang")
                                                continue
                                        except:
                                            print("Input tidak valid, harap input ulang")
                                            continue

                                    if is_delete_again:    
                                        continue
                                    else:
                                        break        
                            except:
                                print("Input tidak valid, harap input ulang.")
                                continue     
                        elif user_input == '2':
                            # keluar dari Menu 4 dan kembali ke Main Menu    
                            print("-------------------------------")
                            print("Anda telah keluar dari Menu : 4")
                            print("-------------------------------")
                            break
                        else:
                            print("Input tidak valid, harap input ulang.")
                            continue
                    except:
                        print("Input tidak valid, harap input ulang.")
                        continue 
                continue
            elif user_input == '5':
                # exit dari program 
                is_keluar = False
                while True:
                    try:
                        input_user = input("Apakah yakin ingin keluar (y/n): ").lower()
                        if input_user.strip() == '':
                            print("Input tidak boleh kosong. Silakan coba lagi.")
                            continue
                        if input_user in ['y','yes']:
                            is_keluar = True
                            break
                        elif input_user in ['n','no']:
                            is_keluar = False
                            break
                        else:
                            print("Format input tidak valid. Silakan coba lagi.")    
                    except:
                        print("Input tidak valid, harap input ulang.")
                        continue 
                if is_keluar:
                    break
                else:
                    continue
            else:
                print("Input tidak valid, harap periksa input yang anda masukkan")   
                continue    
        except:
            print("Input tidak valid, harap periksa input yang anda masukkan")
            continue
    # exit dari program 
    print()
    print("Anda keluar dari aplikasi")
    print("Terima kasih telah menggunakan 'RentalMobilKu'")
#-----------------------------------------------------------------------------------
# Akhir bagian admin
#-----------------------------------------------------------------------------------      
#-----------------------------------------------------------------------------------
# Start bagian user    
#-----------------------------------------------------------------------------------    
else: # login sebagai 'user-01' atau 'user-02'
    print()
    print(f"Halo, {user}. Selamat datang!")
    while True:
        try:
            print("""
Berikut hal yang dapat anda lakukan :
    
1.  (Read) Membaca/Melihat list mobil-mobil dalam daftar.
2.  (Order) Melakukan pemesanan.
3.  (Exit) Keluar dari Program.
        """)
            user_input = input("Main Menu, masukkan pilihan nomer yang ingin dilakukan: '1'-'2' Menu dan '3' Exit: ")
            if user_input == '1':
                # do read function
                if len(car_data) == 0:
                    print("Database kosong, mohon pastikan data tersedia. Silahkan exit dari program")
                    continue
                print("Berikut daftar mobil yang tersedia: ")
                show_records(car_data)
                continue
            elif user_input == '2':
                # do order function
                if len(car_data) == 0:
                    print("Database kosong, mohon pastikan data tersedia. Silahkan exit dari program")
                    continue
                print("Anda akan melakukan pemesanan")
                while True:
                    try:
                         # Definisi pattern untuk regular expression dan ambil input
                        nomer_reg_pattern = r'^[A-Za-z]{2}-[A-Za-z]{2}-\d{2}$'
                        nomer_registrasi = get_input("Silahkan masukkan nomer registrasi sesuai daftar (contoh: 'RS-MT-01'): ", nomer_reg_pattern)
                        nomer_registrasi = nomer_registrasi.upper()   
                        put_order(car_data, data_pesanan, user, nomer_registrasi)
                        if nomer_registrasi in car_data:
                            print("Data pesanan terbaru: ")
                            show_data_pesanan(data_pesanan)
                        break  
                    except:
                        print("Invalid input, harap input ulang")
                        continue
                continue
            elif user_input == '3':
                # Keluar program
                break
            else:
                print("Invalid input, harap input ulang")
                continue    
        except:
            print("Invalid input, harap input ulang")
            continue
    # exit dari program 
    print()
    print("Anda keluar dari aplikasi")
    print("Terima kasih telah menggunakan 'RentalMobilKu'")
#-----------------------------------------------------------------------------------
# Akhir bagian user    
#-----------------------------------------------------------------------------------      