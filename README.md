```markdown
# GraphRag Frontend

GraphRag Frontend is a Streamlit-based application designed to provide a user-friendly Q&A interface for querying and interacting with graph-based data structures managed by the GraphRag package. This README provides detailed instructions on how to install and use the tool.

## Table of Contents
- [Installation](#installation)
- [Adding PDF Documents](#adding-pdf-documents)
- [Environment Setup](#environment-setup)
- [Run](#run)
- [Usage](#usage)
- [License](#license)

## Installation

To get started with GraphRag Frontend, you need to have Python installed on your system. Follow the steps below to set up the project:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/MMohana4984/graphrag_frontend.git
    cd graphrag_frontend
    ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Adding PDF Documents

To add your PDF documents for indexing, follow these steps:

1. **Place your PDF documents in the `pdfs` folder:**
    - Ensure all PDF files you want to index are placed inside the `pdfs` directory within the project root.

## Environment Setup

Create a `.env` file in the project root with the following content:

```env
GRAPHRAG_API_KEY=<API_KEY>
```

Replace `<API_KEY>` with your actual GraphRag API key.

## Run

To preprocess the PDF documents, convert them into text files, and run the Streamlit app, follow these steps:

1. **Run the script:**
    ```sh
    python run.py
    ```

    - This script will read the PDF files from the `pdfs` folder, create corresponding text files in the `input` folder, and start the Streamlit app.

## Usage

After running the `run.py` script, you can use GraphRag Frontend to perform various Q&A operations on your indexed graph data. The specific usage commands and options depend on your exact needs and the functionality provided by the tool.

### Running the Streamlit App

To start the Streamlit app and interact with your graph data via a web interface, navigate to the local address provided by Streamlit after running the `run.py` script. The interface is designed to be intuitive and easy to use, providing real-time feedback and results.

## License

GraphRag Frontend is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
```

This updated README now includes instructions to simply run the `run.py` script, which handles preprocessing the PDF documents and starting the Streamlit app.
