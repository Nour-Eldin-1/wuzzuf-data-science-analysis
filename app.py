import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Wuzzuf Data Science Jobs", layout="wide")

st.title("📊 Wuzzuf Data Science Market Dashboard (Egypt)")
st.markdown("An interactive dashboard exploring the Data Science job market in Egypt based on scraped Wuzzuf data.")

# Load and prepare data
@st.cache_data
def load_data():
    df = pd.read_csv("Wuzzuf_Cleaned_Jobs.csv")
    
    def clean_location(loc):
        if pd.isna(loc) or loc == 'N/A': return 'Unknown'
        loc = str(loc)
        if 'Remote' in loc: return 'Remote'
        elif 'Cairo' in loc: return 'Cairo'
        elif 'Giza' in loc: return 'Giza'
        elif 'Alexandria' in loc: return 'Alexandria'
        else: return loc.split(',')[-1].strip()

    df['Clean_Location'] = df['Location'].apply(clean_location)
    return df

df = load_data()

# -------------------------------------------------------------
# Sidebar Filters
# -------------------------------------------------------------
st.sidebar.header("🔍 Search Filters")

# Location Filter
locations = ["All"] + list(df['Clean_Location'].unique())
selected_loc = st.sidebar.selectbox("Select Location:", locations)

# Experience Level Filter
exp_levels = ["All"] + list(df['Experience Level'].dropna().unique())
selected_exp = st.sidebar.selectbox("Select Experience Level:", exp_levels)

# Filter dataframe
filtered_df = df.copy()
if selected_loc != "All":
    filtered_df = filtered_df[filtered_df['Clean_Location'] == selected_loc]

if selected_exp != "All":
    filtered_df = filtered_df[filtered_df['Experience Level'] == selected_exp]

# -------------------------------------------------------------
# KPI Metrics
# -------------------------------------------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Total Jobs Available", len(filtered_df))
avg_min = filtered_df['Min_Exp'].mean()
col2.metric("Avg Min Experience", f"{avg_min:.1f} Yrs" if pd.notna(avg_min) else "N/A")
col3.metric("Top Location", filtered_df['Clean_Location'].mode()[0] if not filtered_df.empty else "N/A")

st.divider()

# -------------------------------------------------------------
# Visualizations
# -------------------------------------------------------------
col_chart1, col_chart2 = st.columns(2)

# Chart 1: Top Technical Skills
with col_chart1:
    st.subheader("🔥 Top Demanded Technical Skills")
    if not filtered_df.empty:
        skills_series = filtered_df['Skills & Tools'].replace('N/A', None).dropna()
        exploded_skills = skills_series.str.split(r'\s*\|\s*').explode().str.strip()
        
        ignore_words = [
            'Computer Science', 'Information Technology (IT)', 'Engineering', 
            'Software Development', 'Quality Assurance', 'Quality Control', 'Analysis'
        ]
        top_skills = exploded_skills[~exploded_skills.isin(ignore_words + ['', 'N/A'])].value_counts().head(8)

        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.barplot(x=top_skills.values, y=top_skills.index, hue=top_skills.index, palette="viridis", legend=False, ax=ax1)
        ax1.set_xlabel("Number of Job Postings")
        st.pyplot(fig1)
    else:
        st.warning("No data available for the selected filters.")

# Chart 2: Location Distribution
with col_chart2:
    st.subheader("📍 Job Distribution by Location")
    if not filtered_df.empty:
        loc_counts = filtered_df['Clean_Location'].value_counts()
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.barplot(x=loc_counts.index, y=loc_counts.values, hue=loc_counts.index, palette="rocket", legend=False, ax=ax2)
        plt.xticks(rotation=30)
        ax2.set_ylabel("Number of Jobs")
        st.pyplot(fig2)

# Interactive Data Table
st.divider()
st.subheader("📋 Filtered Job Listings")
st.dataframe(filtered_df[['Job Title', 'Company Name', 'Clean_Location', 'Experience Level', 'Min_Exp', 'Skills & Tools']])