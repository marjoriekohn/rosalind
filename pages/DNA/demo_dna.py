import streamlit
from dna import dna


with streamlit.form("Demo"):
    streamlit.write("Enter a DNA string")
    input_val = streamlit.text_input("Sample data: AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
    submitted = streamlit.form_submit_button("Submit")

    if submitted:
        result = dna(input_val)
        streamlit.write("The respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in the DNA string is: ")
        streamlit.write(", ".join(map(str, result)))
