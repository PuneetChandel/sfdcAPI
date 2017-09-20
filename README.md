SF API that support POST(single and multiple records),GET,PATCH  

1. Update config.yml as per your credentials  
2. setup virtual env  
3. install dependencies from requirements.txt  

schema validation  
1. if schema validation is required for any object, add that object in settings file for list of objects to be validated.  
2. Add schema in schema folder, for this example i have only added account  

Header:
object name is required as part of Header  
Example : x-object-name: account  

To run  
python3 app.py  

Examples:  
1. Create  
curl -X POST \  
  http://0.0.0.0:5001/v1/sfobject \  
  -H 'content-type: application/json' \  
  -H 'x-object-name: account' \  
  -d '[  
	'''{  
    "name": "My new acc 1001",  
    "industry": "Banking",  
    "BillingStreet": "345 Shoreline Park\nMountain View, CA 94043\nUSA",  
    "BillingCity": "Mountain View",  
    "BillingState": "CA",  
    "Phone": "123456789",  
    "Fax": "123456789",  
    "AccountNumber": "123456789",  
    "Website": "www.myaccount.com",  
    "Sic": "00001",  
    "Industry": "Biotechnology",  
    "AnnualRevenue": 30000000,  
    "Ownership": "Private"  
	},  
	{  
     "name": "My new acc 1002",  
    "industry": "Banking",  
    "BillingStreet": "345 Shoreline Park\nMountain View, CA 94043\nUSA",   
    "BillingCity": "Mountain View",  
    "BillingState": "CA",   
    "Phone": "123456789",  
    "Fax": "123456789",   
    "AccountNumber": "123456789",  
    "Website": "www.myaccount.com",  
    "Sic": "00001",   
    "Industry": "Biotechnology",  
    "AnnualRevenue": 30000000,   
    "Ownership": "Private"   
	}   
] '''  

curl -X POST \   
  http://0.0.0.0:5001/v1/sfobject \   
  -H 'content-type: application/json' \   
  -H 'x-object-name: contact' \   
  -d '[ {   

    "Email": "lboyle@xxx.com",   
    "LastName": "Boyle"  
 }]'   

   
2. Update   

curl -X PATCH \   
  http://0.0.0.0:5001/v1/sfobject/0014100000qx0BxAAI \   
  -H 'content-type: application/json' \   
  -H 'x-object-name: account' \   
  -d '  
	{  
     "name": "Update Name for acc 1001"  
	}'   

3. GET   

curl -X GET \   
  http://0.0.0.0:5001/v1/sfobject/0014100000qx0BxAAI \    
  -H 'x-object-name: account'   

curl -X GET \  
  http://0.0.0.0:5001/v1/sfobject/00341000001q7cB \   
  -H 'x-object-name: contact'   

