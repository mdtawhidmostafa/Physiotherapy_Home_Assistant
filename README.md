# 🧠 (AI-Monitored) Physiotherapy Home Assessment Solution

### Revolutionizing Remote Physiotherapy Through Artificial Intelligence

---

## 📖 Overview

This project presents an **AI-powered home physiotherapy assessment system** that enables patients to perform prescribed exercises at home while receiving **real-time feedback and progress evaluation**.  
The solution integrates a **deep learning model** with a **web-based management platform**, allowing patients, doctors, and admins to collaborate seamlessly in a remote rehabilitation environment.

---

## 💡 Motivation

Elderly and mobility-impaired patients often struggle to access physiotherapy services due to transportation issues, cost, and time constraints.  
Regular physiotherapy is critical for recovery — yet difficult to maintain without continuous monitoring.  

**Our goal:**  
To provide a **remote, AI-assisted platform** that evaluates exercise performance, generates automated reports, and helps doctors monitor patients’ progress efficiently from anywhere.

---

## 🧩 System Architecture

### 🔹 1. Web Application (Django Framework)
The web portal connects all users and enables interaction through secure accounts.

**Key Features:**
- **Patient Dashboard:** Upload exercise videos, view AI-generated scores, and download reports.
- **Doctor Dashboard:** Assign exercises, review performance, and provide personalized feedback.
- **Admin Dashboard:** Manage users (patients, doctors, assistants, and admins) and exercise libraries.
- **Automated Reporting:** AI analysis results are converted into performance reports accessible to both doctor and patient.

---

### 🔹 2. AI Model

A deep learning model was trained to **assess physiotherapy exercises** based on uploaded videos.

**Model Highlights:**
- **Architectures Used:** 3D CNN, ConvLSTM, and LST
- **Input Data:** 30 evenly spaced frames per video (128×128 resolution, normalized)
- **Output:** A continuous **performance score (regression)** reflecting exercise quality
- **Evaluation Metrics:** RMSE and MAD for 9 physiotherapy exercises
- **Best Model:** 3D CNN achieved the highest accuracy and stability

---

## ⚙️ Technical Implementation

| Component | Technology |
|------------|-------------|
| Frontend | HTML5, CSS3, JavaScript, Bootstrap |
| Backend | Django (Python) |
| Database | SQLite / PostgreSQL |
| AI Model | TensorFlow / Keras |
| Model Training | Jupyter Notebook / Python |
| Deployment | Localhost / Cloud-based Django server |

---

## 🧾 Dataset and Preprocessing

- Dataset collected and labeled by **expert physiotherapists**.  
- **Subdataset of 613 videos** (adduction, back extension, hip flexion) used for model evaluation.  
- Frames resized to **128×128 pixels**, normalized to `[0,1]`.  
- 30 frames selected per video for consistent model input.

---

## 📊 Results

| Model | Exercises Tested | Evaluation Metrics | Performance |
|--------|------------------|--------------------|-------------|
| 3D CNN | 9 | RMSE, MAD | Best accuracy |
| ConvLSTM | 9 | RMSE, MAD | Moderate |
| LSTM | 9 | RMSE, MAD | Lower accuracy |

> ✅ The **3D CNN** model outperformed others, providing the most reliable regression scores for exercise quality evaluation.

---

## 🌍 Impact

### For Patients:
- Perform physiotherapy at home safely  
- Receive real-time feedback and progress tracking  
- Improve motivation and adherence  

### For Doctors:
- Monitor multiple patients remotely  
- Access detailed AI-generated reports  
- Reduce workload and enhance care quality  

### For Elderly Patients:
- Improve accessibility, independence, and quality of life  

---

## 🚀 Future Scope

- Expand dataset to include more exercises  
- Integrate **real-time video feedback** using pose estimation  
- Incorporate **wearable sensor data** for motion accuracy  
- Introduce **personalized rehabilitation plans** using AI recommendations  

---

## 🧑‍💻 Team & Contributions

| Name | Role | Contribution |
|------|------|--------------|
| **Tawhid Mostafa** | Developer / Researcher | AI Model Development, System Integration, Web development, Model training, Dataset preparation, Documentation |
| **Team Members** | Collaborators | Dataset preparation, UI Design, Testing, Documentation |

---

## 🧠 Citation

If you use this project or its methodology in your research, please cite:

