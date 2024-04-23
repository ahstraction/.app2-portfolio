import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    image_path = (
        "C:/Users/Dell/OneDrive/Documents/Python/.app2-portfolio/images/photo.jpg")
    st.image(image_path)

with col2:
    st.title("Ahsan Ali")
    content = """I am Ahsan Ali, a passionate and results-oriented Computer Science graduate from The University of Lahore, Pakistan. 
    My interest lies in AI, Machine Learning, and Python, and I am always eager to learn and grow in these fields. 
    I have a strong foundation in programming, data analysis, and machine learning, and have worked on several innovative projects. 
    These include developing a web-based e-commerce platform for visually impaired users, sign language detection using Tensor Flow and Keras, and web scraping using Selenium. 
    I also have experience in creating a WordPress website dedicated to providing comprehensive information and e-commerce solutions for nutraceutical products. 
    My proficiency extends to Natural Language Processing (NLP), Data Visualization, Deep Learning, Image Processing, Numpy, Pandas, Selenium, PyTorch, TensorFlow, MySQL, Microsoft Office, and Python. 
    I am actively seeking opportunities where I can apply my skills and contribute to real-world solutions.
"""
    st.info(content)

note = "Below you can find some of the apps I have built in Python. Feel free to contact me!"
st.write(note)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv(
    "C:/Users/Dell/OneDrive/Documents/Python/.app2-portfolio/data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(
            "C:/Users/Dell/OneDrive/Documents/Python/.app2-portfolio/images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(
            "C:/Users/Dell/OneDrive/Documents/Python/.app2-portfolio/images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
