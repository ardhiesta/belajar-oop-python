"""
Hello2.py
ini adalah contoh code class yang dilengkapi dengan fungsi

struktur class dalam Python kurang lebih sebagai berikut
class <NamaClass>():
    # initializer, digunakan untuk menginisiasi atribut class
    def __init__(self, <optional param1>, ..., <optional paramN>):
        # kode inisialisasi di sini

    # struktur fungsi / method:
    def <namaFungsi>(self, <optional param1>, ..., <optional paramN>):
        # bagian body dari fungsi / method

ardhi wijayanto
"""
# membuat class Hello
class Hello:
    def ucapkan(self):
        print("hai, ini adalah contoh class dalam bahasa pemrograman Python")

# membuat objek clas Hello
hello1 = Hello()

# memanggil fungsi ucapkan dari class Hello
hello1.ucapkan()