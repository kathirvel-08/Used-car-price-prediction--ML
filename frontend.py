import pandas as pd
import streamlit as st
import pickle

# Load the dataset
df = pd.read_csv('E:/Project/Project files/car_price_prediction/data/car_data.csv')

# Sidebar content
with st.sidebar:
    st.title("OPTION MENU")
    option_menu = st.radio("MENU", ['ABOUT', 'PREDICT'])
    # Custom CSS to add an image background to the sidebar
    st.markdown(
    """
    <style>
    .stSidebar {
        background-image: url('https://images.hdqwalls.com/download/lotus-evija-concept-car-4k-lq-1080x1920.jpg');
        background-size: cover;
        background-position: center;
        color: white; /* Adjust text color for visibility */
    }
    </style>
    """,
    unsafe_allow_html=True  
    )

# MENU == ABOUT
if option_menu == 'ABOUT':
    # Background image CSS
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://www.hdwallpaperspulse.com/wp-content/uploads/2016/03/06/grey-car-background.jpeg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        [data-testid="stHeader"] {
            background-color: rgba(0, 0, 0, 0);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title('USED CAR PRICE PREDICTION')
    st.divider()
    st.write(
        """
    Welcome to our **Car Price Prediction Model**! This tool leverages cutting-edge machine learning algorithms to estimate the market value of cars based on various features such as brand, model, year of manufacture, mileage, engine specifications, and more.  

    The primary goal of this model is to assist car buyers, sellers, and enthusiasts in making informed decisions by providing accurate and reliable price predictions.  

    ### Key Highlights:
    1. **Data-Driven Insights**:  
    The model is trained on a robust dataset containing thousands of car listings, ensuring predictions are grounded in real-world trends.  

    2. **Customizable Inputs**:  
    Users can input specific car details to get a tailored price estimate.  

    3. **Efficiency and Accuracy**:  
    Using advanced machine learning techniques, such as regression models, ensures predictions are both precise and timely.  

    ### Who Can Benefit:
    - **Buyers**: Understand if a car's asking price aligns with its market value.  
    - **Sellers**: Determine the optimal price point for your vehicle.  
    - **Dealers and Brokers**: Gain a competitive edge with data-backed pricing.  


        """
    )

# MENU == PREDICT
elif option_menu == 'PREDICT':
    # Background image CSS
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://i.pinimg.com/originals/0e/13/c0/0e13c0a0c04befda2b72c1d5754a2368.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        [data-testid="stHeader"] {
            background-color: rgba(0, 0, 0, 0);
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.header("PREDICT CAR PRICE AS YOUR WISH!")
    st.divider()

    # Order numbers and user input collection
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        # 1. Gear Box
        Gear_box = st.selectbox('1.Gear Box', options=df['Gear Box'].unique())
    with col2:
        # 2. Length
        Length = st.slider("2.Length (CM)", min_value=min(df['Length']), max_value=max(df['Length']))
    with col3:
        # 3. Width
        Width = st.slider("3.Width (CM)", min_value=min(df['Width']), max_value=max(df['Width']))
    with col4:
        # 4. Model Year
        Model_year = st.selectbox('4.Model Year', options=sorted(df['modelYear'].unique()))
    with col5:
        # 5. Height
        Height = st.slider("5.Height (CM)", min_value=min(df['Height']), max_value=max(df['Height']))
        
    st.divider()
    
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        # 6. Kerb Weight
        Kerb_weight = st.slider("6.Kerb Weight (KG)", min_value=min(df['Kerb Weight']), max_value=max(df['Kerb Weight']))
    with col7:
        # 7. Number of Cylinders
        No_cylinders = st.selectbox("7.No. of Cylinders", sorted(df['No of Cylinder'].dropna().unique()))
    with col8:
        # 8. Kilometers
        km = st.slider("8.Kilometers", min_value=100, max_value=500000)
    with col9:
        # 9. Transmission
        Transmission = st.selectbox("9.Transmission", df['transmission'].unique())
    with col10:
        # 10. Registration Year
        Registration_Year = st.selectbox('10.Registration Year', sorted(df['Registration Year'].dropna().unique()))

    st.divider()

    col11, col12, col13, col14, col15 = st.columns(5)
    with col11:
        # 11. Wheel Base
        Wheel_base = st.slider("11.Wheel Base", min_value=min(df['Wheel Base']), max_value=max(df['Wheel Base']))
    with col12:
        # 12. Engine Displacement
        Engine_displacement = st.slider("12.Engine Displacement (CC)", min_value=620.0, max_value=max(df['Engine Displacement']))
    with col13:
        # 13. Model
        model = st.selectbox("13.Model", sorted(df['model'].dropna().unique()))
    with col14:
        # 14. Mileage
        Mileage = st.slider("14.Mileage (KM/L)", min_value=min(df['Mileage']), max_value=40.0)
    with col15:
        # 15. State
        state = st.selectbox("15.State", sorted(df['State'].unique()))

    st.divider()

    col16, col17, col18, col19, col20 = st.columns(5)
    with col16:
        # 16. Color
        color = st.selectbox("16.Color", df['Color'].dropna().unique())
    with col17:
        # 17. Rear Brake Type
        Rear_brake_type = st.selectbox("17.Rear Brake Type", df['Rear Brake Type'].dropna().unique())
    with col18:
        # 18. Body Type
        bt = st.selectbox("18.Body Type", df['bt'].dropna().unique())
    with col19:
        # 19. Manufacturer
        oem = st.selectbox("19.Manufacturer", df['oem'].unique())
    with col20:
        # 20. Tyre Type
        Tyre_type = st.selectbox("20.Tyre Type", df['Tyre Type'].dropna().unique())
    
    st.divider()
    
    # Prediction Input Data
    input_order = {
        'Gear Box': Gear_box,
        'Length': Length,
        'Width': Width,
        'modelYear': Model_year,
        'Height': Height,
        'Kerb Weight': Kerb_weight,
        'No of Cylinder': No_cylinders,
        'km': km,
        'transmission': Transmission,
        'Registration Year': Registration_Year,
        'Wheel Base': Wheel_base,
        'Engine Displacement': Engine_displacement,
        'model': model,
        'Mileage': Mileage,
        'State': state,
        'Color': color,
        'Rear Brake Type': Rear_brake_type,
        'bt': bt,
        'oem': oem,
        'Tyre Type': Tyre_type
    }

    if st.button("PREDICT"):
        # Convert to DataFrame
        input_df = pd.DataFrame([input_order])

        # Load encoder
        with open('E:/Project/Project files/car_price_prediction/Preseved/encoders.pkl', 'rb') as f:
            encoder = pickle.load(f)

        # Encode categorical variables
        categorical = ['bt', 'transmission', 'oem', 'model', 'Color', 'Gear Box', 'Rear Brake Type', 'Tyre Type', 'State']
        for col in categorical:
            input_df[col] = encoder[col].transform(input_df[col])

        # Load model and make prediction
        with open("E:/Project/Project files/car_price_prediction/Preseved/model.pkl", 'rb') as f:
            ML_model = pickle.load(f)

        predicted_price = str(int(ML_model.predict(input_df)[0]))
        st.success(f"Predicted Price: {predicted_price[:]}")
        
