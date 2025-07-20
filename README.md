# 🎬 Movies Recommender System

This is a content-based movie recommendation system built with Python and Streamlit. It recommends 5 similar movies based on your selected movie using cosine similarity and TMDB data.

---

## 🚀 Features

- Recommends movies based on similarity
- Shows movie posters using TMDB API
- Clean and interactive UI using Streamlit

---

## 📁 Project Structure

PROJECT-MOVIES/
│
├── artifacts/
│ ├── movie_list.pkl
│ └── similarity.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── preview.png


---

## ⚙️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Lucky920487/PROJECT-MOVIES
   cd your PROJECT-MOVIES
   
2. **Create virtual environment (optional but recommended)**:
   python -m venv venv
   venv\Scripts\activate  # For Windows
   source venv/bin/activate  # For Mac/Linux
   
4. **Install dependencies**:
   pip install -r requirements.txt
5. **Run the app**:
   streamlit run app.py

   **💾 LFS Note
   Large files like .pkl are tracked using Git LFS:**

   git lfs install
   git lfs track "*.pkl"

   **📷 Preview
   Below is a screenshot of the app interface:**
  
  <img width="1862" height="934" alt="Screenshot 2025-07-20 123014" src="https://github.com/user-attachments/assets/e3b43512-e597-40b1-8a49-f261c4865cbd" />

  
  <img width="1736" height="876" alt="Screenshot 2025-07-20 123120" src="https://github.com/user-attachments/assets/f76a1e0c-008e-478b-8117-59f8be1c33d8" />

**👩‍💻 Created By
By Lucky_Kumari

**IIT PATNA**

Made with ❤️ using Python, Streamlit, and TMDB API.**


