import streamlit as st
import pandas as pd
import plotly.express as px

# Page Configuration
st.set_page_config(page_title="MoEYS PIP Dashboard", layout="wide")

st.title("🏛️ MoEYS - Public Investment Program (PIP) 2027–2029")
st.markdown("**Department of Planning - Portfolio Overview**")
st.divider()

# Top Level Metrics 
st.subheader("Financing Structure & Portfolio Status")
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total PIP Portfolio", "$715.6M")
col2.metric("Funded by DPs", "$715.6M", "100% of Total") 
col3.metric("Ongoing Projects", "$493.1M")
col4.metric("Pipeline / New", "$222.5M")

st.divider()

# Top Row: Trend Bar Chart & Donut Chart
top_col1, top_col2 = st.columns(2)

with top_col1:
    st.subheader("Funding Trend (2027-2029)")
    portfolio_data = {
        "Year": ["2027", "2028", "2029", "2027", "2028", "2029"],
        "Project Type": ["Ongoing", "Ongoing", "Ongoing", "Pipeline", "Pipeline", "Pipeline"],
        "Amount (Millions USD)": [143.4, 194.8, 74.7, 0.0, 39.2, 57.2]
    }
    df_portfolio = pd.DataFrame(portfolio_data)
    fig_portfolio = px.bar(
        df_portfolio, x="Year", y="Amount (Millions USD)", 
        color="Project Type", barmode="group",
        color_discrete_sequence=["#1f77b4", "#ff7f0e"] 
    )
    st.plotly_chart(fig_portfolio, use_container_width=True)

with top_col2:
    st.subheader("Portfolio Breakdown")
    pie_data = {
        "Status": ["Ongoing Projects", "Pipeline / New Projects"],
        "Total (Millions USD)": [493.1, 222.5]
    }
    df_pie = pd.DataFrame(pie_data)
    
    fig_pie = px.pie(
        df_pie, values="Total (Millions USD)", names="Status", 
        hole=0.4, color_discrete_sequence=["#1f77b4", "#ff7f0e"]
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.divider()

# Bottom Row: Project Rankings & Focus Areas
bot_col1, bot_col2 = st.columns(2)

with bot_col1:
    st.subheader("Major Investment Projects")
    project_data = {
        "Project Name": ["GEIP-AF", "BEIP", "SE4HC", "HEIP2", "STEP UP", "HGSF", "Tech Ed EU-Cam", "BRACE"],
        "Budget (Millions USD)": [150, 105, 83, 81, 78, 41, 40, 16]
    }
    df_projects = pd.DataFrame(project_data)
    fig_projects = px.bar(
        df_projects, x="Budget (Millions USD)", y="Project Name", 
        orientation='h', text="Budget (Millions USD)",
        color="Budget (Millions USD)", color_continuous_scale="Blues"
    )
    fig_projects.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_projects, use_container_width=True)

with bot_col2:
    st.subheader("🎯 7 Key Focus Areas")
    focus_areas = [
        "1. Basic Education Improvement",
        "2. Secondary & STEM Education Expansion",
        "3. Higher Education Reform",
        "4. ICT & EMIS Strengthening",
        "5. Climate Resilience in Education",
        "6. Teacher Capacity Development",
        "7. School Feeding & Youth Skills Programs"
    ]
    for area in focus_areas:
        st.markdown(f"✅ **{area}**")