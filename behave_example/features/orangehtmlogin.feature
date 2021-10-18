Feature: OrangeHRM Logo
    Scenario: Logo to OrangeHRM with valid parameters
        Given I launch chrome browser
        When I open orange hrm Homepage
        And Enter username "admin"  and password "admin123"
        And Click on login button
        Then User must successfully login to the Dashboard page