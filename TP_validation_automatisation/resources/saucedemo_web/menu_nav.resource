*** Settings ***
Documentation    Keywords concernant le menu
Library    SeleniumLibrary

Resource    ../../resources/saucedemo_web/connexion.resource


*** Keywords ***
He Clicks On Open Menu Button
    [Documentation]    Ouvrir le menu latéral
    Click Element  id=react-burger-menu-btn

The Menu Appears On Side
    [Documentation]    Verification d'ouverture du menu
    Wait Until Element Is Visible  id=logout_sidebar_link

He Clicks On Logout Link
    [Documentation]    Cliquer sur le lien de deconnexion
    Click Element  id=logout_sidebar_link

He Is Deconnected And He Goes Back To The Homepage
    [Documentation]    Verification de la deconnexion
    Wait Until Element Is Visible  id=user-name

User Is Connected With Standard Account
    [Documentation]    Connexion effectuee
    User Is On Swag Labs Connexion Page
    He Enters "${username1}" In Username Field
    He Enters "${password}" In Password Field
    Fields Are Not Empty
    He Clicks On Login Button
    User Is Connected And WebPage Has Changed
