Feature: testPsthc

Rule: The user is already on the website
  Background: User go on psthc website and accept cookies
    Given he opens "https://www.psthc.fr" website
    And he accepts cookies

  @Login
  Scenario Outline: User wants to be connected to his account
    When he clicks on the signin button
    Then he goes on login page
    When he clicks on the username empty field and type <username>
    And he clicks on the password empty field and type <password>
    And he clicks on the connection button
    Then he is connected as <username>
    Examples:
      | username   | password    |
      | "********" | "*********" |

  @AmazonStore
  Scenario: User wanna go psthc amazon store
    When he clicks on shopping link
    Then shopping stores page is opened
    When he clicks on amazon image
    Then amazon store page is opened in a new tab
