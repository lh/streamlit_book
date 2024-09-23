import streamlit as st
import pandas as pd
from palmerpenguins import load_penguins
import xlsxwriter
from io import BytesIO
import matplotlib.pyplot as plt
import plotly.express as px
import geopandas
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

show_code = st.toggle("Click to show or hide the code", value=True)

tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Text, Headers and Markdown",
    "User Inputs",
    "Dataframes, Charts, Metrics and Maps",
    "Upload and Download Buttons",
    "Other Media"
    ])

with tab1:

    if show_code:
        st.code(
    '''
    st.markdown("# This is header level 1")

    st.markdown("## This is header level 2")

    st.markdown("### This is header level 3")

    st.markdown("#### This is header level 4")

    st.markdown("##### This is header level 5")

    st.markdown("This is standard text")

    st.markdown("You can use emojis :sunglasses:")

    st.markdown("Or Google material icons :material/favorite:")

    st.markdown("You can colour text :red[text to be colored]")

    st.markdown("Or colour the background of text :green-background[text to be colored]")

    st.markdown("""
    You can also do multiline text.

    This allows you to more easily do multi-line text.
    Notice
    the
    impact

    of different numbers of newlines between the lines.
    """)
    '''
        )

    st.markdown("# This is header level 1")

    st.markdown("## This is header level 2")

    st.markdown("### This is header level 3")

    st.markdown("#### This is header level 4")

    st.markdown("##### This is header level 5")

    st.markdown("This is standard text")

    st.markdown("You can use emojis :sunglasses:")

    st.markdown("Or Google material icons :material/favorite:")

    st.markdown("You can colour text :red[text to be colored]")

    st.markdown("Or colour the background of text :green-background[text to be colored]")

    st.markdown("""
    You can also do multiline text.

    This allows you to more easily do multi-line text.
    Notice
    the
    impact

    of different numbers of newlines between the lines.
    """)

