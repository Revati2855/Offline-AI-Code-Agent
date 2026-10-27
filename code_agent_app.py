
import streamlit as st

from code_agent_brain import OfflineCodingAgent
from code_agent_tools import check_python_syntax


st.set_page_config(
    page_title="Offline AI Coding Assistant",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Offline AI Coding Assistant")
st.write(
    "Generate Python code, explain programs, "
    "debug errors, and check Python syntax using a local AI model."
)

# Load the model only once per Streamlit session.
@st.cache_resource
def load_agent():
    return OfflineCodingAgent()


with st.spinner("Loading the local AI model..."):
    agent = load_agent()

st.success("Local AI model is ready!")

task = st.selectbox(
    "What would you like the assistant to do?",
    [
        "Generate Code",
        "Explain Code",
        "Debug Code",
        "Check Python Syntax"
    ]
)

if task == "Generate Code":
    request = st.text_area(
        "Describe the Python program you want:",
        placeholder="Example: Create a program to check whether a number is even or odd."
    )

    if st.button("Generate Code"):
        if request.strip():
            with st.spinner("Generating code locally..."):
                result = agent.generate_code(request)

            st.subheader("AI Response")
            st.markdown(result)
        else:
            st.warning("Please describe the program you need.")

elif task == "Explain Code":
    code = st.text_area(
        "Paste your Python code:",
        height=220
    )

    if st.button("Explain Code"):
        if code.strip():
            with st.spinner("Explaining code..."):
                result = agent.explain_code(code)

            st.subheader("Explanation")
            st.markdown(result)
        else:
            st.warning("Please enter some Python code.")

elif task == "Debug Code":
    code = st.text_area(
        "Paste the Python code you want to debug:",
        height=220
    )

    if st.button("Debug Code"):
        if code.strip():
            with st.spinner("Analyzing code..."):
                result = agent.debug_code(code)

            st.subheader("Debugging Results")
            st.markdown(result)
        else:
            st.warning("Please enter some Python code.")

elif task == "Check Python Syntax":
    code = st.text_area(
        "Paste your Python code:",
        height=220
    )

    if st.button("Check Syntax"):
        if code.strip():
            result = check_python_syntax(code)

            st.subheader("Syntax Check")

            if result["success"]:
                st.success(result["message"])
            else:
                st.error(result["message"])
                st.write("Details:", result["details"])
                st.write("Line:", result["line"])
                st.write("Column:", result["column"])
        else:
            st.warning("Please enter some Python code.")

st.divider()
st.caption(
    "Runs inference using a local model. "
    "Generated code is displayed, not automatically executed."
)
