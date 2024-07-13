import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Function to load images from a URL
def load_image(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        return None

# Set the page layout
st.set_page_config(layout="wide", page_title="Georges Zamfiroiu - Computer Engineering Student")

# Sidebar with profile picture and brief introduction
with st.sidebar:
    profile_img_url = "https://avatars.githubusercontent.com/u/your_github_user_id"  # replace with your actual GitHub user ID image link
    profile_img = load_image(profile_img_url)
    if profile_img:
        st.image(profile_img, caption="Georges Zamfiroiu", width=150)
    st.write("""
    ## Georges Zamfiroiu
    Computer Engineering Student at CESI Nanterre
    Passionate about IT and automation.
    """)
    st.write("📧 [Email me](mailto:zamgeorges0@gmail.com)")
    st.write("💼 [GitHub](https://github.com/GeorgesZam)")

# Page title
st.title("Georges Zamfiroiu - Computer Engineering Student")

# Introduction
st.header("Hello! 👋")
st.write("""
My name is Georges Zamfiroiu, and I am currently a computer engineering student at CESI Nanterre, one of the most renowned engineering schools in France. 
Passionate about information technology and always looking for new opportunities to apply my skills, I am here to help you achieve your projects with professionalism and efficiency.
""")

# Skills section with columns
st.header("My Skills")
col1, col2 = st.columns(2)

with col1:
    st.write("""
    - **Web and Mobile Development**: Design and development of websites and mobile applications using the latest technologies.
    - **Programming**: Proficient in several programming languages such as Python, Java, C++, and JavaScript.
    """)

with col2:
    st.write("""
    - **Databases**: Design, implementation, and management of relational and non-relational databases.
    - **Systems and Networks**: Administration of systems and networks, cybersecurity, and infrastructure management.
    - **Artificial Intelligence and Machine Learning**: Development of predictive models and data analysis.
    """)

# Certification section with images
st.header("Certifications")
st.write("""
- **Fusion 360 Certification**: Certified in using Fusion 360 for 3D CAD, CAM, and CAE.
""")
fusion_img_url = "https://via.placeholder.com/200x100"  # replace with an actual image URL if available
fusion_img = load_image(fusion_img_url)
if fusion_img:
    st.image(fusion_img, caption="Fusion 360 Certification", width=200)

# Why Choose Me section with icons
st.header("Why Choose Me?")
st.write("""
- 🎓 **Quality Education**: Currently pursuing an engineering degree at CESI Nanterre, I have gained a solid theoretical and practical foundation.
- 🔥 **Passion and Commitment**: I am passionate about IT and committed to delivering high-quality solutions for every project.
- 💡 **Innovative Mindset**: Always exploring new technologies and methods to enhance processes and results.
""")

# Services section with bullet points
st.header("Services I Offer")
st.write("""
- 🌐 Website and mobile application development
- ⚙️ Custom programming and automated scripts
- 🗄️ Database design and management
- 🖧 System and network configuration and administration
- 🤖 Artificial intelligence and machine learning projects
""")



# Contact section with a form
st.header("Contact Me")
st.write("I am eager to collaborate with you and contribute to the success of your projects. Feel free to contact me to discuss your specific needs.")

contact_form = st.form(key='contact_form')
name = contact_form.text_input('Name')
email = contact_form.text_input('Email')
message = contact_form.text_area('Message')
submit_button = contact_form.form_submit_button(label='Send')

if submit_button:
    st.write(f"Thank you {name}! I will get back to you at {email} soon.")

# Footer
st.write("**Contact me today to start our collaboration!**")
