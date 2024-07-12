import streamlit as st
import subprocess
import sys
import os
import warnings

# Function to adjust the Python path
def set_python_path():
    module_path = os.path.abspath(os.path.join('.'))
    if module_path not in sys.path:
        sys.path.append(module_path)

# Function to run a command with utf-8 encoding and suppress warnings
def run_command(command):
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        result = subprocess.run(command, capture_output=True, text=True, env=env)
    return result

# Function to query GraphRAG
def query_graphrag(question):
    st.write(f"Running query: {question}")
    result = run_command([sys.executable, "-m", "graphrag.query", "--root", ".", "--method", "local", question])
    if result.returncode == 0:
        st.write("Query executed successfully.")
        # Parse and display the required output
        output = result.stdout
        print(output)
        required_output = parse_output(output)
        st.write(required_output)
    else:
        st.write("Error in running query:", result.stderr)

# Function to parse the output and extract the required information
def parse_output(output):
    start_marker = "SUCCESS: Local Search Response:"
    start = output.find(start_marker) + len(start_marker)
    if start != -1:
        return output[start:].strip()
    return "Error parsing the output."

# Set the Python path to include the current directory
set_python_path()

# Streamlit UI
st.title("GraphRAG Streamlit App")

question = st.text_input("Enter your question:")
if st.button("Run Query"):
    if question:
        query_graphrag(question)
    else:
        st.write("Please enter a question.")
