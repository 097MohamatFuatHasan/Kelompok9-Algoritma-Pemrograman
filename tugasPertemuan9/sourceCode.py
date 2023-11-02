# Daftar menu pizza
menu_pizza = {
    #Jenis pilihan Pizza yang tersedia
    "Frankfurter BBQ": {
        #Jenis Crust
        "Pan": {
            #Jenis Ukuran
            "Personal": 43637,
            "Regular": 100910,
            "Large": 132728
        },
        "StuffedCrust Cheese": {
            "Personal": 55455,
            "Regular": 120910,
            "Large": 160000
        },
        "StuffedCrust Sausage": {
            "Personal": 52728,
            "Regular": 117273,
            "Large": 155455
        },
        "Cheese Bites": {
            "Personal": 57273,
            "Regular": 123637,
            "Large": 164546
        },
        "Crowncrust": {
            "Personal": 55455,
            "Regular": 120910,
            "Large": 160000
        }
    },

    "Meat Monsta": {
        "Pan": {
            "Personal": 43637,
            "Regular": 100910,
            "Large": 132728
        },
        "StuffedCrust Cheese": {
            "Personal": 55455,
            "Regular": 120910,
            "Large": 160000
         },
        "StuffedCrust Sausage": {
            "Personal": 52728,
            "Regular": 117273,
            "Large": 155455
        },
        "Cheese Bites": {
            "Personal": 57273,
            "Regular": 123637,
            "Large": 164546
        },
        "Crowncrust": {
            "Personal": 55455,
            "Regular": 120910,
            "Large": 160000
        }
    },

    "Super Supreme": {
        "Pan": {
            "Personal": 43637,
            "Regular": 100910,
            "Large": 132728
        },
        "StuffedCrust Cheese": {
            "Personal": 55455,
            "Regular": 120910,
            "Large": 160000
        },
        "StuffedCrust Sausage": {
            "Personal": 52728,
            "Regular": 117273,
            "Large": 155455
        },
        "Cheese Bites": {
            "Personal": 57273,
            "Regular": 123637,
            "Large": 164546
        },
        "Crowncrust": {
            "Personal": 55455,
            "Regular": 120910,
            "Large": 160000
        }
    },

    "Super Supreme Chicken": {
        "Pan": {
            "Personal": 43637,
            "Regular": 100910,
            "Large": 132728
        },
        "StuffedCrust Cheese": {
            "Personal": 55455,
            "Regular": 120910,
            "Large": 160000
        },
        "StuffedCrust Sausage": {
            "Personal": 52728,
            "Regular": 117273,
            "Large": 155455
        },
        "Cheese Bites": {
            "Personal": 57273,
            "Regular": 123637,
            "Large": 164546
        },
        "Crowncrust": {
            "Personal": 55455,
            "Regular": 120910,
            "Large": 160000
        }
    }
}

# Daftar menu topping
menu_topping = {
    "Cheese": {
        "Personal": 13636,
        "Regular": 16364,
        "Large": 19091
    }
}

# Inisialisasi pesanan
total_harga = 0
selected_toppings = []

# Memulai Program
print("======================== Selamat datang di Pizza Hut! ========================")
print("Pilihan menu pizza:")
# Menampilkan menu pizza 
for pizza in menu_pizza:
    print(pizza)

# Meminta user memasukkan pizza yang ingin di pesan
pilihan_pizza = input("Pilih Pizza yang anda inginkan :")

# Kondisi untuk memilih pizza, ukuran pizza, dan crust 
if pilihan_pizza in menu_pizza:

    print("Pilih ukuran pizza anda :")
    for size in menu_pizza[pilihan_pizza]["Pan"]:
        print(size)

    pilihan_ukuran = input("Pilih ukuran pizza anda :")

    if pilihan_ukuran in menu_pizza[pilihan_pizza]["Pan"]:
        print("Pilihan crust:")
        for crust in menu_pizza[pilihan_pizza]:

            print(crust)

        pilihan_crust = input("Pilih crust:")

        if pilihan_crust in menu_pizza[pilihan_pizza]:
            total_harga += menu_pizza[pilihan_pizza][pilihan_crust][pilihan_ukuran]
            pesanan = f"Anda memesan {pilihan_pizza} ukuran {pilihan_ukuran} dengan crust {pilihan_crust}"

        else:
            print("Crust yang anda pilih tidak ada dalam menu.")

    else:
        print("Ukuran yang anda pilih tidak ada dalam menu.")

else:
    print("pizza yang anda pilih tidak ada dalam menu.")

tambah_topping = input("Apakah anda ingin menambahkan topping? (ya/tidak): ").lower()

# Kondisi untuk menambahkan topping "Cheese" atau tidak
if tambah_topping == "ya"or tambah_topping == "cheese":
    pilihan_topping = "Cheese"

if pilihan_topping in menu_topping:
    total_harga += menu_topping[pilihan_topping][pilihan_ukuran]
    selected_toppings.append(pilihan_topping)
    pesanan += f" dengan topping {pilihan_topping}"

# Menghitung total harga dari semua pesanan
pesanan += f" seharga Rp. {total_harga}"
# Menampilkan item yang telah di pesan beserta dengan harganya 
print(f"Pesanan Anda: {pesanan}")
print("===================== Terima kasih telah memesan di Pizza Hut! =====================")
