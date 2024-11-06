from selenium import webdriver  
from selenium.webdriver.edge.service import Service  
from selenium.webdriver.common.by import By  
from webdriver_manager.microsoft import EdgeChromiumDriverManager  
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.common.exceptions import NoSuchElementException  
from selenium.common.exceptions import ElementNotVisibleException  
from time import sleep  

# Class Data for given URL for Automation
class Data:
    url = "https://jqueryui.com/droppable/"  

# Class Locators to hold locators for elements on the webpage
class Locators:

    source_element_locator = "draggable"  # ID locator for the element to be dragged
    target_element_locator = "droppable"  # ID locator for the target drop area
    frame_locator = "iframe.demo-frame"  # CSS selector for the iframe containing the draggable elements

# Main class DragAndDrop for performing drag-and-drop operation and inheriting from Data and Locators class
class DragAndDrop(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))  # Install and start EdgeChromiumDriver
        self.action = ActionChains(self.driver)  # Create an ActionChains object for performing actions

    # Method to Start Automation
    def start_automation(self):
        self.driver.maximize_window()  # Maximize the browser window
        self.driver.get(self.url)  # Navigate to the specified URL
        sleep(5)  # Wait for 5 seconds to allow the page to fully load

    # Method to perform Drag and Drop Operations
    def drag_drop(self):
        try:
            self.start_automation() # Start automation by opening the webpage

            # Locate the iframe by CSS selector
            frame_element = self.driver.find_element(by=By.CSS_SELECTOR, value=self.frame_locator)  
            self.driver.switch_to.frame(frame_element)  # Switch WebDriver focus to the iframe

            # Locate the draggable and droppable elements by their ID attributes
            source_element = self.driver.find_element(by=By.ID, value=self.source_element_locator)  # Locate the element to drag
            target_element = self.driver.find_element(by=By.ID, value=self.target_element_locator)  # Locate the drop target

            # Use ActionChains to perform a drag-and-drop action from source to target
            self.action.drag_and_drop(source_element, target_element).perform()  # Perform the drag-and-drop action
            sleep(2)  # Pause for 2 seconds to observe the result
            print("SUCCESS: Drag and Drop done!")  # Print success message if drag-and-drop is successful

            # Call the verify method to check if drag-and-drop was successful
            self.verify_drag_drop(target_element)            

        # Handle exceptions if elements are missing or not visible
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("Element is not visible!", error)  # Print error message if elements are not accessible

        # Always quit the driver after completion or error to close the browser
        finally:
            self.driver.quit()  # Close the browser session

    # Method to verify if the drag-and-drop action was successful
    def verify_drag_drop(self, target_element):

        # Check if the target element's text changes to "Dropped!" as expected
        if "Dropped!" in target_element.text:
            print("SUCCESS: Drag-and-drop action verified successfully.")
        else:
            print("FAILED: Drag-and-drop action was not successful.")

# Instantiate the DragAndDrop class and execute the drag-and-drop test
myActions = DragAndDrop()  # Create an object of DragAndDrop class
myActions.drag_drop()  # Call the drag_drop method to execute the test
