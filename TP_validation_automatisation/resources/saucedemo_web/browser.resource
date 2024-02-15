*** Settings ***
Documentation    Keywords concernant le navigateur
Library   SeleniumLibrary

Variables    ../../library/saucedemo_data.py


*** Keywords ***
Browser Init
    [Documentation]    Initialise le navigateur
    [Arguments]    ${url}  ${browser}
    Open Browser  ${url}  ${browser}  options=add_experimental_option("detach", True)
    Maximize Browser Window

Browser Close
    [Documentation]    Ferme le navigateur
    Close All Browsers
