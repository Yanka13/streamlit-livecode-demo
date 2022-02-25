import streamlit as st

import numpy as np
import pandas as pd

st.markdown("""# This is a header
# This is a sub header
This is text""")


st.title("hey .....")

df = pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used in order to select the displayed lines
head_df = df.head(line_count)

head_df

# this defines the location where the placeholded code will be displayed
placeholder = st.empty()

# this should be displayed before, according to its position in the code,
# but gets displayed after because it is comes after the placeholder
st.write('2. Some other element')

placeholder.markdown(
    '1. This gets displayed before even though it is called later')
