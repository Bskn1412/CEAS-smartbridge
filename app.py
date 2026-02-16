import os
import json
import base64
import requests
import streamlit as st
from PIL import Image
from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from dotenv import load_dotenv


# -----------------------------
# CONFIG
# -----------------------------
load_dotenv()

API_KEY = os.getenv("NVIDIA_API_KEY")

URL = "https://integrate.api.nvidia.com/v1/chat/completions"

MODEL = "meta/llama-3.2-90b-vision-instruct"

HISTORY_FILE = "history.json"


# -----------------------------
# HISTORY
# -----------------------------
def load_history():

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    return []


def save_history(data):

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# -----------------------------
# PDF EXPORT
# -----------------------------
def create_pdf(entry):

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

    c = canvas.Canvas(filename, pagesize=A4)

    w, h = A4

    y = h - 40


    # Title
    c.setFont("Helvetica-Bold", 20)
    c.drawString(40, y, "AI Image Analysis Report")

    y -= 40


    # Date
    c.setFont("Helvetica", 10)
    c.drawString(40, y, f"Date: {entry['time']}")

    y -= 30


    # Prompt
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Prompt:")

    y -= 15

    c.setFont("Helvetica", 10)

    for line in entry["prompt"].split("\n"):
        c.drawString(40, y, line)
        y -= 14


    y -= 20


    # Result
    c.setFont("Helvetica-Bold", 12)
    c.drawString(40, y, "Result:")

    y -= 15

    c.setFont("Helvetica", 10)

    text = c.beginText(40, y)

    for line in entry["result"].split("\n"):
        text.textLine(line)

    c.drawText(text)


    # Image
    img_bytes = base64.b64decode(entry["image_base64"])

    img = Image.open(BytesIO(img_bytes))

    img_path = "temp.jpg"

    img.save(img_path)

    c.showPage()

    c.drawImage(img_path, 40, 200, width=500, preserveAspectRatio=True)

    c.save()

    os.remove(img_path)

    return filename


# -----------------------------
# STREAMLIT SETUP
# -----------------------------
st.set_page_config("Image AI Inspector", layout="wide")

st.title("🏗️ Civil Engineering AI Studio")


# Load history
if "history" not in st.session_state:

    st.session_state.history = load_history()


history = st.session_state.history


# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📚 History")

if history:

    selected = st.sidebar.radio(
        "Saved Reports",
        range(len(history)),
        format_func=lambda i: history[i]["time"]
    )

else:
    selected = None
    st.sidebar.info("No reports yet")


# -----------------------------
# MAIN UI
# -----------------------------
uploaded = st.file_uploader("Upload Image", ["jpg", "png", "jpeg"])

prompt = st.text_input("Optional instruction")


if uploaded:

    img = Image.open(uploaded).convert("RGB")

    st.image(img, width=350)


    buf = BytesIO()
    img.save(buf, format="JPEG")

    img_b64 = base64.b64encode(buf.getvalue()).decode()


    if st.button("Analyze"):

        with st.spinner("Processing..."):

            if not prompt.strip():
                prompt = "Describe this image in detail."

            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }

            payload = {
                "model": MODEL,
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{img_b64}"
                                }
                            }
                        ]
                    }
                ],
                "max_tokens": 600
            }

            r = requests.post(URL, headers=headers, json=payload)

            if r.status_code == 200:

                result = r.json()["choices"][0]["message"]["content"]

                entry = {
                    "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "prompt": prompt,
                    "image_base64": img_b64,
                    "result": result
                }

                history.append(entry)

                save_history(history)

                st.success("Done!")

                st.markdown(result)

            else:
                st.error("API Error")


# -----------------------------
# VIEW HISTORY
# -----------------------------
if selected is not None:

    st.divider()

    st.subheader("📄 Saved Report")

    item = history[selected]

    img = Image.open(BytesIO(base64.b64decode(item["image_base64"])))

    st.image(img, width=400)

    st.write("**Prompt:**", item["prompt"])

    st.write("**Result:**")

    st.write(item["result"])


    # PDF Button
    if st.button("📥 Export PDF"):

        pdf = create_pdf(item)

        with open(pdf, "rb") as f:

            st.download_button(
                "Download Report",
                f,
                file_name=pdf,
                mime="application/pdf"
            )
