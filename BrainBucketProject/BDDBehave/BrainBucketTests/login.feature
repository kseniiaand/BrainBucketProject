Feature: Login functionality
  Background:
    Given a web browser is at the BrainBucket login page


  Scenario: user can't login without entering email
    Given User is not logged in
    When Password is entered
    And User click Login button
    Then 'Warning: No match for E-Mail Address and/or Password' will be shown


   Scenario: user can recover his password
     Given User is not logged in
     When User clicks 'Forgotten Password' button
     And enters his email
     Then Message 'An email with a confirmation link has been sent your email address.' will be dispalyed

