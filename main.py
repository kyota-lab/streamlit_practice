from turtle import right
import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!'
# left_column,right_column = st.columns(2)
# button=left_column.button('右')
# if button:
#     right_column.write('sbcs')

# expander=st.expander('qa')
# expander.write('qa')

# option1 = st.slider('?',0,100,50)

# option2 = st.text_input('?')

# 'abc',option1,option2

# img = Image.open('沖縄イメージ1.jpg')
# if(st.checkbox('show Image')):
#     st.image(img,caption='okinawa',use_column_width=True)
