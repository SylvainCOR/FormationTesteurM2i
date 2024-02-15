*** Settings ***
Documentation    Tests de l'appli calculatrice sur Android
Library    AppiumLibrary


*** Keywords ***
User Is On Calculator App
    [Documentation]    Ouvrir la calculatrice
    Wait Until Element Is Visible  //android.widget.TextView[@content-desc="Chrome"]
    Swipe  700  2300  700  300
    Click Element  //android.widget.TextView[@content-desc="Calculator"]
    Wait Until Element Is Visible  //android.widget.ImageButton[@content-desc="clear"]

Reset Calculator
    [Documentation]    Reset la calculatrice
    Click Element  //android.widget.ImageButton[@content-desc="clear"]
    Element Text Should Be  com.google.android.calculator:id/formula  expected=
    Press Keycode  3
