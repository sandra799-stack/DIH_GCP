import streamlit as st
import requests

if "access_token" in st.session_state:
    token = st.session_state["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Get user repos
    repos_resp = requests.get("https://api.github.com/user/repos", headers=headers, params={"per_page": 100})
    repos = repos_resp.json()

    if isinstance(repos, list) and repos:
        repo_names = [repo["full_name"] for repo in repos]  # format: owner/repo
        selected_repo = st.selectbox("📂 Choose a repo to open in Codespaces", repo_names)

        if selected_repo:
            # Dynamic Markdown Button
            codespaces_url = f"https://github.com/codespaces/new?repo={selected_repo}"
            st.markdown(f"""
            <a href="{codespaces_url}" target="_blank">
                <img src="https://github.com/codespaces/badge.svg" alt="Open in GitHub Codespaces">
            </a>
            """, unsafe_allow_html=True)
    else:
        st.warning("No repos found or token invalid.")
else:
    st.warning("Please log in with GitHub first.")