with tab2:
    st.subheader("Numeric Input")

    if show_code:
        st.code("""
        chosen_number = st.number_input(
            "Pick a Number"
            )
        """)

    chosen_number = st.number_input("Pick a Number")

    st.write(f"The number you have chosen is {chosen_number}")

    chosen_number_multiplied_by_5 = chosen_number * 5

    st.write(f"Your number multiplied by 5 is {chosen_number_multiplied_by_5}")

    st.write(f"Your number plus 7 is {chosen_number + 7}")

    st.subheader("Numeric Slider")

    if show_code:
        st.code(
            """
        chosen_number_slider = st.slider(
            "Pick a Number on the slider",
            min_value=0,
            max_value=250,
            value=50
            )
            """
        )

    chosen_number_slider = st.slider("Pick a Number on the slider", min_value=0, max_value=250, value=50)

    st.write(f"The number you have chosen is {chosen_number_slider}")

    chosen_number_slider_multiplied_by_8 = chosen_number * 8

    st.write(f"Your number multiplied by 8 is {chosen_number_slider_multiplied_by_8}")

    st.write(f"Your number plus 3 is {chosen_number_slider + 3}")

    from datetime import datetime, time

    st.subheader("Range Slider")

    if show_code:
        st.code("""
        lower_value, upper_value = st.slider("Pick a lower and upper limit",  min_value=0, max_value=100, value=(35, 80))
        """)

    lower_value, upper_value = st.slider("Pick a lower and upper limit",  min_value=0, max_value=100, value=(35, 80))

    st.write(f"Your inputs are {lower_value} and {upper_value}")
    st.write(f"They are of type {type(lower_value)} and {type(upper_value)}")

    st.subheader("Time Slider")

    if show_code:
        st.code("""
        chosen_time = st.slider(
            "Select a time:", time(11, 30)
        )
        """)

    chosen_time = st.slider(
        "Select a time:", time(11, 30)
    )

    st.write(f"Your input is {chosen_time}")
    st.write(f"It is of type {type(chosen_time)}")

    st.subheader("Date Slider")

    if show_code:
        st.code("""
        selected_date = st.slider(
            "Select a date",
            value=datetime(2022, 1, 1),
            format="DD/MM/YYYY",
        )
        """)

    selected_date = st.slider(
        "Select a date",
        value=datetime(2022, 1, 1),
        format="DD/MM/YYYY",
    )

    st.write(f"Your input is {selected_date}")
    st.write(f"It is of type {type(selected_date)}")

    st.subheader("Date Range Slider")

    if show_code:
        st.code("""
        start_date, end_date = st.slider(
            "Select a date?",
            value=(datetime(2022, 1, 1), datetime(2023, 6, 1)),
            format="DD/MM/YYYY",
        )
        """)

    start_date, end_date = st.slider(
        "Select a date?",
        value=(datetime(2022, 1, 1), datetime(2023, 6, 1)),

        format="DD/MM/YYYY",
    )

    st.write(f"Your inputs are {start_date} and {end_date}")
    st.write(f"They are of type {type(start_date)} and {end_date}")

    st.subheader("Time Range Slider")

    if show_code:
        st.code("""
        start_time, end_time = st.slider(
            "Select a time:", value=(time(11, 30), time(12, 45))
        )
        """)

    start_time, end_time = st.slider(
        "Select a time:", value=(time(11, 30), time(12, 45))
    )

    st.write(f"Your inputs are {start_time} and {end_time}")
    st.write(f"They are of type {type(start_time)} and {end_time}")

    st.subheader("Datetime Sliders")

    if show_code:
        st.code("""
        chosen_datetime = st.slider(
            "Select a date and time",
            value=datetime(2022, 1, 1, 12, 0),
            format="DD/MM/YYYY @ hh:mm",
        )
        """)

    chosen_datetime = st.slider(
        "Select a date and time",
        value=datetime(2022, 1, 1, 12, 0),
        format="DD/MM/YYYY @ hh:mm",
    )

    st.write(f"Your input is {chosen_datetime}")
    st.write(f"It is of type {type(chosen_datetime)}")

    st.header("Date and time input elements")

    if show_code:
        st.code("""
        selected_date = st.date_input("Choose a date on the calendar picker")
        """)

    selected_date = st.date_input("Choose a date on the calendar picker")

    st.write(f"Your input is {selected_date}")
    st.write(f"It is of type {type(selected_date)}")

    if show_code:
        st.code("""
        selected_time = st.time_input("Select a time")
        """)

    selected_time = st.time_input("Select a time")

    st.write(f"Your input is {selected_time}")
    st.write(f"It is of type {type(selected_time)}")

    st.header("Text Inputs")

    if show_code:
        st.code("""
        longer_text_input = st.text_area(
            "Use this input to enter a larger piece of text"
            )
        """)

    longer_text_input = st.text_area("Use this input to enter a larger piece of text")

    st.write(f"Your input is {longer_text_input}")
    st.write(f"It is of type {type(longer_text_input)}")

    if show_code:
        st.code("""
        shorter_text_input = st.text_input(
            "We saw this before - this is an input for a short bit of text"
            )
        """)

    shorter_text_input = st.text_input("We saw this before - this is an input for a short bit of text")

    st.write(f"Your input is {shorter_text_input}")
    st.write(f"It is of type {type(shorter_text_input)}")

    if show_code:
        st.code("""
        colour_options = ["Green", "Blue", "Red", "Yellow", "Purple"]
        """)

    colour_options = ["Green", "Blue", "Red", "Yellow", "Purple"]

    st.subheader("Radio Select")

    if show_code:
        st.code("""
        radio_colour_select = st.radio(
            "Which of these colours is your favourite?",
            options=colour_options
            )
        """)

    radio_colour_select = st.radio(
        "Which of these colours is your favourite?", options=colour_options
        )

    st.subheader("Single Selectbox")

    if show_code:
        st.code("""
        selectbox_colour_select = st.selectbox(
            "Which of these colours is your favourite?",
            options=colour_options
            )
        """)

    selectbox_colour_select = st.selectbox(
        "Which of these colours is your favourite?",
        options=colour_options
        )

    st.subheader("Multiselect")

    if show_code:
        st.code(
            """
        multiselect_colour_select = st.multiselect(
            "Which of these colours are your favourite? You can pick more than one!",
            options=colour_options
            )

            """
        )

    multiselect_colour_select = st.multiselect(
        "Which of these colours are your favourite? You can pick more than one!",
        options=colour_options
        )

    st.subheader("Select Slider")

    if show_code:
        st.code("""
        slider_colour_select = st.select_slider(
            "Which of these colours is your favourite?",
            options=colour_options
            )
        """)

    slider_colour_select = st.select_slider(
        "Which of these colours is your favourite?", options=colour_options
        )


    st.subheader("Checkbox")

    if show_code:
        st.code("""
        checkbox_value = st.checkbox(
            "Tick or untick me!"
            )
        """
        )

    checkbox_value = st.checkbox("Tick or untick me!")

    st.write(f"The value of the checkbox is {checkbox_value}")

    st.subheader("Toggle")

    if show_code:
        st.code("""
        toggle_value = st.toggle("Tick or untick me!")
        """)

    toggle_value = st.toggle("Tick or untick me!")

    st.write(f"The value of the toggle is {toggle_value}")


