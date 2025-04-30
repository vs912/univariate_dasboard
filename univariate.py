import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load your dataset
df = pd.read_csv("temp.csv")

# Set layout
st.set_page_config(page_title="Mental Health Dashboard", layout="centered")
st.title("🧠 Mental Health Survey - Univariate Analysis")

# Variable-to-title mapping
univariate_titles = {
    'Gender': "What is your gender?",
    'self_employed': "Are you self-employed?",
    'family_history': "Do you have a family history of mental illness?",
    'treatment': "Have you sought treatment for mental health?",
    'remote_work': "Do you work remotely?",
    'tech_company': "Do you work for a tech company?",
    'benefits': "Are mental health benefits provided by your employer?",
    'care_options': "Are mental health care options available?",
    'wellness_program': "Does your employer provide a wellness program?",
    'anonymity': "Can you seek help anonymously?",
    'leave': "Are you comfortable taking mental health leave?",
    'mental_health_consequence': "Is there a consequence to discussing mental health at work?",
    'phys_health_consequence': "Is there a consequence to discussing physical health at work?",
    'coworkers': "Are you comfortable discussing mental health with coworkers?",
    'supervisor': "Are you comfortable discussing mental health with your supervisor?",
    'mental_health_interview': "Would you disclose mental health issues in an interview?",
    'phys_health_interview': "Would you disclose physical health issues in an interview?",
    'mental_vs_physical': "Is mental health as important as physical health?",
    'obs_consequence': "Have you observed negative consequences due to mental health disclosure?"
}

# Dropdown selection
selected_var = st.selectbox("Select a variable to visualize:", list(univariate_titles.keys()))

# Generate chart
if selected_var:
    temp = df[[selected_var]].dropna()
    counts = temp[selected_var].value_counts().reset_index()
    counts.columns = ['Category', 'Count']

    fig = go.Figure(data=[
        go.Pie(
            labels=counts['Category'],
            values=counts['Count'],
            hole=0.5,
            textinfo='percent+label',
            marker=dict(colors=px.colors.qualitative.Set2),
            pull=[0.05]*len(counts),
            showlegend=True
        )
    ])

    fig.update_layout(
        title={
            'text': univariate_titles[selected_var],
            'x': 0.5,
            'xanchor': 'center',
            'font': dict(size=20, color='black')  # ✅ Title visible in all modes
        },
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="top",
            y=0.95,
            xanchor="left",
            x=1.05,
            font=dict(color="black")  # Legend text visible
        ),
        paper_bgcolor='white',
        plot_bgcolor='white',
        font=dict(size=15, color='black')
    )

    st.plotly_chart(fig, use_container_width=True)
