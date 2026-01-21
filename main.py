import sys
import streamlit
import importlib.util
from pathlib import Path

# --- set up and configuration ---
streamlit.set_page_config(page_title="Rosalind Solutions", layout="wide")

# --- define directories using pathlib ---
BASE_DIRECTORY = Path.cwd()
PAGES_DIRECTORY = BASE_DIRECTORY / "pages"


# --- Helper Functions ---
def get_problem_ids(directory):
	"""scans the directory for valid problem folders and returns a list of their names"""
	if not directory.exists():
		return []
	return sorted(
		[problem.name for problem in directory.iterdir() if problem.is_dir() and not problem.name.startswith("_")]
		)


def get_file_by_pattern(directory, pattern):
	"""finds the first file matching a glob pattern"""
	try:
		return next(directory.glob(pattern))
	except StopIteration:
		return None


def run_demo_module(file_path):
	"""dynamically imports and executes the demo script"""
	try:
		# add the directory to sys.path so imports inside demo work
		if str(file_path.parent) not in sys.path:
			sys.path.append(str(file_path.parent))

		spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
		module = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(module)

	except Exception as e:
		streamlit.error(f"Error loading demo: {e}")


# --- Main App Layout ---
streamlit.title("Rosalind Problem Repository")

# --- sidebar selection ---
problem_ids = get_problem_ids(PAGES_DIRECTORY)

if problem_ids:
	# selection box (includes a search bar)
	selected_id = streamlit.sidebar.selectbox("Select a Problem", problem_ids)

	# define the specific folder for the selected problem
	current_problem_dir = PAGES_DIRECTORY / selected_id
else:
	streamlit.error(f"No problem folders found in {PAGES_DIRECTORY}")
	streamlit.stop()


# --- Main Content Tabs ---
tab_details, tab_pseudo, tab_solution, tab_demo = streamlit.tabs(["📄 Details", "🧠 Pseudocode", "💻 Solution", "▶️ Demo"])

# 1. Details Tab
with tab_details:
	# look for .md file that doesn't start with 'pseudo'
	details_file = get_file_by_pattern(current_problem_dir, "[!p]*.md")

	if details_file:
		streamlit.markdown(details_file.read_text())
	else:
		streamlit.warning("No details file found.")


# 2. Pseudocode Tab
with tab_pseudo:
	# look for file starting with 'pseudo' and ending in .md or .txt
	pseudo_file = get_file_by_pattern(current_problem_dir, "pseudo*")

	if pseudo_file:
		streamlit.markdown(pseudo_file.read_text())
	else:
		streamlit.info("No pseudocode provided.")


# 3. Solution Tab
with tab_solution:
	# look for python files that aren't the demo or test files
	python_files = list(current_problem_dir.glob("*.py"))
	solution_file = next((f for f in python_files if "demo" not in f.name and "test" not in f.name), None)

	if solution_file:
		streamlit.code(solution_file.read_text(), language='python')
	else:
		streamlit.warning("No solution code found.")


# 4. Demo Tab
@streamlit.fragment
def run_demo_fragment(file_path):
	run_demo_module(file_path)


with tab_demo:
	demo_file = get_file_by_pattern(current_problem_dir, "*demo*.py")

	if demo_file:
		run_demo_fragment(demo_file)
	else:
		streamlit.info("No interactive demo available for this problem.")
