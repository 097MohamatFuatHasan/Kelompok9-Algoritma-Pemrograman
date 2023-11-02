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
