import streamlit as st

st.title("🎈 Web Penghitung Alas Segitiga")
st.write(
    "Test doang Njir,arelnya lagi gabut"
)

alas = st.number_input("Masukan Alas", 0)
tinggi = st.number_input("Masukan Tinggi", 0)
hitung = st.button("Hitung Luas")

if hitung:
    luas = 0.5 * alas * tinggi
    st.write("Luas Segitiganya Adalah", luas)
