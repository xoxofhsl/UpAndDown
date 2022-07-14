import streamlit as st
import random
import time
from PIL import Image
import os
'..\\resoursces\\down.png'
def start():
    st.session_state['randnum'] = random.randint(1, 100)
def grn():
    if 'randnum' in st.session_state:
        return st.session_state['randnum']
    return None
def clse():
    st.session_state.clear()
def getImage(imagename):
    curruntPath = os.path.abspath(os.path.dirname(__file__))
    # st.write(curruntPath, imagename)
    a =  os.path.join(curruntPath, '..', 'resources', imagename)
    st.write(a)
    return a
def UpAndDown():
    st.title('×º°”˜`”°º× ᴜᴘ ᴀɴᴅ ᴅᴏᴡɴ ×º°”˜`”°º×')
    sb = st.button("그에으임 스이즈악")
    if sb:
        start()
    computer = grn()
    if computer != None:
        n_inp = st.number_input('숫자를 맞춰보세요(1~100)', 1, 100)
        app_but = st.button('정답')
        if n_inp or app_but:
            if n_inp == computer:
                st.write('Right')
                imgpath = getImage('JeongDeop.png')
                image = Image.open(imgpath)
                getImage(image)
                time.sleep(2)
                clse()
            elif n_inp > computer:
                st.write('Down')
                imgpath = getImage('Down.png')
                image = Image.open(imgpath)
                getImage(image)
            else:
                st.write('Up')
                imgpath = getImage('Up.png')
                image = Image.open(imgpath)
                getImage(image)