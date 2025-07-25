Feature: Login functionality on Herokuapp

  Scenario: Successful login
    Given I open the login page
    When I login with username "tomsmith" and password "SuperSecretPassword!"
    Then I should see message "You logged into a secure area!"

  Scenario: Failed login
    Given I open the login page
    When I login with username "wronguser" and password "wrongpass"
    Then I should see message "Your username is invalid!"
