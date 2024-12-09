from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# import undetected_chromedriver as uc
from DrissionPage import ChromiumPage, ChromiumOptions
import pywhatkit as kit
import time
import requests
from bs4 import BeautifulSoup
import pyautogui
import time
import json
#import js2py

# Replace these values with your credentials
EMAIL = "shivijha1603@gmail.com"
PASSWORD = "Daniel@5"

def make_a_appointment(driver):
    try:
        driver.run_js("document.querySelector('button.mat-raised-button').click()")
        time.sleep(6)

        # Find and click the dropdown to expand it
        print("above")
        driver.run_script("document.getElementsByClassName('mat-select-value ng-tns-c97-10')[0].click()")
        #driver.ele('@class:mat-select-value ng-tns-c97-10').click()
        print("dropdown")
        time.sleep(3)
        # Wait for the dropdown options to appear and select the "All" option
        driver.run_js("document.getElementsByClassName('mat-option-text')[0].click()")
        time.sleep(3)
        print("All")

        driver.run_js("document.querySelector('button.mat-focus-indicator').click()")

        time.sleep(15)


    except Exception:
        pass

def your_details(driver):
    # Mock data for form fields
    mock_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone': '911234567891',
        'passport': 'A12345678',
        'nationality': 'India'
    }
    # Step 1: Fill in First Name
    first_name_input = driver.ele('#mat-input-11') # Update selector if needed
    if first_name_input:
        first_name_input.input(mock_data['first_name'])
    else:
        print("First name input not found")

    # Step 2: Fill in Last Name
    last_name_input = driver.ele('#mat-input-12')  # Update selector if needed
    if last_name_input:
        last_name_input.input(mock_data['last_name'])
    else:
        print("Last name input not found")

    # Step 3: Fill in Email Address
    email_input = driver.ele('#mat-input-16')  # Update selector if needed
    if email_input:
        email_input.input(mock_data['email'])
    else:
        print("Email address input not found")

    

    # Step 5: Enter Phone Number
    nation_code = driver.ele('#mat-input-14')  # Adjust selector as needed
    if nation_code:
        nation_code.input(mock_data['phone'])
    else:
        print("Phone nation input not found")

    contact_number = driver.ele('#mat-input-15')  # Adjust selector as needed
    if contact_number:
        contact_number.input(mock_data['phone'])
    else:
        print("Phone number input not found")


    # Step 6: Enter Passport Number
    passport_Number = driver.ele('#mat-input-13')  # Adjust selector as needed
    if passport_Number:
        passport_Number.input(mock_data['passport'])
    else:
        print("Passport input not found")

    passport_expiry_date = driver.ele('#passportExpirtyDate')  # Adjust selector as needed
    if passport_expiry_date:
        passport_expiry_date.input(mock_data['passport'])
    else:
        print("Passport input not found")

    # Step 7: Click Save Button using JavaScript
    driver.run_js("document.querySelector('button.mat-stroked-button').click();")  # Adjust selector if needed

    # Confirm submission
    print("Form submitted!")

def js_your_details(driver):
    # Fill out the "First Name" field
    driver.run_script("""
    const firstNameInput = document.querySelector('#mat-input-5');
    if (firstNameInput) {
        firstNameInput.value = 'John';
        firstNameInput.dispatchEvent(new Event('input')); // Trigger any input-related event listeners
    }

    // Fill out the "Last Name" field
    const lastNameInput = document.querySelector('#mat-input-6');
    if (lastNameInput) {
        lastNameInput.value = 'Doe';
        lastNameInput.dispatchEvent(new Event('input'));
    }

    // Select a value for "Current Nationality" dropdown
    const nationalityDropdown = document.querySelector('#mat-select-6');
    if (nationalityDropdown) {
        nationalityDropdown.click(); // Open the dropdown
        setTimeout(() => {
            const options = document.querySelectorAll('mat-option');
            if (options.length > 0) {
                options[0].click(); // Select the first option (replace index for specific selection)
            }
        }, 500); // Delay to ensure dropdown has opened
    }

    // Fill out the "Passport Number" field
    const passportNumberInput = document.querySelector('#mat-input-7');
    if (passportNumberInput) {
        passportNumberInput.value = 'A12345678';
        passportNumberInput.dispatchEvent(new Event('input'));
    }

    console.log('Form fields filled programmatically.');""")

