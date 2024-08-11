from selenium.webdriver.common.by import By

from hrmPages.base_page import BasePage


class DashboardPage(BasePage):
    heading = (By.XPATH, "//*[@class='oxd-topbar-header-breadcrumb']/h6")
    assign_leave_option = (By.XPATH, "//*[@title='Assign Leave']")
    time_at_work_option = (By.XPATH, "//*[@title='Time at Work']")

    def actual_heading(self):
        return self.find(self.heading).text

    def assign_leave_displayed(self):
        return self.find(self.assign_leave_option).is_displayed()

    def time_at_work_displayed(self):
        return self.find(self.assign_leave_option).is_displayed()