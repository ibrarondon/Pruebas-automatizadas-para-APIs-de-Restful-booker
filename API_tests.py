import APIs_setup, data

class TestAPIs:

    def test_ping_API(self): #Checks API health
        assert APIs_setup.ping_API().status_code == 201

    def test_create_token(self): #Create a token to update bookings
        assert APIs_setup.create_token().status_code == 200

    def test_create_booking(self): #Create a booking
        create_booking = APIs_setup.create_booking()
        assert create_booking.status_code == 200
        response = APIs_setup.delete_booking(create_booking.json()["bookingid"])
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(create_booking.json()["bookingid"])
        assert response.status_code == 404, "The booking was not deleted"

    def test_create_booking_with_empty_body(self): #Create a booking with empty body
        booking_body = {}
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200 :
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500 , "A booking was created with an empty body"

    def test_create_booking_with_firstname_only(self,firstname="Jose"): #Create an invalid booking with firstname only
        booking_body= {"firstname": firstname}
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200 :
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500 , "A booking was created with a firstname only"

    def test_create_booking_with_empty_firstname(self,firstname=""): #Create an invalid booking with empty firstname only
        booking_body = data.booking_body
        booking_body["firstname"]= firstname
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200 :
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with an empty firstname"

    def test_create_booking_with_boolean_firstname(self,firstname=True): #Create an invalid booking with invalid data type
        booking_body = data.booking_body
        booking_body["firstname"]= firstname
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200 :
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with a boolean firstname"

    def test_create_booking_with_empty_lastname(self,lastname=""): #Create an invalid booking with empty lastname only
        booking_body = data.booking_body
        booking_body["lastname"]= lastname
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200 :
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with an empty lastname"

    def test_create_booking_with_boolean_lastname(self,lastname=True): #Create an invalid booking with invalid data type
        booking_body = data.booking_body
        booking_body["lastname"]= lastname
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with a boolean lastname"

    def test_create_booking_with_empty_totalprice(self,totalprice=""): #Create an invalid booking with empty totalprice only
        booking_body = data.booking_body
        booking_body["totalprice"]= totalprice
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with an empty totalprice"

    def test_create_booking_with_invalid_totalprice(self,totalprice=True): #Create an invalid booking with invalid data type
        booking_body = data.booking_body
        booking_body["totalprice"]= totalprice
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with a invalid totalprice"

    def test_create_booking_with_empty_depositpaid(self,depositpaid=""): #Create an invalid booking with empty depositpaid only
        booking_body = data.booking_body
        booking_body["depositpaid"]= depositpaid
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with an empty depositpaid"

    def test_create_booking_with_invalid_depositpaid(self,depositpaid= 2): #Create an invalid booking with invalid data type
        booking_body = data.booking_body
        booking_body["depositpaid"]= depositpaid
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with a invalid depositpaid"

    def test_create_booking_with_empty_checkin(self,checkin=""): #Create an invalid booking with empty checkin only
        booking_body = data.booking_body
        booking_body["checkin"]= checkin
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with an empty checkin"

    def test_create_booking_with_invalid_checkin(self,checkin=True):
        booking_body = data.booking_body
        booking_body["checkin"]= checkin
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with a invalid checkin"

    def test_create_booking_with_empty_checkout(self,checkout=""): #Create an invalid booking with empty checkout only
        booking_body = data.booking_body
        booking_body["checkout"]= checkout
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with an empty checkout"

    def test_create_booking_with_invalid_checkout(self,checkout=True): #Create an invalid booking with invalid data type
        booking_body = data.booking_body
        booking_body["checkout"]= checkout
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with a invalid checkout"

    def test_create_booking_with_empty_additionalneeds(self,additionalneeds=""):  #Create an invalid booking with empty additionalneeds only
        booking_body = data.booking_body
        booking_body["additionalneeds"]= additionalneeds
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with an empty additionalneeds"

    def test_create_booking_with_boolean_additionalneeds(self,additionalneeds=True): #Create an invalid booking with invalid data type
        booking_body = data.booking_body
        booking_body["additionalneeds"]= additionalneeds
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500, "A booking was created with a boolean additionalneeds"

    def test_create_booking_with_totalprice_checkin_and_additionalneeds(self,totalprice=150,checkin="2025-10-20",additionalneeds="Breakfast"): #Create an invalid booking without mandatory fields
        booking_body= {"totalprice": totalprice,"bookingdates": {"checkin": checkin},"additionalneeds":additionalneeds}
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500

    def test_create_booking_with_lastname_depositpaid_and_checkout(self,lastname="Perez",depositpaid=True,checkout="2025-10-31"): #Create an invalid booking without mandatory fields
        booking_body= {"lastname": lastname,"depositpaid":depositpaid,"bookingdates": {"checkout": checkout}}
        create_booking = APIs_setup.create_booking(booking_body)
        if create_booking.status_code == 200:
            booking_id = create_booking.json().get("bookingid")
            response = APIs_setup.delete_booking(booking_id)
            assert response.status_code == 201, "There is no booking with that ID"
            response = APIs_setup.get_booking_by_ID(booking_id)
            assert response.status_code == 404, "The booking was not deleted"
        assert create_booking.status_code == 500

    def test_get_all_bookings(self): #Retrieve all bookings created
        assert APIs_setup.get_all_bookings().status_code == 200

    def test_get_booking_by_name(self,firstname="Jose"): #Retrieve all bookings by firstname
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_name = APIs_setup.get_booking_by_name(firstname)
        booking_id = bookings_by_name.json()[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        assert bookings_by_name.status_code == 200, "Query could not be processed"
        assert booking_details["firstname"] == firstname, "Firstname was not found"
        assert new_booking_ID == booking_id , "Firstname was not found"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_empty_name(self,firstname=""): #Retrieve all bookings with empty firstname
        assert APIs_setup.get_booking_by_name(firstname).status_code == 404, "There are bookings retrieved with empty firstname query"

    def test_get_booking_by_invalid_name(self,firstname="JoseLuis"): #Retrieve bookings by unregistered firstname
        assert APIs_setup.get_booking_by_name(firstname).status_code == 404, "There are bookings retrieved with invalid firstname query"

    def test_get_booking_by_lastname(self,lastname="Perez"): #Retrieve all bookings by lastname
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_lastname = APIs_setup.get_booking_by_lastname(lastname)
        booking_id = bookings_by_lastname.json()[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        assert bookings_by_lastname.status_code == 200, "Query could not be processed"
        assert booking_details["lastname"] == lastname, "Lastname was not found"
        assert new_booking_ID == booking_id , "Lastname was not found"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_empty_lastname(self,lastname=""): #Retrieve all bookings with empty lastname
        assert APIs_setup.get_booking_by_lastname(lastname).status_code == 404, "There are bookings retrieved with empty lastname query"

    def test_get_booking_by_invalid_lastname(self,lastname="JoseLuis"): #Retrieve bookings by unregistered lastname
        assert APIs_setup.get_booking_by_lastname(lastname).status_code == 404, "There are bookings retrieved with invalid lastname query"

    def test_get_booking_by_checkin(self,checkin="2025-10-20"): #Retrieve all bookings by checkin date
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_checkin = APIs_setup.get_booking_by_checkin(checkin).json()
        if len(bookings_by_checkin) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert False, "There are no bookings with that checkin date"
        booking_id = bookings_by_checkin[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["bookingdates"]["checkin"] == checkin , "There are no bookings with that checkin date"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_empty_checkin(self,checkin=""): #Retrieve all bookings by empty date
        assert APIs_setup.get_booking_by_checkin(checkin).status_code == 500, "Invalid entry, server cannot look for it"

    def test_get_booking_by_str_checkin(self,checkin="a"): #Retrieve all bookings with invalid checkin date type
        assert APIs_setup.get_booking_by_checkin(checkin).status_code == 500, "Invalid entry, server cannot look for it"

    def test_get_booking_by_nonexistent_checkin(self,checkin="2999-12-10"): #Retrieve all bookings by non-existent checkin date
        assert APIs_setup.get_booking_by_checkin(checkin).status_code == 404, "There are bookings retrieved with non-existent checkin query"

    def test_get_booking_by_invalid_checkin(self,checkin="2025-99-10"): #Retrieve all bookings by invalid checkin date
        assert APIs_setup.get_booking_by_checkin(checkin).status_code == 500, "Invalid entry, server cannot look for it"

    def test_get_booking_by_checkout(self,checkout="2025-10-31"): #Retrieve all bookings by checkout date
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_checkout = APIs_setup.get_booking_by_checkout(checkout).json()
        if len(bookings_by_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert False, "There are no bookings with that checkout date"
        booking_id = bookings_by_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["bookingdates"]["checkout"] == checkout, "There are no bookings with that checkout date"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_empty_checkout(self,checkout=""):  #Retrieve all bookings by empty date
        assert APIs_setup.get_booking_by_checkin(checkout).status_code == 500, "Invalid entry, server cannot look for it"

    def test_get_booking_by_str_checkout(self,checkout="a"): #Retrieve all bookings with invalid checkout date type
        assert APIs_setup.get_booking_by_checkin(checkout).status_code == 500, "Invalid entry, server cannot look for it"

    def test_get_booking_by_nonexistent_checkout(self,checkout="2999-12-10"): #Retrieve all bookings by non-existent checkout date
        assert APIs_setup.get_booking_by_checkin(checkout).status_code == 404, "There are bookings retrieved with non-existent checkin query"

    def test_get_booking_by_invalid_checkout(self,checkout="2025-99-10"): #Retrieve all bookings by invalid checkin date
        assert APIs_setup.get_booking_by_checkin(checkout).status_code == 500, "Invalid entry, server cannot look for it"

    def test_get_booking_by_lastname_and_checkin(self,lastname="Perez",checkin="2025-10-20"): #Retrieve all bookings by lastname and checkin date
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_lastname_and_checkin = APIs_setup.get_booking_by_lastname_and_checkin(lastname,checkin).json()
        if len(bookings_by_lastname_and_checkin) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert False,  "There are no bookings with that checkout date"
        booking_id = bookings_by_lastname_and_checkin[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["lastname"] == lastname, "There are no bookings with that lastname"
        assert booking_details["bookingdates"]["checkin"] == checkin, "There are no bookings with that checkin date"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_checkin_and_checkout(self,checkin="2025-10-20",checkout="2025-10-31"): #Retrieve all bookings by checkin and checkout dates
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_checkin_and_checkout = APIs_setup.get_booking_by_checkin_and_checkout(checkin,checkout).json()
        if len(bookings_by_checkin_and_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert False, "There are no bookings with that checkout date"
        booking_id = bookings_by_checkin_and_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["bookingdates"]["checkin"] == checkin , "There are no bookings with that checkin date"
        assert booking_details["bookingdates"]["checkout"] == checkout , "There are no bookings with that checkout date"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_lastname_and_checkout(self,lastname="Perez",checkout="2025-10-31"): #Retrieve all bookings by lastname and checkout date
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_lastname_and_checkout = APIs_setup.get_booking_by_lastname_and_checkout(lastname, checkout).json()
        if len(bookings_by_lastname_and_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert False, "There are no bookings with that checkout date"
        booking_id = bookings_by_lastname_and_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["lastname"] == lastname, "There are no bookings with that lastname"
        assert booking_details["bookingdates"]["checkout"] == checkout, "There are no bookings with that checkout date"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_name_lastname_and_checkout(self,firstname="Jose",lastname="Perez",checkout="2025-10-31"): #Retrieve all bookings by firstname, lastname and checkout date
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_name_lastname_and_checkout = APIs_setup.get_booking_by_name_lastname_and_checkout(firstname,lastname,checkout).json()
        if len(bookings_by_name_lastname_and_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert False, "There are no bookings with that checkout date"
        booking_id = bookings_by_name_lastname_and_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["firstname"] == firstname, "There is no booking with that firstname"
        assert booking_details["lastname"] == lastname , "There is no booking with that lastname"
        assert booking_details["bookingdates"]["checkout"] == checkout , "There are no bookings with that checkout date"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_name_lastname_and_checkin(self,firstname="Jose",lastname="Perez",checkin="2025-10-20"): #Retrieve all bookings by firstname, lastname and checkin date
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_name_lastname_and_checkin = APIs_setup.get_booking_by_name_lastname_and_checkin(firstname,lastname,checkin).json()
        if len(bookings_by_name_lastname_and_checkin) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert False, "There are no bookings with that checkout date"
        booking_id = bookings_by_name_lastname_and_checkin[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["firstname"] == firstname, "There is no booking with that firstname"
        assert booking_details["lastname"] == lastname, "There is no booking with that lastname"
        assert booking_details["bookingdates"]["checkin"] == checkin, "There are no bookings with that checkin date"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_name_checkin_and_checkout(self,firstname="Jose",checkin="2025-10-20",checkout="2025-10-31"): #Retrieve all bookings by firstname, checkin and checkout dates
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_name_checkin_and_checkout = APIs_setup.get_booking_by_name_checkin_and_checkout(firstname,checkin,checkout).json()
        if len(bookings_by_name_checkin_and_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert False, "There are no bookings with that checkout date"
        booking_id = bookings_by_name_checkin_and_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["firstname"] == firstname, "There is no booking with that firstname"
        assert booking_details["bookingdates"]["checkin"] == checkin, "There are no bookings with that checkin date"
        assert booking_details["bookingdates"]["checkout"] == checkout, "There are no bookings with that checkout date"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_valid_ID(self): #Retrieve booking information by its ID
        create_booking = APIs_setup.create_booking()
        response = APIs_setup.get_booking_by_ID(create_booking.json()["bookingid"])
        assert response.status_code == 200 , "There is no booking with that ID"
        response = APIs_setup.delete_booking(create_booking.json()["bookingid"])
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(create_booking.json()["bookingid"])
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_invalid_numeric_ID(self, id = 9999999999): #Retrieve non-existent booking information by its ID
        response = APIs_setup.get_booking_by_ID(id)
        assert response.status_code == 404, "A booking was retrieved with an invalid ID"

    def test_get_booking_by_str_ID(self, id = "Test"):#Retrieve booking information with invalid ID type
        response = APIs_setup.get_booking_by_ID(id)
        assert response.status_code == 500, "The response is not correct"

    def test_get_booking_by_empty_ID(self, id = ""): #Retrieve booking information by empty ID (all bookings)
        response = APIs_setup.get_booking_by_ID(id)
        assert response.status_code == 200, "There are no bookings"

    def test_update_booing(self, name="Raul", lastname="Paez", totalprice=100, depositpaid=False, checkin="2025-11-20", checkout="2025-11-25", needs="None"): #Updates all booking fields
        new_booking_ID = APIs_setup.create_booking().json()["bookingid"]
        update_booking = APIs_setup.update_booking(new_booking_ID,name,lastname,totalprice,depositpaid,checkin,checkout,needs)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = update_booking.json()
        assert update_booking["firstname"] == name, "firstname was not updated"
        assert update_booking["lastname"] == lastname, "lastname was not updated"
        assert update_booking["totalprice"] == totalprice, "totalprice was not updated"
        assert update_booking["depositpaid"] == depositpaid, "depositpaid was not updated"
        assert update_booking["bookingdates"]["checkin"] == checkin, "checkin was not updated"
        assert update_booking["bookingdates"]["checkout"] == checkout, "checkout was not updated"
        assert update_booking["additionalneeds"] == needs, "additionalneeds was not updated"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_update_firstname_in_booking(self, name="Raul"): #Updates firstname in booking
        new_booking_ID = APIs_setup.create_booking().json()["bookingid"]
        update_booking = APIs_setup.update_booking_firstname(new_booking_ID, name)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = update_booking.json()
        assert update_booking["firstname"] == name, "Firstname was not updated"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_update_totalprice_checkin_and_additionalneeds_in_booking(self,totalprice=100, checkin="2025-11-20", needs="None"): #Updates totalprice, checkin and additionalneeds in booking fields
        new_booking_ID = APIs_setup.create_booking().json()["bookingid"]
        update_booking = APIs_setup.update_booking_totalprice(new_booking_ID,totalprice)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = APIs_setup.update_booking_checkin(new_booking_ID, checkin)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = APIs_setup.update_booking_additionalneeds(new_booking_ID, needs)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = update_booking.json()
        assert update_booking["totalprice"] == totalprice, "totalprice was not updated"
        assert update_booking["bookingdates"]["checkin"] == checkin, "checkin was not updated"
        assert update_booking["additionalneeds"] == needs, "additionalneeds was not updated"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_update_lastname_depositpaid_and_checkout_in_booking(self, lastname="Paez", depositpaid=False, checkout="2025-11-25"): #Updates lastname, depositpaid and checkout in booking fields
        new_booking_ID = APIs_setup.create_booking().json()["bookingid"]
        update_booking = APIs_setup.update_booking_lastname(new_booking_ID, lastname)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = APIs_setup.update_booking_depositpaid(new_booking_ID, depositpaid)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = APIs_setup.update_booking_checkout(new_booking_ID, checkout)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = update_booking.json()
        assert update_booking["lastname"] == lastname, "lastname was not updated"
        assert update_booking["depositpaid"] == depositpaid, "depositpaid was not updated"
        assert update_booking["bookingdates"]["checkout"] == checkout, "checkout was not updated"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_delete_booking_by_ID(self): #Deletes a booking by ID
        create_booking = APIs_setup.create_booking()
        response = APIs_setup.delete_booking(create_booking.json()["bookingid"])
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(create_booking.json()["bookingid"])
        assert response.status_code == 404, "The booking was not deleted"

    def test_delete_booking_with_empty_ID(self, id = ""): #Deletes a booking with empty ID in query
        response = APIs_setup.delete_booking(id)
        assert response.status_code == 404, "The response is not correct"

    def test_delete_booking_with_invalid_ID(self, id = "NotValid"): #Deletes a booking with invalid ID in query
        response = APIs_setup.delete_booking(id)
        assert response.status_code == 404, "The response is not correct"

    def test_delete_booking_with_nonexistent_ID(self, id = 999999999): #Deletes a booking with invalid ID in query
        response = APIs_setup.delete_booking(id)
        assert response.status_code == 404, "The response is not correct"