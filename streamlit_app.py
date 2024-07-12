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
    st.success(f"Luas Segitiganya Adalah {luas}")
    st.balloons()

st.write('Aplikasi ini menghitung tekanan hidrostatis di dalam fluida.')

h = st.number_input('Kedalaman Fluida (meter)', min_value=0.0, step=0.1, format="%.2f")
rho = st.number_input('Massa Jenis Fluida (kg/m^3)', min_value=0.0, step=1.0, format="%.1f")
g = st.number_input('Percepatan Gravitasi (m/s^2)', min_value=0.0, step=1.0, format="%.1f", value=9.81)
hitungtekanan = st.button("Hitung Tekanan")

if hitungtekanan:
    tekanan = rho * g * h
    st.write(f'Tekanan Hidrostatis = {tekanan:.2f} Pascal')

