#!/usr/bin/env python3

# FILE:  test_sim.py

# PURPOSE: Test simulated easygopigo3.py

print("Importing gopigo3 module")
import gopigo3

print("Instantiating a gopigo3.GoPiGo3() object")
gpg = gopigo3.GoPiGo3()

print("Importing easygopigo3 module")
import easygopigo3

print("Instantiating a gopigo3.GoPiGo3() object")
egpg = easygopigo3.EasyGoPiGo3()

print("Test EasyGoPiGo3.drive_cm(10)")
egpg.drive_cm(10)

