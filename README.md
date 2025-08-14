Crypto Dashboard: Full-Stack Data Visualization Platform 📈

An interactive platform built with Python, Flask, and Plotly to provide real-time and historical cryptocurrency market analysis. This project demonstrates core skills in full-stack development, API integration, and data visualization.

🚀 Key Features

    Real-Time Data Integration: Connects to the CoinGecko API to fetch and display up-to-the-minute cryptocurrency prices.

    Dynamic Data Visualization: Generates and renders a historical price chart using the Plotly library, allowing for interactive exploration of market trends over the past 30 days.

    Modular Architecture: The backend logic (data fetching and processing) is decoupled from the frontend presentation (HTML templates), showcasing an understanding of maintainable and scalable web application design.

    Efficient Data Handling: Utilizes the Pandas library for efficient data manipulation and preparation, demonstrating a strong foundation in data science libraries.

🛠️ Technology Stack

    Backend: Python, Flask, Pandas, Requests

    Frontend: HTML, Jinja2, Plotly.js (via CDN)

    Deployment & Management: Git, Poetry

▶️ Quick Start

This project is ready to run with a simple local setup.

    Clone the repository:
    Bash

git clone https://github.com/your-username/your-project.git
cd your-project

Install dependencies:
Bash

poetry install

Run the application:
Bash

    poetry run python app.py

    Navigate to http://127.0.0.1:5000 to view the dashboard.

💡 Project Roadmap

    Implement User Interactivity: Add forms to allow users to select specific cryptocurrencies and customize the historical time range.

    Advanced Data Analysis: Integrate Pandas to calculate and visualize a moving average on the historical price chart, demonstrating time-series analysis skills.

    Refactor to Streamlit: Restructure the project to use a data-centric framework to showcase the ability to rapidly prototype and build data applications.