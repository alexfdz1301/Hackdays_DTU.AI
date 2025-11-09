```markdown
# DTU Grievance & Circular System

## Overview
This project automates how DTU students access and understand university circulars and submit grievances.  
It fetches circulars from Telegram, extracts and summarizes them, and provides a basic grievance routing system.

## Features
- Fetches circular PDFs automatically from Telegram.  
- Extracts and summarizes circulars for quick reading.  
- Classifies student grievances by department type.  
- Simple Streamlit interface for both modules.

## Project Structure
```

Hackdays_DTU.AI/
├── app.py               # Main Streamlit app
├── telegram_fetch.py    # Telegram circular fetcher
├── .env                 # Environment variables (tokens, keys)
├── requirements.txt     # Dependencies
└── README.md

````

## Setup
1. Clone the repository  
   ```bash
   git clone https://github.com/alexfdz1301/Hackdays_DTU.AI.git
   cd Hackdays_DTU.AI
````

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Add required keys in `.env`

   ```
   TELEGRAM_TOKEN=your_token_here
   ```
4. Run the app

   ```bash
   streamlit run app.py
   ```
5. (Optional) Run Telegram fetcher

   ```bash
   python telegram_fetch.py
   ```

## Tech Used

* Python
* Streamlit
* Hugging Face Transformers
* pdfplumber
* python-telegram-bot

## Author

Govind – DTU Internal Hackathon “AI for DTU”

```
```
