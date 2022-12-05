#!/usr/bin/env python
# coding: utf-8

# In[4]:


import streamlit as st
from pytube import YouTube
from streamlit.widgets.directory_picker import directory_picker

st.title("Descargador de videos de YouTube")
st.markdown("Ingresa la URL del video que deseas descargar, selecciona la resolución que deseas y elige la ubicación donde lo quieres guardar.")

url = st.text_input("URL del video")

yt = YouTube(url)
resolutions = yt.streams.filter(progressive=True).order_by("resolution").desc()

selected_resolution = st.selectbox("Selecciona la resolución:", [(f"{r.resolution} ({r.filesize / 1e6:.2f} MB)", r) for r in resolutions])
download_dir = st.directory_picker("Elige el directorio de descarga:")

if st.button("Descargar"):
    selected_resolution.download(download_dir)

