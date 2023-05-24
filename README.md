# sentence-transformer-demo
A Very Simple Semantic Search Application Using Pinecone and Sentence Transformers

This repository provides an implementation of a semantic search engine using Pinecone and Sentence Transformers. The script reads the text of Paradise Lost, creates sentence embeddings, indexes these embeddings in Pinecone, and then allows for semantic searches based on given phrases.

This project is a simple example of how to use Pinecone for semantic search. It is not designed for large-scale or real-world applications.

## Setup and Installation
To set up and run the example, follow these steps:

1. Clone this repository: `git clone https://github.com/adiekaye/sentence-transformer-demo.git`
2. Navigate to the project directory: `cd sentence-transformer-demo`
3. Create a virtual environment: for Python 3.6 and above: `python -m venv venv`
4. Activate the virtual environment:
- For Windows: `venv\Scripts\activate`
- For macOS/Linux: `source venv/bin/activate`
5. Install the required libraries: `pip install -r requirements.txt`
6. Run the script to see the semantic search engine in action: `python main.py`
7. To exit the virtual environment, type `deactivate` in the terminal.

Note: The virtual environment and requirements installation steps are optional but recommended to ensure compatibility and avoid conflicts with other Python packages you may have installed.

## Contents
- `main.py`: Main script implementing the Pinecone semantic search engine
- `helpers.py`: Contains a helper function used in `main.py`
- `paradise_lost.txt`: Contains the text of Paradise Lost used for this project
- `requirements.txt`: Lists the required libraries for this project
- `README.md`: Provides instructions for setting up and running the example, and explains the contents of the repository
- `.gitignore`: A simple Git configuration file to ignore the virtual environment directory

## Usage
Replace <YOUR API KEY HERE> with your actual Pinecone API key in the `main.py` file.

The script will create a 768-dimensional index in Pinecone, upsert vectors (sentence embeddings), and perform a query to find similar sentences. The results will be displayed in the console.

## License
This project is licensed under the MIT License.
