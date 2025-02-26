import random
import streamlit as st

def choose_word():
    words = ["python", "hangman", "developer", "programming", "streamlit", "machine learning", "artificial intelligence", "data science", "web development", "mobile development"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

st.title("Hangman Game")

if "word" not in st.session_state:
    st.session_state.word = choose_word()
    st.session_state.guessed_letters = set()
    st.session_state.attempts = 6

st.write("Attempts left:", st.session_state.attempts)
st.write("Word:", display_word(st.session_state.word, st.session_state.guessed_letters))

guess = st.text_input("Guess a letter:", max_chars=1).lower()

if st.button("Submit"):
    if guess and guess.isalpha():
        if guess in st.session_state.guessed_letters:
            st.warning("You already guessed that letter!")
        else:
            st.session_state.guessed_letters.add(guess)
            if guess not in st.session_state.word:
                st.session_state.attempts -= 1
                st.error(f"Incorrect! You have {st.session_state.attempts} attempts left.")
            else:
                st.success("Correct guess!")
    else:
        st.error("Please enter a valid letter.")

if all(letter in st.session_state.guessed_letters for letter in st.session_state.word):
    st.success(f"Congratulations! You guessed the word: {st.session_state.word}")
    st.button("Play Again", on_click=lambda: st.session_state.clear())
elif st.session_state.attempts == 0:
    st.error(f"Game Over! The word was: {st.session_state.word}")
    st.button("Try Again", on_click=lambda: st.session_state.clear())
