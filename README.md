# MedGuide AI — Medicine Label & Safety Assistant

A local web app that helps students understand medicine labels in one place: scan a strip, extract text, and show simple safety info.

Python + EasyOCR on backend, Streamlit on frontend, and gpt-oss:20b for simplifying leaflet. No login, no data stored. Educational use only.

> ⚠️ **Disclaimer:** For education only. Not medical advice. Always consult doctor or pharmacist. No dose suggestion, no prescription.

# 💊 MedGuide AI — Medicine Label & Safety Assistant

### 🔴 LIVE APP LINK: https://med-guide-ai.streamlit.app

> Click above link to see live demo

A local web app that keeps medicine label info in one place.

### Features

| Area | What it does |
| :--- | :--- |
| **Label Scan** | Upload medicine strip / box photo. OCR reads name, dosage, expiry. Validates image quality. |
| **Text Extract** | Cleans OCR text, shows generic name, strength, manufacturer. Filtered before it's shown. |
| **Safety Info** | Shows common uses, storage, how to take, when to avoid. Data from MedlinePlus and local json. |
| **Simple Language** | Converts leaflet language to easy English. No API key needed, runs locally. |
| **Interaction Check** | Add 2 medicine names, checks known interaction list. Shows warning to ask pharmacist. |
| **Dashboard** | Recent scans, quick tips, expiry alert. All numbers come from current session. |

### Project structure

medguide-ai/
├── app.py              # main Streamlit app, all views
├── ocr_utils.py        # OCR cleaning logic
├── med_data.json       # local medicine info (20 samples)
├── requirements.txt    # pip dependencies
├── style.css           # styling
└── README.md


Streamlit serves the frontend itself, so there is one process, one address.

### Quick start

backend + frontendpython -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py


Then open http://localhost:8501

### API overview

All responses look like {"medicine": "Paracetamol", "strength": "500mg"}

- Scan: POST /scan - image upload
- Extract: POST /api/extract - OCR text
- Info: POST /api/info - {"name": "Paracetamol"}
- Safety: GET /api/safety - returns uses, storage, warnings

### Data

Local file med_data.json with 20 sample medicines. OCR processed in memory. Nothing stored server-side. Every scan is temporary. Data sourced from open info like MedlinePlus.

### Limits

- OCR may misread blurry images. Clear photo needed.
- Info from open sources and sample json. May be incomplete.
- AI output depends on model. Invalid responses are rejected with error rather than replaced with made-up content.
- No dose suggestion for a specific person. No prescription generation.
- Educational prototype only. Do not use for real medical decisions. Talk to pharmacist / doctor.
- The browser loads Streamlit, so it needs internet. No authentication. Run locally and don't expose it to the internet as is.

### Built By

rahila banu — medguide_ai Project | 
