from data_analysis import analyse_data
from movies_data import movies_data
from web_scrapping import create_csv_file
import time

while True:
    print("web scrapping : 1")
    print("movies data : 2")
    print("data analysis : 3")
    print("exit : 4")

    answer = input("select a code challenge: ")

    if answer == "1":
        create_csv_file()
        time.sleep(2) 
    elif answer == "2":
        movies_data()
        time.sleep(2) 
    elif answer == "3":
        analyse_data()
        time.sleep(2) 
    elif answer == "4":
        break
    else:
        print("Invalid input. Please select a valid option.")
        time.sleep(1)