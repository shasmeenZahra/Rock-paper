import streamlit as st
import random

st.title("✊ Rock, 📄 Paper, ✂️ Scissors Game!")
st.write("Play against the computer and see who wins!")

# Choices
choices = ["Rock", "Paper", "Scissors"]
emojis = {"Rock": "✊", "Paper": "📄", "Scissors": "✂️"}

# Initialize session state for scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
    st.session_state.computer_score = 0

# User selection
user_choice = st.radio("Choose your move:", choices, horizontal=True)

# Play button
if st.button("🎮 Play"):
    computer_choice = random.choice(choices)  # Computer randomly selects

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Draw! 🤝"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "🎉 You Win!"
        st.session_state.user_score += 1
    else:
        result = "😢 Computer Wins!"
        st.session_state.computer_score += 1

    # Show choices and result
    st.subheader(f"You chose: {emojis[user_choice]}   |   Computer chose: {emojis[computer_choice]}")
    st.success(result)

# Scoreboard
st.sidebar.header("📊 Scoreboard")
st.sidebar.write(f"🧑 Your Score: {st.session_state.user_score}")
st.sidebar.write(f"🤖 Computer Score: {st.session_state.computer_score}")

# Reset button
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.rerun()
