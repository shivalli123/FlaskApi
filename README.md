# ProductScrape Flask Application

This repository contains a Flask application named ProductScrape, which serves an endpoint to retrieve product details from the Lululemon website.

## Overview

The ProductScrape application is built using Flask, a lightweight web framework for Python. It includes two main components:
1. Flask application (`productscrape.py`): Defines the `/get_product_details` endpoint and handles the retrieval of product details from the Lululemon website.
2. Unit tests (`test_productscrape.py`): Contains unit tests for verifying the functionality of the Flask application.

## Usage

### Prerequisites
- Python 3.x
- Flask
- requests

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/shivalli123/FlaskApi

2. Navigate to the project directory:
    cd productscrape

## Running the Application
Run the Flask application:
python productscrape.py
Access the endpoint in a web browser or using tools like cURL or Postman.
http://localhost:5000/get_product_details
## Running Tests
Run the unit tests:
	Python -m unittest utest.py

The unit tests use the unittest framework along with the unittest.mock module for mocking external dependencies such as requests to the Lululemon API. This ensures isolated testing of the Flask application without making actual HTTP requests.
