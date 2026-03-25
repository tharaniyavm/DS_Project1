import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Project Index", page_icon="🍴", layout="wide")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .project-card {
        background-color: #1f2937;
        padding: 40px;
        border-radius: 20px;
        border-left: 10px solid #00D1B2;
        box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        margin-bottom: 25px;
    }
    .skill-tag {
        display: inline-block;
        background-color: #374151;
        color: #00D1B2;
        padding: 5px 15px;
        border-radius: 50px;
        margin: 5px;
        font-size: 0.85rem;
        font-weight: 600;
        border: 1px solid #4b5563;
    }
    .domain-text {
        color: #9ca3af;
        font-style: italic;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("📂 Project Portfolio")
st.divider()

# --- PROJECT CARD ---
with st.container():
    st.markdown(f"""
    <div class="project-card">
        <h1 style='color: white; margin-bottom: 0;'>Uber Eats Bangalore</h1>
        <p style='color: #00D1B2; font-size: 1.5rem; font-weight: 300;'>Restaurant Intelligence & Decision Support Systems</p>
        <hr style='border-color: #374151;'>  Project Completed - By VM Tharaniya
       
    </div>
    """, unsafe_allow_html=True)

# --- SKILLS & ACTIONS SECTION ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🛠️ Technical Skills Acquired")
    skills = ["Python", "Pandas", "SQL", "Streamlit", "Statistics", "Data Science", "Data Cleaning","Data Engineering"]
    
    # Create stylish tags using HTML
    skill_html = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
    st.markdown(skill_html, unsafe_allow_html=True)

with col2:
     
    if st.button("Source Code (GitHub)", use_container_width=True):
        st.info("https://github.com/tharaniyavm/DS_Project1")

# --- PROJECT DESCRIPTION/ABSTRACT ---
st.write("---")
with st.expander("📖 Read Project Abstract"):
    st.write("""
        This project focuses on analyzing the restaurant ecosystem in Bangalore using Uber Eats data. 
        By leveraging **MySQL** for data storage and **Pandas** for processing, the system provides 
        actionable insights into market trends, pricing strategies, and customer preferences through 
        an interactive **Streamlit** interface.
    """)

# --- FOOTER ---
st.markdown("<br><center><small>Built with ❤️ using Streamlit</small></center>", unsafe_allow_html=True)
