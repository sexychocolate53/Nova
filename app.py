import streamlit as st
import requests
from PIL import Image

# Display avatar
nova_avatar = Image.open("images/nova.png")  # Make sure this image exists in your project
st.image(nova_avatar, caption="Meet Nova – Your Digital Strategy Agent", use_column_width=False, width=150)

st.markdown("### 👩🏽‍💻 Meet Nova – Your Lead Magnet & Email Specialist")
st.markdown("""
**Role Title:** Digital Strategy Agent  
**Name:** Nova  
**Mission:** Nova helps attract new clients to your credit repair business by creating irresistible lead magnets, building engaging email sequences, and automating the journey from "just looking" to loyal customer.

---

🎯 **Nova’s Top Responsibilities**

**Lead Magnet Creation**  
- Design and write powerful PDFs (e.g., “5 Steps to Boost Your Credit Fast”)  
- Tailor content for both beginners and experienced clients  
- Generate freebie ideas that convert leads  

**Email Sequence Builder**  
- Write welcome emails after downloads  
- Personalize follow-ups to stay connected  
- Suggest what to say and when to say it  

**Automation Assistant**  
- Recommend tools like Mailchimp, Systeme.io, or Flowdesk  
- Guide integration of lead magnets with signup forms  
- Help you create a smooth funnel  

---

🛠️ **Nova’s Toolbox**  
- PDF lead magnet templates  
- Email sequence copywriting  
- Funnel strategy tips  
- A/B testing suggestions  

---

💬 **Motto:**  
**Nova helps your leads feel seen, supported, and ready to take the next step!**
""")

# Chat box (optional)
user_question = st.text_input("💬 Ask Nova a question about lead magnets, emails, or digital strategy:")

def query_nova(prompt):
    full_prompt = f"You are Nova, the Digital Strategy Agent for a credit repair business. Answer only questions related to lead magnets, emails, and marketing strategy. If someone asks about disputes or business decisions, direct them to the appropriate agent (Tali, Valor, etc).\n\nQuestion: {prompt}\n\nAnswer:"
    
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "gemma:2b",
            "prompt": full_prompt,
            "stream": False
        }
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "Sorry, I'm having trouble reaching Nova right now."

if user_question:
    with st.spinner("Nova is thinking..."):
        answer = query_nova(user_question)
        st.markdown(f"**Nova's Answer:**\n\n{answer}")
