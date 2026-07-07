# 🚴 Pixela Habit Tracker

A Python application that integrates with the Pixela API to track daily cycling distance. This project demonstrates API integration, HTTP requests, and secure credential management using environment variables.

## Features

* Create a Pixela user account
* Create a cycling graph
* Add daily cycling records
* Update existing records
* Delete records
* Store API credentials securely using `.env`

## Technologies Used

* Python
* Requests
* python-dotenv
* Pixela API

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/pikuwa/Pixela-Habit-Tracker.git
   ```

2. Navigate to the project:

   ```bash
   cd Pixela-Habit-Tracker
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file using `.env.example` and add your Pixela credentials:

   ```env
   TOKEN=your_token
   USERNAME=your_username
   GRAPH_ID=your_graph_id
   ```

5. Run the project:

   ```bash
   python main.py
   ```

## Project Structure

```text
Pixela-Habit-Tracker/
│── main.py
│── requirements.txt
│── .env.example
│── .gitignore
└── README.md
```

## Note

The `.env` file is excluded from Git using `.gitignore`, ensuring that sensitive information such as API tokens is not uploaded to GitHub.
