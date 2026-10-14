# --- Import required libraries ---
import streamlit as st
import random
import time
import pandas as pd
import altair as alt

# --- Page Title ---
st.title("🏈 Fried Night Footy Match Simulator")
st.caption("A Year 5 Passion Project Game")

# --- NRL Team List (Includes PNG Chiefs) ---
nrl_teams = [
    "PNG Chiefs",
    "Penrith Panthers",
    "Brisbane Broncos",
    "Melbourne Storm",
    "Sydney Roosters",
    "South Sydney Rabbitohs",
    "Parramatta Eels",
    "Manly Sea Eagles",
    "Cronulla Sharks",
    "Canterbury Bulldogs",
    "North Queensland Cowboys",
    "Dolphins",
    "Canberra Raiders",
    "Newcastle Knights",
    "Gold Coast Titans",
    "St George Illawarra Dragons",
    "Wests Tigers",
    "New Zealand Warriors"
]

# --- Sidebar Match Options ---
st.sidebar.header("Match Settings")

# Dropdowns to pick Home and Away teams
team1 = st.sidebar.selectbox("Home Team:", nrl_teams, index=0) # Defaults to PNG Chiefs
team2_options = [t for t in nrl_teams if t != team1]
team2 = st.sidebar.selectbox("Away Team:", team2_options, index=0)

# Game length setting
sets_per_half = st.sidebar.slider("Number of Sets per Half:", 5, 20, 8)

# Kickoff Button
start_button = st.sidebar.button("🏉 Start Match!")

# --- Main Scoreboard Area ---
score_display = st.empty()

if start_button:
    final_scores = {team1: 0, team2: 0}
    final_tries = {team1: 0, team2: 0}

    def update_scoreboard(current_half, attacking_team, commentary):
        """Display the stadium scoreboard screen."""
        scoreboard_html = f"""
        <div style='background-color:#003366; color:white; padding:20px; border-radius:12px; text-align:center;'>
            <h3 style='margin:0; color:#ffd700;'>Friday Night Footy - Half {current_half}</h3>
            <h1 style='margin:10px 0; font-size:42px; color:#ffffff;'>
                <b>{team1}: {final_scores[team1]}</b> &nbsp;|&nbsp; <b>{team2}: {final_scores[team2]}</b>
            </h1>
            <p style='margin:0; font-size:18px; color:#a2d2ff;'>
                <b>Attacking:</b> {attacking_team} | <b>Commentary:</b> {commentary}
            </p>
        </div>
        """
        score_display.markdown(scoreboard_html, unsafe_allow_html=True)

    def play_half(half_num):
        """Simulate one half of play for both teams."""
        t1_history, t2_history = [], []

        for _ in range(sets_per_half):
            # --- Team 1 Attack ---
            event1 = random.choices(["Tackled", "Try!", "Field Goal", "Knock On"], weights=[60, 20, 5, 15])[0]
            pts1 = 0

            if event1 == "Try!":
                pts1 = 4
                commentary1 = f"TRY! {team1} cross the line! (+4)"
                # Conversion attempt (+2 points)
                if random.choice([True, False]):
                    pts1 += 2
                    commentary1 += " & Kicked Conversion! (+2)"
                else:
                    commentary1 += " (Conversion missed)"
                final_tries[team1] += 1

            elif event1 == "Field Goal":
                pts1 = 1
                commentary1 = f"FIELD GOAL! {team1} slots 1 point!"

            elif event1 == "Knock On":
                pts1 = 0
                commentary1 = f"Knock on by {team1}! Turnover ball."

            else:
                pts1 = 0
                commentary1 = f"Tackled! Good defense against {team1}."

            final_scores[team1] += pts1
            t1_history.append(final_scores[team1])
            update_scoreboard(half_num, team1, commentary1)
            time.sleep(0.3)

            # --- Team 2 Attack ---
            event2 = random.choices(["Tackled", "Try!", "Field Goal", "Knock On"], weights=[60, 20, 5, 15])[0]
            pts2 = 0

            if event2 == "Try!":
                pts2 = 4
                commentary2 = f"TRY! {team2} score a great try! (+4)"
                if random.choice([True, False]):
                    pts2 += 2
                    commentary2 += " & Kicked Conversion! (+2)"
                else:
                    commentary2 += " (Conversion missed)"
                final_tries[team2] += 1

            elif event2 == "Field Goal":
                pts2 = 1
                commentary2 = f"FIELD GOAL! {team2} scores 1 point!"

            elif event2 == "Knock On":
                pts2 = 0
                commentary2 = f"Knock on by {team2}! Lost possession."

            else:
                pts2 = 0
                commentary2 = f"Tackled! {team2} completed their set."

            final_scores[team2] += pts2
            t2_history.append(final_scores[team2])
            update_scoreboard(half_num, team2, commentary2)
            time.sleep(0.3)

        return t1_history, t2_history

    # --- Run Match (2 Halves) ---
    st.info("🔔 **First Half Kickoff!**")
    t1_h1, t2_h1 = play_half(1)

    st.info("⏸️ **Halftime Break!**")
    time.sleep(1)

    st.info("🔔 **Second Half Kickoff!**")
    t1_h2, t2_h2 = play_half(2)

    # Combine total points history
    t1_all = t1_h1 + t1_h2
    t2_all = t2_h1 + t2_h2

    update_scoreboard("FULL TIME", "Match Over", "Final Siren Has Blown!")
    st.write("---")

    # --- Match Results & Winner ---
    if final_scores[team1] > final_scores[team2]:
        st.markdown(f"<h1 style='color:#38b000; text-align:center;'>🏆 {team1} WINS THE MATCH! 🏆</h1>", unsafe_allow_html=True)
    elif final_scores[team2] > final_scores[team1]:
        st.markdown(f"<h1 style='color:#38b000; text-align:center;'>🏆 {team2} WINS THE MATCH! 🏆</h1>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h1 style='color:#ffb703; text-align:center;'>🤝 IT'S A TIE! GO TO THE TIEBREAKER PAGE!</h1>", unsafe_allow_html=True)

    # --- Summary Stats ---
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label=f"{team1} Final Score", value=final_scores[team1], delta=f"{final_tries[team1]} Tries")
    with col2:
        st.metric(label=f"{team2} Final Score", value=final_scores[team2], delta=f"{final_tries[team2]} Tries")

    # --- Line Graph: Score Progression ---
    st.subheader("📈 Score Progression Graph")
    sets_count = len(t1_all)
    df1 = pd.DataFrame({'Set Number': list(range(1, sets_count + 1)), 'Score': t1_all, 'Team': team1})
    df2 = pd.DataFrame({'Set Number': list(range(1, sets_count + 1)), 'Score': t2_all, 'Team': team2})
    df = pd.concat([df1, df2])

    line_chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X('Set Number:O', title='Attack Set Number'),
        y=alt.Y('Score:Q', title='Total Points'),
        color=alt.Color('Team', scale=alt.Scale(domain=[team1, team2], range=['#0077b6', '#d62828'])),
        tooltip=['Set Number', 'Score', 'Team']
    ).interactive()

    st.altair_chart(line_chart, use_container_width=True)