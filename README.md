# Claude Chat App
A full-stack chat application built with **FastAPI** (Backend) and **Node.js/Express** (Frontend). This project has used  **Groq API** , insted of Anthropic Claude API because Groq API is free to use.

## 🚀 Features

- **High-Speed Inference**: Utilizes Groq's LPU™ Inference Engine for near-instant responses.
- **Modern Backend**: Built with Python and FastAPI for high performance and easy extensibility.
- **Simple Frontend**: Lightweight Node.js & Express server serving a clean HTML/JS interface.
- **Real-time Chat**: Interactive chat interface for communicating with the AI.

## 🛠️ Tech Stack

- **Backend**
  - [Python](https://www.python.org/) (3.8+)
  - [FastAPI](https://fastapi.tiangolo.com/) - Web framework
  - [Uvicorn](https://www.uvicorn.org/) - ASGI server
  - [Groq Python SDK](https://console.groq.com/docs/libraries/python) - AI inference
  - [Python-dotenv](https://pypi.org/project/python-dotenv/) - Environment management

- **Frontend**
  - [Node.js](https://nodejs.org/) & [Express](https://expressjs.com/)
  - Vanilla HTML, CSS, JavaScript

## 📋 Prerequisites

Before running the application, ensure you have the following installed:
- **Python 3.8+**
- **Node.js** (v14 or higher) & **npm**
- A **Groq API Key** (Get one at [console.groq.com](https://console.groq.com/))

## ⚙️ Installation & Setup

### 1. Backend Setup

1.  Navigate to the backend directory:
    ```bash
    cd backend
    ```

2.  Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4.  Set up environment variables:
    Create a `.env` file in the `backend/` directory and add your Groq API key:
    ```env
    GROQ_API_KEY=your_groq_api_key_here
    ```

5.  Run the backend server:
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

### 2. Frontend Setup

1.  Open a new terminal and navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2.  Install dependencies:
    ```bash
    npm install
    ```

3.  Start the frontend server:
    ```bash
    npm start
    ```
    Or manually:
    ```bash
    node server.js
    ```

4.  Access the application:
    Open your browser and visit `http://localhost:3000`.

## 📁 Project Structure

```
claude-chat-app/
├── backend/                # FastAPI Backend
│   ├── app/
│   │   ├── api/            # API Routes (chat.py)
│   │   ├── services/       # AI Services (groq_service.py)
│   │   └── main.py         # App Entry Point
│   ├── requirements.txt    # Python Dependencies
│   └── .env                # Env Variables (GitIgnored)
│
├── frontend/               # Node.js Frontend
│   ├── public/             # Static Assets (HTML/CSS/JS)
│   ├── server.js           # Express Server
│   └── package.json        # Node Dependencies
│
└── README.md               # Project Documentation
```

## 📝 Usage

1.  Ensure both the backend (`localhost:8000`) and frontend (`localhost:3000`) servers are running.
2.  Go to `http://localhost:3000` in your web browser.
3.  Type a message in the chat input and visualize the high-speed response from Groq!
