from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.checkout_page import CheckoutPage

#Añadir un producto al carro de compras
def test_add_a_product_to_cart(browser, base_url):
    home = BasePage(browser, base_url)
    home.open()
    target = "Combination Pliers"
    home.click_product_by_name(target)
    ProductPage(browser).assert_loaded_with_name(target)
    ProductPage(browser).add_to_cart()
    ProductPage(browser).wait_added_to_cart_message()
