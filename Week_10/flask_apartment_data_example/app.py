from flask import Flask, render_template, url_for
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Non-GUI backend (required when plotting inside a web server)
import matplotlib.pyplot as plt
import os

# Paths relative to this file (app works independent of the working directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '..', 'Data', 'apartments_data_enriched_cleaned.csv')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Set global Matplotlib style for dark background
plt.style.use('dark_background')

# Initialize Flask app
app = Flask(__name__)

# Load the apartment data from CSV
@app.route('/')
def index():
    # Load the CSV file (update the path if needed)
    df = pd.read_csv(DATA_PATH)

    # Calculate KPIs and round them
    mean_price = round(df['price'].mean(), 2)
    mean_area = round(df['area'].mean(), 2)

    # Plot histogram of prices (dark theme is applied globally)
    plt.figure(figsize=(10,6))
    
    # Plot the histogram with skyblue bars and white edges
    color = (102/255, 204/255, 0/255)
    plt.hist(df['price'], bins=20, color=color, edgecolor='white')
    
    # Set title and labels with greenyellow color
    plt.title('Price Distribution of Apartments', color='greenyellow')
    plt.xlabel('Price (CHF)', color='greenyellow')
    plt.ylabel('Number of Apartments', color='greenyellow')

    # Customize grid, tick parameters
    plt.grid(color='gray', linestyle='--')
    plt.tick_params(colors='greenyellow')  # Change the tick color

    # Save histogram to the static folder
    os.makedirs(STATIC_DIR, exist_ok=True)
    plt.savefig(os.path.join(STATIC_DIR, 'price_histogram.png'),
                bbox_inches='tight', transparent=True)
    plt.close()
    histogram_path = url_for('static', filename='price_histogram.png')

    # Convert dataframe to a list of dictionaries
    apartments = df.to_dict(orient='records')

    # Render the index.html template and pass KPI data and histogram
    return render_template('index.html', apartments=apartments, 
                           mean_price=mean_price, 
                           mean_area=mean_area, 
                           histogram_path=histogram_path)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0')
