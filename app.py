import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Configure page
st.set_page_config(
    page_title="Lebanon Climate Change Analysis",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    """Main application function"""
    
    # Header
    st.title("🌍 Lebanon Climate Change Analysis")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("Navigation")
        page = st.selectbox(
            "Choose a section:",
            ["Overview", "Data Analysis", "Visualizations", "Insights"]
        )
    
    # Main content based on selection
    if page == "Overview":
        show_overview()
    elif page == "Data Analysis":
        show_data_analysis()
    elif page == "Visualizations":
        show_visualizations()
    elif page == "Insights":
        show_insights()

def show_overview():
    """Display overview section"""
    st.header("📊 Project Overview")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("About This Project")
        st.write("""
        This Streamlit application analyzes climate change data for Lebanon.
        The analysis focuses on environmental indicators and their trends over time.
        """)
        
        st.subheader("Data Sources")
        st.write("- Climate data from research publications")
        st.write("- Environmental indicators")
        st.write("- Regional analysis")
    
    with col2:
        st.subheader("Key Metrics")
        
        # Sample metrics (replace with actual data)
        metric_col1, metric_col2, metric_col3 = st.columns(3)
        with metric_col1:
            st.metric("Temperature Change", "+2.1°C", "0.3°C")
        with metric_col2:
            st.metric("Precipitation Change", "-15%", "-2%")
        with metric_col3:
            st.metric("Data Points", "1,250", "50")

def show_data_analysis():
    """Display data analysis section"""
    st.header("📈 Data Analysis")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Upload your data file",
        type=['xlsx', 'csv', 'json'],
        help="Upload Excel, CSV, or JSON files for analysis"
    )
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            elif uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            
            st.success(f"File '{uploaded_file.name}' loaded successfully!")
            
            # Display basic info
            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Dataset Info")
                st.write(f"Shape: {df.shape}")
                st.write(f"Columns: {len(df.columns)}")
            
            with col2:
                st.subheader("Column Names")
                st.write(df.columns.tolist())
            
            # Display data preview
            st.subheader("Data Preview")
            st.dataframe(df.head(), use_container_width=True)
            
        except Exception as e:
            st.error(f"Error loading file: {str(e)}")
    else:
        st.info("Please upload a data file to begin analysis.")

def show_visualizations():
    """Display visualizations section"""
    st.header("📊 Visualizations")
    
    # Sample data for demonstration
    sample_data = pd.DataFrame({
        'Year': range(2000, 2021),
        'Temperature': np.random.normal(25, 2, 21) + np.linspace(0, 2, 21),
        'Precipitation': np.random.normal(800, 100, 21) - np.linspace(0, 120, 21),
        'CO2_Levels': np.random.normal(400, 20, 21) + np.linspace(0, 50, 21)
    })
    
    # Chart selection
    chart_type = st.selectbox(
        "Select chart type:",
        ["Line Chart", "Bar Chart", "Scatter Plot", "Area Chart"]
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        if chart_type == "Line Chart":
            fig = px.line(sample_data, x='Year', y='Temperature', 
                         title='Temperature Trends Over Time')
            st.plotly_chart(fig, use_container_width=True)
        elif chart_type == "Bar Chart":
            fig = px.bar(sample_data, x='Year', y='Precipitation',
                        title='Annual Precipitation')
            st.plotly_chart(fig, use_container_width=True)
        elif chart_type == "Scatter Plot":
            fig = px.scatter(sample_data, x='Temperature', y='CO2_Levels',
                           title='Temperature vs CO2 Levels')
            st.plotly_chart(fig, use_container_width=True)
        elif chart_type == "Area Chart":
            fig = px.area(sample_data, x='Year', y='CO2_Levels',
                         title='CO2 Levels Over Time')
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Data Summary")
        st.dataframe(sample_data.describe(), use_container_width=True)

def show_insights():
    """Display insights section"""
    st.header("💡 Key Insights")
    
    insights = [
        {
            "title": "Rising Temperature Trends",
            "description": "Average temperatures have increased by 2.1°C over the past two decades.",
            "impact": "High",
            "color": "red"
        },
        {
            "title": "Decreasing Precipitation",
            "description": "Annual precipitation has decreased by 15% since 2000.",
            "impact": "Medium",
            "color": "orange"
        },
        {
            "title": "CO2 Level Changes",
            "description": "Atmospheric CO2 levels show consistent upward trend.",
            "impact": "High",
            "color": "red"
        }
    ]
    
    for insight in insights:
        with st.expander(f"🔍 {insight['title']}"):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(insight['description'])
            with col2:
                if insight['impact'] == 'High':
                    st.error(f"Impact: {insight['impact']}")
                elif insight['impact'] == 'Medium':
                    st.warning(f"Impact: {insight['impact']}")
                else:
                    st.info(f"Impact: {insight['impact']}")
    
    st.markdown("---")
    st.subheader("Recommendations")
    st.write("""
    Based on the analysis:
    1. **Monitor temperature trends** - Implement regular monitoring systems
    2. **Water conservation** - Address decreasing precipitation patterns
    3. **Carbon reduction** - Focus on reducing CO2 emissions
    4. **Data collection** - Expand data collection efforts for better insights
    """)

# Run the main function directly for Streamlit Cloud compatibility
main()
