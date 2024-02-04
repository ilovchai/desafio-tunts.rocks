# Student Grade Management System
## Overview
This is a Python script for managing student grades stored in a Google Sheets document. It fetches student data from a Google Sheets spreadsheet, calculates the average grades, determines the students' status (e.g., pass, fail, retest), and updates the spreadsheet accordingly.

## Prerequisites
 - gspread library (pip install gspread)
 -  pandas library (pip install pandas)
 -  numpy library (pip install numpy)

## Setup
  - Clone the repository:
  - git clone https://github.com/ilovchai/desafio-tunts.rocks.git
  - Install the required Python libraries
    
## Obtain Google Sheets API credentials:
  - Create a project in the Google Developers Console.
  - Enable the Google Sheets and Google Drive APIs for the project.
  - Create credentials for a service account and download the JSON file containing your credentials.
  - Share your Google Sheets document with the email address associated with the service account.

## Usage
Place your credentials.json file containing your Google Sheets API credentials in the root directory of the project.

## Execute the script:
python main.py
The script will fetch student data from the specified Google Sheets document, calculate average grades, determine student status, update the spreadsheet with the results, and print the updated student data.
