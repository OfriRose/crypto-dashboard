Crypto Dashboard 📈

A real-time, dynamic web dashboard built with Python and Flask for visualizing cryptocurrency prices. This project fetches live and historical data from the CoinGecko API and presents it using Plotly charts for a rich user experience.

🧐 Features

    Live Price Tracking: Fetches and displays the current prices of Bitcoin, Ethereum, and other cryptocurrencies in USD.

    Historical Price Chart: Visualizes historical price data over the last 30 days for selected cryptocurrencies using an interactive line graph.

    Python-Powered Backend: The core logic, including API calls and data processing, is handled by a Flask server.

    Dynamic Visualization: Uses the Plotly library to generate beautiful, interactive charts that are rendered directly in the browser.

🛠️ Technology Stack

    Backend: Python 🐍

        Framework: Flask

        Data Processing: Pandas

        Visualization: Plotly

    Frontend:

        Templating: Jinja2

        JavaScript: Plotly.js (via CDN)

    API: CoinGecko API

⚙️ Getting Started

Follow these steps to get a local copy of the project up and running.

Prerequisites

You'll need python3 and poetry installed.

Installation

    Clone the repository:
    Bash

git clone https://github.com/your-username/your-project.git
cd your-project

Install the project dependencies using Poetry:
Bash

poetry install

Activate the virtual environment:
Bash

poetry shell

Run the Flask application:
Bash

    python app.py

    Open your browser and navigate to http://127.0.0.1:5000 to view the dashboard.

📝 Future Plans

    Implement user interactivity to allow for custom cryptocurrency and time-range selections.

    Add advanced data analysis, such as moving averages, to the historical chart.

    Refactor the project to use a pure Python framework like Streamlit to demonstrate rapid prototyping skills.