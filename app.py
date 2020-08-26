import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.title("Sales Prediction App")
st.subheader(
"""
This is a demo of a app which gives the predicted sales for different aspects such as consoles, ratings, publisher, category and many more. You will encounter it below.
""")
st.text("")

model = pickle.load(open("finalized_model.sav", 'rb'))
le = pickle.load(open("labelencoding.sav","rb"))

def get_prediction():
    data = {"CONSOLE":console,"YEAR":year, "CATEGORY":category, "PUBLISHER":publisher,"RATING":rating, "CRITIC_RATING":critic_rating, "USER_RATING":user_rating}
    df = pd.DataFrame(data, index=[0])
    objFeatures = df.select_dtypes(include="object").columns
    for feat in objFeatures:
        df[feat] = le.fit_transform(df[feat].astype(str))
    pred = model.predict(df)
    return pred[0]

def main():
    year = st.sidebar.selectbox(
        'Select Year',
        (1997,1998,1999,2000,2001,2002,2003,2004,2005,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019))
    st.write('**You selected:**', year)

    console = st.sidebar.selectbox(
        'Select Console',
        ('dc', 'wiiu', 'psv', 'ps', '3ds', 'xone', 'ps4', 'gba', 'gc', 'psp', 'ds', 'wii', 'x', 'pc', 'ps3', 'x360', 'ps2')
    )
    st.write('**You selected:**', console)

    category = st.sidebar.selectbox(
        'Select Category',
        ('puzzle', 'adventure', 'strategy', 'simulation', 'fighting', 'platform', 'misc', 'racing', 'role-playing', 'shooter', 'sports', 'action')
    )
    st.write('**You selected:**', category)

    publisher = st.sidebar.selectbox(
        'Select Publisher',
        ('Bethesda', 'Nippon', 'Ichi', 'Rising', 'Softworks', 'Deep', 'Silver', 'Acclaim', '505', 'Lucasarts', 'Star', 'Software', 'Disney', 'Codemasters', 'Eidos', 'Vivendi', 'Midway', 'Tecmo', 'Koei', 'Square', 'Enix', 'Capcom', 'Warner', 'Bros.', 'Atari', 'Microsoft', 'Game', 'Namco', 'Bandai', 'Konami', 'Digital', 'Studios', 'Sega', 'Take-Two', 'Computer', 'Sony', 'Thq', 'Nintendo', 'Ubisoft', 'Activision', 'Games', 'Interactive', 'Entertainment', 'Electronic', 'Arts')
    )
    st.write('**You selected:**', publisher)

    rating = st.sidebar.selectbox(
        'Select Rating',
        ('T', 'E', 'M', 'E10+', 'RP', 'K-A')
    )
    st.write('**You selected:**', rating)

    user_rating = st.sidebar.slider('Select User Rating', 0.0, 1.5, 0.05, 0.01)
    st.write('**You selected:**', user_rating)

    critic_rating = st.sidebar.slider('Select Critic Rating', 0.0, 10.0, 1.0, 1.0)
    st.write('**You selected:**', critic_rating)
    if st.button('Run Me!'):
        result = get_prediction()
        st.write('**Predicted Sales in Millions:**', result)

if __name__ == "__main__":
    main()