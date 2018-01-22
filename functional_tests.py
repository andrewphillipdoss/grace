from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class PageVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_home_page(self):

        # User navigates to page: "GRACE"
        self.browser.get('http://localhost:8000/')
        assert 'GRACE' in self.browser.title, "Browser title was: " + browser.title
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('GRACE', header_text)

        # User clicks select all and every
        # person is selected
        select_all = self.browser.find_element_by_id('checkbox_select_all')
        select_all.click()
        checkboxes = self.browser.find_elements_by_class_name('checkbox')
        self.assertTrue(
            all(checkbox.is_selected() == True for checkbox in checkboxes)
        )

        # User clicks the first available unique
        # button (which is the first button) and a modal opens
        # User notices not every person has a Unique
        # button.
        unique_button = self.browser.find_element_by_class_name('button_unique')
        unique_button.click()
        time_modal = self.browser.find_element_by_id('modal_time')
        self.assertTrue(time_modal.is_displayed())

        # User enters 6:00:00.00 AM into the modal
        # then closes the modal. 6:00:00.00 PM is now displayed
        # in the Unique cell (keep in mind, that unique is aware of
        # a 6 hour and 12 minute range after the input time...
        # in this case: 12:12:00.00 PM)
        time_input = self.browser.find_element_by_id('input_time')
        # FIX THIS SO TIME INPUT IS STANDARD
        time_input.send_keys('6:00:00.00 AM')
        close_time_modal = self.browser.find_element_by_id('button_close_modal')
        close_time_modal.click()
        self.assertFalse(time_modal.is_displayed())
        unique_time = self.browser.find_element_by_class_name('unique_time').text
        self.assertTrue(unique_time == '6:00:00.00 AM')

        # User clicks the stop button of the same person as
        # the unique button and a modal opens.
        stop_button = self.browser.find_element_by_class_name('button_stop')
        stop_button.click()
        self.assertTrue(time_modal.is_displayed())

        # User enters 12:12:00.01 PM into the modal
        # then closes the modal. 12:12:00.01 PM is now displayed
        # in the stop cell. User notices one sandwich is added
        # to that person
        time_input.send_keys('12:12:00.01 PM')
        close_time_modal.click()
        self.assertFalse(time_modal.is_displayed())
        stop_time = self.browser.find_element_by_class_name('stop_time').text
        self.assertTrue(stop_time == '12:12:00.01 PM')
        sandwich = self.browser.find_element_by_class_name('sandwich_number').text
        self.assertTrue(sandwich == '1')

        # User clicks the second available unique button and a modal
        # opens.
        unique_button = self.browser.find_elements_by_class_name('button_unique')[1]
        unique_button.click()
        self.asserTrue(time_modal.is_displayed())

        # User enters 7:00:00.00 AM and closes the modal.
        # 7:00:00.00 AM is now displayed in the unique modal.
        time_input.send_keys('7:00:00.00 AM')
        close_time_modal.click()
        self.assertFalse(time_modal.is_displayed())
        unique_time = self.browser.find_elements_by_class_name('unique_time')[1].text
        self.assertTrue(unique_time == '7:00:00.00 AM')

        # User clicks the stop button of the same person and a
        # modal opens
        stop_button = self.browser.find_elements_by_class_name('button_stop')[1].text
        stop_button.click()
        self.assertTrue(time_modal.is_displayed())

        # User enters 5:00:00.00 PM and closes the modal.
        # 5:00:00.00 PM is now displayed. User notices that
        # 7 sandwhiches are added to the sandwhich column.
        time_input.send_keys('5:00:00.00 PM')
        close_time_modal.click()
        self.assertFalse(time_modal.is_displayed())
        stop_time = self.browser.find_elements_by_class_name('stop_time')[1].text
        self.assertTrue(stop_time == '5:00:00.00 PM')
        sandwich = self.browser.find_elements_by_class_name('sandwich_number')[1].text
        self.assertTrue(sandwich_number == '7')


        # User then clicks a download button at the bottom.
        # a .csv file of the data is downloaded.
        download_button = self.browser.find_element_by_id('button_download')
        download_button.click()

        ##### CHECK IF FILE downloaded
        self.fail('Write a test to see if file downloaded')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
