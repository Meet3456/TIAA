import streamlit as st
import requests
import folium
from streamlit_folium import folium_static
import pandas as pd
import json
from streamlit_lottie import st_lottie

api_key = '8b48d602daee4aa98c1e47f03b228e50'
st.set_page_config(
    page_title="Nearme Explorer",
    page_icon=":map:",
    layout="wide",
    initial_sidebar_state="expanded"

)
def load_lottiefile(filepath: str):
    with open(filepath, "r") as file:
        return json.load(file)
def get_coordinates(location):
    base_url = 'https://api.opencagedata.com/geocode/v1/json'
    params = {
        'q': location,
        'key': api_key,
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['results']:
        lat = data['results'][0]['geometry']['lat']
        lon = data['results'][0]['geometry']['lng']
        return lat, lon
    else:
        return None

def get_nearby_places(location, category):
    coordinates = get_coordinates(location)
    if coordinates:
        lat, lon = coordinates
        places_url = 'https://api.opencagedata.com/geocode/v1/json'
        places_params = {
            'q': f'{category} in {location}',
            'key': api_key,
            'language': 'en',  # Language for results
            'limit': 15,  # Adjust the limit based on the number of places you want
            'radius': 10000,
        }
        places_response = requests.get(places_url, params=places_params)
        places_data = places_response.json()
        return places_data.get('results', [])
    else:
        return []

def main():
    c1,c2 = st.columns([3.5, 1])
    with c1:
        st.header('NearMe Explorer!')

        # Sidebar for user input and fetched location details
        location = st.text_input(':blue[Enter your location:]')
        selected_category = st.selectbox(':blue[Select nearby places category:]', 
                                          ['Yoga/Meditation centers', 'Gymkhanas', 'Parks/Sports Grounds','Gardens',
                                           'Medicals', 'Hospitals', 'Dentists', 'Eye care centers', 'Doctors'])

        st.header(f"Nearby {selected_category}")

        if location:
            # Display the map centered at the user's location
            coordinates = get_coordinates(location)
            if coordinates:
                map_center = coordinates

                # Create a folium map
                m = folium.Map(location=map_center, zoom_start=13)

                # Display nearby places based on the selected category on the map
                category_mapping = {
                    'Yoga/Meditation centers': 'yoga',
                    'Gymkhanas': 'gym',
                    'Parks/Sports Grounds': 'park',
                    'Gardens':'garden',
                    'Medicals': 'medical',
                    'Hospitals': 'hospital',
                    'Dentists': 'dentist',
                    'Eye care centers': 'Eyecare centers',
                    'Doctors': 'doctor',
                }
                selected_category_lower = category_mapping[selected_category]
                nearby_places = get_nearby_places(location, selected_category_lower)
                for place in nearby_places:
                    folium.Marker(
                        location=[place['geometry']['lat'], place['geometry']['lng']],
                        popup=f"{place['formatted']} \n Address: {place['formatted']}",
                        icon=folium.Icon(color='blue', icon='info-sign')
                    ).add_to(m)

                # Display the map in the Streamlit app
                folium_static(m)

                # Display the details of fetched locations on the main screen
                for index, row in pd.DataFrame(nearby_places).iterrows():
                    st.subheader(row['formatted'])
                    st.write(f"Latitude: {row['geometry']['lat']}, Longitude: {row['geometry']['lng']}")
                    st.write(f"Address: {row['formatted']}")
                    st.write('---')

    with c2:
        st.header("About")

        subheader_text = f'<span style="color: blue; font-size:18px">Explore All the essential Places nearby you in Just 2 Clicks!!</span>'
        st.markdown(subheader_text, unsafe_allow_html=True)

        lottie1 = load_lottiefile('assets/Animation-maps.json')
        st_lottie(lottie1, key="hello1")

    st.sidebar.header(':blue[Welcome Retirees!]')
    st.sidebar.write("Explore nearby places and find easy way to access different locations for a healthy retirement.")

    # Display an image in the sidebar
    iframe_code = '<iframe src="https://lottie.host/?file=65d40f87-4500-498a-a5fb-721b170478b6/V36cmQjGI3.json"height="300" width="300"></iframe>'
    st.sidebar.markdown(iframe_code, unsafe_allow_html=True)
    # Useful links for retirees
    st.sidebar.header(':blue[Useful Links]')
  
    # Retirement Planning
    st.sidebar.markdown('**Retirement Planning**')
    st.sidebar.markdown('[Kiplinger - Retirement](https://www.kiplinger.com/retirement)')
    st.sidebar.markdown('[Vanguard - Retirement Savings Calculator](https://retirementplans.vanguard.com/)')
    st.sidebar.markdown('[Government Senior Citizen Portal](https://www.seniorcitizen.gov.in/)')
    # Social Interaction
    st.sidebar.markdown('**Social Interaction**')
    st.sidebar.markdown('[Meetup - Find and build local communities](https://www.meetup.com/)')

    # Physical and Mental Health
    st.sidebar.markdown('**Physical and Mental Health**')
    st.sidebar.markdown('[National Institute on Aging - Healthy Aging Tips](https://www.nia.nih.gov/news-events/nia-news/2020/07/tips-staying-healthy-older-adults-during-covid-19-pandemic)')
    st.sidebar.markdown('[SeniorAdvice.com - Senior Living](https://www.senioradvice.com/)')

    # Schemes/Policies
    st.sidebar.markdown('**Schemes/Policies**')
    st.sidebar.markdown('[Medicare - Official U.S. Government Site](https://www.medicare.gov/)')


    footer = """
    <style>
        .footer {
            width: 100%;
            background-color: #d4cbb1;
            padding: 10px;
            text-align: center;
            color: black;
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
        }
    </style>
    <div class="footer">
        <p>© 2023 Stock-Bot. All rights reserved.</p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
if __name__ == '__main__':
    main()
