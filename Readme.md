### 🎤 House Price Prediction Dashboard

A modern Machine Learning web app built using Streamlit that predicts house prices based on user inputs like 
- **area**
- **bedrooms**
- **bathrooms**
- **balconies**

---
## Table of Contents

- <a href="#Features">Features</a>
- <a href="#Technologies Used">Technologies Used</a>
- <a href="#Machine Learning Model">Machine Learning Model</a>
- <a href="#Project Structure">Project Structure</a>
- <a href="#WorkFlow">WorkFlow</a>
- <a href="#How to Run">How to Run</a>
- <a href="#Future Improvements">Future Improvements</a>
- <a href="#Author">Author</a>

---
<h2><a class="anchor" id="Features"></a>Features</h2>

- Input property details (Area, Bedrooms, Bathrooms, Balconies)
- ML Model: Random Forest Regressor
- Predicts estimated house price (in Lakhs)
- Shows price per square foot
- Smart insights (Attached & Common bathrooms)
- Clean and interactive UI (Dark theme dashboard)
- Visual feedback with animations

---
<h2><a class="anchor" id="Technologies Used"></a>Technologies Used</h2>

- Frontend
 -  Streamlit UI
- Backend 
 - Python logic
- Machine Learning 
 - Scikit-learn model
- Dataset
 - Custom housing dataset (house prediction.csv)

---
<h2><a class="anchor" id="Machine Learning Model"></a>Machine Learning Model</h2>

- Algorithm: Random Forest Regressor
- Dataset: Housing dataset (house prediction.csv)
- Features used:
  - Total Area (sq ft)
  - Bedrooms
  - Bathrooms
  -Balconies

--- 
<h2><a class="anchor" id="Project Structure"></a>Project Structure</h2>

📁 House-Price-Predictor
│── app.py              
│── model.pkl           
│── house prediction.csv 
│── README.md           

--- 
<h2><a class="anchor" id="WorkFlow"></a>WorkFlow</h2>

- Data Preparation
  - Sample housing data is created manually
  - Converted into a Pandas DataFrame

- Model Training
  - Features (X): area, bath, balcony
  - Target (y): price
  - Model: Random Forest Regressor trained on dataset

- Model Saving
  - Model is saved using Pickle

- Web Application
  - Streamlit loads the trained model
  - User inputs property details
  - Model predicts price instantly

---

--- 
<h2><a class="anchor" id="How to Run"></a>How to Run</h2>

- Install Dependencies
   pip install pandas numpy scikit-learn streamlit plotly

- Train the Model
   python train.py

- Run the App
   streamlit run app.py


--- 
<h2><a class="anchor" id="Future Improvements"></a>Future Improvements</h2>

- Add location-based prediction
- Show price trends & graphs
- Add AI recommendations
- Deploy on Streamlit Cloud

----
## Author

Ram Krishna
- Email: ramkrishna000888@gmail.com
- Linkeddin: https://www.linkedin.com/in/ramkrishna000/

