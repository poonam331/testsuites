Feature: OrangeHRM login
    Background: common steps
        Given User launch browser
        When User open application
        And User Enter valid username and password
        And User click on login button

    Scenario: User Login to HRM Application        
        Then User must be able to login to Dashboard page
    
    Scenario: Search username        
        When navigate to search page
        Then search page should display

    Scenario: Advanced Search user        
        When navigate to advanced search page
        Then advanced search page should display
