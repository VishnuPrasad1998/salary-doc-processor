# salary-doc-processor(v1)
Salary doc processor is a web api created for the purpose of extracting data from a salary slip and save them in a NoSQL Database. It is in version1 and is customisable for different sorts of salary slips.

# Libraries/Frameworks/Tools Used:
Flask, Postman, MongoDB, PyMongo, Python3 and PyMuPDF

## Steps for Installation and Running:
1. Clone the repo using ```
git clone <reponame> ```
2.```cd <reponame>``` 
3. Grab a virtual environment and activate it
```
virtualenv venv
source venv/bin/activate
```
4. Install Dependencies inside requirements.txt by running
```
pip install -r requirements.txt
```
5. Inside config.py give your mongodb url for the local host.
6. Change the code inside docuparsercore/parser.py according to the fields and requirements of the business case.
7. To Run the server
```
python manage.py run
```
8. Open postman and hit the URL with POST request, request body is of file type.
 ```
   http://0.0.0.0:5000/pdf/v1/parse-data
   Request body in form-data:
   document_pdf(File): pay-slip.pdf
   Response:
   {
    "status": "OK",
    "code": 200,
    "response_data": {
        "Name": "Vishnu Prasad",
        "Employee Code": "4XX1",
        "Designation": "Engineer",
        "PAN": "FLQPXXXXXX",
        "Basic Pay": "12000",
        "DA": "3600",
        "Bonus": "700",
        "House Rent": "4800",
        "Transport Allowance": "1600",
        "Performance Allowance": "6099",
        "Total Earnings": "Rs. 32,450",
        "Month and Year": "June 2021",
        "_id": "6228d102679b281883dea1f7"
    },
    "message": "PDF details extracted and saved in DB"
   }
  ```
 9. You can see the data in mongodb atlast

To see some snapshots click here 
[Image1](https://ibb.co/fYQt7hp) 
[Image2](https://ibb.co/R267hnL)
