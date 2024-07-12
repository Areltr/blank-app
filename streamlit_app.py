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

def hitung_tekanan(h, rho, g):
    tekanan = rho * g * h
    return tekanan

# Judul dan deskripsi aplikasi
st.title('Kalkulator Tekanan Hidrostatis')
st.write('Aplikasi ini menghitung tekanan hidrostatis di dalam fluida.')

# Input dari pengguna
h = st.number_input('Kedalaman Fluida (meter)', min_value=0.0, step=0.1, format="%.2f")
rho = st.number_input('Massa Jenis Fluida (kg/m^3)', min_value=0.0, step=1.0, format="%.1f")
g = st.number_input('Percepatan Gravitasi (m/s^2)', min_value=0.0, step=1.0, format="%.1f", value=9.81)

# Tombol untuk menghitung tekanan
if st.button('Hitung Tekanan'):
    tekanan = hitung_tekanan(h, rho, g)
    st.write(f'Tekanan Hidrostatis = {tekanan:.2f} Pascal')

