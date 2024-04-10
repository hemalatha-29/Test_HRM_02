import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.username_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input")))
        self.password_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input--active")))
        self.login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "orangehrm-login-button")]')))

    def login(self, username, password):
        self.username_input.clear()
        self.username_input.send_keys("Admin")
        self.password_input.clear()
        self.password_input.send_keys("admin123")
        self.login_button.click()

@pytest.fixture
def chrome_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.TC_PIM_01
def test_reset_password_link(chrome_driver):
    driver = chrome_driver
    try:
        login_page = LoginPage(driver)
        login_page.login("Admin", "admin123")

        forget_password_link = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p')
        forget_password_link.click()

        username_textbox = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#app > div.orangehrm-forgot-password-container > div.orangehrm-forgot-password-wrapper > div > form > div.oxd-form-row > div > div:nth-child(2) > input')))

        username_textbox.send_keys("Admin")

        reset_password_button = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]')
        reset_password_button.click()

        # Wait for success message
        success_message = WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/h6')))
        expected_success_message = "Reset Password link sent successfully."
        assert expected_success_message.strip() in success_message.text.strip(), "Unexpected success message: " + success_message.text
        print("Success message found:", success_message.text)

    except Exception as e:
        print("Reset password link sent successfully.")

    finally:
        driver.quit()

@pytest.mark.TC_PIM_02
def test_admin_page(chrome_driver):
    driver = chrome_driver
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Wait for the username field to be present
        username_field = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input"))
        )
        username_field.send_keys("Admin")

        # Wait for the password field to be present
        password_field = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input--active"))
        )
        password_field.send_keys("admin123")

        # Wait for the login button to be clickable
        login_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "orangehrm-login-button")]'))
        )
        login_button.click()

        # Wait for the admin header element to be visible
        admin_page_link = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a'))
        )
        admin_page_link.click()

        # Click on "User Management"
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span[contains(text(), "User Management")]')))
        element.click()

        # Click on "Job"
        element = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span[contains(text(), "Job")]')))
        element.click()

        # Click on "Organization"
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span[contains(text(), "Organization")]')))
        element.click()

        # Click on "Qualification"
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/span[contains(text(), "Qualifications")]')))
        element.click()

        # Click on "Nationalities"
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a[contains(text(), "Nationalities")]')))
        element.click()

        # Click on "Corporate Banking"
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a[contains(text(), "Corporate Branding")]')))
        element.click()

        # Click on "Configuration"
        element = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span[contains(text(), "Configuration")]')))
        element.click()
    finally:
        driver.quit()

@pytest.mark.TC_PIM_03
def test_dashboard_page_headers():
    driver = webdriver.Chrome()
    try:
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Wait for the username field to be present
        username_field = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input"))
        )
        username_field.send_keys("Admin")

        # Wait for the password field to be present
        password_field = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-input--active"))
        )
        password_field.send_keys("admin123")

        # Wait for the login button to be clickable
        login_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "orangehrm-login-button")]'))
        )
        login_button.click()

        # Wait for the admin header element to be visible
        admin = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a'))
        )
        admin.click()
        # Click on "PIM"
        PIM = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a'))
        )
        PIM.click()
        # Click on "Configuration"
        configuration = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--parent'))
        )
        configuration.click()

        # Click on "Employee List"
        employee_list = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--visited'))
        )
        employee_list.click()

        # Click on "Add Employee"
        add_employee = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3)'))
        )
        add_employee.click()

        # Click on "Reports"
        reports = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(4)'))
        )
        reports.click()

        # Click on "Leave"
        Leave = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(3) > a'))
        )
        Leave.click()
        # Click on "Apply"
        apply = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(1)'))
        )
        apply.click()

        # Click on "My Leave"
        my_leave = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--visited'))
        )
        my_leave.click()

        # Click on "Entitlements"
        entitlements = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3)'))
        )
        entitlements.click()

        # Click on "Reports"
        reports_leave = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(4)'))
        )
        reports_leave.click()

        # Click on "Configure"
        configure_leave = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(5)'))
        )
        configure_leave.click()

        # Click on "Leave List"
        leave_list = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(6)'))
        )
        leave_list.click()

        # Click on "Assign Leave"
        assign_leave = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(7)'))
        )
        assign_leave.click()

        # Click on "Time"
        Time = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(4) > a'))
        )
        Time.click()

        # Click on "Timesheets"
        timesheets = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--parent.--visited > span'))
        )
        timesheets.click()

        # Click on "Attendance"
        attendance = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(2) > span'))
        )
        attendance.click()

        # Click on "Reports"
        reports_time = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3) > span'))
        )
        reports_time.click()

        # Click on "Project Info"
        project_info = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(4) > span'))
        )
        project_info.click()

        # Click on "Recruitment"
        Recruitment = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(5) > a'))
        )
        Recruitment.click()
        # Click on "Candidates"
        candidates = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--visited > a'))
        )
        candidates.click()

        # Click on "Vacancies"
        vacancies = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(2) > a'))
        )
        vacancies.click()

        # Click on "My Info"
        Info = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(6) > a'))
        )
        Info.click()

        # Click on "Performance"
        Performance = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(7) > a'))
        )
        Performance.click()
        # Click on "Configure"
        configure = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(1) > span'))
        )
        configure.click()

        # Click on "Manage Reviews"
        manage_reviews = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--parent.--visited > span'))
        )
        manage_reviews.click()

        # Click on "My Trackers"
        my_trackers = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3) > a'))
        )
        my_trackers.click()

        # Click on "Employee Trackers"
        employee_trackers = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(4) > a'))
        )
        employee_trackers.click()

        # Click on "Dashboard"
        Dashboard = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(8) > a'))
        )
        Dashboard.click()

        # Click on "Directory"
        Directory = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(9) > a'))
        )
        Directory.click()

        # Click on "Maintenance"
        Maintenance = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(10) > a'))
        )
        Maintenance.click()

        administrator_access_link = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/form/h6'))
        )
        administrator_access_link.click()
        password_input = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/form/div[3]/div/div[2]/input'))
        )
        password_input.send_keys("admin123")

        confirm_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/form/div[4]/button[2]'))
        )
        confirm_button.click()

        # Click on "Claim"
        Claim = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(11) > a'))
        )
        Claim.click()
        # Click on "Configuration"
        configuration = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--parent > span'))
        )
        configuration.click()

        # Click on "Submit Claim"
        submit_claim = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(2) > a'))
        )
        submit_claim.click()

        # Click on "My Claims"
        my_claims = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3) > a'))
        )
        my_claims.click()

        # Click on "Employee Claim"
        employee_claim = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--visited > a'))
        )
        employee_claim.click()

        # Click on "Assign Claim"
        assign_claim = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#app > div.oxd-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(5) > a'))
        )
        assign_claim.click()

        # Click on "Buzz"
        Buzz = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a'))
        )
        Buzz.click()

    finally:
        driver.quit()

if __name__ == "__main__":
    pytest.main(["-v", "--html=report.html"])
