import pandas as pd
import streamlit as st


def app():
    st.title('Below table shows the name of the field and type which it expects.')
    df=pd.read_csv('data_schema.csv')
    st.dataframe(df)

    st.write(
    '''

    building_id - ID of the building

    meter - The meter id code. Read as {0: electricity, 1: chilledwater, 2: steam, 3: hotwater}. Not every building has all meter types.

    day_of_week - The day of the week with Monday=0, Sunday=6

    hour - at which time you required to predict meter reading

    week_of_year - week number in the year

    week_end - 1 if it is sunday or saturday and 0 for other days

    site_id - ID of the site

    primary_use - Indicator of the primary category of activities for the building based on EnergyStar property type definitions

    square_feet - Gross floor area of the building

    floor_count - Number of floors of the building

    air_temperature - Degrees Celsius

    cloud_coverage - Portion of the sky covered in clouds, in oktas

    dew_temperature - Degrees Celsius

    precip_depth_1_hr - Millimeters

    sea_level_pressure - Millibar/hectopascals

    wind_direction - Compass direction (0-360)

    wind_speed - Meters per second

    ''')