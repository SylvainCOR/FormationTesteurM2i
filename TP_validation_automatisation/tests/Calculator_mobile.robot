*** Settings ***
Documentation    Tests de l'appli calculatrice sur Android
Library    AppiumLibrary

Resource    ../resources/calculator_app/navigation.resource
Resource    ../resources/calculator_app/operations.resource

Test Setup  Open Application  remote_url=${REMOTE_URL}  platformName=${PLATFORM_NAME}
...    deviceName=${DEVICE_NAME}  app=${APP}  platformVersion=${ANDROID_PLATFORM_VERSION}
Test Teardown  Reset Calculator


*** Variables ***
${REMOTE_URL}  http://localhost:4723/wd/hub
${PLATFORM_NAME}  Android
${DEVICE_NAME}  Pixel 7 Pro
${APP}  ${CURDIR}/com.google.android.calculator_8.4.apk
${ANDROID_PLATFORM_VERSION}   %{ANDROID_PLATFORM_VERSION=11}


*** Comments ***
Définition d'un cas de test unique, dupliqué pour chaque opération à effectuer.
Les opérations sont définies dans le fichier de données "calculator_data.py" sous forme de dictionnaires.


*** Test Cases ***
Cas de test 1
    [Documentation]    Addition
    Given User Is On Calculator App
    When He Taps On "${operation1['number1']}"
    And He Taps On "${operation1['operative_sign']}"
    And He Taps On "${operation1['number2']}"
    Then Calculator Displays Formula And Preview Result Of "${operation1}"
    When He Taps On Equal Symbol
    Then Calculator Displays The Result Of "${operation1}"

Cas de test 2
    [Documentation]    Multiplication
    Given User Is On Calculator App
    When He Taps On "${operation2['number1']}"
    And He Taps On "${operation2['operative_sign']}"
    And He Taps On "${operation2['number2']}"
    Then Calculator Displays Formula And Preview Result Of "${operation2}"
    When He Taps On Equal Symbol
    Then Calculator Displays The Result Of "${operation2}"

Cas de test 3
    [Documentation]    Division entière
    Given User Is On Calculator App
    When He Taps On "${operation3['number1']}"
    And He Taps On "${operation3['operative_sign']}"
    And He Taps On "${operation3['number2']}"
    Then Calculator Displays Formula And Preview Result Of "${operation3}"
    When He Taps On Equal Symbol
    Then Calculator Displays The Result Of "${operation3}"

Cas de test 4
    [Documentation]    Soustraction
    Given User Is On Calculator App
    When He Taps On "${operation4['number1']}"
    And He Taps On "${operation4['operative_sign']}"
    And He Taps On "${operation4['number2']}"
    Then Calculator Displays Formula And Preview Result Of "${operation4}"
    When He Taps On Equal Symbol
    Then Calculator Displays The Result Of "${operation4}"

Cas de test 5
    [Documentation]    Addition nombre
    Given User Is On Calculator App
    When He Taps On "${operation5['number1']}"
    And He Taps On "${operation5['operative_sign']}"
    And He Taps On "${operation5['number2']}"
    Then Calculator Displays Formula And Preview Result Of "${operation5}"
    When He Taps On Equal Symbol
    Then Calculator Displays The Result Of "${operation5}"

Cas de test 6
    [Documentation]    Multiplication nombre
    Given User Is On Calculator App
    When He Taps On "${operation6['number1']}"
    And He Taps On "${operation6['operative_sign']}"
    And He Taps On "${operation6['number2']}"
    Then Calculator Displays Formula And Preview Result Of "${operation6}"
    When He Taps On Equal Symbol
    Then Calculator Displays The Result Of "${operation6}"

Cas de test 7
    [Documentation]    Multiplication grand nombre
    Given User Is On Calculator App
    When He Taps On "${operation7['number1']}"
    And He Taps On "${operation7['operative_sign']}"
    And He Taps On "${operation7['number2']}"
    Then Calculator Displays Formula And Preview Result Of "${operation7}"
    When He Taps On Equal Symbol
    Then Calculator Displays The Result Of "${operation7}"
