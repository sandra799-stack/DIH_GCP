import streamlit as st
import requests

# Page config
st.set_page_config(page_title="DBot", layout="wide")

st.image("chatbotD.png", width=250) 
GITHUB_CLIENT_ID = "Ov23li7VLjufh99QANN9"
GITHUB_CLIENT_SECRET = "1a1a346a1c8bcb35d5a3e8920e05b59f50df05c8"
REDIRECT_URI = "http://localhost:8501/"  # or your deployed domain
github_auth_url = f"https://github.com/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=read:user user:email"

query_params = st.query_params
code = query_params.get("code")

if code:
    st.info("🔄 Exchanging GitHub code for token...")

    # Exchange code for access token
    token_url = "https://github.com/login/oauth/access_token"
    headers = {"Accept": "application/json"}
    data = {
        "client_id": GITHUB_CLIENT_ID,
        "client_secret": GITHUB_CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI
    }

    response = requests.post(token_url, headers=headers, data=data)
    access_token = response.json().get("access_token")

    if access_token:
        st.success("✅ GitHub Login Successful!")
        st.session_state["access_token"] = access_token
        # Fetch user data
        user_resp = requests.get(
            "https://api.github.com/user",
            headers={"Authorization": f"Bearer {access_token}"}
        )
        user_data = user_resp.json()
        st.write("👤 Logged in as:", user_data.get("login"))

        # Optional: Clear query params from URL after login
        st.query_params.clear()

    else:
        st.error("❌ GitHub Login Failed.")  
# Custom styles
st.markdown("""
<style>
/* General Styles */
body {
    font-family: 'Segoe UI', sans-serif;
    background-color: #f9f9f9;
    margin: 0;
    padding: 0;
}

/* Hero Section */
.hero {
    height: 100vh;
    background-color: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    padding: 0 2rem;
}
.hero h1 {
    font-size: 4rem;
    margin-bottom: 1rem;
}
.hero p {
    font-size: 1.25rem;
    color: #666;
    margin-bottom: 2rem;
}
.hero .cta-btn {
    padding: 0.75rem 2rem;
    background-color: #4f46e5;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
    text-decoration: none;
}

/* Intelligent Features Section */
.intelligent-section {
    height: 100vh;
    width: 100%;
    background-color: #f5f7fa;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 2rem;
    box-sizing: border-box;
    text-align: center;
}
.intelligent-section h2 {
    font-size: 3rem;
    margin-bottom: 2rem;
    font-weight: 700;
}
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    width: 100%;
    max-width: 1100px;
    padding: 0 1rem;
}
.feature-card {
    background: white;
    border-radius: 18px;
    padding: 2rem;
    box-shadow: 0 8px 24px rgba(0,0,0,0.07);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.feature-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 14px 28px rgba(0,0,0,0.12);
}
.feature-card h3 {
    margin-bottom: 0.75rem;
    font-size: 1.4rem;
    font-weight: 600;
}
.feature-card p {
    color: #555;
    font-size: 1rem;
}

/* CTA Section */
.cta-section {
    padding: 4rem 2rem;
    text-align: center;
    background-color: #ffffff;
}
.cta-section h2 {
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
}
.cta-form input[type="email"] {
    padding: 0.7rem;
    width: 300px;
    max-width: 80%;
    border-radius: 8px;
    border: 1px solid #ccc;
    margin-right: 0.5rem;
}
.cta-form button {
    padding: 0.7rem 1.5rem;
    background-color: #4f46e5;
    color: white;
    border: none;
    border-radius: 8px;
    font-size: 1rem;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<style>
.logo {
    font-size: 2.8rem;
    font-weight: 700;
    display: inline-flex;
    align-items: flex-end;
    gap: 0.2rem;
    line-height: 1;
}
.d-letter {
    position: relative;
    display: inline-block;
}
.green-dot {
    position: absolute;
    bottom: 0.1rem;
    right: -0.4rem;
    height: 0.5rem;
    width: 0.5rem;
    background-color: #22c55e;
    border-radius: 50%;
    box-shadow: 0 0 4px rgba(34,197,94,0.4);
}
.bot-text {
    font-weight: 500;
}
</style>

<div class="hero">
    <h1 class="logo">
      <span class="d-letter">D<span class="green-dot"></span></span>
      <span class="bot-text">Bot</span>
    </h1>
    <p>Your silent coding partner. Smarter suggestions. Faster flow.</p>
    <a href="#intelligent-features" class="cta-btn">Explore Features</a>
</div>
""", unsafe_allow_html=True)
# Intelligent Features Section
st.markdown("""
<div class="intelligent-section" id="intelligent-features">
    <h2>Intelligent Features</h2>
    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">📝</div>
            <h3>Standup Meeting Notes</h3>
            <p>Keep track of your daily standup meetings, what was done, and what's planned.</p>
        </div>
        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <h3>Security Analysis</h3>
            <p>Detect security vulnerabilities and receive guidance to fix potential issues.</p>
        </div>
        <div class="feature-card">
            <div class="step-icon">🧠</div>
            <h3>Code Quality</h3>
            <p>Get insights on code quality, complexity and maintainability with actionable tips.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.feature-container {
    text-align: center;
    padding: 2rem 0;
}

.feature-icon {
    font-size: 3rem;
    color: #4f46e5;
    margin-bottom: 1rem;
}

.feature-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #111827;
}

.feature-desc {
    font-size: 1rem;
    color: #6b7280;
}
</style>
""", unsafe_allow_html=True)

