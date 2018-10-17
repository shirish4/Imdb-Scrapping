# Imdb-Scrapping
This project fetches information about the series or shows and sends the information as email to user.
1. About details function
The way it works is first the python code is written to scrape the search results of a particular show then we scrape the url of first search result. Later we check if this is a series by checking if there is any information about the seasons so far or upcoming seasons of the series. Then we move to the last season where we find out the airdate mentioned about each episode from which we consider the latest airdate, we convert the airdate in the required format i.e. yyyy-mm-dd using the py file.Then we check if only year is mentioned about the show than we can say that information is mentioned about the next season. If this airdate is more than the current date than the information is about next episode. If the airdate is less than the current date than the show has completed and no further information is available.

2. About Config file
The config file takes the input of email address that is to be used to send emails to users and the password and the email address of the user and string of shows seperated by comma. This file converts the show data in string to list of shows format.

3. Main file
This file takes the list input of shows from config file and then finds out the information about the shows using the details function.
It saves the information about the email address of user and the list of shows in MySQL database by creating table if not created then insert the information about the email address and the show details. The information is fetched from the database and sent to the user's email id.

To run this program you must download following libraries and you must have mysql installed.
1. import requests
2. from lxml import html
3. from datetime import date
4. import smtplib
5. import pymysql
