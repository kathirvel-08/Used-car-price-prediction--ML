# Car Price Prediction Application

## Overview
This project is a **Streamlit-based web application** that predicts the price of used cars. It leverages **machine learning models** trained on historical car sales data to provide accurate and reliable predictions. The application is designed to assist buyers, sellers, and dealers in making informed decisions about car pricing.

---

## Features

1. **User-Friendly Interface**:
   - Intuitive input fields for entering car specifications.
   - Organized layout with options to learn about the application or make predictions.

2. **Customizable Inputs**:
   - Users can input specific car details such as mileage, year, engine specifications, etc.

3. **Advanced Machine Learning**:
   - Utilizes a trained regression model to predict car prices.
   - Encodes categorical variables for model compatibility.

4. **Interactive Sidebar**:
   - Navigate between the **About** and **Predict** sections.
   - Custom CSS styling for an enhanced visual experience.

5. **Dynamic Background and Images**:
   - Displays relevant car images and a styled interface based on user interactions.

---

## Project Structure

### Files and Directories
- **data/car_data.csv**: Dataset containing historical car details.
- **Preseved/encoders.pkl**: Encoded values for categorical variables.
- **Preseved/model.pkl**: Trained regression model.
- **app.py**: Streamlit application code.

### Application Workflow

#### Sidebar Menu:
- **About**: Provides an overview of the application and its key features.
- **Predict**: Allows users to input car specifications and predict the price.

#### Input Fields:
- Includes 20 ordered fields, such as Gear Box, Model Year, Engine Displacement, etc.
- Allows users to customize inputs via sliders and dropdowns.

#### Prediction:
- User inputs are processed and encoded.
- The model predicts the price, which is displayed to the user.
- A car image is displayed for visual context.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/username/car_price_prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. Open the application in your browser using the URL provided by Streamlit.

---

## Future Improvements

1. **Add More Features**:
   - Include additional fields like fuel type, drivetrain, etc.
2. **Improve Model Accuracy**:
   - Experiment with advanced models like XGBoost or Neural Networks.
3. **Deploy Application**:
   - Deploy the application on platforms like Heroku or AWS.
4. **User Authentication**:
   - Add login functionality for personalized predictions.

---

## Acknowledgments

- **Streamlit**: For providing an easy-to-use framework for web applications.
- **Scikit-Learn**: For robust machine learning tools.
- **Pandas**: For efficient data manipulation.

---

## License

This project is licensed under the MIT License.

---

## Contact

- **Email**: [kathirvel15082k@gmail.com](mailto:kathirvel15082k@gmail.com)
- **LinkedIn**: [Kathirvel P](https://www.linkedin.com/in/kathirvel-p-4089a7296?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