def login_and_get_token(url):
    print("hello9")
    try:
        print("hello10")
        options = ChromiumOptions() #.set_headless(False)
        print("hello11")
        driver = ChromiumPage(options)
        # Open the login page with the passed URL
        print("hello")
        driver.get(url)
        print("Hello2")
        time.sleep(5)

        try:
          button = driver.ele("#onetrust-accept-btn-handler")
          button.click()
        except Exception:
            pass
        print("console")
        email_input= driver.ele("#email").input(EMAIL)
        
        password_input = driver.ele("#password").input(PASSWORD)
        
        time.sleep(5)

        result = driver.run_js("""
                const xpath = "//div[@class='my-10 ng-star-inserted']/div";
                const el = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

                if (el) {
                    const rect = el.getBoundingClientRect();
                    return JSON.stringify({
                        x: rect.left + window.screenX,
                        y: rect.top + window.screenY,
                        width: rect.width,
                        height: rect.height
                    });
                } else {
                    return null
                }
            """)
        if result:
            rect = json.loads(result)
            x = rect['x'] + 32
            y = rect['y'] + 126
            print(x)
            print(y)
            pyautogui.click(x,y)


        time.sleep(5)
        driver.run_js("document.querySelector('button.mat-stroked-button.btn.btn-brand-orange').click()")
        time.sleep(15)
        
        make_a_appointment(driver)
        print("yourDetails")
        js_your_details(driver)
# # Find all cards
        print("html start")
        html_content = driver.html
        # Parse the HTML dynamically
        soup = BeautifulSoup(html_content, "html.parser")
        appointment_cards = soup.find_all("div", class_="card-header bg-brand-footer px-15 px-lg-30")
        appointments = []
        for card in appointment_cards:
    # Extract appointment type
            appointment_type = card.find("div", class7_="fs-18 fs-sm-24 mb-15").text.strip()

    # Extract group reference number
            group_reference = card.find("div", class_="col-12 col-md mb-15 c-brand-grey-para ng-star-inserted").text.strip()

    # Extract applicant name
            applicant_name = card.find("div", class_="c-brand-grey-para").text.strip()

    # Combine details
            appointment_details = f"""
            Appointment Details:
            Type: {appointment_type}
            {group_reference}
            Applicant: {applicant_name}
            """
            appointments.append(appointment_details)

# Print all appointments
        for idx, appointment in enumerate(appointments, start=1):
            print(f"Appointment {idx}:")
            print(appointment)
            print("-" * 40)
        appointments_string = ""
        appointments_string += f"""
        Appointment {idx}:
        Type: {appointment_type}
        {group_reference}
        Applicant: {applicant_name}
        ----------------------------------------
        """

        return appointments_string
    except Exception as e:
         print(f"Caught an exception: {e}")
        # pass
    # finally:
    #     driver.quit()

# Main script
if __name__ == "__main__":  # Fixed the typo: "__main__" instead of "_main_"
    try:
        # Replace with the actual URL you want to pass
        browser_url = "https://visa.vfsglobal.com/jpn/en/dnk/login"
        print("main 0" , browser_url)

        # print("Logging in and retrieving token...")
        print("main")
        message = login_and_get_token(browser_url)
        print("main2")
        # print(f"Token retrieved: {token}")

        phone_number = ''  # Replace with the recipient's phone number
        time_hour = 11  # The hour (24-hour format)
        time_minute = 2  # The minute

        # Send the WhatsApp message using pywhatkit
        kit.sendwhatmsg(phone_number, message, time_hour, time_minute)
    except Exception as e:
        print(f"An error occurred: {e}")
