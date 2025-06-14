# SauceDemo Automation Tests

This project contains basic automated tests for the [Sauce Demo](https://www.saucedemo.com/) web application using Selenium WebDriver and Python.

---

## About the Project

- Automated tests cover core functionalities such as:
  - Valid and invalid login
  - Logout
  - Sorting products by price (high to low)
  - Adding products to the cart and removing them
- The project is created as practice for a junior QA position to demonstrate basic web test automation skills.

---

## Technologies and Tools

- Python 3.12
- Selenium WebDriver
- Google Chrome and ChromeDriver
- Git and GitHub for version control

---

## How to Run the Tests

1. Clone the repository
2. Install Selenium if you haven’t yet:
pip install selenium
3. Download the correct ChromeDriver version from [here](https://chromedriver.chromium.org/downloads) and place it in the `drivers/` folder (or update the path in the scripts).
4. Run the test file with Python, for example: python test_login_valid.py


---

## File Structure

- `test_login_valid.py` – Tests valid login and checks if the cart icon is displayed
- `test_login_invalid.py` – Tests invalid login and verifies the error message
- `test_logout.py` – Tests the logout functionality
- `test_sort_products.py` – Tests sorting products by price from high to low
- `test_add_to_cart.py` – Tests adding a product to the cart
- `test_remove_from_cart.py` – Tests removing a product from the cart
- `drivers/` – Folder containing ChromeDriver executable

---

## Notes

- Tests use implicit waits to improve stability.
- Use `assert` statements to validate expected results.
- It’s recommended to close the browser after tests (e.g., `driver.quit()`).
- This is a basic automation project and can be extended with more tests and better structure (e.g., Page Object Model).

---

## Contact

Feel free to reach out for questions or suggestions:

- Email: jakov.marina@gmail.com  
- GitHub: [MarinaInCodeLand](https://github.com/MarinaInCodeLand)

---

Thank you for checking out my project! 😊

