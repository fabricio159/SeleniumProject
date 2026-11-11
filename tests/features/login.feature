Feature: Login
  As a Swag Labs user
  I want to log in
  So that I can browse the products

  Background:
    Given I am on the login page

  Scenario: Successful login
    When I log in as "standard_user" with password "secret_sauce"
    Then I should see the products page
    And the page header should be "Products"

  Scenario Outline: Login is rejected
    When I log in as "<username>" with password "<password>"
    Then I should see the error "<error>"

    Examples:
      | username        | password     | error                                                                     |
      | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out.                       |
      | standard_user   | wrong_pass   | Epic sadface: Username and password do not match any user in this service |
