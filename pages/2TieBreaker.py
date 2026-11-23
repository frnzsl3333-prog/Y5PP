


import random
import streamlit as st

st.title("🎉LET'S HAVE FUN -🐰 BUNNY, 🥕CARROT, 🔫GUN 🎉")

options = ["Bunny", "Carrot", "Gun"]


def show_result(title, message, color, emoji, player_choice, computer_choice):
  st.markdown(
    f"""
    <div style="background: linear-gradient(135deg, {color}, #fff); border: 3px solid {color};
                border-radius: 16px; padding: 18px; margin: 12px 0;
                box-shadow: 0 4px 12px #0002;">
      <div style="font-size: 2rem;">{emoji}</div>
      <h2 style="margin: 4px 0; color: #222;">{title}</h2>
      <p style="font-size: 1.1rem; margin-bottom: 0; color: #333;">{message}</p>
      <p style="font-size: 1rem; margin-bottom: 0; color: #333;">
        Your Choice: <strong>{player_choice}</strong><br>
        Computer Choice: <strong>{computer_choice}</strong>
      </p>
    </div>
    """,
    unsafe_allow_html=True,
  )

st.write(
  "Get ready for a silly showdown! Choose Bunny, Carrot or Gun. "
  "Bunny beats Carrot, Carrot beats Gun, and Gun beats Bunny. "
  "Good luck, champion! 🌟"
)

# Use a dropdown so the player can choose without typing.
player_input = st.selectbox("Bunny, Carrot, Gun:", options)

if st.button("Play"):
  if player_input:
    player = player_input.lower().strip()
    computer = random.choice(options).lower().strip()

    if player == computer:
      show_result("It's a tie!", "Great minds think alike! 😄", "#ffe066", "🤝", player.title(), computer.title())
    elif player == "bunny" and computer == "carrot":
      show_result("You win!", "Your Bunny hopped to victory! 🏆", "#8ce99a", "🐰", player.title(), computer.title())
    elif player == "gun" and computer == "bunny":
      show_result("You win!", "You beat the Bunny! The human wins! 🎉", "#8ce99a", "🎉", player.title(), computer.title())
    elif player == "carrot" and computer == "gun":
      show_result("You win!", "Your Carrot wins! Amazing job! 🏆", "#8ce99a", "🥕", player.title(), computer.title())
    elif player != "carrot" and player != "bunny" and player != "gun":
      show_result("Try again!", "That choice is a little wonky.", "#ffd8a8", "🤔", player.title(), computer.title())
    else:
      show_result(
        "Computer wins!",
        "Better luck next time, superstar! 💪",
        "#ffa8a8",
        "🤖",
        player.title(),
        computer.title(),
      )
  else:
    st.write("👇 Pick your champion above and let's play!")