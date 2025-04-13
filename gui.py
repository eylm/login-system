import tkinter as tk
from tkinter import messagebox
import json
import os

KULLANICI_DOSYA = "data/kullanicilar.json"

if not os.path.exists("data"):
    os.makedirs("data")
if not os.path.exists(KULLANICI_DOSYA):
    with open(KULLANICI_DOSYA, "w") as f:
        json.dump({}, f)

def kullanici_kaydet(kullanici_adi, sifre):
    with open(KULLANICI_DOSYA, "r") as f:
        kullanicilar = json.load(f)
    if kullanici_adi in kullanicilar:
        return False
    kullanicilar[kullanici_adi] = sifre
    with open(KULLANICI_DOSYA, "w") as f:
        json.dump(kullanicilar, f)
    return True

def kayit_ol():
    def kaydet():
        ad = entry_k_adi.get()
        sif = entry_sifre.get()
        if ad.strip() == "" or sif.strip() == "":
            messagebox.showwarning("Uyarı", "Boş alan bırakmayınız.")
            return
        if kullanici_kaydet(ad, sif):
            messagebox.showinfo("Başarılı", "Kayıt başarılı!")
            kayit_pencere.destroy()
        else:
            messagebox.showerror("Hata", "Bu kullanıcı zaten var.")

    kayit_pencere = tk.Toplevel()
    kayit_pencere.title("Kayıt Ol")
    kayit_pencere.configure(bg="#f0f0f0")
    kayit_pencere.geometry("300x200")

    tk.Label(kayit_pencere, text="Kullanıcı Adı:", bg="#f0f0f0").pack(pady=5)
    entry_k_adi = tk.Entry(kayit_pencere)
    entry_k_adi.pack(pady=5)
    tk.Label(kayit_pencere, text="Şifre:", bg="#f0f0f0").pack(pady=5)
    entry_sifre = tk.Entry(kayit_pencere, show="*")
    entry_sifre.pack(pady=5)
    tk.Button(kayit_pencere, text="Kaydet", bg="#4CAF50", fg="white", command=kaydet).pack(pady=10)

def giris_yap():
    ad = giris_kullanici.get()
    sif = giris_sifre.get()
    with open(KULLANICI_DOSYA, "r") as f:
        kullanicilar = json.load(f)
    if kullanicilar.get(ad) == sif:
        messagebox.showinfo("Giriş Başarılı", f"Hoş geldin {ad}!")
        # sohbet_ekrani() yerine başka bir ekran açılabilir
    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

pencere = tk.Tk()
pencere.title("Giriş Ekranı")
pencere.geometry("400x350")
pencere.configure(bg="#e0e0e0")

# Başlık
tk.Label(pencere, text="Hoş Geldiniz", font=("Helvetica", 18, "bold"), bg="#e0e0e0").pack(pady=20)

# Form Alanı
form_frame = tk.Frame(pencere, bg="#e0e0e0")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Kullanıcı Adı:", bg="#e0e0e0").grid(row=0, column=0, pady=10, sticky="e")
giris_kullanici = tk.Entry(form_frame, width=30, bd=2, relief="groove")
giris_kullanici.grid(row=0, column=1, pady=10)

tk.Label(form_frame, text="Şifre:", bg="#e0e0e0").grid(row=1, column=0, pady=10, sticky="e")
giris_sifre = tk.Entry(form_frame, show="*", width=30, bd=2, relief="groove")
giris_sifre.grid(row=1, column=1, pady=10)

# Butonlar
buton_frame = tk.Frame(pencere, bg="#e0e0e0")
buton_frame.pack(pady=20)

tk.Button(buton_frame, text="Giriş Yap", width=15, bg="#1976D2", fg="white", command=giris_yap).pack(pady=5)
tk.Button(buton_frame, text="Kayıt Ol", width=15, bg="#388E3C", fg="white", command=kayit_ol).pack(pady=5)
tk.Button(buton_frame, text="Şifremi Unuttum", width=15, bg="#F57C00", fg="white",
          command=lambda: messagebox.showinfo("Bilgi", "Bu özellik yakında eklenecek.")).pack(pady=5)

pencere.mainloop()
