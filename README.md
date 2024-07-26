# Scalable Data Warehouse for LLM Finetuning
## Project Overview

This project aims to build a scalable data warehouse for collecting, cleaning, processing, and storing text data in Swahili. It encompasses web scraping, database management, API development, and automated workflows to enhance NLP capabilities for African languages. The system facilitates fine-tuning of Llama 2 7B, with benchmarking performed on Llama 2 13B and Llama 2 7B. Data sources include Hugging Face, Zenodo, and web scraping.

## Features

- **Data Collection**: Aggregates data from Hugging Face, Zenodo, and web scraping.
- **Data Processing**: Cleans and preprocesses text and audio data for NLP tasks.
- **API Development**: Creates high-throughput APIs for data ingestion and retrieval.
- **Backend Development**: Implements backend services using Flask.
- **Frontend Development**: Develops user interfaces with React.
- **Workflow Orchestration**: Automates workflows with Apache Airflow
- **Models**:
  - Benchmarking was done using Llama 2 13B and Llama 2 7B.
- **Metrics**:
  - Evaluate model performance on text classofication, summarization, and translation.

## Technologies Used

- **Backend**: Flask
- **Frontend**: React
- **Database**: PostgreSQL
- **Data Ingestion**: Apache Airflow
- **API**: RESTful API with Flask
- **LLMs**: Llama 2 7B, Llama 2 13B
- **Data Sources**:
  - Hugging Face: [Swahili News Dataset](https://huggingface.co/datasets/community-datasets/swahili_news)
  - Zenodo: [Swahili Dataset](https://zenodo.org/records/4300294)

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Introduction

This project addresses the need for a scalable system to enhance NLP capabilities for Swahili. It integrates data collection, processing, API development, and machine learning to support the fine-tuning of Llama 2 models. The project also involves creating a user-friendly interface and automating workflows for seamless data handling.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Node.js and npm
- Docker (optional, for containerization)
- Apache Airflow

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/cheronodaisy/NLPWarehouse.git
    ```
2. Navigate to the project directory:
    ```sh
    cd NLPWarehouse
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    npm install
    ```
    
## Contributing

Contributions from the community are welcome. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature-branch
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature-branch
    ```
5. Open a pull request.

## Acknowledgments

- Hugging Face and Zenodo for the datasets.
