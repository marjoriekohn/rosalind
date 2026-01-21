import streamlit
from dna import dna


with streamlit.form("Demo"):
    streamlit.write("Enter a DNA string")
    input_val = streamlit.text_input("Sample data: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
    submitted = streamlit.form_submit_button("Submit")

    if submitted:
        streamlit.write(dna(input_val))
