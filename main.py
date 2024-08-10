import os
import streamlit
import importlib.util

main_directory = os.getcwd()
pages_directory = 'pages'
problem_IDs = []

for page in os.listdir(pages_directory):
    if os.path.isdir(os.path.join(pages_directory, page)):
        problem_IDs.append(page)

if problem_IDs:
    problem_IDs.sort()
    sidebar = streamlit.sidebar.radio("Problem ID", problem_IDs)
else:
    streamlit.error("No folders found in the 'pages' directory.")
    sidebar = None

details, pseudocode, solution, demo = streamlit.tabs(["Details", "Pseudocode", "Solution", "Demo"])

if sidebar:
    markdown_details_file = None
    markdown_pseudo_file = None
    code_file = None
    demo_file = None
    folder_path = os.path.join(pages_directory, sidebar)

    for file in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, file)):
            continue
        if file.startswith("pseudo"):
            markdown_pseudo_file = file
        elif file.endswith(".md") and "pseudo" not in file:
            markdown_details_file = file
        elif "demo" in file and file.endswith(".py"):
            demo_file = file
        elif "test" not in file and file.endswith(".py"):
            code_file = file

    with details:
        if markdown_details_file:
            file_path = os.path.join(folder_path, markdown_details_file)
            with open(file_path, 'r') as file:
                details_text = file.read()
                streamlit.markdown(details_text)
        else:
            streamlit.write("No details file found in the selected folder.")

    with pseudocode:
        if markdown_pseudo_file:
            file_path = os.path.join(folder_path, markdown_pseudo_file)
            with open(file_path, 'r') as file:
                pseudo_text = file.read()
                streamlit.markdown(pseudo_text)
        else:
            streamlit.write("No pseudocode file found in the selected folder.")

    with solution:
        if code_file:
            file_path = os.path.join(folder_path, code_file)
            with open(file_path, 'r') as file:
                code = file.read()
                streamlit.code(code, language='python')
        else:
            streamlit.write("No solution file found in the selected folder.")

    with demo:
        if demo_file:
            file_path = os.path.join(folder_path, demo_file)
            try:
                os.chdir(folder_path)
                spec = importlib.util.spec_from_file_location("demo_dna", demo_file)
                demo_dna = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(demo_dna)
            except Exception as e:
                streamlit.error(f"Error loading demo: {e}")
            finally:
                os.chdir(main_directory)
        else:
            streamlit.write("No demo file found in the selected folder.")
else:
    streamlit.write("No folder selected.")
