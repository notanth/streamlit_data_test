import streamlit as st
import pandas as pd
import numpy as np

st.text('testing gh updates in browser')







st.text('now flexin wit github.dev testing testing')

st.text('Fixed width text')

st.markdown('_Markdown_') # see #*

st.caption('Balloons. Hundreds of them...')

st.latex(r''' e^{i\pi} + 1 = 0 ''')

st.write('Most objects') # df, err, func, keras!

st.write(['st', 'is <', 3]) # see *

st.title('My title')

st.header('My header')

st.subheader('My sub')

st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)
