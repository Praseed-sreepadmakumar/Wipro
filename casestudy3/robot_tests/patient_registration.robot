*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser To App
Suite Teardown    Close Browser

*** Variables ***
${URL}    http://127.0.0.1:5000
${BROWSER}    chrome

*** Test Cases ***
Register Patient Successfully
    Input Text    id:name    John
    Input Text    id:age     35
    Click Element    xpath://input[@value="Male"]
    Input Text    id:contact    7777777777
    Input Text    id:disease    Cold
    Select From List By Label    id:doctor    Dr. Smith
    Click Button    Register

*** Keywords ***
Open Browser To App
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
