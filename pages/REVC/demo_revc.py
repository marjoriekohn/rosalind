import streamlit
from revc import revc

with streamlit.form("Demo"):
    streamlit.write("Enter a DNA string")
    input_val1 = streamlit.text_input(label="DNA String", placeholder="AAAACCCGGT")
    submitted = streamlit.form_submit_button("Submit")

    if submitted:
        result = revc(input_val1)
        streamlit.write("The reverse complement is: ")
        streamlit.code(result)
