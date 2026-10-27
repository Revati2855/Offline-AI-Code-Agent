# Offline-AI-Code-Agent
Offline AI coding assistant that generates, explains, and checks Python code using a locally running language model.

## Project Overview

The **Offline AI Code Agent** is an AI-powered coding assistant developed using Python. It helps users generate Python code, understand code, and check Python syntax errors using a locally running Large Language Model (LLM).

The project uses the **Qwen2.5-Coder-1.5B-Instruct** model in GGUF format. The model runs locally on the computer through `llama-cpp-python`, so the application does not require an external AI API to generate responses.

The application provides a simple web interface built using Streamlit, making it easy for users to interact with the coding assistant.

## Objectives

- To develop an AI-based coding assistant that works locally.
- To generate Python code from user instructions.
- To explain code in simple language.
- To identify Python syntax errors.
- To analyze code and help users understand it.
- To reduce dependence on external AI APIs.

## Features

- **AI Code Generation:** Generates Python code based on user prompts.
- **Code Explanation:** Explains the purpose and working of code.
- **Python Syntax Checker:** Checks Python code for syntax errors.
- **Code Analysis:** Provides basic analysis of Python code.
- **Offline AI Model:** Uses a locally stored Qwen model without requiring an external AI API.
- **Streamlit Interface:** Provides a simple and interactive web interface.
- **Testing:** Includes test files to check model functionality and coding tools.

## Technologies Used

- Python 3.10
- Streamlit
- Qwen2.5-Coder-1.5B-Instruct
- llama-cpp-python
- Pytest
- Ruff

## Project Architecture

1. **User Input:** The user enters a coding request through the Streamlit interface.
2. **Prompt Processing:** The prompt module helps prepare instructions for the AI model.
3. **Local AI Model:** The Qwen coding model processes the request and generates a response.
4. **Code Tools:** Supporting tools can check Python syntax and perform basic code analysis.
5. **Output:** The application displays the generated code, explanations, or syntax-checking results to the user.

## Project Structure

```text
Offline_AI_Code_Agent/
│
├── code_agent_app.py
├── code_agent_brain.py
├── code_agent_prompts.py
├── code_agent_tools.py
├── code_agent_brain_test.py
├── code_agent_model_test.py
├── code_agent_tools_test.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The file names above represent the expected project structure. Keep the names consistent with the actual files in your repository.*

## Installation and Setup

### Prerequisites

- Python 3.10
- A computer with sufficient memory and storage
- The local Qwen model file

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Offline_AI_Code_Agent
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Create a Virtual Environment

```bash
py -3.10 -m venv code_agent_env
```

Activate the environment on Windows:

```bash
code_agent_env\Scripts\activate
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Download the AI Model

Download the **Qwen2.5-Coder-1.5B-Instruct GGUF Q4_K_M** model and place it at the path expected by the application:

```text
local_models/qwen2.5-coder-1.5b-instruct-q4_k_m.gguf
```

The model file is not included in this GitHub repository because of its large size. Make sure the model path in the code matches the location where you save it.

### Step 5: Run the Application

Run the following command from the project folder:

```bash
streamlit run code_agent_app.py
```

Streamlit will provide a local address, usually:

```text
http://localhost:8501
```

Open the address in your browser to use the coding assistant.

## Testing

The project includes test scripts for checking the model and supporting tools.

Run the tests with:

```bash
python code_agent_model_test.py
python code_agent_tools_test.py
python code_agent_brain_test.py
```

You can also use Pytest if your test files contain compatible Pytest tests:

```bash
pytest
```

## Offline Functionality

The AI model runs locally on the computer, and code generation does not require an external AI API. An internet connection may be needed initially to download the Python packages and model files. After setup, the application can run offline as long as all required dependencies and model files are available locally.

## Limitations

- The quality of generated code depends on the model and the prompt.
- The model may sometimes generate incorrect or incomplete code.
- The model requires sufficient RAM and disk space.
- Syntax checking does not guarantee that code is logically correct or secure.
- The AI model must be downloaded separately.

## Future Enhancements

- Support for additional programming languages.
- Improved code debugging and error suggestions.
- More advanced code analysis.
- Code optimization suggestions.
- Chat history and saved coding sessions.

## Conclusion

The Offline AI Code Agent demonstrates how a locally running Large Language Model can assist with programming tasks. It combines AI code generation, code explanation, and Python syntax checking in a simple Streamlit application while avoiding dependence on external AI APIs.

