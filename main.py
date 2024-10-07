import streamlit as st

st.set_page_config(
    page_title="Hello World, this is my first streamlit project",
    page_icon="shark",
    layout="wide"

)

st.title("Hello my name is Ceyda, this is my first streamlit project!")
st.header("Ceyda Özarslan ")
st.subheader("Data Scientist")
st.text("+905446058252")  # st.text hiçbir tasarım özelliği olmadan eklenen metindir.
st.divider()
st.write(
    "My fundamental goal is to leverage IT internships and the Erasmus+ program to use technology for impactful solutions. Currently focused on developing security systems with AWS and Image Processing Techniques, my academic background in Computer Engineering and Management Information Systems drives my dedication to crafting interactive solutions.")
st.divider()

c1, c2, c3 = st.columns(3, gap='small')

with c1:
    st.subheader("Column One")
    st.divider()
    st.write(
        "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
    )
with c2:
    st.subheader("Column Two")
    st.divider()
    st.image("https://picsum.photos/450/300?random=1", "Column Two Image", use_column_width=True)
with c3:
    st.subheader("Column Three")
    st.divider()
    liste = [
        "a",
        "b",
        "c",
        "d",
        "e",
    ]
    for i in liste: st.write("&rarr;", i)
st.divider()
