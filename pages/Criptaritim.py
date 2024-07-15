import streamlit as st
from itertools import permutations

def solve_cryptarithm(word1, word2, result):
    words = [word1, word2]
    unique_letters = set(''.join(words) + result)
    if len(unique_letters) > 10:
        return None  # Tidak mungkin ada solusi karena hanya ada 10 digit (0-9)

    for perm in permutations('0123456789', len(unique_letters)):
        trans = str.maketrans(''.join(unique_letters), ''.join(perm))
        if all(word[0].translate(trans) != '0' for word in words + [result]):
            if sum(int(word.translate(trans)) for word in words) == int(result.translate(trans)):
                solution = {letter: digit for letter, digit in zip(unique_letters, perm)}
                words_sum = ' + '.join(word.translate(trans) for word in words)
                result_value = result.translate(trans)
                return solution, words_sum, result_value

    return None, None, None

def main():
    st.title("Cryptarithm Solver")

    st.write("""
    Masukkan cryptarithm yang ingin Anda selesaikan. Misalnya:
    - SEND + MORE = MONEY
    """)

    word1 = st.text_input("Masukkan kata pertama:", value="SEND")
    word2 = st.text_input("Masukkan kata kedua:", value="MORE")
    result = st.text_input("Masukkan hasil:", value="MONEY")

    if st.button("Solve"):
        word1 = word1.upper()
        word2 = word2.upper()
        result_word = result.upper()

        solution, words_sum, result_value = solve_cryptarithm(word1, word2, result_word)
        if solution:
            st.write("Solusi ditemukan:")
            st.write(solution)
            st.write(f"{words_sum} = {result_value}")
        else:
            st.write("Tidak ada solusi yang ditemukan.")

if __name__ == "__main__":
    main()
              
