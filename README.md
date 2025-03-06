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
