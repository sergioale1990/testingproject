import os
from pages.login_page import LoginPage
from pages.register_page import RegisterPage

#1) Registro de usuario nuevo (email único):
def test_register_user_success(browser, base_url, make_unique_email):
    login = LoginPage(browser, base_url)
    login.open()
    login.go_to_register()

    register = RegisterPage(browser, base_url)

    email = make_unique_email
    password = "Luz@m4713088013"
    register.register(first_name="Tester", last_name="Tester", date_of_birth="2000-01-01", street="test", postal_code="00000", city="test", state="test", phone="123456789", email = email, password=password)
    register.redirect_to_login_page()

# Validacion de login con el nuevo usuario:
    login = LoginPage(browser, base_url)
    login.open()
    login.login(email=email, password=password)
    login.assert_logged_in()