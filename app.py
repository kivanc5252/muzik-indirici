import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Müzik İndirici", layout="centered")
st.title("🎵 Müzik İndirici")

sarki = st.text_input("Şarkı adı yazın:")

if st.button("İndir"):
    if sarki:
        with st.spinner("Hazırlanıyor..."):
            try:
                opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}],
                    'outtmpl': 'muzik.mp3',
                    'default_search': 'ytsearch1',
                }
                with yt_dlp.YoutubeDL(opts) as ydl:
                    ydl.download([sarki])
                
                with open("muzik.mp3", "rb") as f:
                    st.audio(f.read(), format="audio/mp3")
                    st.download_button("📥 MP3'ü Kaydet", f, file_name=f"{sarki}.mp3")
                os.remove("muzik.mp3")
            except Exception as e:
                st.error(f"Hata: {e}")
