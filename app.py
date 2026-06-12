import streamlit as st
from models.evidence_builder import build_evidence
from models.generator import generate_report
from models.verifier import detect_hallucinations

st.title("🧠 Grounded Medical Report Generator")

history = st.text_input("Patient History")
image = st.file_uploader("Upload X-ray Image")

if st.button("Generate Report"):

    evidence = build_evidence(image, history)

    report = generate_report(evidence)

    result = detect_hallucinations(report, evidence)

    st.subheader("📄 Generated Report")
    st.text(report)

    st.subheader("⚠️ Hallucination Check")
    st.json(result)
