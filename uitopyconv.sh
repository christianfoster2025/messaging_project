#!/bin/bash

pyside6-uic authentication/test_login.ui -o authentication/login_screen.py
echo "login screen compiled"
pyside6-uic authentication/test_signup.ui -o authentication/signup_screen.py
echo "sign up screen compiled"
pyside6-uic authentication/test_start.ui -o authentication/start_screen.py
echo "start screen compiled"