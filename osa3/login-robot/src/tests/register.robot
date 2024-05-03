*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  emppu  emppu123
    Output Should Contain  Username is already in use

Register With Too Short Username And Valid Password
    Input Credentials  em  emppu123
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  emppu123  emppu123
    Output Should Contain  Username should contain only characters a-z

Register With Valid Username And Too Short Password
    Input Credentials  ville  em123
    Output Should Contain  Password must be at least 8 characters long


Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  emilia  termostaatti
    Output Should Contain  Password must contain at least one non-letter character
    
*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  emppu  emppu123
    