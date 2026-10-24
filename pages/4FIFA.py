

import contextlib
import io
import random

import streamlit as st


st.title("⚽ FIFA Match Simulator")
st.caption("Simulate a match and follow the action from kickoff to full time.")

if st.button("Start Match"):
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        print("  Welcome to another game of FIFA, make your final bets now or never!")

        events = ["Pass completed successfully!", "He got skilled, that must have been ambarrasing for him!", "Penalty!", "This is FIFA at the peakest!", "That is what you call football!", "Foul committed and that might be a yellow card!", "Shot at goal but missed", "He scored!", "Out!"]

        print("                           Match Kickoff!                           ")

        for minute in range(10,90,10):
            event = random.choice(events)
            print(f"Minute {minute}': {event}")

        home_goals = 0
        away_goals = 0

        def take_shot(team_name):
            global home_goals, away_goals

            outcomes = ["GOAL!", "Just Missed!", "Saved by the Keeper!", "That was nowhere near the goal!"]
            result = random.choice(outcomes)
            print(f"{team_name} takes a shot... {result}")

            if result =="GOAl!":
                if team_name == "Norway":
                    home_goals += 1
                else:
                        away_goals += 1

        for attack in range(1,5):
            take_shot("Norway")
            take_shot("Brazil")

        print("\n--- FINAL SCORE ---")
        print(f"Norway {home_goals} - {away_goals} Brazil")

        #Player Rating (Out of 99 like FIFA)
        stiker_shooting = 98
        defender_defence = 96

        print(f"1v1 Situation! Striker Shooting: {stiker_shooting} vs Defender: {defender_defence}")

        striker_score = stiker_shooting + random.randint(1,15)
        defender_score = defender_defence + random.randint(1,15)

        if striker_score > defender_score:
            print("the striker skills the defender and SCORES a GOAL!")
        else:
            print("Amazing tackle! The defender will be on less pressure now!")

        team_a = "Norway"
        team_b = "Brazil"

        team_a_score = 0
        team_b_score = 0

        commentary = [
            "great team passing in midfield.",
            "a dangerous counter-attack!",
            "a long distance power shot!",
            "a quick corner kick into the box."
        ]

        print(f"=== FIFA MATCH: {team_a} vs {team_b} ===\n")

        for minute in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            atacking_team = random.choice([team_a, team_b])
            action = random.choice(commentary)
            print(f"Minute {minute}': {atacking_team} with {action}")

            if random.random() < 0.30:
                if atacking_team == team_a:
                    team_a_score += 1
            else:
                team_b_score += 1
            print(f"⚽ GOAL for {atacking_team}! Current Score: {team_a} {team_a_score} - {team_b_score} {team_b}")

            print("   -> Defence clears the danger!")
            print()
        print("====================================")
        print(f"FULL TIME RESULT: {team_a} {team_a_score} - {team_b_score} {team_b}")
        print("====================================")

    match_output = output.getvalue()
    final_result = next(
        (line.removeprefix("FULL TIME RESULT: ") for line in match_output.splitlines()
         if line.startswith("FULL TIME RESULT:")),
        "Final result unavailable",
    )

    st.subheader("🏁 Full-time score")
    st.success(final_result)

    with st.expander("Match events and commentary", expanded=True):
        st.text(match_output)