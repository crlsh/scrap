from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%d/%m/%Y,")
print("date and time:",date_time)


import json
import datetime

employee = {
    "id": 456,
    "name": "William Smith",
    "salary": 8000,
    "joindate": datetime.datetime.now()
}
print("JSON Data")
print(json.dumps(employee, default=str))
