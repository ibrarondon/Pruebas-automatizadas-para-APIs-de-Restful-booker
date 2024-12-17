user_body = { "username": "admin", "password": "password123" }
user_header = {"Content-Type": "application/json"}    #header usado para crear usuario nuevo
booking_header = {"Content-Type": "application/json", "Accept": "application/json"}

booking_body = {
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