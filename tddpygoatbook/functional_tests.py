import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_todo_list(self):
        self.browser.get("http://localhost:8000")

        self.assertIn("To-Do", self.browser.title)

        self.fail("Finish the test!")


if __name__ == "__main__":
    unittest.main(warnings="ignore")

# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# Edith has heard about a cool new online to-do app.
# She goes to check out its homepage
# browser.get("http://localhost:8000")

# She notices the page title and header mention to-do lists
# assert "To-Do" in browser.title
# print(browser.title)
# print('OK')

# She is invited to enter a to-do item straight away

# She types "Buy peacock feathers" into a text box
# (Edith's hobby is tying fly-fishing lures)

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item.
# She enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Satisfied, she goes back to sleep
