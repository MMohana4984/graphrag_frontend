# GraphRag

GraphRag is a powerful and efficient indexing tool designed to manage and query graph-based data structures. This README provides detailed instructions on how to install and use the tool.

## Table of Contents
- [Installation](#installation)
- [Initialization](#initialization)
- [Indexing](#indexing)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with GraphRag, you need to have Python installed on your system. Follow the steps below to set up the project:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/MMohana4984/graphrag_frontend.git
    cd graphrag
    ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Initialization

Before you can start indexing your graph data, you need to initialize the GraphRag index. This sets up the necessary directory structure and configuration files.

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

After initializing and indexing your data, you can use GraphRag to perform various operations on your indexed graph data. The specific usage commands and options depend on your exact needs and the functionality provided by the tool. Refer to the detailed documentation for advanced usage examples and API references.
