import APIs_setup


class TestAPIs:

    def test_ping_API(self):
        assert APIs_setup.ping_API().status_code == 201

    def test_create_token(self):
        assert APIs_setup.create_token().status_code == 200

    def test_create_booking(self):
        create_booking = APIs_setup.create_booking()
        assert create_booking.status_code == 200
        response = APIs_setup.delete_booking(create_booking.json()["bookingid"])
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(create_booking.json()["bookingid"])
        assert response.status_code == 404, "The booking was not deleted"

    def test_create_booking_with_firstname(self,firstname="Jose"):
        booking_body= {"firstname": firstname}
        create_booking = APIs_setup.create_booking(booking_body)
        assert create_booking.status_code == 500

    def test_create_booking_with_totalprice_checkin_and_additionalneeds(self,totalprice=150,checkin="2025-10-20",additionalneeds="Breakfast"):
        booking_body= {"totalprice": totalprice,"bookingdates": {"checkin": checkin},"additionalneeds":additionalneeds}
        create_booking = APIs_setup.create_booking(booking_body)
        assert create_booking.status_code == 500

    def test_create_booking_with_lastname_depositpaid_and_checkout(self,lastname="Perez",depositpaid=True,checkout="2025-10-31"):
        booking_body= {"lastname": lastname,"depositpaid":depositpaid,"bookingdates": {"checkout": checkout}}
        create_booking = APIs_setup.create_booking(booking_body)
        assert create_booking.status_code == 500

    def test_get_all_bookings(self):
        assert APIs_setup.get_all_bookings().status_code == 200

    def test_get_booking_by_name(self,firstname="Jose"): #por revisar si hay que hacer delete luego de cada prueba
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_name = APIs_setup.get_booking_by_name(firstname)
        booking_id = bookings_by_name.json()[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        assert bookings_by_name.status_code == 200, "No se pudo realizar la solicitud"
        assert booking_details["firstname"] == firstname, "No se encontró ese nombre"
        assert new_booking_ID == booking_id , "No se encontró ese nombre"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_lastname(self,lastname="Perez"): #por revisar si hay que hacer delete luego de cada prueba
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_lastname = APIs_setup.get_booking_by_lastname(lastname)
        booking_id = bookings_by_lastname.json()[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        assert bookings_by_lastname.status_code == 200, "No se pudo realizar la solicitud"
        assert booking_details["lastname"] == lastname, "No se encontró ese nombre"
        assert new_booking_ID == booking_id , "No se encontró ese nombre"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_checkin(self,checkin="2025-10-20"):
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_checkin = APIs_setup.get_booking_by_checkin(checkin).json()
        if len(bookings_by_checkin) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert True == False, "La búsqueda no funciona, no arrojó resultados"
        booking_id = bookings_by_checkin[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["bookingdates"]["checkin"] == checkin , "No se encontró esa fecha"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_checkout(self,checkout="2025-10-31"):
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_checkout = APIs_setup.get_booking_by_checkout(checkout).json()
        if len(bookings_by_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert True == False, "La búsqueda no funciona, no arrojó resultados"
        booking_id = bookings_by_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["bookingdates"]["checkout"] == checkout, "No se encontró esa fecha"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_lastname_and_checkin(self,lastname="Perez",checkin="2025-10-20"):
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_lastname_and_checkin = APIs_setup.get_booking_by_lastname_and_checkin(lastname,checkin).json()
        if len(bookings_by_lastname_and_checkin) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert True == False,  "La búsqueda no funciona, no arrojó resultados"
        booking_id = bookings_by_lastname_and_checkin[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["lastname"] == lastname, "No se encontró ese apellido"
        assert booking_details["bookingdates"]["checkin"] == checkin, "No se encontró esa fecha"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_checkin_and_checkout(self,checkin="2025-10-20",checkout="2025-10-31"):
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_checkin_and_checkout = APIs_setup.get_booking_by_checkin_and_checkout(checkin,checkout).json()
        if len(bookings_by_checkin_and_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert True == False, "La búsqueda no funciona, no arrojó resultados"
        booking_id = bookings_by_checkin_and_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["bookingdates"]["checkin"] == checkin , "No se encontró esa fecha"
        assert booking_details["bookingdates"]["checkout"] == checkout , "No se encontró esa fecha"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_lastname_and_checkout(self,lastname="Perez",checkout="2025-10-31"):
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_lastname_and_checkout = APIs_setup.get_booking_by_lastname_and_checkout(lastname, checkout).json()
        if len(bookings_by_lastname_and_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert True == False, "La búsqueda no funciona, no arrojó resultados"
        booking_id = bookings_by_lastname_and_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["lastname"] == lastname, "No se encontró ese apellido"
        assert booking_details["bookingdates"]["checkout"] == checkout, "No se encontró esa fecha"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_name_lastname_and_checkout(self,firstname="Jose",lastname="Perez",checkout="2025-10-31"):
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_name_lastname_and_checkout = APIs_setup.get_booking_by_name_lastname_and_checkout(firstname,lastname,checkout).json()
        if len(bookings_by_name_lastname_and_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert True == False, "La búsqueda no funciona, no arrojó resultados"
        booking_id = bookings_by_name_lastname_and_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["firstname"] == firstname, "No se encontró ese nombre"
        assert booking_details["lastname"] == lastname , "No se encontró ese apellido"
        assert booking_details["bookingdates"]["checkout"] == checkout , "No se encontró esa fecha"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_name_lastname_and_checkin(self,firstname="Jose",lastname="Perez",checkin="2025-10-20"):
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_name_lastname_and_checkin = APIs_setup.get_booking_by_name_lastname_and_checkin(firstname,lastname,checkin).json()
        if len(bookings_by_name_lastname_and_checkin) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert True == False, "La búsqueda no funciona, no arrojó resultados"
        booking_id = bookings_by_name_lastname_and_checkin[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["firstname"] == firstname, "No se encontró ese nombre"
        assert booking_details["lastname"] == lastname, "No se encontró ese apellido"
        assert booking_details["bookingdates"]["checkin"] == checkin, "No se encontró esa fecha"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_name_checkin_and_checkout(self,firstname="Jose",checkin="2025-10-20",checkout="2025-10-31"):
        new_booking_ID = APIs_setup.create_booking().json().get("bookingid")
        bookings_by_name_checkin_and_checkout = APIs_setup.get_booking_by_name_checkin_and_checkout(firstname,checkin,checkout).json()
        if len(bookings_by_name_checkin_and_checkout) == True:
            assert True
        else:
            APIs_setup.delete_booking(new_booking_ID)
            assert True == False, "La búsqueda no funciona, no arrojó resultados"
        booking_id = bookings_by_name_checkin_and_checkout[0].get("bookingid")
        booking_details = APIs_setup.get_booking_by_ID(booking_id).json()
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        assert booking_details["firstname"] == firstname, "No se encontró ese nombre"
        assert booking_details["bookingdates"]["checkin"] == checkin, "No se encontró esa fecha"
        assert booking_details["bookingdates"]["checkout"] == checkout, "No se encontró esa fecha"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_get_booking_by_ID(self):
        create_booking = APIs_setup.create_booking()
        response = APIs_setup.get_booking_by_ID(create_booking.json()["bookingid"])
        assert response.status_code == 200 , "There is no booking with that ID"
        response = APIs_setup.delete_booking(create_booking.json()["bookingid"])
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(create_booking.json()["bookingid"])
        assert response.status_code == 404, "The booking was not deleted"

    def test_update_booking(self, name="Raul", lastname="Paez", totalprice=100, depositpaid=False, checkin="2025-11-20", checkout="2025-11-25", needs="None"):
        new_booking_ID = APIs_setup.create_booking().json()["bookingid"]
        update_booking = APIs_setup.update_booking(new_booking_ID,name,lastname,totalprice,depositpaid,checkin,checkout,needs)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = update_booking.json()
        assert update_booking["firstname"] == name, "No se actualizó el nombre correctamente"
        assert update_booking["lastname"] == lastname, "No se actualizó el apellido correctamente"
        assert update_booking["totalprice"] == totalprice, "No se actualizó el precio correctamente"
        assert update_booking["depositpaid"] == depositpaid, "No se actualizó el depósito correctamente"
        assert update_booking["bookingdates"]["checkin"] == checkin, "No se actualizó la fecha de checkin correctamente"
        assert update_booking["bookingdates"]["checkout"] == checkout, "No se actualizó la fecha de checkout correctamente"
        assert update_booking["additionalneeds"] == needs, "No se actualizaron las necesidades del cliente correctamente"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_update_firstname_in_booking(self, name="Raul"):
        new_booking_ID = APIs_setup.create_booking().json()["bookingid"]
        update_booking = APIs_setup.update_booking_firstname(new_booking_ID, name)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = update_booking.json()
        assert update_booking["firstname"] == name, "No se actualizó el nombre correctamente"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_update_totalprice_checkin_and_additionalneeds_in_booking(self,totalprice=100, checkin="2025-11-20", needs="None"):
        new_booking_ID = APIs_setup.create_booking().json()["bookingid"]
        update_booking = APIs_setup.update_booking_totalprice(new_booking_ID,totalprice)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = APIs_setup.update_booking_checkin(new_booking_ID, checkin)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = APIs_setup.update_booking_additionalneeds(new_booking_ID, needs)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = update_booking.json()
        assert update_booking["totalprice"] == totalprice, "No se actualizó el precio correctamente"
        assert update_booking["bookingdates"]["checkin"] == checkin, "No se actualizó la fecha de checkin correctamente"
        assert update_booking["additionalneeds"] == needs, "No se actualizaron las necesidades del cliente correctamente"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_update_lastname_depositpaid_and_checkout_in_booking(self, lastname="Paez", depositpaid=False, checkout="2025-11-25"):
        new_booking_ID = APIs_setup.create_booking().json()["bookingid"]
        update_booking = APIs_setup.update_booking_lastname(new_booking_ID, lastname)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = APIs_setup.update_booking_depositpaid(new_booking_ID, depositpaid)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = APIs_setup.update_booking_checkout(new_booking_ID, checkout)
        assert update_booking.status_code == 200, "There is no booking with that ID"
        update_booking = update_booking.json()
        assert update_booking["lastname"] == lastname, "No se actualizó el precio correctamente"
        assert update_booking["depositpaid"] == depositpaid, "No se actualizó la fecha de checkin correctamente"
        assert update_booking["bookingdates"]["checkout"] == checkout, "No se actualizaron las necesidades del cliente correctamente"
        response = APIs_setup.delete_booking(new_booking_ID)
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(new_booking_ID)
        assert response.status_code == 404, "The booking was not deleted"

    def test_delete_booking_by_ID(self):
        create_booking = APIs_setup.create_booking()
        response = APIs_setup.delete_booking(create_booking.json()["bookingid"])
        assert response.status_code == 201, "There is no booking with that ID"
        response = APIs_setup.get_booking_by_ID(create_booking.json()["bookingid"])
        assert response.status_code == 404, "The booking was not deleted"