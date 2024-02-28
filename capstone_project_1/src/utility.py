# import module needed
from tabulate import tabulate
import re

# Show
def show_records(car_data):
    headers = ["Nomer registrasi", "Manufacturer" , "Tipe", "Transmisi", "Warna", "Harga"]
    rows = []
    for reg_number, car in car_data.items():
        rows.append([reg_number, car['Manufacturer'], car['Tipe'], car['Transmisi'], car['Warna'], car['Harga']])
    print(tabulate(rows, headers=headers, tablefmt="grid"))

# Create
def create_record(car_data, nomer_registrasi, manufacturer, tipe, transmisi, warna, harga):
    if nomer_registrasi in car_data:
        print("Mobil dengan nomer registrasi ini sudah terdaftar.")
    else:
        car_data[nomer_registrasi] = {
            "Manufacturer" : manufacturer, 
            "Tipe" : tipe, 
            "Transmisi" : transmisi,
            "Warna" : warna,
            "Harga" : harga
        }    
        print(f"'Berhasil ditambahkan' ke daftar, mobil dengan nomer registrasi '{nomer_registrasi}'")


# Read
def read_record(car_data, nomer_registrasi):
    headers = ["Nomer registrasi", "Manufacturer" , "Tipe", "Transmisi", "Warna", "Harga"]
    row = []
    if nomer_registrasi in car_data.keys():
        row.append([nomer_registrasi, 
                    car_data[nomer_registrasi]["Manufacturer"],
                    car_data[nomer_registrasi]["Tipe"],
                    car_data[nomer_registrasi]["Transmisi"],
                    car_data[nomer_registrasi]["Warna"],
                    car_data[nomer_registrasi]["Harga"],])
        print(tabulate(row, headers=headers, tablefmt="grid"))
    else:
        print(f"Mobil dengan nomer registrasi '{nomer_registrasi}' tidak terdaftar")

# Update
def update_record(car_data, nomer_registrasi, **kwargs):
    mobil = car_data.get(nomer_registrasi)
    if mobil:
        # mobil ada di daftar
        for key, val in kwargs.items():
            if key in mobil:
                mobil[key] = val
                print(f"* Data {key} '{nomer_registrasi}' telah diperbaharui")
    else:
        print(f"Error: Mobil dengan nomer registrasi '{nomer_registrasi}' tidak ditemukan")         


# Delete
def delete_record(car_data, nomer_registrasi):
    if nomer_registrasi in car_data:
        del car_data[nomer_registrasi]
        print(f"Mobil dengan nomer registrasi '{nomer_registrasi}' berhasil dihapus")
    else:
        print(f"Mobil dengan nomer registrasi '{nomer_registrasi}' tidak ditemukan")  

# validasi input sesuai pattern
def get_input(prompt, pattern):
    try:
        while True:
            user_input = input(prompt)
            if user_input.strip() == '':
                print("Input tidak boleh kosong. Silakan coba lagi.")
                continue
            if re.fullmatch(pattern, user_input):
                return user_input
            else:
                print("Format input tidak valid. Silakan coba lagi.")
    except:
        print("Format input tidak valid. Silakan coba lagi.")
       
# All data pesanan
def show_data_pesanan(data_pesanan):
    headers = ["Customer ID", "Manufacturer" , "Tipe", "Transmisi", "Warna", "Harga"]
    rows = []
    for user_id, order in data_pesanan.items():
        rows.append([user_id, order['Manufacturer'], order['Tipe'], order['Transmisi'], order['Warna'], order['Harga']])
    print(tabulate(rows, headers=headers, tablefmt="grid"))

# Implementasi user menaruh order
def put_order(car_data, data_pesanan, user_id, nomer_registrasi):
    if nomer_registrasi not in car_data:
        print(f"Tidak ada kendaraan dengan nomer registrasi '{nomer_registrasi}', pastikan mobil sesuai di daftar.")
    else:
        booked_car = car_data[nomer_registrasi]
        data_pesanan[user_id] = booked_car
        print(f"Mobil dengan kode '{nomer_registrasi}' berhasil dipesan")    
                
