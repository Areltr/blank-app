import streamlit as st

def main():
    st.title("Kalkulator Dinamis")
    st.write("""
    - Tambah =  +
    - Kurang =  -
    - Kali   =  *
    - Bagi.  =  /
    """)

    # Input ekspresi matematika
    expression = st.text_input("Masukkan ekspresi matematika:")

    # Tombol untuk menghitung hasil
    if st.button("Hitung"):
        try:
            # Evaluasi ekspresi matematika
            result = eval(expression)
            st.success(f"Hasil: {result}")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
