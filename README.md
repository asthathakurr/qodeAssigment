# 📊 Market Intelligence System

**Qode Technical Assignment**


## Overview

This project implements a **modular Market Intelligence System** that collects, processes, stores, and analyzes social media text data to derive actionable market signals — **without using any paid APIs**.

The solution is built with real-world engineering constraints in mind, particularly platform anti-bot mechanisms, and focuses on **clean architecture, scalability, and analytical correctness** rather than brute-force data extraction.


## Project Objectives

* Design an end-to-end data pipeline
* Perform text-based market signal extraction
* Follow modular, production-style code organization
* Avoid paid or restricted APIs
* Demonstrate data engineering and analysis best practices


## System Architecture

QODE-ASSIGNMENT/
|
|-- data/               
|-- logs/   
|-- src/
|   |-- scraper/       
|   |   |-- twitter_scraper.py
|   |   |-- utils.py
|   |
|   |-- processing/     
|   |   |-- cleaner.py
|   |   |-- deduplicator.py
|   |
|   |-- storage/        
|   |   |-- parquet_writer.py
|   |
|   |-- analysis/      
|       |-- text_to_signal.py
|       |-- visualization.py           
|-- main.py
|-- README.md             
|-- requirements.txt




## Key Features

### 1. Data Collection

* Twitter/X data scraping using **Selenium WebDriver**
* Market-focused hashtag targeting
* Designed to work without paid APIs
* Scraping logic isolated for easy replacement or extension

> Note: Twitter/X enforces strong anti-automation checks. Login prompts during scraping are expected behavior and handled as real-world constraints.

---

### 2. Data Processing

* URL and noise removal using regex
* Text normalization (lowercasing, token cleanup)
* Deduplication via content-based hashing

---

### 3. Data Storage

* Efficient columnar storage using **Apache Parquet**
* Optimized for analytics and scalability

---

### 4. Analysis & Signal Generation

* TF-IDF vectorization of cleaned text
* Signal strength computation per record
* CSV output for downstream analysis


### 5. Visualization

* Lightweight signal visualization using Matplotlib
* Sampling-based plotting for performance efficiency


## Tech Stack

* **Python 3.x**
* **Selenium** – Web scraping
* **Pandas** – Data manipulation
* **Scikit-learn** – TF-IDF vectorization
* **Matplotlib** – Visualization
* **PyArrow** – Parquet file handling


## Setup Instructions

### 1️⃣ Install Dependencies

`pip install -r requirements.txt`

### 2️⃣ ChromeDriver Setup

* Install a ChromeDriver version compatible with your Chrome browser
* Ensure the driver is available in your system `PATH`

### 3️⃣ Run the Pipeline

`python main.py`

## Outputs

Upon successful execution, the following artifacts are generated:

* `data/tweets.parquet` – Processed tweet dataset
* `data/signals.csv` – Computed market signal strengths
* Visualization window displaying sampled signals
* `logs/app.log` – Execution logs


## Handling Platform Constraints

Twitter/X actively restricts automated scraping. Instead of bypassing these mechanisms, this system:

* Separates scraping from processing
* Allows execution with partial or historical datasets
* Supports easy migration to alternative data sources

This mirrors **real-world production system behavior**.


## Scalability & Future Enhancements

The architecture supports easy extension to:

* Additional social media or news sources
* Advanced NLP models (sentiment analysis, embeddings)
* Distributed processing frameworks
* Cloud storage and orchestration tools
* Scheduled or streaming execution models


## Conclusion

This project demonstrates:

* End-to-end data pipeline design
* Practical handling of real-world data constraints
* Clean, modular, and maintainable code structure
* Strong alignment with market intelligence use cases

The solution is **production-oriented, extensible, and evaluation-ready**.


Author: Astha Thakur
Purpose: Qode Technical Assignment
