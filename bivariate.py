import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Load dataset
df = pd.read_csv("cleaned_data.csv")

# Page setup
st.set_page_config(page_title="Grouped Bar Chart Dashboard", layout="centered")
st.title("📊 Mental Health Survey - Grouped Bar Chart Analysis")

# Variables
category_vars = [
    'anonymity', 'remote_work', 'tech_company', 'wellness_program', 'care_options',
    'mental_health_interview', 'phys_health_interview', 'coworkers', 'supervisor',
    'mental_vs_physical', 'obs_consequence', 'leave'
]
grouping_vars = ['treatment', 'Gender', 'family_history']

title_map = {
    'anonymity': "Is mental health support anonymous?",
    'remote_work': "Do you work remotely?",
    'tech_company': "Do you work in a tech company?",
    'wellness_program': "Does your company offer a wellness program?",
    'care_options': "Are mental health care options provided?",
    'mental_health_interview': "Would you disclose mental health issues in an interview?",
    'phys_health_interview': "Would you disclose physical health issues in an interview?",
    'coworkers': "Comfort discussing mental health with coworkers?",
    'supervisor': "Comfort discussing mental health with supervisor?",
    'mental_vs_physical': "Is mental health as important as physical health?",
    'obs_consequence': "Observed consequences for disclosing mental health?",
    'leave': "Comfort taking mental health leave?"
}

# Dropdowns
x_col = st.selectbox("Select a category variable (X-axis):", category_vars)
group_col = st.selectbox("Select a grouping variable (color legend):", grouping_vars)

# Plotting
if x_col and group_col:
    temp = df[[x_col, group_col]].dropna()
    grouped = temp.groupby([x_col, group_col]).size().reset_index(name='Count')

    categories = sorted(temp[x_col].unique())

    fig = go.Figure()

    for group_val in grouped[group_col].unique():
        subset = grouped[grouped[group_col] == group_val]
        fig.add_bar(
            x=subset[x_col],
            y=subset['Count'],
            name=str(group_val)
        )

    fig.update_layout(
        title=dict(
            text=f"{title_map.get(x_col, x_col)} grouped by {group_col}",
            x=0.5,
            xanchor="center",
            font=dict(size=20, color='black')  # 🔧 force black title
        ),
        xaxis=dict(
            title=x_col,
            categoryorder='array',
            categoryarray=categories,
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        yaxis=dict(
            title="Count",
            titlefont=dict(color='black'),
            tickfont=dict(color='black')
        ),
        legend=dict(
            title=group_col,
            font=dict(color='black'),           # 🔧 legend font
            title_font=dict(color='black')      # 🔧 legend title
        ),
        barmode='group',
        bargap=0.2,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='black')  # 🔧 fallback for any missed text
    )

    st.plotly_chart(fig, use_container_width=True)
