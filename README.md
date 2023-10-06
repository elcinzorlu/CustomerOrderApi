# Customer Order Api

- $ pip install -r requirements.txt

- $ flask run 

- Customer Order API is prepared by Elçin ZORLU with Pythonlanguage flask framework and SQLite Database.

The purpose of the Customer Order API is to add, delete, patch and get customer orders.
First of all, the Customer Order API works locally with the pycharm application. The Postman
application is used to demonstrate the usability of the API.
In order to see our transaction in the database, the order id must be entered in addition to
the url and url from our Postman application as in the example. If entered correctly, order
information will be included in the response section.
Our requests should be protected with token authentication. First of all, after the token
authentication request is made and the token is received, it should be added to the token
header as in the figure.
- Methods = POST, Url = http://127.0.0.1:5000/token_authentication

The token should be taken and entered into the authorization section as in the above figure.
Required for every request sent.

- Methods = GET, Url = http://127.0.0.1:5000/get_customer_order/id

The data required to add an order to the database are filled and saved. Figure 1.1 shows an
example.
- Methods =POST, Url = http://127.0.0.1:5000/add_customer_order Json Data =
  
  ![image](https://github.com/elcinzorlu/CustomerOrderApi/assets/107582166/936f82e5-4c29-46c7-9330-23cc93562401)

The field values ​ to be changed are changed and sent to the database. Figure 1.2 shows an
example.
- Methods =PATCH, Url = http://127.0.0.1:5000/update_customer_order/1 Json Data =
  
  ![image](https://github.com/elcinzorlu/CustomerOrderApi/assets/107582166/af3d5149-3d2f-42d3-b840-5ae7d69eec8e)

  
