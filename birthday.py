import streamlit as st
import datetime
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Amish Mahmood's Birthday", layout="centered")

# ------------------ 🎨 CSS STYLES ------------------ #
st.markdown("""
    <style>
    html, body, .stApp {
        height: 100%;
        margin: 0;
        background: linear-gradient(-45deg, #a2d4f6, #80caff, #c1e0ff, #b2d8ff);
        background-size: 600% 600%;
        animation: gradientShift 20s ease infinite;
        font-family: 'Comic Sans MS', cursive;
        color: #002147;
        text-align: center;
    }

    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    .countdown-box {
        background-color: #ffffffdd;
        color: black;
        padding: 20px;
        border-radius: 15px;
        font-size: 1.5rem;
        display: inline-block;
        margin-top: 30px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
    }

    .footer {
        font-size: 1.3rem;
        margin-top: 40px;
        color: #004080;
    }

    .gift-btn {
        background-color: #ff69b4;
        color: white;
        padding: 12px 25px;
        font-size: 18px;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        margin-top: 30px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    .gift-box {
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ 🎉 TITLE ------------------ #
st.markdown("<h1>🎉 Happy 1st Birthday Amish Mahmood! 🎉</h1>", unsafe_allow_html=True)

# ------------------ ⏳ COUNTDOWN ------------------ #
today = datetime.datetime.now()
birthday = datetime.datetime(today.year, 6, 26)
if today > birthday:
    birthday = birthday.replace(year=today.year + 1)

diff = birthday - today
days = diff.days
hours, remainder = divmod(diff.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

st.markdown(
    f"<div class='countdown-box'>⏳ Countdown to next birthday:<br> {days} days, {hours} hours, {minutes} minutes, {seconds} seconds</div>",
    unsafe_allow_html=True
)

# ------------------ 📸 LOCAL BABY IMAGE ------------------ #
st.image("amish.jpg", caption="🎂 Little Birthday Star!", use_column_width=True)

# ------------------ 📦 GIFT BUTTON ------------------ #
if st.button("🎁 Open Gift!"):
    st.success("🎉 Surprise! Wishing you a life full of love and laughter, Amish! 💙")
    st.balloons()
    st.image("amish.jpg", caption="Here's a cute gift for you!", use_column_width=True)

# ------------------ 🎈 FLOATING BALLOONS ANIMATION ------------------ #
balloon_html = """
<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;">
"""
for _ in range(35):
    left = random.randint(0, 100)
    delay = round(random.uniform(0, 4), 2)
    hue = random.randint(200, 240)
    balloon_html += f"""
    <div style="
        position: absolute;
        bottom: -100px;
        left: {left}vw;
        width: 40px;
        height: 60px;
        background: hsl({hue}, 80%, 65%);
        border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
        animation: floatUp {6 + delay}s ease-in infinite;
        animation-delay: {delay}s;
        opacity: 0.9;
    "></div>
    """
balloon_html += """
<style>
@keyframes floatUp {
  0% { transform: translateY(0); opacity: 1; }
  100% { transform: translateY(-120vh); opacity: 0; }
}
</style>
</div>
"""
components.html(balloon_html, height=600)

# ------------------ 💌 FOOTER ------------------ #
st.markdown("<div class='footer'>💙 With love, blessings, and joyful vibes for little Amish!</div>", unsafe_allow_html=True)
