import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Import your SalesAnalyzer class code here
# You can place the entire class code above or in a separate module and import

# Example placeholder (replace with your class)
# from your_module import SalesAnalyzer

# --- Streamlit App ---
st.set_page_config(page_title="Sales Analysis Dashboard", layout="wide")

st.title("📊 Sales Analysis Dashboard")

# File uploader
uploaded_file = st.file_uploader("", type=['xlsx'])

if uploaded_file is not None:
    # Load data
    df = pd.read_excel(uploaded_file)
    st.success("File uploaded successfully!")

    # Initialize analyzer
    analyzer = SalesAnalyzer(df)

    # Run analysis
    if st.button("Run Complete Sales Analysis"):
        with st.spinner("Analyzing data..."):
            results = analyzer.run_complete_analysis()
        st.success("Analysis complete!")

        # --- Display results ---
        # Segments
        st.header("🔹 Customer Segments")
        st.dataframe(analyzer.segments)

        st.header("🔹 Segment Profiles")
        st.dataframe(analyzer.segment_profiles)

        # Trend Analysis
        st.header("🔹 Trend Analysis Correlations")
        st.write(results['trend_analysis'][0])

        st.header("🔹 Time Trends Data")
        st.dataframe(results['trend_analysis'][1])

        # Competitor Analysis
        st.header("🔹 Competitor Impact Assessment")
        st.write(results['competitor_analysis'])

        # Additional Insights
        st.header("🔹 Top Products")
        st.dataframe(results['additional_insights'][0])

        st.header("🔹 Advertising Efficiency")
        st.write(results['additional_insights'][1])

        # --- Visualizations ---
        st.header("🔹 Visualizations")
        st.pyplot(plt.gcf())  # Show the last Matplotlib figure created

else:
    st.info("Please upload a dataset to begin.")

