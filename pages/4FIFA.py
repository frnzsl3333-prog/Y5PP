import random

import streamlit as st


st.set_page_config(page_title="Football Fun Match", page_icon="⚽")
st.title("⚽🎉 Football Fun Match! 🎉⚽")
st.markdown("### Pick your seat, cheer loudly, and see what happens! 📣")
st.info("A friendly, just-for-fun match between Norway 🇳🇴 and Brazil 🇧🇷")

if st.button("▶️ Kick off!", type="primary", use_container_width=True):
    teams = ["Norway", "Brazil"]
    flags = {"Norway": "🇳🇴", "Brazil": "🇧🇷"}
    score = {team: 0 for team in teams}
    events = []

    commentary = [
        "Lovely passing across the pitch! 🤝",
        "What a speedy counter-attack! 💨",
        "A brilliant save by the goalkeeper! 🧤",
        "The crowd is cheering so loudly! 📣",
        "A clever little trick gets past a defender! ✨",
        "The shot goes just wide—so close! 😮",
        "A corner kick swings into the box! 🌀",
    ]

    for minute in range(10, 91, 10):
        team = random.choice(teams)
        action = random.choice(commentary)
        event = f"⏱️ {minute}' — {flags[team]} **{team}:** {action}"

        if random.random() < 0.22:
            score[team] += 1
            event += f"\n\n🥅 **GOAL!** What a fantastic shot for {team}! 🎉"

        events.append(event)

    st.markdown("## 🏟️ Full-time scoreboard")
    left, middle, right = st.columns([2, 1, 2])
    with left:
        st.metric(f"{flags['Norway']} Norway", score["Norway"])
    with middle:
        st.markdown("<h1 style='text-align: center; padding-top: 12px;'>⚽</h1>", unsafe_allow_html=True)
    with right:
        st.metric(f"{flags['Brazil']} Brazil", score["Brazil"])

    if score["Norway"] > score["Brazil"]:
        st.success("🏆 Norway wins! Great game, everyone!")
        st.balloons()
    elif score["Brazil"] > score["Norway"]:
        st.success("🏆 Brazil wins! Great game, everyone!")
        st.balloons()
    else:
        st.success("🤝 It's a draw! Both teams played brilliantly!")

    st.markdown("## 🎙️ Match highlights")
    for event in events:
        st.markdown(event)
    st.caption("Thanks for watching—and remember, having fun is the real win! 🌟")