# PDF Diff Web App

A simple web application that allows users to compare two PDF files and view a side-by-side HTML diff of the extracted text. This tool is useful for spotting changes between different versions of PDF documents.

## Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Installation & Setup](#installation--setup)
  - [Using Docker](#using-docker)
  - [Running Locally](#running-locally)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This project is a Flask-based web app that extracts text from two uploaded PDF files using [PyPDF2](https://pythonhosted.org/PyPDF2/) and then displays a diff using Python's built-in [difflib](https://docs.python.org/3/library/difflib.html). The web-based interface makes it easy for users to compare PDFs directly from their browser without needing to install any dedicated software.

## Features

- Upload two PDF files for comparison.
- Extract text from PDFs.
- Generate and display a side-by-side diff of the PDFs.
- Run as a Docker container or directly on your laptop.

## Pre-requisites

- [Docker](https://www.docker.com/get-started) (if using Docker)
- Python 3.9+ (if running locally)
- Pip package manager (if running locally)

## Installation & Setup

### Using Docker

1. **Build the Docker image**

   Clone the repository and navigate to the project directory.

   ```sh
   git clone https://github.com/nir351988/PDF-Diff-App.git
   cd PDF-Diff-App
Copy
Insert

Build the Docker image:

docker build -t pdf-diff-app .
Copy
Insert

Run the Docker container Map port 5000 from the container to the laptop:
docker run -p 5000:5000 pdf-diff-app
Copy
Insert

The application will be available at http://localhost:5000.
Running Locally
Clone the repository
git clone https://github.com/nir351988/PDF-Diff-App.git
cd PDF-Diff-App
Copy
Insert

Install dependencies Ensure you are using Python 3.9+. Install the required packages using pip:
pip install -r requirements.txt
Copy
Insert

Run the application Start the Flask web server:
python app.py
Copy
Insert

Visit http://localhost:5000 in your browser to access the app.
Usage
Open your browser and navigate to http://localhost:5000.
You will see a form prompting you to upload two PDF files.
Select your PDFs and click on Compare PDFs.
The application will process the uploads, extract the text, and present a side-by-side diff of the two PDFs in your browser.
Project Structure
PDF-Diff-App/
├── app.py                # The Flask web application code
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration to containerize the app
└── README.md             # Project documentation and instructions
Copy
Insert

Contributing
Contributions are welcome! If you would like to enhance the project or report issues, please create a pull request or open an issue in the repository.

License
This project is open source and available under the MIT License.

Feel free to modify the content above to best suit your project requirements and additional instructions specific to your environment. Enjoy and happy coding!
