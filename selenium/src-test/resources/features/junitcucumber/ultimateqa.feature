Feature: Connexion scenarios

  @SignUp
  Scenario: Go to sign up page
    Given user is on page "https://courses.ultimateqa.com/"
    When he clicks on sign in link in the header
    Then page switch to sign in page
    When he clicks on create an account link at bottom of page
    Then page switch to sign up page

  @SignUp
  Scenario Outline: Check terms of use error message
    Given user is on page <url>
    When he clicks on sign up button
    Then error message <errorMessage> appear between page heading and form
    Examples:
      | url                                            | errorMessage             |
      | "https://courses.ultimateqa.com/users/sign_up" | "Terms must be accepted" |

  @SignUp
  Scenario Outline: Check <fieldLocation> error messages
    Given user is on page <url>
    When he clicks on <fieldLocation> fields
    And he clicks somewhere else to get out of the flied (e.g. on the page heading)
    Then error message <errorMessage1> appear under <fieldLocation> field
    When he clicks on sign up button
    Then error message <errorMessage2> appear between page heading and form
    Examples:
      | url                                            | fieldLocation | errorMessage1                        | errorMessage2               |
      | "https://courses.ultimateqa.com/users/sign_up" | "first_name"  | "This field cannot be blank"         | "First name can't be blank" |
      | "https://courses.ultimateqa.com/users/sign_up" | "last_name"   | "This field cannot be blank"         | "Last name can't be blank"  |
      | "https://courses.ultimateqa.com/users/sign_up" | "email"       | "Please enter a valid email address" | "Email can't be blank"      |
      | "https://courses.ultimateqa.com/users/sign_up" | "password"    | "This field cannot be blank"         | "Password can't be blank"   |

  @SignUp
  Scenario Outline: Create an account
    Given user is on page <url>
    When he fills the first name field with <firstName>
    And he fills the last name field with <lastName>
    And he fills the email field with <email>
    And he fills the password field with <password>
    And he clicks on checkbox to accept terms of use
    And he clicks on sign up button
    Then he's connected on the product page
    Examples:
      | url                                            | firstName | lastName | email                 | password    |
      | "https://courses.ultimateqa.com/users/sign_up" | "John"    | "Doe"    | "johndoe01@gmail.com" | "azerty123" |

  @SignIn
  Scenario Outline: Try sign in with blank fields
    Given user is on page <url>
    When he clicks on the sign in button
    Then error message <errorMessage> appear between page heading and form
    Examples:
      | url                                            | errorMessage                 |
      | "https://courses.ultimateqa.com/users/sign_in" | "Invalid email or password." |

  @SignIn
  Scenario Outline: Check <fieldLocation> error message under field
    Given user is on page <url>
    When he clicks on <fieldLocation> fields
    And he clicks somewhere else to get out of the flied (e.g. on the page heading)
    Then error message <errorMessage> appear under <fieldLocation> field
    Examples:
      | url                                            | errorMessage                         | fieldLocation |
      | "https://courses.ultimateqa.com/users/sign_in" | "Please enter a valid email address" | "email"       |
      | "https://courses.ultimateqa.com/users/sign_in" | "This field cannot be blank"         | "password"    |

  @SignIn
  Scenario Outline: Sign in with an existing account
    Given user is on page <url>
    When he fills the email field with <email>
    And he fills the password field with <password>
    And he clicks on the sign in button
    Then he's connected on the product page
    Examples:
      | url                                            | email               | password    |
      | "https://courses.ultimateqa.com/users/sign_in" | "johndoe@gmail.com" | "azerty123" |