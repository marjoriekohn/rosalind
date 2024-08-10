import streamlit
from hamm import hamm

with streamlit.form("Demo"):
    streamlit.write("Enter two strings of equal length")
    input_val1 = streamlit.text_input(label="String 1", placeholder="GAGCCTACTAACGGGAT")
    input_val2 = streamlit.text_input(label="String 2", placeholder="CATCGTAATGACGGCCT")
    submitted = streamlit.form_submit_button("Submit")

    if submitted:
        result = hamm(input_val1, input_val2)
        streamlit.write("The Hamming distance is: ")
        streamlit.code(result)
