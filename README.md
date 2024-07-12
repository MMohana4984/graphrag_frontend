# GraphRag Frontend

GraphRag Frontend is a Streamlit-based application designed to provide a user-friendly Q&A interface for querying and interacting with graph-based data structures managed by the GraphRag package. This README provides detailed instructions on how to install and use the tool.

## Table of Contents
- [Installation](#installation)
- [Initialization](#initialization)
- [Indexing](#indexing)
- [Usage](#usage)
- [Contributing](#contributing)
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

## Preprocessing

Before indexing, you need to preprocess the PDF documents to convert them into text files.

1. **Run the preprocessing script:**
    ```sh
    python preprocessing.py
    ```

    - This script will read the PDF files from the `pdfs` folder and create corresponding text files in the `input` folder.

## Adding PDF Documents

To add your PDF documents for indexing, follow these steps:

1. **Place your PDF documents in the `pdfs` folder:**
    - Ensure all PDF files you want to index are placed inside the `pdfs` directory within the project root.

2. **Verify your `settings.yaml` configuration:**
    - Ensure your `settings.yaml` file is properly configured with the necessary settings for indexing and querying.

## Environment Setup

Create a `.env` file in the project root with the following content:

```env
GRAPHRAG_API_KEY=<API_KEY>
```

Replace `<API_KEY>` with your actual GraphRag API key.

## Initialization

Before you can start indexing your graph data, you need to initialize the GraphRag index using the backend package. This sets up the necessary directory structure and configuration files.

1. **Initialize the index:**
    ```sh
    py -m graphrag.index --init --root .
    ```

    - `--init`: This flag indicates that you want to initialize the index.
    - `--root .`: This specifies the root directory where the index will be initialized. In this case, the current directory.

## Indexing

Once the index is initialized, you can start indexing your graph data. The following command updates the index with the data in the specified root directory.

1. **Index the graph data:**
    ```sh
    py -m graphrag.index --root .
    ```

    - `--root .`: This specifies the root directory where the graph data is located. The tool will recursively scan this directory for data to index.

## Usage

After initializing and indexing your data, you can use GraphRag Frontend to perform various Q&A operations on your indexed graph data. The specific usage commands and options depend on your exact needs and the functionality provided by the tool.

### Running the Streamlit App

To start the Streamlit app and interact with your graph data via a web interface, use the following command:

```sh
streamlit run app.py
```

Open your web browser and navigate to the local address provided by Streamlit to start using the Q&A interface.


## License

GraphRag Frontend is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
