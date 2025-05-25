import pyodbc
import os
import sys
import logging

#Let's create some test data
test_data = {
    "UnitNumber": "U123",
    "FacilityName": "General Hospital",
    "NPI": "1234567890",
    "AccountNumber": "A456789",
    "MemberName": "John Doe",
    "MemberID": "M789123",
    "ClaimType": "Inpatient",
    "ICN": "ICN001122",
    "PCN": "PCN334455",
    "ServiceDateFrom": "2024-01-01",
    "ServiceDateTo": "2024-01-10",
    "ClaimStatus": "Paid",
    "AmountBilled": 1500.00,
    "AmountAllowed": 1200.00,
    "AmountPaid": 1000.00,
    "PaymentDate": "2024-01-15",
    "PANumber": "PA998877",
    "RemarkCodes": "EFG123",
}

# Set up logging
logging.basicConfig(level=logging.INFO)

# Declare the server and database names
sqlServerName = 'FAMILY_COMPUTER'
databaseName = 'TransferPythonPractice'

# Declare the table name
tableName = 'dbo.GARemitPractice'

#Use windows authentication
trusted_connection = 'yes'
#Connection string to the SQL Server
connection_string = (f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                     f"SERVER={sqlServerName};"
                     f"DATABASE={databaseName};"
                     f"TABLE={tableName};"
                     f"Trusted_Connection={trusted_connection};")

#Create a connection to the SQL Server
try:
    #Create a connection
    connection = pyodbc.connect(connection_string )
    cursor = connection.cursor() 
    #Parameters for the insert statement
    params = (
        test_data["UnitNumber"],
        test_data["FacilityName"],
        test_data["NPI"],
        test_data["AccountNumber"],
        test_data["MemberName"],
        test_data["MemberID"],
        test_data["ClaimType"],
        test_data["ICN"],
        test_data["PCN"],
        test_data["ServiceDateFrom"],
        test_data["ServiceDateTo"],
        test_data["ClaimStatus"],
        test_data["AmountBilled"],
        test_data["AmountAllowed"],
        test_data["AmountPaid"],
        test_data["PaymentDate"],
        test_data["PANumber"],
        test_data["RemarkCodes"]
    )
    #Now let's call the stored insert procedure
    stored_procedure = "dbo.DataInsertPython"
    cursor.execute("{CALL   " + stored_procedure +"(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)}", params)
    #Commit the transaction
    connection.commit()
    logging.info("Data inserted successfully.")
except pyodbc.Error as e:
    logging.error(f"Error connecting to SQL Server: {e}")
    connection.rollback()
finally:
    #Close the connection
    if 'connection' in locals():
        connection.close()
        logging.info("Connection closed.")

