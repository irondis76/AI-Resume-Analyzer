import io
import json
import requests
import streamlit as st

API_URL = st.secrets.get("API_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("AI Resume Analyzer (v1)")

uploaded = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])
if uploaded:
    with st.spinner("Analyzing resume..."):
        files = {"file": (uploaded.name, uploaded.getvalue(), uploaded.type)}
        try:
            resp = requests.post(f"{API_URL}/analyze", files=files, timeout=120)
            resp.raise_for_status()
        except Exception as e:
            st.error(f"Error: {e}")
        else:
            data = resp.json()
            st.subheader("Executive Summary")
            st.write(data.get("summary", ""))

            tabs = st.tabs(["Recommendations", "Report", "Raw JSON"]) 
            with tabs[0]:
                recs = data.get("overall_recommendations", [])
                for r in recs:
                    st.markdown(f"**[{r.get('category')}] {r.get('title')}** — {r.get('impact')} (P{r.get('priority')})")
                    st.write(r.get("description", ""))
                    st.divider()
            with tabs[1]:
                st.markdown(data.get("report_markdown", ""))
            with tabs[2]:
                st.code(json.dumps(data, indent=2))


