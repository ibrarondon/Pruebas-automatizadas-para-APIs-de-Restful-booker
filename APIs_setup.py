import configuration, data, requests

def ping_API(): #shows API status
    response = requests.get(configuration.URL_SERVICE + configuration.PING)
    return response
def create_token(): #creates a token for user requests
    response =  requests.post(configuration.URL_SERVICE + configuration.CREATE_TOKEN,json = data.user_body, headers=data.user_header)
    return response
def get_all_bookings(): #Returns the ids of all the bookings that exist
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS)
    return(response)
def get_booking_by_ID(ID): #Returns a specific booking based upon the booking id provided
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(ID))
    return(response)
def get_booking_by_name(name): #Return bookings with a specific firstname
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"firstname":name})
    return(response)
def get_booking_by_lastname(lastname): #Return bookings with a specific lastname
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"lastname":lastname})
    return(response)
def get_booking_by_checkin(checkin): #Return bookings that have a checkin date greater than or equal to the set checkin date. Format must be CCYY-MM-DD
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"checkin":checkin})
    return(response)
def get_booking_by_checkout(checkout): #Return bookings that have a checkout date greater than or equal to the set checkout date. Format must be CCYY-MM-DD
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"checkout":checkout})
    return(response)
def get_booking_by_lastname_and_checkin(lastname,checkin):
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"lastname":lastname, "checkin":checkin})
    return(response)
def get_booking_by_name_and_lastname(name,lastname):
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"firstname":name, "lastname":lastname})
    return(response)
def get_booking_by_checkin_and_checkout(checkin,checkout):
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"checkin":checkin, "checkout":checkout})
    return(response)
def get_booking_by_lastname_and_checkout(lastname,checkout):
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"lastname":lastname, "checkout":checkout})
    return(response)
def get_booking_by_name_lastname_and_checkout(name,lastname,checkout):
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"firstname":name, "lastname":lastname, "checkout":checkout})
    return(response)
def get_booking_by_name_lastname_and_checkin(name,lastname,checkin):
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"firstname":name, "lastnnme":lastname, "checkin":checkin})
    return(response)
def get_booking_by_name_checkin_and_checkout(name,checkin,checkout):
    response = requests.get(configuration.URL_SERVICE + configuration.BOOKINGS, params={"firstname":name, "checkin":checkin, "checkout":checkout})
    return(response)
def create_booking(booking_body=data.booking_body):   #Creates a new booking in the API
    response = requests.post(configuration.URL_SERVICE + configuration.BOOKINGS, headers=data.booking_header, json = booking_body)
    return response #.json()["bookingid"]
def update_booking(id, name, lastname, totalprice, depositpaid, checkin, checkout, needs):   #Updates a current booking
    booking_body = {
        "firstname": name,
        "lastname": lastname,
        "totalprice": totalprice,
        "depositpaid": depositpaid,
        "bookingdates": {
            "checkin": checkin,
            "checkout": checkout
        },
        "additionalneeds": needs
    }
    authToken = create_token().json()["token"]
    data.booking_header ={"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + authToken}
    response = requests.put(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(id), headers=data.booking_header, json = booking_body)
    return response
def update_booking_firstname(id, name):   #Updates a current booking firstname
    authToken = create_token().json()["token"]
    data.booking_header ={"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + authToken}
    booking_body = get_booking_by_ID(id).json()
    booking_body["firstname"] = name
    response = requests.put(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(id), headers=data.booking_header, json = booking_body)
    return response
def update_booking_lastname(id, lastname):   #Updates a current booking lastname
    authToken = create_token().json()["token"]
    data.booking_header ={"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + authToken}
    booking_body = get_booking_by_ID(id).json()
    booking_body["lastname"] = lastname
    response = requests.put(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(id), headers=data.booking_header, json = booking_body)
    return response
def update_booking_totalprice(id, totalprice):   #Updates the total price for the booking
    authToken = create_token().json()["token"]
    data.booking_header ={"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + authToken}
    booking_body = get_booking_by_ID(id).json()
    booking_body["totalprice"] = totalprice
    response = requests.put(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(id), headers=data.booking_header, json = booking_body)
    return response
def update_booking_depositpaid(id, depositpaid):   #Updates whether the deposit has been paid or not
    authToken = create_token().json()["token"]
    data.booking_header ={"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + authToken}
    booking_body = get_booking_by_ID(id).json()
    booking_body["depositpaid"] = depositpaid
    response = requests.put(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(id), headers=data.booking_header, json = booking_body)
    return response
def update_booking_checkin(id, checkin):   #Updates the date the guest is checking in
    authToken = create_token().json()["token"]
    data.booking_header ={"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + authToken}
    booking_body = get_booking_by_ID(id).json()
    booking_body["bookingdates"]["checkin"] = checkin
    response = requests.put(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(id), headers=data.booking_header, json = booking_body)
    return response
def update_booking_checkout(id, checkout):   #Updates the date the guest is checking out
    authToken = create_token().json()["token"]
    data.booking_header ={"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + authToken}
    booking_body = get_booking_by_ID(id).json()
    booking_body["bookingdates"]["checkout"] = checkout
    response = requests.put(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(id), headers=data.booking_header, json = booking_body)
    return response
def update_booking_additionalneeds(id, needs):   #Updates any other needs the guest has
    authToken = create_token().json()["token"]
    data.booking_header ={"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + authToken}
    booking_body = get_booking_by_ID(id).json()
    booking_body["additionalneeds"] = needs
    response = requests.put(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(id), headers=data.booking_header, json = booking_body)
    return response
def delete_booking(ID): #Deletes a booking by ID
    authToken = create_token().json()["token"]
    booking_header ={"Content-Type": "application/json", "Accept": "application/json", "Cookie": "token=" + authToken}
    response = requests.delete(configuration.URL_SERVICE + configuration.BOOKING_BY_ID + str(ID),headers = booking_header)
    return(response)