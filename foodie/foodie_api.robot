*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://localhost:5000/api/v1

*** Test Cases ***
Full Foodie API Flow

    Create Session    foodie    ${BASE_URL}

    # Register Restaurant
    ${rest_payload}=    Create Dictionary
    ...    name=Robot Food Hub
    ...    category=Indian
    ...    location=Chennai
    ${rest_response}=    POST On Session    foodie    /restaurants    json=${rest_payload}
    Status Should Be    201    ${rest_response}
    ${restaurant}=    Set Variable    ${rest_response.json()}
    ${restaurant_id}=    Set Variable    ${restaurant['id']}

    # Approve Restaurant
    ${approve}=    PUT On Session    foodie    /admin/restaurants/${restaurant_id}/approve
    Status Should Be    200    ${approve}

    # Add Dish
    ${dish_payload}=    Create Dictionary
    ...    name=Dosa
    ...    type=Veg
    ...    price=100
    ${dish_response}=    POST On Session    foodie    /restaurants/${restaurant_id}/dishes    json=${dish_payload}
    Status Should Be    201    ${dish_response}
    ${dish}=    Set Variable    ${dish_response.json()}
    ${dish_id}=    Set Variable    ${dish['id']}

    # Register User
    ${user_payload}=    Create Dictionary
    ...    name=RobotUser
    ...    email=robot@test.com
    ...    password=1234
    ${user_response}=    POST On Session    foodie    /users/register    json=${user_payload}
    Status Should Be    201    ${user_response}
    ${user}=    Set Variable    ${user_response.json()}
    ${user_id}=    Set Variable    ${user['id']}

    # Place Order
    ${dish_list}=    Create List    ${dish_id}
    ${order_payload}=    Create Dictionary
    ...    user_id=${user_id}
    ...    restaurant_id=${restaurant_id}
    ...    dishes=${dish_list}
    ${order_response}=    POST On Session    foodie    /orders    json=${order_payload}
    Status Should Be    201    ${order_response}
    ${order}=    Set Variable    ${order_response.json()}
    ${order_id}=    Set Variable    ${order['id']}

    # Give Rating
    ${rating_payload}=    Create Dictionary
    ...    order_id=${order_id}
    ...    rating=5
    ...    comment=Superb
    ${rating_response}=    POST On Session    foodie    /ratings    json=${rating_payload}
    Status Should Be    201    ${rating_response}

    # Verify Orders by User
    ${orders_user}=    GET On Session    foodie    /users/${user_id}/orders
    Status Should Be    200    ${orders_user}

    # Verify Orders by Restaurant
    ${orders_rest}=    GET On Session    foodie    /restaurants/${restaurant_id}/orders
    Status Should Be    200    ${orders_rest}
