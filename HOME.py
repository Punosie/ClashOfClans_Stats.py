import streamlit as st
from app import get_info
from constants import API

def main():
    # Set page title and configure layout
    st.set_page_config(page_title="Clash of Clans Player Info", layout="wide")

    # Set title and description
    st.title("Clash of Clans Player Info")
    st.markdown(
        "This app fetches information about Clash of Clans players based on their player ID."
    )

    # Input for player ID
    player_id = st.text_input("Enter player ID (without #):")

    if player_id:
        # Fetch player data
        data = get_info(player_id, API)

        if data:
            # Player Info section
            st.header("**Player Info**")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader("General Info")
                st.write(f"**Name:** {data['name']}")
                st.write(f"**Tag:** {data['tag']}")
                st.write(f"**Town Hall Level:** {data['townHallLevel']}")
                st.write(f"**Experience Level:** {data['expLevel']}")
                st.write(f"**Trophies:** {data['trophies']}")
                st.write(f"**Best Trophies:** {data['bestTrophies']}")
            with col2:
                st.subheader("Battle Info")
                st.write(f"**War Stars:** {data['warStars']}")
                st.write(f"**Attack Wins:** {data['attackWins']}")
                st.write(f"**Defense Wins:** {data['defenseWins']}")
                st.write(f"**Builder Hall Level:** {data['builderHallLevel']}")
                st.write(f"**Builder Base Trophies:** {data['builderBaseTrophies']}")
                st.write(f"**Best Builder Base Trophies:** {data['bestBuilderBaseTrophies']}")
                st.write(f"**Role:** {data['role']}")
                st.write(f"**War Preference:** {data['warPreference']}")
            with col3:
                st.subheader("Other Info")
                st.write(f"**Donations:** {data['donations']}")
                st.write(f"**Donations Received:** {data['donationsReceived']}")
                st.write(f"**Clan Capital Contributions:** {data['clanCapitalContributions']}")

            # Clan Info section
            st.header("Clan Info")
            st.write(f"**Clan Name:** {data['clan']['name']}")
            st.write(f"**Clan Tag:** {data['clan']['tag']}")
            st.write(f"**Clan Level:** {data['clan']['clanLevel']}")
            st.image(data['clan']['badgeUrls']['medium'], caption="Clan Badge")

        else:
            st.error("Failed to fetch player data. Please check the player ID and try again.")

if __name__ == "__main__":
    main()
