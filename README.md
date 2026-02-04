# 🔐 Adaptive Network Intrusion Detection System (NIDS)

An **Adaptive Network Intrusion Detection System** that detects malicious network traffic using **machine learning techniques**. The system classifies network connections as **Normal** or **Attack** by analyzing traffic features and continuously adapts to new patterns.

---

## 📌 Project Overview

With the increase in cyber threats, traditional rule-based security systems are insufficient. This project uses **machine learning models** to identify network intrusions more accurately and efficiently.

The system is designed to be **adaptive**, meaning it can retrain and improve performance when new data is provided. A web-based interface allows users to upload network traffic data and view predictions in real time.

---

## 🚀 Features

- 🛡️ Detects **Normal vs Malicious network traffic**
- 📂 Upload and analyze network traffic datasets
- 🤖 Machine Learning–based classification
- 🔁 Adaptive retraining with new data
- 🌐 Web-based interface using Flask
- 📊 Prediction confidence score

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **Framework:** Flask  
- **Libraries:**
  - Pandas
  - NumPy
  - Scikit-learn
  - Matplotlib
  - Pickle
- **Machine Learning:** Supervised Learning
- **Dataset:** Network traffic dataset (KDD / NSL-KDD inspired)

---

## 📂 Project Structure
Adaptive-NIDS/
│
├── app.py
├── model/
│ ├── nids_model.pkl
│
├── data/
│ ├── train.txt
│ ├── test.txt
│
├── static/
├── templates/
│ ├── index.html
│ ├── result.html
│
├── requirements.txt
├── README.md


---

## ⚙️ System Workflow

1. Network traffic data is collected and preprocessed.
2. Relevant features are extracted.
3. ML model is trained using labeled data.
4. Incoming traffic is classified as:
   - **Normal Traffic**
   - **Intrusion / Attack**
5. Results and confidence scores are displayed on the web interface.
6. System adapts by retraining when new data is added.

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/adaptive-nids.git

Step 2: Navigate to Project Directory
cd adaptive-nids

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run the Application
python app.py

Step 5: Open in Browser
http://127.0.0.1:5000/

📈 Output

Traffic classification result (Normal / Attack)

Prediction confidence percentage

Easy-to-use web interface

🔮 Future Enhancements

Deep learning-based intrusion detection

Real-time packet capture integration

Multi-class attack classification

Cloud-based deployment

Dashboard for attack analytics

👩‍💻 Author

Shravani Sakhalkar
Engineering Student | Aspiring Software Engineer
Interests: Cybersecurity, Machine Learning, AI
