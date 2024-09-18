import streamlit as st
from palmerpenguins import load_penguins
import plotly.express as px
from io import StringIO
# the kaleido package must also be installed in the environment for the saving of static plots
# to work

penguins = load_penguins()

axis_options = ['bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g']

col_1 = st.selectbox("Select the column to use for the x axis", axis_options)

axis_options.remove(col_1)

col_2 = st.selectbox("Select the column to use for the x axis", axis_options)

color_factor = st.selectbox("Select the column to colour the chart by",
["species", "sex", "island"])

fig = px.scatter(penguins, x=col_1, y=col_2, color=color_factor,
title=f"Penguins Dataset - {col_1} vs {col_2}, coloured by {color_factor}")

st.plotly_chart(fig)

fig.write_image("plotly_plot_1.png", engine="kaleido")

with open("plotly_plot_1.png", "rb") as img:
    st.download_button(
        label='Download This Plot as an Static Image File',
        data=img,
        file_name=f'{col_1}_vs_{col_2}_by_{color_factor}.png',
        mime='img/png'
    )
