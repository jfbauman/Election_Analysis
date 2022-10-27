
import csv
filepath = "election_results.csv"

print("Hi")
with open(filepath, "r") as f: 
    print("Hello", f)
    csv_values = csv.reader(f)
    print("Hello", csv_values)
    for x in csv_values:
        print(x[1])

print("sssssssssss")



# import datetime as dt
# now = dt.datetime.now()
# print("the time right now is", now)