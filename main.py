import random

import streamlit as st
import data.d220519
import data.d220524
import data.d220526
import data.UPANDDOWN
import menu as m
from data import *
from data import UPANDDOWN

날짜 = ['메인 화면', m.DATE_0519, m.DATE_0524, m.DATE_0526, m.DATE_0628]
게임 = ['메인 화면', m.GAME_UPANDDOWN]
choice = st.sidebar.selectbox('날짜', 날짜)
game_choice = st.sidebar.selectbox('게임', 게임)

if choice == m.DATE_0519:
    if st.button('버튼 만드는 방법'):
        st.write(data.d220519.bt)
if choice == m.DATE_0524:
    if st.button('딕셔너리 반복문'):
        st.write(data.d220524.dicro)
if choice == m.DATE_0526:
    if st.button('버튼 나란히 만드는 방법'):
        st.write(data.d220526.co())
if choice == m.DATE_0628:
    pass
if game_choice == m.GAME_UPANDDOWN:
    UPANDDOWN.UpAndDown()