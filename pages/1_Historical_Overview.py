
import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly.io as pio

st.set_page_config(page_title="Historical Overview")

st.markdown("# 1. Context Matters")

st.markdown(
    """
    <style>
    /* Style for title section */
    .title-section {
        background-color: #000000; /* Black background */
        padding: 2rem;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    .title-section h1 {
        font-family: 'Helvetica-Bold';
        font-size: 2rem;
        color: #FFFFFF; /* White text */
    }
    .title-section p {
        font-size: 1.2rem;
        color: #FFFFFF; /* White text */
        margin-bottom: 3rem;
    }
    /* Centered and narrower margin for text */
    .centered-text {
        max-width: 800px;
        margin: 0 auto;  /* Center horizontally */
        text-align: left;
        font-family: 'Georgia', serif;
        line-height: 1.6;
    }
    .centered-text h1 {
        font-size: 2.5rem;
        color: #333333;
        margin-bottom: 1rem;
    }
    .centered-text p {
        font-size: 1.2rem;
        color: #666666;
        margin-bottom: 2rem;
    }
    /* Style for pull quotes */
    .pull-quote {
        background-color: #f9f9f9;
        border-left: 5px solid #2a76d9;
        padding: 1rem;
        margin: 1rem 0;
        font-style: italic;
        color: #444444;
        font-family: 'Helvetica', sans-serif;
        font-size: 24px;
    }

    /* Style for image and text section */
    .image-section img {
        width: 80%;
        height: auto;
        margin-bottom: 1rem;
    }

    .image-section .text {
        font-family: 'Arial', sans-serif;
        font-size: 1rem;
        color: #333333;
        line-height: 1.5;
    }

    /* Style for bottom-right text */
    .bottom-right-text {
        position: absolute;
        bottom: 10px;
        right: 10px;
        font-size: 1rem;
        color: #f8e86f; /* Yellow text */
        font-family: 'Georgia', serif;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Set global font size for markdown texts */
    .markdown-text {
        font-size: 22px;  
        font-family: 'Helvetica', sans-serif; 
        color: #333333;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.image("assets/images/dickkerrladies.png",caption="Dick, Kerr Ladies regularly played to large crowds of thousands in the 1920-21 season. Source: National Football Museum")

st.write(
    """
    The Dick, Kerr Ladies, founded in 1917 was one of the first recognised women's international teams.
    On Boxing Day, 1920  the team met St Helens Ladies at Everton's Goodison Park, drawing a record crowd for domestic women's football of 53,000 - a record that stood for 99 years.
    However, in 1921, spooked by the success of the women's game, The English Football Association, decided it was not a good idea for women to play football.
    On December 5, 1921, just under a year after the spectacularly successful match at Goodison Park, the FA banned women from using its grounds. Other countries soon followed suit.
    """
)

st.markdown(
    """
    <div class="pull-quote">
        "There is a general feeling that football is no game for women. It is too strenous, that being the view of many famous specialists.”<br>- Sheffield Daily Telegraph, 9 December 1921
    </div>
    """,
    unsafe_allow_html=True,
)

st.write(
    """
    The chart below highlights a select sample of countries in which women's football was banned. I have chosen
    these nations deliberately due to their status as traditional powerhouses in men's international football - 
    yet that success and visibility did not extend to their women’s teams, revealing a clear disparity in support, recognition, and opportunity.
    """
)
         


st.markdown(
    """
    <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
        The Dark Ages
    </h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<span style='font-size:22px; font-weight:bold; color:gray;'>Timeline of Women's Football Bans by Country</span>", 
    unsafe_allow_html=True
)


data = {
    "Country": ["England", "Germany", "Brazil", "France", "Spain"],
    "Start": ["1921", "1955", "1941", "1932", "1935"],
    "End": ["1971", "1970", "1981", "1975", "1980"]
}

bans = pd.DataFrame(data)
bans["Duration"] = bans["End"].astype(int) - bans["Start"].astype(int)
bans = bans.sort_values(by="Duration", ascending=True)

