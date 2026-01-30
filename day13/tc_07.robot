*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet=Sheet1
Suite Setup       Open qafox
Test Template     qafoxregister With Excel
Suite Teardown    Close All Browsers

*** Variables ***
${url}      https://tutorialsninja.com/demo/index.php?route=common/home
${browser}  chrome

*** Keywords ***
Open qafox
    Open Browser    ${url}    ${browser}
    Maximize Browser Window

qafoxregister with Excel
    [Arguments]     ${firstname}    ${lastname}     ${email}    ${telephone}    ${password}     ${passwordconfirm}
    Click Element    xpath=//*[@id="top-links"]/ul/li[2]/a
    Click Link    Register
    Wait Until Element Is Visible    name=firstname      10s
    Input Text    name=firstname    ${firstname}
    Input Text    name=lastname    ${lastname}
    Input Text    name=email    ${email}
    Input Text    name=telephone    ${telephone}
    Input Text    name=password    ${password}
    Input Text    name=confirm    ${passwordconfirm}
    Click Element    xpath=//*[@id="content"]/form/div/div/input[1]
    Click Button    xpath=//*[@id="content"]/form/div/div/input[2]
    Click Element    xpath=//*[@id="content"]/p/a
    Wait Until Element Is Visible    name=email         10s
    Input Text    name=email    ${email}
    Input Text    name=password    ${password}
    Click Element    xpath=//*[@id="content"]/div/div[2]/div/form/input
    Sleep    3s

*** Test Cases ***
tc_07.robot
