import datetime

#Get the current date and time
current_datetime = datetime.datetime.now()

#Format the date in the desired format
formatted_date = current_datetime.strftime("%a%b %d %H:%M:%S IST %Y")

#Print the formatted date
print(formatted_date)
