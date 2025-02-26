# Beta Distribution Visualization

This is a Streamlit application that visualizes a Beta distribution with adjustable parameters.

## Installation

1. Clone this repository
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the Streamlit app with:

```bash
streamlit run app.py
```

This will start the application and open it in your default web browser.

## Features

- Adjust parameters using sliders in the sidebar
- Visualize the Beta distribution based on your parameters
- See the calculated Alpha and Beta posterior values

## Parameters

- **Nr**: Affects the prior alpha and beta values
- **MAX**: Maximum cap for the posterior values
- **Initial P**: Initial probability for calculating prior alpha and beta
- **n_successes**: Number of successes for posterior calculation
- **n_failures**: Number of failures for posterior calculation 