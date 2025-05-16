import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.io as pio


# Set Open Graph metadata using raw HTML
st.markdown(
    """
    <meta property="og:image" content="https://imgur.com/a/prag7rT" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />
    <meta property="og:title" content="From Margins to Main Stage" />
    <meta property="og:description" content="A data story on the rise of women's football." />
    <meta property="og:url" content="https://frommarginstomainstage.streamlit.app/" />
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    /* --- TITLE SECTION --- */
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

    /* --- MAIN TEXT CONTAINER --- */
    .centered-text {
        max-width: 800px;
        margin: auto;
        text-align: left;
        font-family: 'Georgia', serif;
        line-height: 1.6;
        color: #333333;
    }

    /* --- PULL QUOTE STYLE --- */
    .pull-quote {
        border-left: 5px solid #2a76d9;
        padding-left: 1rem;
        margin: 1rem 0;
        font-style: italic;
        color: #444444;
        font-family: 'Georgia', serif;
        font-size: 1.2rem;
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


st.markdown(
    """
    <h2 style="text-align: center; font-size: 26px;">Project Introduction</h2>
        <div style="text-align: left; font-size: 22px;">
   
Everyone watches women’s sports. 

At least, that’s what it says on the front of the viral slogan T-shirt that a good friend gifted me (I was gleeful). 
But the numbers increasingly back it up. Per data from Women’s Sport Trust, more people watched women’s sports in the first four months of 2024 than ever before. 

In women’s football, the international game remains the most dominant form of the sport. The 2022 Euros and 2023 Women’s World Cup were watershed moments, attracting a new wave of supporters and media attention, 
and propelling the game into the broader consciousness.
Armoured with newly-acquired data manipulation and visualisation skills, this football aficionado has decided to take up the mantle of bringing the story of women’s international football to a broader audience.  

The narrative that you will explore across this app has been built and shaped around the following questions: 

- What historical challenges has women’s football faced?
- How global is the Women’s World Cup?
- Which nations have had the most success, and what insights can we gain from their success?
- How can we evaluate the Women’s World Cup as an overall ’product’?
- What inequalities persist in women’s football at the international level?
      </div>""", unsafe_allow_html=True
)