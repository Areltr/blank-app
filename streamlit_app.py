import streamlit as st

st.title("⚙️ Tools Penghitung Luas Segitiga")
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

st.title("⚙️ Tools Penghitung Tekanan Hidrostatis")
st.write("Aku males ngitung")

h = st.number_input('Kedalaman Fluida (meter)', min_value=0.0, step=0.1, format="%.2f")
rho = st.number_input('Massa Jenis Fluida (kg/m^3)', min_value=0.0, step=1.0, format="%.1f")
g = st.number_input('Percepatan Gravitasi (m/s^2)', min_value=0.0, step=1.0, format="%.1f", value=9.81)
hitungtekanan = st.button("Hitung Tekanan")

if hitungtekanan:
    tekanan = rho * g * h
    st.write(f'Tekanan Hidrostatis = {tekanan:.2f} Pascal')

st.title("⚙️ Tools Mencari kedalaman Tekanan Hidrostatis")
st.write("Aku males ngitung")

p = st.number_input('Tekanan Hidrostatis', min_value=0.0, step=0.1, format="%.2f")
kerapatan = st.number_input('Kerapatan Fluida (kg/m^3)', min_value=0.0, step=1.0, format="%.1f")
g1 = st.number_input('Percepatan gravitasi (m/s^2)', min_value=0.0, step=1.0, format="%.1f", value=9.81)
hitungh = st.button("Hitung Kedalaman")

if hitungh:
    tekanan = p / (kerapatan * g1)
    st.write(f'Kedalaman Fluida = {tekanan:.2f} ')

st.set_page_config(
    page_title="apalah",
    page_icon="⚙️",
)
st.sidebar.success("test")
st.title("pp")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.set_option('deprecation.showfileUploaderEncoding', False)
