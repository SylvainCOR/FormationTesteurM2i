*** Settings ***
Documentation    Tests du site https://www.saucedemo.com
Library    SeleniumLibrary

Resource    ../resources/saucedemo_web/browser.resource
Resource    ../resources/saucedemo_web/connexion.resource
Resource    ../resources/saucedemo_web/menu_nav.resource
Resource    ../resources/saucedemo_web/products.resource
Resource    ../resources/saucedemo_web/checkout.resource
Resource    ../resources/saucedemo_web/cart.resource

Test Setup    Run Keyword  Browser Init  ${saucedemo}  ${browser}
Test Teardown    Browser Close


*** Test Cases ***
Cas de test 1
    [Documentation]    Connexion - Deconnexion
    Given User Is On Swag Labs Connexion Page
    When He Enters "${username1}" In Username Field
    And He Enters "${password}" In Password Field
    Then Fields Are Not Empty
    When He Clicks On Login Button
    Then User Is Connected And WebPage Has Changed
    When He Clicks On Open Menu Button
    Then The Menu Appears On Side
    And He Clicks On Logout Link
    Then He Is Deconnected And He Goes Back To The Homepage

Cas de test 2
    [Documentation]    Connexion avec compte bloqué
    Given User Is On Swag Labs Connexion Page
    When He Enters "${username2}" In Username Field
    And He Enters "${password}" In Password Field
    Then Fields Are Not Empty
    When He Clicks On Login Button
    Then Locked Out Error Message Appears

Cas de test 3
    [Documentation]    Effectuer une commande
    Given User Is Connected With Standard Account
    When He Clicks On Product Sort Container To Select Price High To Low
    Then The Most Expensive Item Is In First Position
    When User Adds Products To Cart
    And He Clicks On Checkout Button
    Then Page Change To A Form
    When He Enters "${firstname}", "${lastname}", "${zipcode}" And Clicks On Continue Button
    Then He Checks His Order And Prices
    When He Clicks On Finish Button
    Then His Checkout Is Complete And He Can Go Back To HomePage


*** Keywords ***
User Adds Products To Cart
    [Documentation]    Ajout de produits dans le panier
    When He Adds Product Number "${number1}" To The Cart
    Then Button Of Product "${number1}" Add To Cart Become Remove Button
    When He Adds Product Number "${number2}" To The Cart
    Then Button Of Product "${number2}" Add To Cart Become Remove Button
    When He Clicks On The Cart Icon In The Header
    Then Page Change To Cart Containing "${nb_produits}"

He Checks His Order And Prices
    [Documentation]    Vérifications lors de la commande
    Then Checkout Overview Appears
    And Item Total Price Is Correct
    And Total Price Is Correct
