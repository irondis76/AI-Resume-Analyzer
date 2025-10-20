import io
import json
import os
import requests
import streamlit as st

# Get API URL from environment variable or use default
API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")
st.title("🤖 AI Resume Analyzer (v1)")
st.markdown("Upload your resume to get AI-powered analysis and improvement recommendations.")

# API Status Check
with st.expander("🔧 API Status", expanded=False):
    try:
        health_resp = requests.get(f"{API_URL}/health", timeout=5)
        if health_resp.status_code == 200:
            st.success(f"✅ API is running at {API_URL}")
        else:
            st.error(f"❌ API returned status {health_resp.status_code}")
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Cannot connect to API at {API_URL}")
        st.info("Make sure the backend is running: `uv run uvicorn backend.api.main:app --reload`")

uploaded = st.file_uploader(
    "📄 Upload your resume (PDF or DOCX)", 
    type=["pdf", "docx"],
    help="Supported formats: PDF and DOCX files up to 10MB"
)

if uploaded:
    # Show file info
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("File Name", uploaded.name)
    with col2:
        st.metric("File Size", f"{uploaded.size / 1024:.1f} KB")
    with col3:
        st.metric("File Type", uploaded.type)
    
    if st.button("🚀 Analyze Resume", type="primary"):
        with st.spinner("🤖 AI is analyzing your resume... This may take 30-60 seconds."):
            files = {"file": (uploaded.name, uploaded.getvalue(), uploaded.type)}
            try:
                resp = requests.post(f"{API_URL}/analyze", files=files, timeout=120)
                resp.raise_for_status()
            except requests.exceptions.Timeout:
                st.error("⏰ Analysis timed out. Please try again with a smaller file.")
            except requests.exceptions.RequestException as e:
                st.error(f"❌ Error connecting to API: {e}")
                st.info("Make sure the backend is running and accessible.")
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
            else:
                data = resp.json()
                
                # Success message
                st.success("✅ Analysis complete!")
                
                # Executive Summary
                st.subheader("📊 Executive Summary")
                summary = data.get("summary", "No summary available.")
                st.info(summary)
                
                # Tabs for different views
                tabs = st.tabs(["🎯 Recommendations", "📋 Full Report", "🔍 Raw Data"]) 
                
                with tabs[0]:
                    st.subheader("🎯 Key Recommendations")
                    recs = data.get("overall_recommendations", [])
                    if recs:
                        for i, r in enumerate(recs, 1):
                            with st.container():
                                col1, col2 = st.columns([3, 1])
                                with col1:
                                    st.markdown(f"**{i}. [{r.get('category', 'General')}] {r.get('title', 'Recommendation')}**")
                                    st.write(r.get("description", ""))
                                with col2:
                                    impact = r.get('impact', 'Medium')
                                    priority = r.get('priority', 3)
                                    if impact == 'High':
                                        st.markdown("🔴 **High Impact**")
                                    elif impact == 'Medium':
                                        st.markdown("🟡 **Medium Impact**")
                                    else:
                                        st.markdown("🟢 **Low Impact**")
                                    st.markdown(f"Priority: {priority}")
                                st.divider()
                    else:
                        st.info("No specific recommendations available.")
                
                with tabs[1]:
                    st.subheader("📋 Detailed Report")
                    report = data.get("report_markdown", "No detailed report available.")
                    st.markdown(report)
                
                with tabs[2]:
                    st.subheader("🔍 Raw Analysis Data")
                    st.json(data)
                    
                    # Download buttons
                    col1, col2 = st.columns(2)
                    with col1:
                        st.download_button(
                            label="📥 Download JSON",
                            data=json.dumps(data, indent=2),
                            file_name=f"resume_analysis_{uploaded.name}.json",
                            mime="application/json"
                        )
                    with col2:
                        st.download_button(
                            label="📥 Download Report",
                            data=report,
                            file_name=f"resume_report_{uploaded.name}.md",
                            mime="text/markdown"
                        )