#Graph 1: Bans Timeline

fig = px.timeline(
    bans,
    x_start="Start",
    x_end="End",
    y="Country",
    text="Duration",
    template="plotly_white",
    hover_data={
        "Country":False,
        "Duration":False,
        "Start": True, 
        "End": True}, 
)

fig.update_layout(
    xaxis=dict(title='',showgrid=False,tickfont=dict(size=14)),
    yaxis=dict(title="",automargin=True,tickfont=dict(size=14)), 
    template="plotly_white",
    width=1200,
    height=300,
    font=dict(
        family="Helvetica",  
        size=18, 
        color="black"),  
    showlegend=False,
    bargap=0.1
)

fig.update_traces(
    hovertemplate=(
        "<b>Start:</b> %{customdata[0]}<br>"  # Use customdata for Start
        "<b>End:</b> %{customdata[1]}<br>"    # Use customdata for End
    ),
    customdata=bans[["Start","End"]].values,
    textposition="inside",  # Places text inside the bars
    texttemplate="%{text} years",
    marker_color="#2a76d9")

st.plotly_chart(fig,use_container_width=True)

st.markdown(
    """
    <div class="pull-quote">
        "In the battle for the ball, feminine grace vanishes, body and soul inevitably suffer damage." - Deutscher Fussball Bund, 1955
    </div>
    """,
    unsafe_allow_html=True,
)

st.write(
    """
    Bans did not mean that women were forbidden from the playing the sport outright.
    Instead, female teams were banned from playing in stadiums, which resulted in a massive downturn
    in attendance and visibility. Teams were left with no choice but to play in local parks and fields. 
    """
)


# st.markdown(
#     """
#     <h1 style="font-size: 30px; color: black; text-align: left; font-family: 'Helvetica-Bold';">
#         Late Bloomers
#     </h1>
#     """,
#     unsafe_allow_html=True
# )
# st.markdown(
#     "<span style='font-size:20px; font-weight:bold; color:gray;'>FIFA World Cup Timeline</span>", 
#     unsafe_allow_html=True
# )

# #Graph 2: World Cup Timeline
# timeline = pd.read_csv("data/timeline.csv",index_col=0)
# timeline["Tournament"] = ["Men"] * 22 + ["Women"] * 9

# fig_1 = px.scatter(
#     timeline,
#     x="Year",
#     y="Tournament",
#     size="Teams",
#     color="Tournament",
#     hover_name="Host",
#     hover_data={"Year": True, "Teams": True, "Tournament": False},
#     template="plotly_white",
#     size_max=15,
#     color_discrete_map={"Men":"#d92ace", "Women":"#2a76d9"},
# )
# fig_1.update_layout(
#     font=dict(
#         family="Helvetica",  # Font style
#         size=14,  # General font size
#         color="black"  # Font color
#     ),
#     margin={"t": 40},
#     yaxis=dict(showgrid=True),
#     showlegend=False,
#     width=1200,
#     height=200,
# )
# fig_1.update_xaxes(title='',showgrid=True, showline=True,linewidth=2,tickfont=dict(size=14),
#         linecolor="black",tickmode='array', tickvals=[1930,1991, 1995, 1999, 2003, 2007, 2011, 2015, 2019, 2023],tickangle=90)
# fig_1.update_yaxes(
#     title="",
#     tickmode="array",
#     tickvals=["Men", "Women"],  # Adjust tick values to be based on actual y-axis categories
#     ticktext=["Men's World Cup", "Women's World Cup"],  # Add corresponding labels for better clarity
#     tickangle=0,
#     showgrid=True,
#     showline=False,
#     linewidth=2,
#     categoryorder="array",  # Use array to control the category order
#     categoryarray=["Men", "Women"],  
#     tickfont=dict(size=14)
# )
# fig_1.for_each_trace(
#     lambda trace: trace.update(marker=dict(opacity=0.2)) if trace.name == "Men" else trace.update(marker=dict(opacity=1))
# )

# st.plotly_chart(fig_1,use_container_width=True)


