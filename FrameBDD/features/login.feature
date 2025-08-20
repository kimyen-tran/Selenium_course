Feature: Login functionality on SP Migrate 

  Scenario: Successful login
    Given I open the login page
    When I login with username "admin" and password "SP@123456"
    Then I should get new page with url "https://dev.sp.leadplus.net/bundle_list"

  Scenario: Failed login
    Given I open the login page
    When I login with username "wronguser" and password "wrongpass"
    Then I should see message "User or password invalid."


Feature: Configure budget adjustment mode
  As a user
  I want to turn automatic budget adjustment ON or OFF
  So that the system saves valid settings and shows validation below the dropdown when needed.

  Background:
    Given I am logged into the application
    And I am on the Budget Setting screen
    And I open the "Setting budget adjustment mode" popup
    And the field "Budget adjustment mode" is required
    
  Scenario: Change from OFF to ON successfully (NO budget setting is "Waiting")
    Given the current Budget adjustment mode is "Not automatically adjust"
    And having NO budget setting is "Waiting"
    When I choose "Automatically adjust" in the Budget adjustment mode dropdown
    And I click "Save"
    Then the setting is saved successfully
    And No msg is displayed

  Scenario: Change from OFF to ON successfully (BG start date is 1st)
    Given a BG master "BG175" exists
    And the current Budget adjustment mode is "Not automatically adjust"
    And the following child BGs under "BG175" exist in stt "Waiting":
      | code     | start_date  |
      | BG-A     | 2025-09-05  |
      | BG-B     | 2025-09-01  |  # earliest (API/DB)
      | BG-C     | 2025-09-10  |
    And all children have baseline values captured
    When I choose "Automatically adjust" in the Budget adjustment mode dropdown
    And I click "Save"
    Then I see msg " Due to specifications regarding date of budget group creation and timing of the switch to the next budget group, portfolio assign budget will not be automatically adjusted from XX onward. If any changes to portfolio assign budget are necessary, please update them manually."

  Scenario: Change from ON to OFF successfully (BG start date is 1st)
    Given a BG master "BG175" exists
    And the current Budget adjustment mode is "Automatically adjust"
    And the following child BGs under "BG175" exist in stt "Waiting":
      | code     | start_date  |
      | BG-A     | 2025-09-05  |
      | BG-B     | 2025-09-01  |  # earliest (API/DB)
      | BG-C     | 2025-09-10  |
    And all children have baseline values captured
    When I choose "Not automatically adjust" in the Budget adjustment mode dropdown
    And I click "Save"
    Then No msg is displayed 