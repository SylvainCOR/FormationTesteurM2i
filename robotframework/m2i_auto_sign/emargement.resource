*** Settings ***
Documentation    Keywords concernant la signature
Library   SeleniumLibrary


*** Keywords ***
Ouvrir Calendrier
    [Documentation]    Ouvrir le calendrier d'émargement
    Click Element    (//a[@href="/timesheet"])[last()]
    Wait Until Element Is Visible    (//./div[@class="col-3" and contains(., "Formateur")])[1]

Emarger
    [Documentation]    Signer à l'endroit voulu
    [Arguments]    ${date_jour_format}
    Wait Until Element Is Visible    id=${date_jour_format}
    Click Element     id=${date_jour_format}
    Sleep    1s
    Capture Page Screenshot    SignatureDu${date_jour_format}

Valider Et Quitter
    [Documentation]    Valider le calendrier d'émargement
    Click Element    (//a[@href="/timesheet"])[1]
    Wait Until Element Is Visible    (//a[@href="/close-session"])[1]
    Click Element    (//a[@href="/close-session"])[1]
    Wait Until Element Is Visible    id=inputPhoneNumber
    Close All Browsers
