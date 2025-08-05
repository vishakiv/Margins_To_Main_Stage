import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio

#CSS styling
st.markdown(
    """
    <style>
    .title-section {
        background-color: #000000;
        padding: 2rem;
        text-align: center;
    }
    .title-section h1 {
        font-size: 2rem;
        color: #FDFBD4;
        font-family: 'Georgia', serif;
    }
    .title-section p {
        font-size: 1.2rem;
        color: #ffffff;
    }
    .heading {
        text-align:center;
        font-size: 26px;
        font-weight: bold;
    }
    .text {
        text-align: left;
        font-size: 22px;
    } 
    </style>
    """,
    unsafe_allow_html=True
)
# Title and introduction
st.markdown(
    """
    <div class="title-section">
        <h1>From Margins to Main Stage: <br>  The Rise of Women's Football</h1>
    </div>
    """,
    unsafe_allow_html=True,
)
st.image("assets/images/jamaica.png", caption="Jamaican Joy. Photograph: Anadolu Agency/Getty Images")

st.markdown("""
<div class="heading">
            Project Introduction
            </div>
            """,
             unsafe_allow_html=True,
)

st.markdown(
    """
<div class="text">
<br><br>
Everyone watches women’s sports.<br><br>
At least, that’s the phrase on the front of the now-iconic T-shirt that a friend gifted me. (This was a case of perfect match between recipient and gift.) 
But the numbers increasingly back it up. Per data from Women’s Sport Trust, more people watched women’s sports in the first four months of 2024 than ever before.<br><br>
In women’s football, the international game remains the most dominant form of the sport. The 2022 Euros and 2023 Women’s World Cup were watershed moments, attracting a new wave of supporters and media attention, 
and propelling the game into the broader consciousness.
Armoured with newly-acquired data manipulation and visualisation skills, this budding football journalist has decided to take up the mantle of bringing the story of women’s international football to a broader audience.  
<br><br>The narrative that you will explore across this app has been shaped around the following questions: 

- What historical challenges has women’s football faced?
- How global is the Women’s World Cup?
- Which nations have had the most success, and what insights can we gain from their success?
- How can we evaluate the Women’s World Cup as a product?
- What inequalities persist in women’s football at the international level?
      </div>""", unsafe_allow_html=True
)

