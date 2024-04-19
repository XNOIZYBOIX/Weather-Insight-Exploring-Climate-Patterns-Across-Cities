import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

combined_dataset = pd.read_csv("updated_combined_dataset_with_city.csv")

combined_dataset['time'] = pd.to_datetime(combined_dataset['time'], format='%d-%m-%Y', errors='coerce')

selected_city = st.sidebar.selectbox("Select City", combined_dataset['city'].unique())

start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

filtered_data = combined_dataset[(combined_dataset['city'] == selected_city) & 
                                 (combined_dataset['time'] >= pd.Timestamp(start_date)) & 
                                 (combined_dataset['time'] <= pd.Timestamp(end_date))]

show_prcp = st.sidebar.checkbox("Show Precipitation Data")

st.write(filtered_data)

show_aggregated_stats = st.sidebar.checkbox("Show Aggregated Statistics")

if show_aggregated_stats:
    aggregated_stats = filtered_data.describe()
    
    st.write(aggregated_stats)

st.subheader("Visualization")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(filtered_data['time'], filtered_data['tavg'], label='Average Temperature')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Average Temperature Over Time')
ax.legend()

if show_prcp:
    ax.plot(filtered_data['time'], filtered_data['prcp'], label='Precipitation')
    ax.set_ylabel('Temperature (°C) / Precipitation (mm)')

st.pyplot(fig)
