import random
import streamlit as st

st.title("BUNNY, CARROT, GUN SHOWDOWN")

options = ["Bunny", "Carrot", "Gun"]

st.write(
    "Competitor, choose in your head 1 of these 3 words, Bunny, Carrot and Gun."
    " In this game,  Bunny wins over  Carrot, Carrot wins over gun and Gun wins"
    " over Bunny."
)

# Replacing input() with a Streamlit text input
player_input = st.text_input("Bunny, Carrot, Gun:")

if st.button("Play"):
  if player_input:
    player = player_input.lower().strip()
    computer = random.choice(options).lower().strip()

    st.write("Computer chose:" + computer)

    if player == computer:
      st.write("Tie!")
    elif player == "bunny" and computer == "carrot":
      st.write("Congratulations, you won")
    elif player == "gun" and computer == "bunny":
      st.write("And the winner is... the human")
    elif player == "carrot" and computer == "gun":
      st.write("We found a winner, you won")
    elif player != "carrot" and player != "bunny" and player != "gun":
      st.write("Invalid option")
    else:
      st.write("Such a L O S E R")
  else:
    st.write("Please type your choice above!")