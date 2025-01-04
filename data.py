user_body = { "username": "admin", "password": "password123" }  #username to create authtoken
user_header = {"Content-Type": "application/json"}    #header to create authtoken
booking_header = {"Content-Type": "application/json", "Accept": "application/json"} #header to create a booking

booking_body = {    #booking body with mandatory fields
        "firstname": "Jose",
        "lastname": "Perez",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-10-20",
            "checkout": "2025-10-31"
        },
        "additionalneeds": "Breakfast"
    }