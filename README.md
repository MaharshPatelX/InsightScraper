# InsightScraper

## Overview

**InsightScraper** is a powerful tool designed to scrape websites and convert the content into insightful markdown files. The tool leverages Selenium for web scraping and a language model to generate insightful data from the scraped content.

## Features

- **Web Scraping**: Scrape entire websites and convert pages to markdown format.
- **Insight Generation**: Generate insightful data from the scraped content using a language model.
- **Structured Output**: Save the processed markdown files in a structured format.

## Installation

### Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver corresponding to your Chrome version

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/InsightScraper.git


2. **Navigate to the project directory**:
    ```bash
    cd InsightScraper
  

3. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
  

4. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt


5. **Configure the project**:
    * Update config/config.yaml with the necessary details like the path to ChromeDriver and your Groq API key.

### Configuration
Update the configuration file config/config.yaml with your settings:

```yaml
scraper:
  download_path: "downloads"
  chromedriver_path: "path/to/chromedriver"
  headless: true

insights:
  groq_api_key: "your_groq_api_key"
  model_name: "llama3-70b-8192"
```

### Usage
#### Web Scraping
To scrape a website, run the following command and provide the base URL when prompted:

```bash
python scripts/scrape_website.py
```

#### Generating Insights
To generate insights from the scraped markdown files, run:

```bash
python scripts/generate_insights.py
```

### Directory Structure
```markdown
InsightScraper/
├── config/
│   └── config.yaml
├── src/
│   ├── __init__.py
│   ├── scraper/
│   │   ├── __init__.py
│   │   └── website_md.py
│   ├── insights/
│   │   ├── __init__.py
│   │   └── md_to_insightful_data.py
├── tests/
│   ├── __init__.py
│   ├── test_website_md.py
│   └── test_md_to_insightful_data.py
├── scripts/
│   ├── scrape_website.py
│   └── generate_insights.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

### Testing
To run tests, use:

```bash
python -m unittest discover tests
```

### Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

### License
This project is licensed under the MIT License - see the (LICENSE)[https://github.com/MaharshPatelX/InsightScraper/blob/main/LICENSE] file for details.
