#Working with CSV files
#CSV stands for Comma Separated Values
#CSV files are used to store tabular data in plain text

#First, we need to import the csv module
import csv
#The csv module provides functionality to read from and write to CSV files

#Using the writer() method and the writerow() method
#The writer() method returns a writer object that converts data into a delimited string
#The writerow() method writes a single row to the CSV file

'''with open("example.csv", 'w', newline='') as file:
    #Create a CSV writer object with , comma as the delimiter
    w = csv.writer(file, delimiter=',')
    #Write the header row
    w.writerow(['Name', 'Age', 'City'])
    #Write some data rows
    w.writerow(['Howard', '62', 'Madisonville'])
    w.writerow(['Shelby', '35', 'South Bend'])
    w.writerow(['Luis', '51', 'Weehawken'])
#The above code creates a CSV file named example.csv and writes the header and data rows to it'''

#Reading from a CSV file
#The reader() method returns a reader object that reads the data from the CSV file
#Let's read the data from the example.csv file we just created
with open("example.csv", 'r') as readfile:
    #Create a CSV reader object
    r = csv.reader(readfile, delimiter=",")
    #Read the header row
    #The header row is the first row of the CSV file
    header = next(r)
    print("Header:", header)
    #Read the data rows
    for row in r:
        print("Row:", row)
    