with tab4:

    st.header("File Uploads")

    if show_code:
        st.code(
    """
    uploaded_file = st.file_uploader(
        "Please upload a csv data file",
        type=['csv'] # <1>
        )

    if uploaded_file is not None:
        uploaded_df = pd.read_csv(uploaded_file)

        st.write(uploaded_df.head())
    """
        )

    uploaded_file = st.file_uploader(
        "Please upload a csv data file",
        type=['csv'] # <1>
        )

    if uploaded_file is not None:
        uploaded_df = pd.read_csv(uploaded_file)

        st.write(uploaded_df.head())

    st.header("File Downloads")

    penguins_df = load_penguins()

    st.header("CSV files")

    st.download_button(
        "Click here to download the dataframe as a csv file", # <1>
        data=penguins_df.to_csv(index=False).encode('utf-8'), # <2>
        file_name="penguins_df.csv",
        mime="text/csv"
        )

    st.header("Excel Files")

    output = BytesIO()

    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    penguins_df.to_excel(writer, sheet_name="Penguins Data", index=False)

    writer.close()

    st.download_button(
    "Click here to download the dataframe as an Excel file",
    data = output.getvalue(),
    file_name=f"penguins.xlsx",
    mime="application/vnd.ms-excel"
    )

    st.header("Matplotlib Plots")

    fig, ax = plt.subplots(figsize=(15,10))
    plt.scatter(x=penguins_df["body_mass_g"], y=penguins_df["bill_length_mm"])
    plt.title("Penguin Body Mass (g) versus Bill Length (mm)")
    ax.set_xlabel("Body Mass (g)")
    ax.set_ylabel("Bill Length (mm)")

    st.pyplot(fig)

    filename = 'penguins_scatter_method_1.png'
    plt.savefig(filename)
    with open(filename, "rb") as img:
        btn = st.download_button(
            label="Download image",
            data=img,
            file_name=filename,
            mime="image/png"
        )


    st.header("Plotly Plots")

    fig = px.scatter(penguins_df, x="body_mass_g", y="bill_length_mm")

    st.plotly_chart(fig)

    fig.write_html("plotly_chart.html")

    with open("plotly_chart.html", "rb") as file:
        st.download_button(
            label='Download This Plot as an Interactive HTML file',
            data=file,
            file_name=f'penguins_scatterplot.html',
            mime='text/html'
        )

with tab3:
    penguins_df = load_penguins()

    st.header("Matplotlib Plots")

    fig, ax = plt.subplots(figsize=(15,10))
    plt.scatter(x=penguins_df["body_mass_g"], y=penguins_df["bill_length_mm"])
    plt.title("Penguin Body Mass (g) versus Bill Length (mm)")
    ax.set_xlabel("Body Mass (g)")
    ax.set_ylabel("Bill Length (mm)")

    st.pyplot(fig)

    st.header("Plotly Plots")

    plotly_fig = px.scatter(penguins_df, x="body_mass_g", y="bill_length_mm")

    st.plotly_chart(plotly_fig)

    st.header("Static Maps")

    @st.cache_data
    def load_crime_data():
        return geopandas.read_file("https://github.com/Bergam0t/streamlit_book/raw/refs/heads/main/crime_dataset.gpkg")

    lsoa_2011_crime_figures_df = load_crime_data()

    fig, ax = plt.subplots()

    lsoa_2011_crime_figures_df.plot(
        column="sw_5forces_street_by_lsoa_Other crime",
        legend=True,
        ax=ax
        )

    st.pyplot(fig)

    filename = 'other_crime_devon.png'

    plt.savefig(filename)

    with open(filename, "rb") as img:
        btn = st.download_button(
            label="Download Map",
            data=img,
            file_name=filename,
            mime="image/png"
        )

    st.header("Interactive Maps")

    @st.cache_data
    def load_gp_data():
        return geopandas.read_file(
        "https://github.com/Bergam0t/streamlit_book/raw/refs/heads/main/gps_sw.gpkg"
        )

    gp_list_gdf_sw = load_gp_data()

    # Filter out instances with no geometry
    gp_list_gdf_sw = gp_list_gdf_sw[~gp_list_gdf_sw['geometry'].is_empty]

    # Create a geometry list from the GeoDataFrame
    geo_df_list = [[point.xy[1][0], point.xy[0][0]] for point in gp_list_gdf_sw.geometry]

    gp_map_tooltip = folium.Map(
        location=[50.7, -4.2],
        zoom_start=8,
        tiles='openstreetmap',
        )

    for i, coordinates in enumerate(geo_df_list):

        gp_map_tooltip = gp_map_tooltip.add_child(
            folium.Marker(
                location=coordinates,
                tooltip=gp_list_gdf_sw['name'].values[i],
                icon=folium.Icon(icon="user-md", prefix='fa', color="black")
                )
        )

    st_folium(gp_map_tooltip)


with tab5:
    st.header("Images")
    st.subheader("Local/Relative Image")
    st.image("resources/cover_image_robot.jpeg")

    st.subheader("Web Image")
    st.image("https://upload.wikimedia.org/wikipedia/en/d/d2/Back_to_the_Future.jpg")

    st.header("Videos")

    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
