🧠 DTU SmartConnect – AI Helpdesk & Circular Insight Engine  
*(Project under Hackdays_DTU.AI – DTU Internal Hackathon “AI for DTU”)*  

🎯 Overview
**DTU SmartConnect** is an AI-powered system built to simplify how DTU students access official information and raise grievances.  
It automates grievance routing, circular summarization, and Telegram-based circular fetching — bringing all communication into one platform.

This project was developed as a **solo submission** for DTU’s internal hackathon **“AI for DTU”**, focusing on *learning practical NLP applications, model integration, and AI workflow building.*

---

## 🧩 Problem
Students waste hours figuring out which department to approach for issues (Exam Cell, Hostel Office, Administration, etc.).  
Circulars and announcements are long, repetitive, and not specific to each branch or year.  
Telegram updates get buried or ignored.  

---

## 💡 Solution
### 1. Grievance Routing & Suggestion Assistant
- Classifies grievances into categories using **Zero-Shot Classification (facebook/bart-large-mnli)**.  
- Generates next-step actions using **FLAN-T5** (instruction-tuned model).  
  > Example: “My marks are missing on the portal.” → “Category: Exam. Visit Exam Cell or email exam@dtu.ac.in.”

### 2. Circular Summarizer
- Extracts circular text using **pdfplumber**.  
- Summarizes using **facebook/bart-large-cnn** for short, clear summaries.  
- Filters summary content by **branch** or **year** for relevance.

### 3. Telegram Circular Fetcher
- Automatically fetches PDFs from official DTU Telegram channels (e.g., NOTI).  
- Extracts and summarizes them in real time.  
- Stores extracted data locally for later reference.

### 4. Streamlit Interface
Two tabs for clarity:
- **Grievance Assistant** – text input → classify + suggest actions.  
- **Circular Insights** – view summaries of fetched or uploaded circulars.
## 🗂️ Project Structure

Hackdays_DTU.AI/
│
├── app.py                   # Main Streamlit interface
├── telegram_fetch.py        # Telegram circular extraction script
├── .env                     # API keys and environment variables
└── README.md

---

## 🚀 Setup & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/alexfdz1301/Hackdays_DTU.AI.git
cd Hackdays_DTU.AI
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables

Create a `.env` file in the root:

```
TELEGRAM_TOKEN=your_telegram_token
COMET_API_KEY=your_comet_key
```

### 4. Run the App

```bash
streamlit run app.py
```

### 5. (Optional) Fetch Telegram Circulars

```bash
python telegram_fetch.py
```

---

## 📊 Example Scenarios

| Input                             | Output                                                                |
| --------------------------------- | --------------------------------------------------------------------- |
| “Hostel Wi-Fi not working.”       | Category: Hostel → Suggestion: Contact Hostel Tech Office (Room 203). |
| Circular: “Mid-Sem Exam Schedule” | Summary: Key exam dates + relevant branch info displayed in UI.       |
| Telegram Circular posted          | Automatically downloaded, summarized, and added to app feed.          |

---

## 🧠 Learning Focus

* Practical understanding of **zero-shot classification** and **text summarization**
* Using **instruction-tuned models (FLAN-T5)** for contextual suggestions
* Building **end-to-end AI apps** with **Streamlit**
* Automating workflows using **Telegram API**
* Logging AI experiments via **Comet ML**

---

## 🔮 Future Enhancements

* Fine-tune the grievance classifier on DTU-specific data
* Add authentication (Student / Faculty)
* Store summarized circulars in a local database
* Deploy app on Streamlit Cloud or Hugging Face Spaces
* Add keyword-based search and chatbot interface

---

## 👤 Author

**Govind**
Solo participant – *DTU Internal Hackathon (“AI for DTU”)*
[GitHub Repository](https://github.com/alexfdz1301/Hackdays_DTU.AI)

