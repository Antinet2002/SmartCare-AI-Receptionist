# 🤖 SmartCare AI Receptionist

A web-based AI Receptionist application built with **Python, Flask, HTML, CSS, JavaScript, and SQLite**.

SmartCare AI Receptionist provides an interactive virtual receptionist that can answer common customer queries, provide service information, share working hours, assist with appointment requests, and store customer and appointment data.

---

## 🚀 Features

* 🤖 Interactive AI Receptionist
* 💬 Real-time chatbot interface
* 📅 Appointment booking system
* 👤 Customer information management
* 🗄️ SQLite database integration
* 📊 Admin Dashboard
* 🎤 Voice input support
* 🕒 Working hours information
* 🛠️ Technical support information
* 💼 Business consultation information
* 📱 Responsive web interface
* 🔐 No API key required for the current local chatbot version

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite

### Development Tools

* VS Code
* Python Virtual Environment
* Git & GitHub

---

## 📂 Project Structure

```text
AI_Receptionist_Project/
│
├── app.py
├── ai_service.py
├── database.py
├── receptionist.db
├── requirements.txt
├── .env
│
├── templates/
│   ├── index.html
│   └── admin.html
│
└── static/
    ├── style.css
    ├── script.js
    └── background.png
```

---

## 🔄 Application Workflow

```text
User
  ↓
Web Interface
  ↓
index.html
  ↓
JavaScript
  ↓
Flask Backend
  ↓
app.py
  ↓
 ┌───────────────────┐
 │                   │
 ↓                   ↓
ai_service.py   database.py
 │                   │
 ↓                   ↓
Chat Response    SQLite DB
                     │
                     ↓
              receptionist.db
                     │
                     ↓
              Admin Dashboard
```

---

## 💬 Chatbot Capabilities

The receptionist can handle common queries such as:

* Greetings
* Company information
* Available services
* Working hours
* Appointment requests
* Technical support
* Business consultation
* Contact information
* Thank-you messages
* Goodbye messages

Example:

```text
User: Hello

Bot: Hello! Welcome to SmartCare Solutions.
     How can I help you today?
```

---

## 📅 Appointment Booking

Users can provide:

* Full Name
* Phone Number
* Email
* Service
* Appointment Date
* Appointment Time

The application checks whether the selected time slot is already booked before saving the appointment.

---

## 🗄️ Database

The project uses **SQLite** for storing application data.

Database file:

```text
receptionist.db
```

The database manages:

* Customer information
* Appointment information
* Conversation history

---

## 📊 Admin Dashboard

The Admin Dashboard allows the administrator to view stored appointment information.

Open:

```text
http://127.0.0.1:5000/admin
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd AI_Receptionist_Project
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Flask server:

```powershell
python app.py
```

The application will run at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser.

---

## ❤️ Health Check

The project includes a health-check endpoint.

Open:

```text
http://127.0.0.1:5000/health
```

Expected response:

```json
{
    "status": "running",
    "message": "AI Receptionist server is running."
}
```

---

## 🔐 Environment Variables

If environment variables are required in future versions, create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

**Never upload your `.env` file or API keys to GitHub.**

Add this to `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

---

## 🧠 Current AI Implementation

The current version uses a **local rule-based receptionist system**.

It does not require an external AI API or API credits.

The response logic is implemented in:

```text
ai_service.py
```

This makes the project easy to run locally without depending on an external API.

---

## 🔮 Future Improvements

Possible future enhancements include:

* Integration with a Large Language Model
* Natural language understanding
* Multilingual chatbot support
* Email appointment confirmations
* WhatsApp integration
* Calendar integration
* Authentication for Admin Dashboard
* Appointment cancellation and rescheduling
* Customer analytics
* Advanced conversation memory
* Speech-to-text and text-to-speech
* Deployment using Docker
* Cloud database integration

---

## 🎯 Use Cases

SmartCare AI Receptionist can be adapted for:

* Healthcare organizations
* Small businesses
* Service companies
* Clinics
* Customer support teams
* Consultation businesses
* Product demonstration services

---

## 👩‍💻 Author

**Antinet Ghodke**

B.Tech in Computer Science | 2025

### Skills Demonstrated

* Python
* Flask
* SQL
* SQLite
* HTML
* CSS
* JavaScript
* REST APIs
* Database Management
* Web Application Development
* AI/Automation Concepts

---

## 📌 Project Status

**Status:** Completed Local Prototype

The application is functional as a local Flask web application with chatbot, appointment booking, database storage, and admin dashboard functionality.

---

## ⭐ Project Highlights

This project demonstrates how a virtual receptionist system can combine:

**Frontend + Backend + Database + Automation + AI-style Conversation**

into a single web application.
