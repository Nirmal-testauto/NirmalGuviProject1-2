rom selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import requests
import time


# Declaring class Guvi

class Guvi:
    url = "https://www.zenclass.in/login"
    driver = webdriver.Firefox()
    data = requests.get(url)
    driver.maximize_window()

    # Function for login page code

    def login(self):
        username = "motivenkat555@gmail.com"
        password = "Nirmalmba555@"
        self.driver.get(self.url)

    # Timer for 5 seconds to load the elements

        time.sleep(5)

    # Code for executing the Username by XPATH

        username1_XPATH = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input'
        username1= self.driver.find_element(by=By.XPATH, value=username1_XPATH)
        username1.send_keys(username)

    # Timer for 5 seconds to load the elements

        time.sleep(5)

    # Code for executing the password by XPATH

        password_XPATH = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input'
        password1 = self.driver.find_element(by=By.XPATH, value=password_XPATH)
        password1.send_keys(password)

    # Timer for 5 seconds to load the elements

        time.sleep(5)

    # Code for executing the login button by XPATH

        login_button = '//*[@id="root"]/div/div/div[1]/div[2]/div/div[1]/form/button'
        login1 = self.driver.find_element(by=By.XPATH, value=login_button)
        login1.click()

    # Timer for 5 seconds to load the elements

        time.sleep(5)

    """This is a function for list out and document
             all the information and left-hand side ribbon 
             of the Zen portal.
    """

    def main_menu(self):

        # Accessing Zen portal items on the left-hand side of the page

        time.sleep(5)
        l_menu = self.driver.execute_script(
            " l_menu_items=document.getElementsByClassName"
            '("list-scroll py-3 color-area");'
            " l_menu_logo= document.getElementsByClassName"
            '("ml-3 d-inline-block mt-3 font-weight-bold")[0].innerText;'
            "l_menu_head=document.getElementsByClassName"
            '("list-scroll py-3 active-area active-left-bar")[0].innerText;'
            " l_menu=[];"
            """for (let index = 0; index < l_menu_items.length; index++)
                   {
                   l_menu[index]=l_menu_items.item(index).innerText;
                   }
                   l_menu.splice(0,0,l_menu_logo,l_menu_head);
                   return l_menu ;"""
        )
        # Convert list to dataframe

        df_fm = pd.DataFrame(l_menu, columns=["Main-menu"])

        writer = pd.ExcelWriter("ZenClass.xlsx", engine="xlsxwriter")

        # Convert the dataframe to an XlsxWriter Excel object

        df_fm.to_excel(writer, sheet_name="Main-menu", index=False)

        # Get the xlsxwriter workbook and worksheet object

        workbook = writer.book
        worksheet = workbook.add_worksheet("Class")

        # Take screenshot of the page
        self.driver.get_full_page_screenshot_as_file("Class.png")

        # Insert an image
        worksheet.insert_image("A1", "Class.png")

        # Close the Pandas Excel writer and output the Excel file
        writer.save()
        return df_fm

    # Code for Function query

    def query(self):

        # Variable declaring a title 'heading' and description 'body' of the query

        heading = "Guvi Python AT – 1 &2 Automation Project"
        body = "This is a Project Test Code Running for the Python Automation – 1&2 Project Given by mentor Mr. Suman Gangopadhyay."
        # Code for clicking the query button by XPATH

        query_button: str = '//*[@id="root"]/div[1]/nav/ul/div[6]/li/span/div/div[2]'
        query_button1 = self.driver.find_element(by=By.XPATH, value=query_button)
        query_button1.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for clicking the normal in webpage by XPATH

        normal: str = ' // *[ @ id = "root"] / nav'
        just1 = self.driver.find_element(by=By.XPATH, value=normal)
        just1.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for clicking the create button by XPATH

        create_button: str = '//*[@id="root"]/div[2]/div/div[1]/div[1]/button'
        create_button_query = self.driver.find_element(by=By.XPATH, value=create_button)
        create_button_query.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for closing the quick query box by XPATH

        close_button: str = '/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]'
        close_button1 = self.driver.find_element(by=By.XPATH, value=close_button)
        close_button1.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for clicking the category by XPATH

        category: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'
        category1 = self.driver.find_element(by=By.XPATH, value=category)
        category1.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for clicking the choose option under category by XPATH

        category_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select/option[4]'
        category_option1 = self.driver.find_element(by=By.XPATH, value=category_option)
        category_option1.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for clicking the subcategory by XPATH

        subcategory: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select'
        subcategory1 = self.driver.find_element(by=By.XPATH, value=subcategory)
        subcategory1.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for clicking the choose option under subcategory by XPATH

        subcategory_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select/option[2]'
        subcategory_option1 = self.driver.find_element(by=By.XPATH, value=subcategory_option)
        subcategory_option1.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for clicking the language by XPATH

        language: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[3]/select'
        language1 = self.driver.find_element(by=By.XPATH, value=language)
        language1.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for clicking the choose options under language by XPATH

        language_option: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[2]/div[3]/select/option[4]'
        language_option1 = self.driver.find_element(by=By.XPATH, value=language_option)
        language_option1.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for executing the query title heading by XPATH

        query_title: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/div/input'
        query_title1 = self.driver.find_element(by=By.XPATH, value=query_title)
        query_title1.send_keys(heading)

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for executing the query description body by XPATH

        query_description: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[5]/textarea'
        query_description1 = self.driver.find_element(by=By.XPATH, value=query_description)
        query_description1.send_keys(body)

        # Timer for 5 seconds to load the elements

        time.sleep(5)

        # Code for clicking the submit button by XPATH

        create_button1: str = '//*[@id="root"]/div[2]/div/div[2]/div/div/form/div[13]/div/button'
        create_button_xpath = self.driver.find_element(by=By.XPATH, value=create_button1)
        create_button_xpath.click()

        # Timer for 5 seconds to load the elements

        time.sleep(5)

s = Guvi()

