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
