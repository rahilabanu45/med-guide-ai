import streamlit as st
from PIL import Image
import json

st.set_page_config(page_title="MedGuide AI", page_icon="💊", layout="centered")

st.title("💊 MedGuide AI — Medicine Label & Safety Assistant")
st.caption("A local web app that keeps medicine label info in one place")
st.warning("⚠️ For education only. Not medical advice. Always consult doctor or pharmacist.")

# Load sample data
try:
    with open("med_data.json", "r") as f:
        med_db = json.load(f)
except:
    med_db = {}

# Upload
uploaded = st.file_uploader("Upload medicine strip / box photo", type=["jpg","jpeg","png"])

if uploaded:
    image = Image.open(uploaded)
    st.image(image, caption="Uploaded Label", width=300)
    
    st.divider()
    st.subheader("🔍 Extracted Text (Demo)")
    # Demo text - baad me EasyOCR connect karoge
    demo_text = "PARACETAMOL 500mg"
    st.code(demo_text)
    
    # Simple matching
    med_name = "paracetamol"
    if med_name in med_db:
        info = med_db[med_name]
        st.subheader(f"📋 Safety Info: {info['name']}")
        st.write(f"**Generic:** {info['generic']}")
        st.write(f"**Strength:** {info['strength']}")
        st.write(f"**Common Use:** {info['use']}")
        st.write(f"**Storage:** {info['storage']}")
        st.write(f"**Warning:** {info['warning']}")
    else:
        st.info("Sample data not found. Showing demo info.")
        st.write("**Generic:** Paracetamol 500mg")
        st.write("**Common Use:** Fever, mild pain — as per leaflet")
        st.write("**Storage:** Cool, dry place, below 30°C")
        st.write("**When to avoid:** If allergic to paracetamol")

st.divider()

# Interaction checker
st.subheader("💊💊 Interaction Checker (Demo)")
m1 = st.text_input("Medicine 1", placeholder="Paracetamol")
m2 = st.text_input("Medicine 2", placeholder="Alcohol")
if st.button("Check Interaction"):
    if m1 and m2:
        st.error(f"⚠️ Possible interaction between {m1} + {m2}: May increase liver load. Ask pharmacist. (Demo warning — not real medical advice)")
    else:
        st.write("Enter both names")

st.caption("Built by rahila banu | Educational Project | Data from MedlinePlus + local json")