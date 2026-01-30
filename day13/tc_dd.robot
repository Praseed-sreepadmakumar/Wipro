*** SETTINGS ***
Library    SeleniumLibrary

*** Variables ***
${url}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
${browser}      chrome
${username}     Admin
${password}     admin123

*** Keywords ***
open orangehrm
    Open Browser    ${url}     ${browser}
    Maximize Browser Window
orangehrmlogin
    [Arguments]    ${username}  ${password}
    input text    name=username    ${username}
    input text    name=password    ${password}
    sleep           5s
     capture page screenshot    beforelogin.png
    click button    xpath=//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button
     sleep           5s
    capture page screenshot    afterlogin.png
    close browser

*** Test Cases ***
tc_dd.robot
    open orangehrm
    Sleep    5s
    orangehrmlogin    Admin    admin123

