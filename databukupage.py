from itertools import count
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

import mysql.connector

class databuku_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Data Buku")
        self.root.geometry("1550x800+0+0")

        self.id_buku=StringVar()
        self.nama_buku=StringVar()
        self.pengarang_buku=StringVar()
        self.penerbit_buku=StringVar()
        self.kategori_buku=StringVar()
        self.bahasa_buku=StringVar()
        self.harga_buku=StringVar()
        self.stok_buku=StringVar()


        lbltitle = Label(self.root,text="Data Buku",fg="black",font=("Calibri",30,"bold"))
        lbltitle.grid(row=0,column=0, sticky=W, columnspan=2, padx=10, pady=10)

        #style
        style = ttk.Style()

        #theme
        style.theme_use('default')

        #configure the treeview colors
        style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=30, fieldbackground="white")

        #change selected color
        style.map('Treeview', background=[('selected', "#347083")])

        #frame tabel
        tabel_frame = Frame(self.root)
        tabel_frame.place(x=10, y=150, width=1510, height=620)

        #scrollbar
        tabel_scroll = ttk.Scrollbar(tabel_frame, orient=VERTICAL)
        tabel_scroll.pack(side=RIGHT, fill=Y)

        #create tabel
        self.my_tabel = ttk.Treeview(tabel_frame, column=("IDBuku","Nama Buku", "Pengarang Buku", "Penerbit Buku", "Kategori Buku", "Bahasa Buku", "Harga Buku", "Stok Buku"),
                                                            yscrollcommand=tabel_scroll.set)
        self.my_tabel.pack()

        #configure our columns
        tabel_scroll=ttk.Scrollbar(command=self.my_tabel.yview)

        #define columns
        #self.my_tabel['column'] = ("IDBuku","Nama Buku", "Pengarang Buku", "Penerbit Buku", "Kategori Buku", "Bahasa Buku", "Harga Buku", "Stok Buku")
        
        #headings
        self.my_tabel.heading("#0", text="", anchor=W)
        self.my_tabel.heading("IDBuku", text="ID Buku")
        self.my_tabel.heading("Nama Buku", text="Nama Buku")
        self.my_tabel.heading("Pengarang Buku", text="Pengarang Buku")
        self.my_tabel.heading("Penerbit Buku", text="Penerbit Buku")
        self.my_tabel.heading("Kategori Buku", text="Kategori Buku")
        self.my_tabel.heading("Bahasa Buku", text="Bahasa Buku")
        self.my_tabel.heading("Harga Buku", text="Harga Buku")
        self.my_tabel.heading("Stok Buku", text="Stok Buku")

        self.my_tabel["show"]="headings"

        #format columns
        self.my_tabel.column("#0", width=0, stretch=NO)
        self.my_tabel.column("IDBuku", width=100)
        self.my_tabel.column("Nama Buku", width=100)
        self.my_tabel.column("Pengarang Buku", width=100)
        self.my_tabel.column("Penerbit Buku", width=100)
        self.my_tabel.column("Kategori Buku", width=100)
        self.my_tabel.column("Bahasa Buku", width=100)
        self.my_tabel.column("Harga Buku", width=100)
        self.my_tabel.column("Stok Buku", width=100)

        self.my_tabel.pack(fill=BOTH,expand=1)

        #data dummy
        data = [
            [1, "Bibi Gill", "Tere Liye", "PENERBIT SABAK GRIP", "Fiksi Ilmiah", "Indonesia", "89000", 50],
            [2, "Spy X Family 03", "Endo Tatsuya", "Elex Media Komputindo", "Manga", "Indonesia", "36000", 50],
            [3, "Laut Bercerita", "Leila S. Chudori", "Kepustakaan Populer Gramedia", "Fiksi Ilmiah", "Indonesia", "70000", 50],
            [4, "Sebuah Seni untuk Bersikap Bodo Amat", "Nark Manson", "Gramedia Widiasarana Indonesia", "Pengembangan Diri", "Indonesia", "54600", 50],
            [5, "Hai, Miko! 34 - Premium", "Ono Eriko", "m&c!", "Manga", "Indonesia", "42000", 50],
            [6, "Home Sweet Loan", "Almira Bastari", "Gramedia Pustaka Utama", "Novel", "Indonesia", "66500", 50],
            [7, "Jujutsu Kaisen 05", "Gege Akutami", "Elex Media Komputindo", "Manga", "Indonesia", "32000", 50],
            [8, "Sagaras", "Tere Liye", "PENERBIT SABAK GRIP", "Fiksi Ilmiah", "Indonesia", "89000", 50],
            [9, "Merawat Luka Batin", "Dr Jiemi Ardian", "Gramedia Pustaka Utama", "Pengembangan Diri", "Indonesia", "78400", 50],
            [10, "Heartbreak Motel", "Ika Natassa", "Gramedia Pustaka Utama", "Romance", "Indonesia", "69300", 50],
            [11, "Anak Bajang Mengayun Bulan", "Sindhunata", "Gramedia Pustaka Utama", "Novel", "Indonesia", "170800", 50],
            [12, "Pachinko", "Min Jin Lee", "Gramedia Pustaka Utama", "Romance", "Indonesia", "95200", 50],
            [13, "Cr: The Sweetest Hours", "Cathryn Parry", "Elex Media Komputindo", "Romance", "Indonesia", "72000", 50],
            [14, "Membasmi Frustasi Fotografer", "Edwin Effendi", "Elex Media Komputindo", "Seni Desain", "Indonesia", "72000", 50],
            [15, "Panduan Praktis Seminar Edisi Ketiga", "Indra Yuzal", "Pt Rajagrafindo Persada", "Pendidikan", "Indonesia", "69000", 50],
            [16, "Cake Kekinian Favorit", "Meida Felici", "Gramedia Pustaka Utama", "Buku Masakan", "Indonesia", "78400", 50],
            [17, "Yuk Belajar Nabung Saham", "Ryan Filbert Wijaya, S.Sn, ME.", "Elex Media Komputindo", "Finansial", "Indonesia", "63000", 50],
            [18, "Siap-Siap Jadi Orangtua", "Najelaa Shihab", "Buah Hati", "Buku Parenting", "Indonesia", "120000", 50],
            [19, "Violet", "Kyung Sook Shin", "Gramedia Pustaka Utama", "Sastra", "Indonesia", "61600", 50],
            [20, "35 Fabel Anak", "Any Hidayati", "Anak Hebat Indonesia", "Buku Anak", "Indonesia", "55500", 50]
        ]

        #create striped row tags
        self.my_tabel.tag_configure('oddrow', background="white")
        self.my_tabel.tag_configure('evenrow', background="lemonchiffon3")

        #add our data to the screen
        global count
        count = 0

        for record in data:
            if count % 2 == 0:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('evenrow',))
            else:
                self.my_tabel.insert(parent='', index='end', text=f'{count + 1}', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags=('oddrow',))
        
            #increment count
            count += 1
        
        
        #add buttons
        #button tambah buku
        add_new_book_btn=Button(self.root, text="tambah", font=("Calibri",12),bd=3,fg="black")
        add_new_book_btn.place(x=1350,y=80,width=120,height=35)

        delete_book_btn=Button(self.root, text="hapus", font=("Calibri",12),bd=3,fg="black")
        delete_book_btn.place(x=1230,y=80,width=120,height=35)

        viewall_book_btn=Button(self.root, text="lihat detail", font=("Calibri",12),bd=3,fg="black")
        viewall_book_btn.place(x=1050,y=80,width=180,height=35)

        edit_book_btn=Button(self.root, text="edit", font=("Calibri",12),bd=3,fg="black")
        edit_book_btn.place(x=930,y=80,width=120,height=35)




    '''def add_new_book(self):
        self.new_window=Toplevel(self.root)
        self.app=tambahbuku_window(self.new_window)'''


if __name__ == "__main__":
    root=Tk()
    app = databuku_window(root)
    root.mainloop()