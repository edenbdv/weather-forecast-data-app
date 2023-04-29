import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

def get_date(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures

d, t = get_date(days)
# we can get a figure object from a data visualization library
# such as "Plotly" or "Bokeh".
# create a line graph, we need to give the axis array's objects
figure = px.line(x=d, y=t, labels={"x": "Date", "y": "Temperature (C)"})
# this method gets a figure object as input
st.plotly_chart(figure)





