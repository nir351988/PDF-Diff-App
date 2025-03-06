# PDF Diff Web App

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker Build](https://img.shields.io/docker/cloud/build/yourusername/pdf-diff-app)](https://hub.docker.com/r/yourusername/pdf-diff-app)
[![GitHub issues](https://img.shields.io/github/issues/nir351988/PDF-Diff-App)](https://github.com/nir351988/PDF-Diff-App/issues)

A simple **Flask**-based web application that compares two PDF files by extracting their text and displaying a side-by-side diff. Perfect for quickly spotting differences between document versions.

---

## Table of Contents

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

---

## Project Overview

This project provides a lightweight web interface that extracts text from two uploaded PDF files using [PyPDF2](https://pythonhosted.org/PyPDF2/) and then generates a visual diff using Python's built-in [difflib](https://docs.python.org/3/library/difflib.html). The design focuses on ease of use with a minimalistic interface to help you compare PDFs effortlessly.

---

## Features

- **Upload & Compare:** Upload two PDF files and see their differences highlighted side-by-side.
- **Web-Based:** Run the application from your browser.
- **Flexible Deployment:** Available to run locally or through Docker.

---

## Pre-requisites

- **Docker:** [Download Docker](https://www.docker.com/get-started) if you prefer containerization.
- **Python 3.9+ & Pip:** Required for local installations.

---

## Installation & Setup

### Using Docker

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/nir351988/PDF-Diff-App.git
   cd PDF-Diff-App
