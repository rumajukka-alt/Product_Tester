*** Settings ***
Library    ../libs/measurement_keywords.py

*** Keywords ***
Measure Current Should Be Within Limits
    ${i}=    Measure Current
    Should Be True    ${i} > 0