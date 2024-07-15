import streamlit as st
from itertools import permutations

def solve_cryptarithm(words, result):
    unique_letters = set(''.join(words) + result)
    if len(unique_letters) > 10:
        return None  # Tidak mungkin ada solusi karena hanya ada 10 digit (0-9)

    for perm in permutations('0123456789', len(unique_letters)):
        trans = str.maketrans(''.join(unique_letters), ''.join(perm))
        if all(word[0].translate(trans) != '0' for word in words + [result]):
            if sum(int(word.translate(trans)) for word in words) == int(result.translate(trans)):
                return {letter: digit for letter, digit in zip(unique_letters, perm)}

    return None

def main():
    st.title("Cryptarithm Solver")

    st.write("""
    Masukkan cryptarithm yang ingin Anda selesaikan. Misalnya:
    - SEND + MORE = MONEY
    """)

    words = st.text_input("Masukkan kata-kata (dipisahkan dengan spasi):", value="SEND MORE")
    result = st.text_input("Masukkan hasil:", value="MONEY")

    if st.button("Solve"):
        words_list = words.upper().split()
        result_word = result.upper()

        solution = solve_cryptarithm(words_list, result_word)
        if solution:
            st.write("Solusi ditemukan:")
            st.write(solution)
        else:
            st.write("Tidak ada solusi yang ditemukan.")

if __name__ == "__main__":
    main()
