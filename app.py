import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
import pdfplumber
import pytesseract
from PIL import Image
from telegram_fetch import fetch_and_download  # ✅ updated import

# --- LOGIN MOCK PAGE ---
def login_screen():
    st.title("🔐 DTU AI Assistant Login")
    st.markdown("Welcome! Please sign in to access the Circular Dashboard.")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username and password:
            st.session_state["authenticated"] = True
            st.success(f"Welcome, {username}!")
            st.rerun()
        else:
            st.error("Please enter both username and password to continue.")


# --- Initialize login state ---
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login_screen()
    st.stop()
# --- Load environment ---
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    st.error("❌ Missing GOOGLE_API_KEY in .env file.")
    st.stop()

# --- Initialize the GenAI client (latest API) ---
client = genai.Client(api_key=API_KEY)

# --- Branch Maps ---
BRANCH_MAP_25 = {
    "A01": "CSE","A02": "CSE","A03": "CSE","A04": "CSE","A05": "CSE","A06": "CSE",
    "A07": "DA","A08": "IT","A09": "IT","A10": "CY","A11": "ECE","A12": "ECE",
    "A13": "ECE","A14": "VL","A15": "EE","A16": "EE","A17": "EE","A18": "EE","A19": "EE",
    "B01": "SE","B02": "SE","B03": "SE","B04": "MCE","B05": "MCE","B06": "MCE",
    "B07": "EP","B08": "EP","B09": "ME","B10": "ME","B11": "ME","B12": "ME",
    "B13": "MAM","B14": "CHE","B15": "CHE","B16": "Civil","B17": "Civil","B18": "ENE","B19": "BT"
}

# --- Helper Functions ---
def extract_text(file):
    """Extracts text from PDFs or images."""
    if file.name.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            return "\n".join([p.extract_text() for p in pdf.pages if p.extract_text()])
    elif file.type.startswith("image/"):
        return pytesseract.image_to_string(Image.open(file))
    else:
        return file.read().decode("utf-8", errors="ignore")

def interpret_circular(text):
    """Uses Gemini 2.0 Flash to summarize and map branches."""
    prompt = f"""
    Analyze the following DTU circular.
    1. Summarize it in 2-3 lines.
    2. Identify the related branches using this mapping:
    {BRANCH_MAP_25}
    3. Classify the type of notice (Exam, Holiday, Result, General).
    Circular Text:
    {text}
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

# --- Streamlit Interface ---
st.set_page_config(page_title="DTU Circular Interpreter", layout="wide")
st.title("📜 DTU Circular Interpreter (Gemini 2.0 API)")

# --- Manual Upload ---
uploaded = st.file_uploader("Upload DTU circular (PDF/Image/Text):")

if uploaded:
    with st.spinner("Extracting and analyzing..."):
        extracted = extract_text(uploaded)
        st.text_area("Extracted Text Preview:", extracted[:2000])
        result = interpret_circular(extracted)
        st.subheader("AI Interpretation")
        st.write(result)

# --- Telegram Auto Fetch Section ---
st.header("DTU Circular Auto Fetch")

if st.button("Fetch & Summarize Latest Telegram Circulars"):
    docs = fetch_and_download(limit=3)
    if not docs:
        st.warning("No circulars found.")
    else:
        for doc in docs:
            st.write(f"📄 Processing: {doc['name']}")
            with open(doc["path"], "rb") as f:
                extracted = extract_text(f)
            result = interpret_circular(extracted)
            st.success(f"✅ {doc['name']} summarized:")
            st.write(result)
