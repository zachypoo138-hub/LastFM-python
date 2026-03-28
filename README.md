# Last.fm Daily Scrobble Predictor
A CLI tool that uses machine learning to forecast listening activity.

## Overview
This script pulls your total scrobble count for the current day via the Last.fm API and compares it against historical data stored in \`scrobble_history.json\`. It uses **Linear Regression** to predict future scrobble counts based on your established listening velocity.

## Features
- **Data Logging**: Records daily scrobble totals to a local JSON file.
- **Trend Forecasting**: Uses \`scikit-learn\` to calculate a linear trend line.
- **Predictive Analysis**: Estimates tomorrow's scrobble count based on past performance.

## Setup
1. **Prepare Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate

   pip install -r requirements.txt

