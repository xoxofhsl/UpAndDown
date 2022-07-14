import streamlit as st
def co():
    col1, col2, col3 = st.columns(3)
    col1.write('''
    ```python
    import streamlit as st
    col1, col2 = st.column(2)
    col1.button(버튼1이름)
    col2.button(버튼2이름)
    ```
    이렇게 하면 버튼 2개가 나란히 만들어진다.
    --->>>''')
    col2.button('버튼1')
    col3.button('버튼2')