from hrmPages.dashbord_page import DashboardPage
from hrmPages.login_page import LoginPage


def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.execute_login("Admin", "admin123")
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.actual_heading() == "Dashboard"


def test_time_at_work(driver):
    login_page = LoginPage(driver)
    login_page.execute_login("Admin", "admin123")
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.time_at_work_displayed()