# Define custom CSS for styling
st.markdown("""
<style>
.how-it-works {
    padding: 2rem 0;
    text-align: center;
}

.how-it-works h2 {
    font-size: 2.5rem;
    margin-bottom: 2rem;
    color: #1e293b;
}

.step {
    background-color: #f9fafb;
    border-radius: 1rem;
    padding: 1.5rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transition: transform 0.3s ease;
    text-align: center;
}

.step:hover {
    transform: translateY(-5px);
}

.step-icon {
    font-size: 2.5rem;
    color: #4f46e5;
    margin-bottom: 1rem;
}

.step-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: #111827;
}

.step-desc {
    font-size: 1rem;
    color: #6b7280;
}
</style>
""", unsafe_allow_html=True)

# Inject custom CSS for layout
st.markdown("""
<style>
.step-section {
    padding: 3rem 1rem;
    text-align: center;
}

.step-section h2 {
    font-size: 2.5rem;
    margin-bottom: 3rem;
    color: #1e293b;
}

.step-row {
    display: flex;
    justify-content: center;
    gap: 2rem;
    flex-wrap: wrap;
}

.step-card {
    background: #f9fafb;
    padding: 2rem 1.5rem;
    border-radius: 1rem;
    width: 260px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    position: relative;
    text-align: center;
    transition: transform 0.3s ease;
}

.step-card:hover {
    transform: translateY(-5px);
}

.step-number {
    font-size: 0.9rem;
    font-weight: bold;
    background-color: #4f46e5;
    color: white;
    padding: 0.3rem 0.75rem;
    border-radius: 999px;
    position: absolute;
    top: -12px;
    left: 50%;
    transform: translateX(-50%);
}

.step-title {
    font-size: 1.3rem;
    font-weight: 600;
    margin-top: 2rem;
    color: #111827;
}

.step-desc {
    font-size: 0.95rem;
    color: #6b7280;
    margin-top: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# HTML layout with 3 cards
st.markdown(f"""
<div class="step-section">
  <h2>How It Works</h2>
  <div class="step-row">
    <div class="step-card">
      <div class="step-number">01</div>
      <div class="step-title">Connect Your Codebase</div>
      <div class="step-desc">Simply connect your repository or upload your code files to get started.</div>
      <div style="margin-top: 15px;">
        <a href="{github_auth_url}" target="_self">
            <button style="padding: 10px 20px; font-size: 14px; background-color: #24292e; color: white; border: none; border-radius: 6px; cursor: pointer;">
                <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="16" style="vertical-align: middle; margin-right: 8px;">
                Login with GitHub
            </button>
        </a>
      </div>
    </div> 
     <div class="step-card">
      <div class="step-number">02</div>
      <div class="step-title">AI Analysis</div>
      <div class="step-desc">Our engine reads and understands your code structure and intent.</div>
    </div>  
    <div class="step-card">
      <div class="step-number">03</div>
      <div class="step-title">Receive Insights</div>
      <div class="step-desc">Get detailed analysis with performance metrics, security issues, and quality insights.</div>
    </div>        
  </div>

</div>
""", unsafe_allow_html=True)