

import random

import streamlit as st


TEAMS = ("Penrith Panthers", "Melbourne Storm")

EVENTS = [
    "Boom! Goodbye! He is absolute lightning!",
    "That is rugby league at its absolute best!",
    "He has stepped him like a schoolboy!",
    "That is a tough call from the referee.",
    "What a tackle! He has stopped him in his tracks!",
    "They need to earn the right to go wide.",
]


def simulate_match():
    scores = {team: 0 for team in TEAMS}
    commentary = []

    for minute in range(1, 81):
        if random.random() < 0.06:
            team = random.choice(TEAMS)
            scores[team] += 4
            commentary.append(
                f"**{minute}′ TRY!** {team} score! (+4 points)"
            )

            if random.random() < 0.65:
                scores[team] += 2
                commentary.append("Conversion successful! (+2 points)")
            else:
                commentary.append("The conversion attempt misses.")
        elif random.random() < 0.35:
            commentary.append(f"**{minute}′** {random.choice(EVENTS)}")

    return scores, commentary


st.title("🏉 Welcome to Friday Night Footy 🏉")
st.write("🎙️ The match is about to kick off. Five... four... three... two... one!")

if st.button("🏟️ Start match"):
    st.session_state.match = simulate_match()

if "match" in st.session_state:
    scores, commentary = st.session_state.match

    st.subheader("🏆 Final Score")
    st.markdown(
        f"**{TEAMS[0]} {scores[TEAMS[0]]} — "
        f"{scores[TEAMS[1]]} {TEAMS[1]}**"
    )

    st.subheader("🎙️ Match Commentary")
    for line in commentary:
        st.markdown(line)