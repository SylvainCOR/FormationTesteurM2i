*** Settings ***
Documentation    Keywords concernant la connexion
Library   SeleniumLibrary


*** Keywords ***
Se Connecter
    [Documentation]    Connexion sur l'espace stagiaire M2i
    [Arguments]    ${identifiant}  ${mdp}
    Wait Until Element Is Visible    (//h5[text()="Espace stagiaire"])[last()]
    Click Element    (//h5[text()="Espace stagiaire"])[last()]
    Wait Until Element Is Visible    id=inputPhoneNumber
    Input Text    id=inputPhoneNumber  ${identifiant}
    Input Text    id=inputSmsCode  ${mdp}
    Click Element    id=connexion
    Wait Until Element Is Visible    (//a[@href="/timesheet"])[1]  timeout=10
