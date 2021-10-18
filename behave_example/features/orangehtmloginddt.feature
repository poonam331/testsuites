Feature: OrangeHRM Logo
    Scenario Outline: Logo to OrangeHRM with valid parameters
        Given We launch chrome browser
        When We open orange hrm Homepage
        And So Enter username "<username>"  and password "<password>"
        And Now Click on login button
        Then User must successfully login to the Dashboard page and see the header Dashboard

        Examples:
            |username|password|
            |admin|admin123|
            |admin123|admin|
            |ggg|gggtt|
            |aaa|bbb|

