import streamlit as st
from app import get_info
from constants import API

def main():
    st.title("Clash of Clans Player Info")

    player_id = st.text_input("Enter player ID (without #):")
    if player_id:
        data = get_info(player_id, API)
        if data:
            st.subheader("Player Info")
            st.write(f"Name: {data['name']}")
            st.write(f"Tag: {data['tag']}")
            st.write(f"Town Hall Level: {data['townHallLevel']}")
            st.write(f"Experience Level: {data['expLevel']}")
            st.write(f"Trophies: {data['trophies']}")
            st.write(f"Best Trophies: {data['bestTrophies']}")
            st.write(f"War Stars: {data['warStars']}")
            st.write(f"Attack Wins: {data['attackWins']}")
            st.write(f"Defense Wins: {data['defenseWins']}")
            st.write(f"Builder Hall Level: {data['builderHallLevel']}")
            st.write(f"Builder Base Trophies: {data['builderBaseTrophies']}")
            st.write(f"Best Builder Base Trophies: {data['bestBuilderBaseTrophies']}")
            st.write(f"Role: {data['role']}")
            st.write(f"War Preference: {data['warPreference']}")
            st.write(f"Donations: {data['donations']}")
            st.write(f"Donations Received: {data['donationsReceived']}")
            st.write(f"Clan Capital Contributions: {data['clanCapitalContributions']}")

            st.subheader("Clan Info")
            clan_info = data['clan']
            st.write(f"Clan Name: {clan_info['name']}")
            st.write(f"Clan Tag: {clan_info['tag']}")
            st.write(f"Clan Level: {clan_info['clanLevel']}")
            st.image(clan_info['badgeUrls']['medium'], caption="Clan Badge")

        else:
            st.error("Failed to fetch player data. Please check the player ID and try again.")

if __name__ == "__main__":
    main()
