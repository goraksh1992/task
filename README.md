1. Use any Python MVC framework with OOPs concepts to develop below exercise. 

Create Table router_details with attributes: Sapid(18), Hostname(14), Loopback(IPv4), Mac 
address(17). Create token-based authentication to access below APIs 

    i) Create new router details with unique Sapid, Hostname, Loopback and Mac address 

    ii) Update existing router details based on unique Loopback

    iii) Get the list of all routers with details

    iv) Get the list of routers as per given IP range values 

    v) Soft delete existing router details based on unique Loopback

Installtion Steps
Step 1. Create virtual environment

    >> python -m venv env
    
Step 2. Activate virtual environment

    >> cd venv/Script/activate
    
Step 3. Install all requirements (Packages)

    >> cd Task
    
    >> pip install -r requirements.txt
    
Step 4. Start Development Server

    >> python manage.py runserver
    
    
--------------------------------------------------------------------------

1. Create Token

url: http://127.0.0.1:8000/login

Type: GET

Request: { "username": "admin", "password": "123"}

Response: { "token": "13095e36d774b0f46395cceef4a9471ceb28adf8" }

-------------------------------------------------------------------------

2. Create Route Detail

url: http://127.0.0.1:8000/route-detail

Type: POST

Request: 
{
    "sapid": "admin12l1",
    "hostname": "12320q5",
    "loopback": "192.0.2.160",
    "macAddress": "00:00:5e:00:53:a8"
}

Response:
{
    "status": 200,
    "message": "Route detail added",
    "route_detail": {
        "id": 6,
        "sapid": "admin3",
        "hostname": "1230",
        "loopback": "192.0.2.170",
        "macAddress": "00:00:5e:00:53:an"
    }
}

---------------------------------------------------------------------------

3. Get Route Details list

url: http://127.0.0.1:8000/route-detail

Type: GET

Request: No Input

Response:
{
    "status": 200,
    "route_datas": [
        {
            "id": 2,
            "sapid": "admin1204",
            "hostname": "12321",
            "loopback": "192.0.2.148",
            "macAddress": "00:00:5e:00:53:ar"
        },
        {
            "id": 3,
            "sapid": "admin1207",
            "hostname": "123201",
            "loopback": "192.0.2.149",
            "macAddress": "00:00:5e:00:53:ap"
        }
    ]
}

-----------------------------------------------------------------------------

4. Get the list of routers as per given IP range values

url: http://127.0.0.1:8000/route-detail/192.0.2.148/192.0.2.150

Type: GET

Request: loopback(192.0.2.148/192.0.2.150)

Response:
{
    "status": 200,
    "route_datas": [
        {
            "id": 2,
            "sapid": "admin1204",
            "hostname": "12321",
            "loopback": "192.0.2.148",
            "macAddress": "00:00:5e:00:53:ar"
        },
        {
            "id": 3,
            "sapid": "admin1207",
            "hostname": "123201",
            "loopback": "192.0.2.149",
            "macAddress": "00:00:5e:00:53:ap"
        }
    ]
}


-------------------------------------------------------------------------------

5. Update Route Detail

url: http://127.0.0.1:8000/route-detail/192.0.2.170

Type: PUT

Request:
{
    "sapid": "admin",
    "hostname": "1230",
    "loopback": "192.0.2.170",
    "macAddress": "00:00:5e:00:53:an"
}

Response:
{
    "status": 200,
    "message": "Route detail updated",
    "route_detail": {
        "id": 6,
        "sapid": "admin",
        "hostname": "1230",
        "loopback": "192.0.2.170",
        "macAddress": "00:00:5e:00:53:an"
    }
}


---------------------------------------------------------------------------------------

6. Soft delete existing router details based on unique Loopback

url: http://127.0.0.1:8000/route-detail/192.0.2.170

Type: DELETE

Response: loopback(192.0.2.170)

Response:
{
    "status": 200,
    "message": "Route detail deleted",
    "route_details": [
        {
            "id": 3,
            "sapid": "admin1207",
            "hostname": "123201",
            "loopback": "192.0.2.149",
            "macAddress": "00:00:5e:00:53:ap"
        },
        {
            "id": 4,
            "sapid": "admin1201",
            "hostname": "12320qw",
            "loopback": "192.0.2.150",
            "macAddress": "00:00:5e:00:53:au"
        }
    ]
}


------------------------------------------------------------------------------------------------------------------------
    

2. Write a script in Python using paramiko or netmiko library to

    i) SSH to the server. Run a command(ls) on the server and save its output to an external text file
    
    ii) File transfer to the server(FTP)
    
    
Step 1. Activate virtual environment

    >> cd Task
    
    >> cd venv/Script/activate
    
Step 2. Run Command

    >> cd Task_2
    
    >> python script.py
        1. SSH to the server. Run a command(ls) on the server and save its output to an external text file

        2. File transfer to the server(FTP)

        Enter your Choice:  2
        
        Enter source file path: C:\Goraksh\Practice\Python\Task\task\Task_2\test.txt
        
        Enter destination path: /root/demo
        
        File Transfer

--------------------------------------------------------------------------------------------------------------------
3. Write a script in python to print the below pattern

1

3 2

6 5 4

10 9 8 7


Step 1. Run Command
    >> cd Task_2
    >> python pattern.py

---------------------------------------------------------------------------------------------------------------------


