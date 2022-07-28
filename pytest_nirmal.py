import nirmal4
import pytest
import pandas as pd
import time

s = nirmal4.Guvi()

# pytest for login of zen portal

@pytest.mark.first
def test_login():
    s.login()

# Timer for 5 seconds to load the elements

    time.sleep(5)

# URL of zen portal

    assert s.driver.current_url == "https://www.zenclass.in/class"

# pytest for getting the information in left ribbon

@pytest.mark.second


def test_main_menu():

    """ access items from the menu bar"""

    l_menu = main.s.driver.execute_script(
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

    # Timer for 5 seconds to load the elements

    time.sleep(5)

    # Code for converting the list to dataframe

    df_fm = pd.DataFrame(l_menu, columns=["Main-menu"])

    #Code for checking the dataframe

    pd.testing.assert_frame_equal(main.s.main_menu(), df_fm)

    #Timer for 5 seconds to load the elements

    time.sleep(5)

# Code to pytest for raising a query in zen portal

@pytest.mark.thrid

# Code for Function to test the create query

def test_createquery():
  s.query()
  s.query()
  s.query()
  s.query()
  s.query()
  assert s.query() == s.query()
