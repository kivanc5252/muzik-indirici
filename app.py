import tkinter as tk
from tkinter import messagebox
import yt_dlp
import threading

def mp3_indir(sarki_ismi, durum_etiketi):
    durum_etiketi.config(text="🔍 Aranıyor ve İndiriliyor...\nLütfen bekleyin.", fg="blue")
    
    ayarlar = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'default_search': 'ytsearch1',
    }

    try:
        with yt_dlp.YoutubeDL(ayarlar) as ydl:
            ydl.download([sarki_ismi])
            
        durum_etiketi.config(text="✅ İndirme Başarılı!", fg="green")
        messagebox.showinfo("Başarılı", f"'{sarki_ismi}' indirildi!")
    except Exception as hata:
        durum_etiketi.config(text="❌ Hata oluştu!", fg="red")
        messagebox.showerror("Hata", f"Sorun: {hata}")

def butona_tiklandi():
    sarki = giris_kutusu.get()
    
    if not sarki.strip():
        messagebox.showwarning("Uyarı", "Bir şarkı adı girin!")
        return
    
    # Değişken ismini 'indirme_thread' olarak düzelttik
    indirme_thread = threading.Thread(target=mp3_indir, args=(sarki, durum_etiketi))
    indirme_thread.start()

# --- Arayüz ---
pencere = tk.Tk()
pencere.title("Kolay MP3 İndirici")
pencere.geometry("450x250")
pencere.configure(bg="#2c3e50")

tk.Label(pencere, text="🎵 Şarkı İndirici", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white").pack(pady=15)
tk.Label(pencere, text="Şarkı adı yazın:", bg="#2c3e50", fg="white").pack()

giris_kutusu = tk.Entry(pencere, width=40, font=("Arial", 12))
giris_kutusu.pack(pady=5)

tk.Button(pencere, text="İNDİR", command=butona_tiklandi, bg="#27ae60", fg="white", width=20).pack(pady=10)

durum_etiketi = tk.Label(pencere, text="Hazır.", bg="#2c3e50", fg="white")
durum_etiketi.pack()

pencere.mainloop()
