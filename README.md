# Open API to Excel Streamlit App

This Streamlit app allows users to call building register data from Korea DATA Portal open API and export the data to an Excel file. The app is
built using Python and utilizes the requests library to call the API and the pandas library to create the Excel file.

## How to use

1. Clone the repository
   ```console
   git clone https://github.com/hyeminoh96/where-is-my-home-building-register.git
   ```
2. Install the required libraries
   ```console
   pip install -r requirements.txt
   ```
3. Run the streamlit app
   ```console
   python src/streamlit_app.py
   ```
4. Click the "Call API" button to retrieve the data from the API.

5. Review the data in the app and select the columns you want to include in the Excel file.

6. Click the "Export to Excel" button to create the Excel file. The file will be saved in the current working directory.

7. The app allows you to call the API and export data to excel as many times you want.

## Setting environment variables

In order to call the API, you need to have API_KEY as an environment variable. \
You can either set the variable in your local environment or store it in a .env file.

### Option 1: Setting in local environment

#### Windows

1. Open the Command Prompt
2. Type the following command and replace API_KEY with your actual API key:
    ```console
    set API_KEY "your_api_key"
    ```
3. Close and reopen the Command Prompt to apply the changes

#### Linux or macOS

1. Open the terminal
2. Type the following command and replace API_KEY with your actual API key:
    ```console
    export API_KEY="your_api_key"
    ```
3. Add the above command to your .bashrc or .bash_profile file to make the environment variable permanent.

### Option 2: Storing in a .env file

1. Create a new file named .env in the root of your project
2. Add the following line to the file and replace API_KEY with your actual API key:
    ```toml
   [openapi]
    API_KEY="your_api_key"
    ```

Make sure that you have set the environment variable correctly before running the app.

## Note

- Please make sure that you have the right credentials or access to the API that you are trying to call.
- You can also add some error handling code to handle any possible errors while calling the API or creating the excel
  file.

## License
