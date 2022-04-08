from django.shortcuts import render
import pdfkit
import streamlit as st
import wikipedia
import os
from jinja2 import Environment,  FileSystemLoader, select_autoescape
import keyboard as kb



st.set_page_config(layout="centered", page_icon="logo.jpeg",
                   page_title="Question Pdf")

st.header("QUESTION TO PDF")


# here coder for templating using jinja2
env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())

template = env.get_template("abhay.html")


txt = open("abhay.txt", "a")
question = st.text_input("question Please.......")


# this is code for question to find answer from wikipedia
lines = []
html = ""
combine = []
if st.button("add next question"):

    txt.write(question+"//")
    txt.close()
    with open('abhay.txt') as f:
        for line in f.readlines()[0].split("//"):
            lines.append(line)

    for i in range(len(lines)-1):

        answer = wikipedia.summary(lines[i], sentences=2).split(".")
        combine.append({"question": lines[i].upper(), "answer": answer[:-1]})

        # this code for show the queston answer in webpage
        st.subheader(lines[i])
        for j in answer[:-1]:
            st.write(j)

    # here render the template for html abhay.html file here use combine both question in list a seperate
    html = template.render(

        combine=combine

    )

    # create pdf from string using pdfkit
    data = pdfkit.from_string(html, False)


    st.success("Welcome! You can download the pdf for the question's answer.")
    # here code for genrate download btn
    st.download_button(label="Download",
                       data=data,
                       file_name=lines[0]+".pdf",
                       mime="image/png")
         
    st.balloons()

 


# here use the button for delete previous question
if st.button("previous clean question") == True:

    os.remove("abhay.txt")


# question=f"""<h1 style="color:red">{ }?<h1>"""
