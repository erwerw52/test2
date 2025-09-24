# Linear Regression Analyzer

This is an interactive web application built with Streamlit that allows you to explore the concepts of simple linear regression.

## Features

*   **Interactive Sliders:** Adjust the parameters of the data generation process, including the number of data points, the coefficient 'a', and the noise variance.
*   **Live Visualization:** See the changes to the data and the regression line in real-time.
*   **Outlier Detection:** The top 5 outliers (the points with the largest residuals) are highlighted on the plot.
*   **Model Information:** The coefficients of the fitted linear regression model are displayed.
*   **Data Download:** Download the generated data as a CSV file.

## How to Run

1.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py --server.port 8501
    ```

3.  **Open the application in your browser:**

    The application will be available at `http://localhost:8501`.

## How to Use

*   **Use the sliders in the sidebar** to control the data generation parameters.
*   **The plot shows** the generated data, the linear regression line, and the top 5 outliers.
*   **The model coefficients and outlier information** are displayed below the plot.
*   **You can download the generated data** as a CSV file using the download button.

## Deployment

To deploy this application, you can use Streamlit Cloud or any other platform that supports hosting Streamlit applications.

The first step for deployment is to upload your code to a GitHub repository.

## My deployed Streamlit application: ## [https://aiothw1-5114056034.streamlit.app/]( https://aiothw1-5114056034.streamlit.app/)

1.  **Initialize a Git repository and commit your files:**

    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

2.  **Add your GitHub repository as a remote and push your code:**

    ```bash
    git remote add origin <your-github-repository-url>
    git push -u origin master
    ```

    *Note: You will need to handle the authentication with GitHub yourself.*

3.  **For more detailed instructions on deployment, please refer to the official Streamlit documentation:**

    [https://docs.streamlit.io/en/stable/deploy_streamlit_app.html](https://docs.streamlit.io/en/stable/deploy_streamlit_app.html)
