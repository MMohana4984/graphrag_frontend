Sure, here is the updated README:

```markdown
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

### Basic Query Example

Within the Streamlit app, you can input your queries and receive answers based on the indexed graph data. The interface is designed to be intuitive and easy to use, providing real-time feedback and results.

## Contributing

We welcome contributions to GraphRag Frontend! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

Please ensure your code adheres to our coding standards and includes appropriate tests.

## License

GraphRag Frontend is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

```

Feel free to customize further as per your specific project requirements.
