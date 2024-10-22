import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Georges Zam - Professional Automation Services",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Ajout de la balise HTML pour la vérification Google
st.markdown("""
<head>
   <meta name="google-site-verification" content="PXT10Ykx5Xmkwq0sbBpDsRplXknMCH1-7akU8WXxSyc" />
   </head>
""", unsafe_allow_html=True)

# Sidebar avec brève introduction
with st.sidebar:
    st.write("""
    ## Georges Zamfiroiu
    Computer Engineering Student at CESI Nanterre
    Passionate about IT and automation.
    """)
    st.write("📧 [Email me](mailto:zamgeorges0@gmail.com)")

# Contenu de la page
st.title("Georges Zamfiroiu - Professional Automation Services")
st.write("""
Welcome to my professional automation services page. Here you will find information about the services I offer, including task automation, custom scripts, and database management.
""")

# Section d'introduction
st.header("Hello! 👋")
st.write("""
My name is Georges Zamfiroiu, and I am currently a computer engineering student at CESI Nanterre, one of the most renowned engineering schools in France. 
Passionate about information technology and always looking for new opportunities to apply my skills, I am here to help you achieve your projects with professionalism and efficiency.
""")

# Section des compétences avec des colonnes
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

# Section des certifications
st.header("Certifications")
st.write("""
- **Fusion 360 Certification**: Certified in using Fusion 360 for 3D CAD, CAM, and CAE.
""")

# Section Pourquoi Me Choisir avec des icônes
st.header("Why Choose Me?")
st.write("""
- 🎓 **Quality Education**: Currently pursuing an engineering degree at CESI Nanterre, I have gained a solid theoretical and practical foundation.
- 🔥 **Passion and Commitment**: I am passionate about IT and committed to delivering high-quality solutions for every project.
- 💡 **Innovative Mindset**: Always exploring new technologies and methods to enhance processes and results.
""")

# Section des services offerts avec des points
st.header("Services I Offer")
st.write("""
- 🌐 Website and mobile application development
- ⚙️ Custom programming and automated scripts
- 🗄️ Database design and management
- 🖧 System and network configuration and administration
- 🤖 Artificial intelligence and machine learning projects
""")

# Pied de page
st.write("Contact me: [zamgeorges0@gmail.com](mailto:zamgeorges0@gmail.com)")
