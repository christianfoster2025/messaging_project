#!/bin/bash

{
    pyside6-uic authentication/test_login.ui -o authentication/login_screen.py &&
    echo "login screen compiled"

} || {
    echo 'login screen compilation failed'
}

{
    pyside6-uic authentication/test_signup.ui -o authentication/signup_screen.py &&
    echo "sign up screen compiled"

} || {
    echo 'sign up screen compilation failed'
}

{
    pyside6-uic authentication/test_start.ui -o authentication/start_screen.py &&
    echo "start screen compiled"

} || {
    echo 'start screen compilation failed'
}

{
    pyside6-uic main_window/test_mainwindow.ui -o main_window/main_screen.py &&
    echo "main screen compiled"

} || {
    echo 'main screen compilation failed'
}

{
    pyside6-uic main_window/test_contactdialogue.ui -o main_window/contact_dialogue.py &&
    echo "contact dialogue compiled"

} || {
    echo 'contact dialogue compilation failed'
}
