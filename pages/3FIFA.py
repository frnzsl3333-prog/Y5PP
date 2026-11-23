


import random
import streamlit as st


st.set_page_config(page_title="FIFA Fun Match", page_icon="⚽")
st.title("⚽🎉 FIFA Fun Match! 🎉⚽")
st.markdown("### Pick your nation, choose the opposition, and play for fun! 📣")

fifa_teams = {
    "Algeria": "🇩🇿",
    "Argentina": "🇦🇷",
    "Australia": "🇦🇺",
    "Austria": "🇦🇹",
    "Belgium": "🇧🇪",
    "Bosnia and Herzegovina": "🇧🇦",
    "Brazil": "🇧🇷",
    "Cabo Verde": "🇨🇻",
    "Canada": "🇨🇦",
    "Colombia": "🇨🇴",
    "Congo DR": "🇨🇩",
    "Côte d'Ivoire": "🇨🇮",
    "Croatia": "🇭🇷",
    "Curaçao": "🇨🇼",
    "Czechia": "🇨🇿",
    "Ecuador": "🇪🇨",
    "Egypt": "🇪🇬",
    "England": "🏴",
    "France": "🇫🇷",
    "Germany": "🇩🇪",
    "Ghana": "🇬🇭",
    "Haiti": "🇭🇹",
    "Iran": "🇮🇷",
    "Iraq": "🇮🇶",
    "Japan": "🇯🇵",
    "Jordan": "🇯🇴",
    "Korea Republic": "🇰🇷",
    "Mexico": "🇲🇽",
    "Morocco": "🇲🇦",
    "Netherlands": "🇳🇱",
    "New Zealand": "🇳🇿",
    "Norway": "🇳🇴",
    "Panama": "🇵🇦",
    "Paraguay": "🇵🇾",
    "Portugal": "🇵🇹",
    "Qatar": "🇶🇦",
    "Saudi Arabia": "🇸🇦",
    "Scotland": "🏴",
    "Senegal": "🇸🇳",
    "South Africa": "🇿🇦",
    "Spain": "🇪🇸",
    "Sweden": "🇸🇪",
    "Switzerland": "🇨🇭",
    "Tunisia": "🇹🇳",
    "Türkiye": "🇹🇷",
    "Uruguay": "🇺🇾",
    "USA": "🇺🇸",
    "Uzbekistan": "🇺🇿",
}

with st.sidebar:
    st.header("FIFA match settings")
    supported_team = st.selectbox("Choose your team", list(fifa_teams))
    opponent_options = [team for team in fifa_teams if team != supported_team]
    opponent_team = st.selectbox("Choose the opposition", opponent_options)
    match_mode = st.selectbox("Match mode", ["Friendly", "World Cup", "Legend"])
    kick_off = st.button("▶️ Kick off!", type="primary", use_container_width=True)

st.info(
    f"{fifa_teams[supported_team]} {supported_team} vs "
    f"{fifa_teams[opponent_team]} {opponent_team} — {match_mode}"
)

if kick_off:
    teams = [supported_team, opponent_team]
    goal_chances = {"Friendly": 0.22, "World Cup": 0.18, "Legend": 0.28}
    goal_chance = goal_chances[match_mode]
    commentary = [
        "A composed passing move builds through midfield.",
        "A quick counter-attack puts the defence under pressure.",
        "The goalkeeper makes an excellent reaction save.",
        "The crowd responds as the tempo rises.",
        "A well-timed dribble creates space in the final third.",
        "The effort narrowly misses the target.",
        "The delivery from the corner causes a dangerous moment.",
        "A sharp one-two opens up a path toward goal.",
        "The midfielder switches play with a precise long pass.",
        "A defender steps in to make a timely interception.",
        "The winger cuts inside and tests the defence.",
        "A clever through ball sends a runner into space.",
        "The back line holds firm under pressure.",
        "A free kick finds its way into the penalty area.",
        "Both sides battle for control in the middle of the pitch.",
        "The keeper claims the cross confidently.",
        "A late run gives the attack another option.",
        "The referee signals advantage as play continues.",
    ]

    st.markdown(f"Your team: **{fifa_teams[supported_team]} {supported_team}**")
    score = {team: 0 for team in teams}
    events = []

    for minute in range(10, 91, 10):
        team = random.choice(teams)
        action = random.choice(commentary)
        event = f"⏱️ {minute}' — {fifa_teams[team]} **{team}:** {action}"

        if random.random() < goal_chance:
            score[team] += 1
            event += f"\n\n🥅 **GOAL!** What a fantastic shot for {team}! 🎉"

        events.append(event)

    st.markdown("## 🏟️ Full-time scoreboard")
    left, middle, right = st.columns([2, 1, 2])

    with left:
        st.metric(f"{fifa_teams[supported_team]} {supported_team}", score[supported_team])
    with middle:
        st.markdown("<h1 style='text-align: center; padding-top: 12px;'>⚽</h1>", unsafe_allow_html=True)
    with right:
        st.metric(f"{fifa_teams[opponent_team]} {opponent_team}", score[opponent_team])

    if score[supported_team] > score[opponent_team]:
        st.success(f"🏆 {supported_team} wins! Great game, everyone!")
        st.balloons()
    elif score[supported_team] == score[opponent_team]:
        st.success("🤝 It's a draw! Both teams played brilliantly!")
    else:
        st.info(f"🏆 {opponent_team} wins this match!")

    st.markdown("### 🎙️ Match highlights")
    for event in events:
        st.markdown(event)

    st.caption("Thanks for watching—and remember, having fun is the real win! 🌟")