
import streamlit as st 
import pandas as pd
import plotly.express as px
import plotly.io as pio

st.set_page_config(page_title="I. The Sport Too Popular to Be Allowed")

#styling using class-based CSS
st.markdown(
    """
    <style>
    .pull-quote {
        border-left: 5px solid #2a76d9;
        padding: 1rem;
        margin: 1rem 0;
        font-style: italic;
        color: #444444;
        font-size: 22px;
    }
    .text {
        text-align: left;
        font-size: 22px;
    }
    .graph-title {
        font-size: 30px;
        font-weight: bold;
        color: black; 
        text-align: left;
    } 
    .graph-subtitle {
        font-size:22px;
        font-weight:bold;
        color:gray;
    }  
    """,
    unsafe_allow_html=True
)

st.title("I. The Sport Too Popular to Be Allowed")

st.image("assets/images/dickkerrladies.png",caption="Dick, Kerr Ladies regularly played to large crowds of thousands in the 1920-21 season. Source: National Football Museum")

#†ext
st.markdown(
    """
    <div class="text">

    Women have been playing football since the 1800s. And not quietly, either. 
    
    In the early 20th century, crowds in their thousands came to watch women's games in England.
    The Dick, Kerr Ladies, founded in 1917, was one of the first recognised women's international teams.
    On Boxing Day, 1920, the team met St Helens Ladies at Everton's Goodison Park, drawing a record crowd for domestic women's football of 53,000 — a record that stood for 99 years.


    This was a problem for the men in suits at The English Football Association. Women's football was too popular, and in terms of profit and attendance, was becoming a rival to the men's game.
    The huge sums of money being raised at women's games were outside the control and jurisdiciton of the FA, and were often being channelled towards political and working-class causes antithetical to the establishment.
    
    And there were, of course, still strong prevailing ideas about what were and were not considered suitable activities for women in the public sphere.
     </div>""", unsafe_allow_html=True
)

#pull-quote
st.markdown(
    """
    <div class="pull-quote">
        "There is a general feeling that football is no game for women. It is too strenous, that being the view of many famous specialists.”<br><br>— Sheffield Daily Telegraph, 9 December 1921
    </div>
    """, unsafe_allow_html=True,
)

#text
st.markdown(
    """
    <div class="text">

    On December 5, 1921, just under a year after the spectacularly successful match at Goodison Park, the FA banned women from using its grounds, effectively decimating the game. Other countries soon followed suit. 

    This chart does not represent the full list of countries in which women's football was banned, but only a small selection —
    these nations have been chosen deliberately due to their status as traditional powerhouses in men's international football.
    Yet that success and visibility did not extend to their women’s teams, revealing a clear disparity in support, recognition, and opportunity.
     </div>""", unsafe_allow_html=True
)
         
#graph headings and sub-headings
st.markdown(

    """
    <div class="graph-title">
    The Dark Ages
    </div>
    <div class="graph-subtitle">
    Timeline of Women's Football Bans by Country
    </div>
    """,
    unsafe_allow_html=True
)

#function
def plot_bans_timeline(data):
    data["Duration"] = data["End"].astype(int) - data["Start"].astype(int)
    data = data.sort_values(by="Duration", ascending=True)

    fig = px.timeline(
        data,
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
        template="plotly_white",
        width=1200,
        height=300,
        font=dict(  
            size=18
            ),  
        showlegend=False,
        bargap=0.1,
        yaxis_title ="",
        xaxis=dict(tickfont=dict(size=18)),
        yaxis=dict(tickfont=dict(size=18))
    )

    fig.update_traces(
        hovertemplate=(
            "<b>Start:</b> %{customdata[0]}<br>"  # Use customdata for Start
            "<b>End:</b> %{customdata[1]}<br>"    # Use customdata for End
        ),
        customdata=data[["Start","End"]].values,
        textposition="inside",  # Places text inside the bars
        texttemplate="%{text} years",
        marker_color="#2a76d9")
    
    st.plotly_chart(fig,use_container_width=True)

data = {
    "Country": ["England 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "Germany 🇩🇪", "Brazil 🇧🇷", "France 🇫🇷", "Spain 🇪🇸"],
    "Start": ["1921", "1955", "1941", "1932", "1935"],
    "End": ["1971", "1970", "1981", "1975", "1980"]
}

bans_df = pd.DataFrame(data)
plot_bans_timeline(bans_df)

#pull-quote
st.markdown(
    """
    <div class="pull-quote">
        "In the battle for the ball, feminine grace vanishes, body and soul inevitably suffer damage."<br><br> — Deutscher Fussball Bund, 1955
    </div>
    """,
    unsafe_allow_html=True,
)




