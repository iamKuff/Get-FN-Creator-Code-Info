# Fortnite Creator Code Info

This Python script uses the Fortnite API to retrieve information about a creator code.

## API Used

This project utilizes the Fortnite API v2 to fetch details about a creator code based on the creator's name.

API endpoint:
https://fortnite-api.com/v2/creatorcode?name={creator_name}

## How to Use

1. Make sure you have Python installed on your system.
2. Install the necessary packages: ```pip install requests```
3. Run the script using Python: ```python fortnite_creator_code_info.py```
4. Enter the creator's name in the GUI input field and click "Fetch Info" to retrieve their code details.

## GUI Interface

The script provides a simple GUI (built with Tkinter) where you can input a creator's name and fetch their creator code information.

![Screenshot](capture.png)

## Notes

- If the creator name is valid, it will display the creator's code, account ID, name, status, and verification status.
- Error handling is included for cases such as invalid parameters or when the code does not exist.



