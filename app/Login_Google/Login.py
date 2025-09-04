import streamlit as st
from streamlit_oauth import OAuth2Component

# ========================
# Google OAuth Credentials
# (Replace with your own)
# ========================
CLIENT_ID = "505247402568-sbksip2qrr7dqr2hm7h789anoomj6v1o.apps.googleusercontent.com"
CLIENT_SECRET = "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"  # <-- paste from Console

AUTHORIZE_URL = "https://accounts.google.com/o/oauth2/auth"
TOKEN_URL = "https://oauth2.googleapis.com/token"
REFRESH_TOKEN_URL = "https://oauth2.googleapis.com/token"
REVOKE_TOKEN_URL = "https://oauth2.googleapis.com/revoke"

REDIRECT_URI = "http://localhost:8501"   # must match what you set in Console
SCOPE = "openid email profile"

# ========================
# Initialize OAuth
# ========================
oauth2 = OAuth2Component(
    CLIENT_ID,
    CLIENT_SECRET,
    AUTHORIZE_URL,
    TOKEN_URL,
    REFRESH_TOKEN_URL,
    REVOKE_TOKEN_URL
)

# ========================
# Streamlit UI
# ========================
st.title("🔑 Google Login Demo")

if "token" not in st.session_state:
    result = oauth2.authorize_button("Login with Google", REDIRECT_URI, SCOPE)

    if result and "token" in result:
        st.session_state.token = result["token"]
        st.experimental_rerun()

else:
    st.success("✅ You are logged in!")
    st.json(st.session_state.token)

    if st.button("Logout"):
        del st.session_state["token"]
        st.experimental_rerun()
