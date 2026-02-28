from tabulate import tabulate
from kurs import kurs
import konverter

def format_rupiah(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")

def tampilkan_tabel():
    data = []
    for kode, nilai in kurs.items():
        data.append([kode, f"{nilai:,}".replace(",", ".")])
    print(tabulate(data, headers=["Kode", "Kurs"], tablefmt="github"))

def main():
    print("=== KONVERTER MATA UANG ===")
    tampilkan_tabel()

    pilihan = ["IDR"] + list(kurs.keys())

    dari = input(f"\nDari ({'/'.join(pilihan)}): ").upper()
    ke = input(f"Ke   ({'/'.join(pilihan)}): ").upper()
    jumlah = float(input("Jumlah: "))

    if dari == "IDR" and ke != "IDR":
        hasil = konverter.dari_idr(jumlah, ke)
        print(f"\n{format_rupiah(jumlah)} = {hasil:.2f} {ke}")

    elif dari != "IDR" and ke == "IDR":
        hasil = konverter.ke_idr(jumlah, dari)
        print(f"\n{jumlah:.2f} {dari} = {format_rupiah(hasil)}")

    elif dari != "IDR" and ke != "IDR":
        ke_idr = konverter.ke_idr(jumlah, dari)
        hasil = konverter.dari_idr(ke_idr, ke)
        print(f"\n{jumlah:.2f} {dari} = {hasil:.2f} {ke}")

    else:
        print("Tidak ada konversi dilakukan.")

if __name__ == "__main__":
    main()
