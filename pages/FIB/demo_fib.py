import streamlit
from fib import fib

with streamlit.form("Demo"):
    streamlit.write("Enter months and litter size")
    input_val1 = streamlit.number_input(label="Months", min_value=1)
    input_val2 = streamlit.number_input(label="Litter Size", min_value=1)
    submitted = streamlit.form_submit_button("Submit")

    if submitted:
        result = fib(input_val1, input_val2)
        streamlit.write("The total number of rabbit pairs that will be present after", input_val1, "months")
        streamlit.code(result)
