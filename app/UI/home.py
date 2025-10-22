import streamlit as st

def homePage() -> bool:
    st.title("Welcome to IceAlert: Ice Forecasting Application")
    st.write("This application forecasts Lake Michigan ice conditions 3 days ahead.")
    st.divider()
    
    # Create 3 columns layout
    col1, col2, col3 = st.columns(3)
    
    # Column 1: Data Overview
    with col1:
        st.subheader("Overview")
        st.metric("Ice Coverage", "34.87%", "+3.67/%") #FIXME PLACEHOLDER
        st.metric("Water Temperature", "15°F", "-2°F") #FIXME PLACEHOLDER
        st.metric("Wind Speed", "12 mph", "+1 mph") #FIXME PLACEHOLDER
        st.metric("Humidity", "78%", "+5%") #FIXME PLACEHOLDER

        with st.expander("View Details"):
            st.write("**Data Sources:**")
            #st.write("- Weather stations: 45")
            #st.write("- Satellite imagery: Daily")
            #st.write("- Historical records: 10 years")
    
    # Column 2: Map/Image with Buttons
    with col2:
        st.subheader(f"Forecast - Day #{'PLACEHOLDER'}")  #FIXME PLACEHOLDER - Update based on prediction shown.
        
        # Placeholder for map/image
        st.image("https://via.placeholder.com/400x300.png?text=Ice+Coverage+Map", 
                 caption="Current Ice Coverage", 
                 use_container_width=True)

        # Map Key
        with st.expander("Legend"):
            st.write("Red   >90% Ice chance")
            st.write("Yellow   >60% Ice chance")
            st.write("Green   >20% Ice chance")

        # Buttons below the map
        st.button("🔄 Increment Day", use_container_width=True)
        st.button("📥 Upload Data", use_container_width=True)
        #st.button("⚙️ Settings", use_container_width=True)
    
    # Column 3: Data Explanation
    with col3:
        st.subheader("ℹ️ About Predictions")
        st.write(f"""
                    **Ice Forecasting Predictions Explained**
                            
                    **Data:**
                        - 
                        - 
                    
                    **Processing:**
                        - 
                        - 
                 
                    **Notes:**
                    Blah blah blah...
                """)
                
    #st.info("💡 Use the sidebar to navigate through different features of the application.")
    
    return True