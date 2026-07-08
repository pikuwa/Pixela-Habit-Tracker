# 🚴 Pixela Habit Tracker

A Python-based habit tracking application that records daily cycling distance using the Pixela API. The application allows users to log their daily activity, securely manage API credentials with environment variables, and visualize progress through an interactive graph.

---

## 📌 Features

- 🚴 Record daily cycling distance
- 📊 Automatically update the Pixela graph
- 🔒 Secure API credentials using `.env`
- ⚠️ Exception handling for API requests
- 🧹 Clean and modular Python code
- 💻 Easy-to-use Command Line Interface (CLI)

---

## 🛠️ Built With

- Python 3
- Requests
- python-dotenv
- Pixela REST API

---

## 📂 Project Structure

```text
Pixela-Habit-Tracker/
│
├── Screenshots/
│   ├── graph.png
│   └── terminal-success.png
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/pikuwa/Pixela-Habit-Tracker.git
```

### 2️⃣ Navigate to the project

```bash
cd Pixela-Habit-Tracker
```

### 3️⃣ Create a virtual environment

```bash
python -m venv .venv
```

### 4️⃣ Activate the virtual environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 5️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
TOKEN=your_pixela_token
USERNAME=your_username
GRAPH_ID=your_graph_id
```

---

## ▶️ Run the Project

```bash
python main.py
```

Example Output

```text
🚴 Enter today's cycling distance (in Km): 10

✅ Cycling record added successfully!
📅 Date      : 07/07/2026
🚴 Distance  : 10 Km
```

---

## 📸 Screenshots

### Graph

![Pixela Graph](Screenshots/graph.png)

---

### Terminal Output

![Terminal Output](Screenshots/terminal-success.png)

---

## 📈 API Used

Pixela REST API

- Create User
- Create Graph
- Add Pixel
- Update Pixel
- Delete Pixel

---

## 💡 Future Improvements

- Update existing records
- Delete records
- Multiple activity tracking
- Weekly & monthly analytics
- GUI using Tkinter or Streamlit

---

## 👨‍💻 Author

**Pratik Prajapati**

- GitHub: https://github.com/pikuwa
- LinkedIn: https://www.linkedin.com/in/pratikxdev

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
