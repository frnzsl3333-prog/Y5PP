

# --- Import required libraries ---
import streamlit as st
import random
import time
import pandas as pd
import altair as alt
from pathlib import Path
import base64

# --- Page Background ---
script_folder = Path(__file__).resolve().parent
image_candidates = [script_folder / "NRL.jpg", script_folder.parent / "NRL.jpg"]
background_image = next((path for path in image_candidates if path.exists()), None)

if background_image:
    image_data = base64.b64encode(background_image.read_bytes()).decode()
    st.markdown(
        f"""
        <style>
        [data-stale="true"] {{
            display: none !important;
        }}
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, 0.82), rgba(255, 255, 255, 0.82)),
                              url("data:image/jpeg;base64,{image_data}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# --- Page Title ---

st.markdown(
    """
    <style>
    h1 {
        color: #000000 !important;
        font-size: 3.5rem !important;
        text-shadow: 2px 2px 5px #003366;
    }
    [data-testid="stCaptionContainer"] p {
        color: #003366 !important;
        font-size: 1.4rem !important;
        font-weight: 700;
        text-shadow: 1px 1px 4px rgba(255, 255, 255, 0.8);
    }
    h3 {
        color: #003366 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("🏈 Fried Night Footy")
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
team1 = st.sidebar.selectbox("Home Team:", nrl_teams, index=6) # Defaults to Parramatta Eels
team2_options = [t for t in nrl_teams if t != team1]
team2 = st.sidebar.selectbox("Away Team:", team2_options, index=1)

# Game length setting
sets_per_half = st.sidebar.slider("Sets per game:", 5, 20, 8)

# Start a fresh match on the button's rerun.
if st.sidebar.button("🏉 Start Match!"):

    # --- Main Scoreboard Area ---
    score_display = st.empty()
    commentary_display = st.empty()
    status_display = st.empty()

    final_scores = {team1: 0, team2: 0}
    final_tries = {team1: 0, team2: 0}
    final_conversions = {team1: 0, team2: 0}
    final_field_goals = {team1: 0, team2: 0}

    def update_scoreboard(current_half, attacking_team, commentary):
        """Display the stadium scoreboard screen."""
        period = "Full Time" if current_half == "FULL TIME" else f"Half {current_half}"
        
        scoreboard_html = f"""
<div style='background-color:#004e7a; color:#ffffff; -webkit-text-fill-color:#ffffff; padding:20px; border-radius:12px; text-align:center;'>
    <div style='margin:0; font-size:42px; font-weight:600; color:#ffffff !important; -webkit-text-fill-color:#ffffff !important;'>
        Friday Night Footy - {period}
    </div>
    <h1 style='margin:10px 0; font-size:42px; color:#ffffff; -webkit-text-fill-color:#ffffff;'>
        <b>{team1}: {final_scores[team1]}</b> &nbsp;|&nbsp; <b>{team2}: {final_scores[team2]}</b>
    </h1>
</div>
"""
        score_display.markdown(scoreboard_html, unsafe_allow_html=True)
        commentary_html = f"""
        <div style='background-color:#fff8dc; color:#222; padding:14px 18px; border-left:6px solid #e6a700; border-radius:8px; margin-top:10px; font-size:18px;'>
            <b>Attacking: {attacking_team}</b><br>{commentary}
        </div>
        """
        commentary_display.markdown(commentary_html, unsafe_allow_html=True)

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
                if random.choice([True, False]):
                    pts1 += 2
                    final_conversions[team1] += 1
                    commentary1 += " & Kicked Conversion! (+2)"
                else:
                    commentary1 += " (Conversion missed)"
                final_tries[team1] += 1

            elif event1 == "Field Goal":
                pts1 = 1
                final_field_goals[team1] += 1
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
                    final_conversions[team2] += 1
                    commentary2 += " & Kicked Conversion! (+2)"
                else:
                    commentary2 += " (Conversion missed)"
                final_tries[team2] += 1

            elif event2 == "Field Goal":
                pts2 = 1
                final_field_goals[team2] += 1
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
    status_display.info("🔔 **First Half Kickoff!**")
    t1_h1, t2_h1 = play_half(1)

    status_display.info("⏸️ **Halftime Break!**")
    time.sleep(1)

    status_display.info("🔔 **Second Half Kickoff!**")
    t1_h2, t2_h2 = play_half(2)

    # Combine total points history
    t1_all = t1_h1 + t1_h2
    t2_all = t2_h1 + t2_h2

    # --- WIPE LIVE CONTAINERS TO SAVE SPACE AT FULL TIME ---
    score_display.empty()
    commentary_display.empty()
    status_display.empty()

    # --- Side-by-Side Final Outcome Screen (Appears immediately at the top) ---
    score_difference = abs(final_scores[team1] - final_scores[team2])
    if final_scores[team1] > final_scores[team2]:
        result = f"🏆 {team1} SMASHED {team2}! 🏆" if score_difference > 20 else f"🏆 {team1} WINS THE MATCH! 🏆"
    elif final_scores[team2] > final_scores[team1]:
        result = f"🏆 {team2} SMASHED {team1}! 🏆" if score_difference > 20 else f"🏆 {team2} WINS THE MATCH! 🏆"
    else:
        result = f"🤝 IT'S A TIE! GO TO THE TIEBREAKER PAGE! 🤝"

    st.markdown(
        f"""
        <div style='background-color:#004e7a; padding:16px 20px; border-radius:12px; margin:12px 0; text-align:center;'>
            <h1 style='color:#ffffff; -webkit-text-fill-color:#ffffff; margin:0; text-shadow:1px 1px 3px #001a33;'>{result}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    # Side-by-side team breakdown columns
    st.markdown(
        """
        <style>
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {
            background-color: rgba(255, 255, 255, 0.97);
            border: 3px solid #003366;
            border-radius: 14px;
            padding: 14px;
            box-shadow: 0 4px 10px rgba(0, 51, 102, 0.18);
        }
        .fnf-team-name {
            background: #003366;
            color: #ffffff;
            border-radius: 8px;
            padding: 12px 10px;
            margin: 0 0 12px 0;
            text-align: center;
            font-size: 26px;
            font-weight: 800;
            line-height: 1.2;
        }
        .fnf-stats {
            background: #fff8dc;
            border: 2px solid #d59e00;
            border-radius: 10px;
            color: #102a43;
            padding: 14px;
            margin-top: 10px;
        }
        .fnf-final-score {
            color: #003366;
            font-size: 38px;
            font-weight: 900;
            text-align: center;
            margin: 8px 0;
        }
        .fnf-stat-line {
            color: #102a43;
            font-size: 20px;
            font-weight: 700;
            padding: 5px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    col_team1, col_team2 = st.columns(2)

    with col_team1:
        st.markdown(f"<div class='fnf-team-name'> {team1}</div>", unsafe_allow_html=True)
        if final_scores[team1] > final_scores[team2]:
            
            st.markdown("<div style='background:#28a745; color:#ffffff; border-radius:8px; padding:10px; font-size:26px; font-weight:800; text-align:center;'>🏆 MATCH WINNER</div>", unsafe_allow_html=True)
        elif final_scores[team1] < final_scores[team2]:
            st.markdown("<div style='background:#dc3545; color:#ffffff; border-radius:8px; padding:10px; font-size:26px; font-weight:800; text-align:center;'>🏅 RUNNER-UP</div>", unsafe_allow_html=True)
        else:
            st.warning("🤝 DRAW")

        st.markdown(
            f"""
            <div class='fnf-stats'>
                <div style='text-align:center; font-size:16px; font-weight:700; color:#003366;'>FINAL SCORE</div>
                <div class='fnf-final-score'>{final_scores[team1]}</div>
                <div class='fnf-stat-line'>🏉 Tries Scored: {final_tries[team1]}</div>
                <div class='fnf-stat-line'>🎯 Conversions: {final_conversions[team1]}</div>
                <div class='fnf-stat-line'>⚽ Field Goals: {final_field_goals[team1]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_team2:
        st.markdown(f"<div class='fnf-team-name'> {team2}</div>", unsafe_allow_html=True)
        if final_scores[team2] > final_scores[team1]:
            st.markdown("<div style='background:#28a745; color:#ffffff; border-radius:8px; padding:10px; font-size:26px; font-weight:800; text-align:center;'>🏆 MATCH WINNER</div>", unsafe_allow_html=True)
        elif final_scores[team2] < final_scores[team1]:
            st.markdown("<div style='background:#dc3545; color:#ffffff; border-radius:8px; padding:10px; font-size:26px; font-weight:800; text-align:center;'>🏅 RUNNER-UP</div>", unsafe_allow_html=True)
        else:
            st.warning("🤝 DRAW")

        st.markdown(
            f"""
            <div class='fnf-stats'>
                <div style='text-align:center; font-size:16px; font-weight:700; color:#003366;'>FINAL SCORE</div>
                <div class='fnf-final-score'>{final_scores[team2]}</div>
                <div class='fnf-stat-line'>🏉 Tries Scored: {final_tries[team2]}</div>
                <div class='fnf-stat-line'>🎯 Conversions: {final_conversions[team2]}</div>
                <div class='fnf-stat-line'>⚽ Field Goals: {final_field_goals[team2]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("---")

    # --- Match Statistics Table ---
    st.subheader("📋 Match Statistics")
    stats = pd.DataFrame(
        {
            "Team": [team1, team2],
            "Tries": [final_tries[team1], final_tries[team2]],
            "Conversions": [final_conversions[team1], final_conversions[team2]],
            "Field goals": [final_field_goals[team1], final_field_goals[team2]],
        }
    )
    st.dataframe(stats, hide_index=True, use_container_width=True)

    # --- Line Graph: Score Progression ---
    st.subheader("📈 Score Progression Graph")
    sets_count = len(t1_all)
    df1 = pd.DataFrame({'Set Number': list(range(1, sets_count + 1)), 'Score': t1_all, 'Team': team1})
    df2 = pd.DataFrame({'Set Number': list(range(1, sets_count + 1)), 'Score': t2_all, 'Team': team2})
    df = pd.concat([df1, df2])

    line_chart = alt.Chart(df).mark_line(point=True).encode(
        x=alt.X('Set Number:O', title='Attack Set Number'),
        y=alt.Y('Score:Q', title='Total Points'),
        color=alt.Color('Team', scale=alt.Scale(domain=[team1, team2], range=['#0077b6', "#dfa00c"])),
        tooltip=['Set Number', 'Score', 'Team']
    ).interactive()

    st.altair_chart(line_chart, use_container_width=True)