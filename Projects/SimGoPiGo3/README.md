# GoPiGo3 SIMULATION for off platform dev

This simulation demonstrates the feasibility of creating an off platform development/test environment for the ModularRobotics GoPiGo3 robot.

Limitations:
- Simulates easygopigo3.EasyGoPiGo3 class
- Simulates the Distance Sensor


Where a program normally has:

```
import easygopigo3
```

the developer can add:
```
# Uncomment import of sim.easygopigo3 or easygopigo3 as appropriate
import sim.easygopigo3 as easygopigo3
# import easygopigo3
```

run the program, and see any print statements as in:

```
$ ./myRobot.py

Log: Starting myRobot.py main()

Log: Instantiate EasyGoPiGo3 object

Log: Instantiate distance sensor object

Log: set_robot_constants(66.4)

Log: save_robot_constants()

Log: load_robot_constants()

Log: volt() returns 9.5v

Log: set_speed(150)

Log: get_speed() returns 150 DPS

Log: reset_speed()

Log: get_speed() after reset returns 300 DPS

Log: forward() for 2 seconds

Log: stop()

Log: egpg.ds.read_mm() returned 914.4 mm

Log: drive_cm(10.16)

Log: egpg.ds.read_mm() returned 814.4 mm

Log: egpg.ds.read_inches() returned 31.9 inches

Log: drive_inches(-4.0)

Log: egpg.ds.read_inches() returned 35.8 inches

Log: End myRobot.py main()
```

and the sim.log contains:

```
$ more sim.log
2020-11-22 23:30|[gopigo3.py.<module>]sim.gopigo3 imported
2020-11-22 23:30|[easygopigo3.py.<module>]sim.easygopigo3 imported
2020-11-22 23:30|[gopigo3.py.__init__]Simulated GoPiGo3 object instantiated
2020-11-22 23:30|[easygopigo3.py.load_robot_constants]sim.easygopigo3.load_robot_constants() called
2020-11-22 23:30|[easygopigo3.py.set_robot_constants]sim.easygopigo3.set_robot_constants(66.6,116.6) called
2020-11-22 23:30|[easygopigo3.py.set_speed]sim.easygopigo3.set_speed(300) called
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_limit_left' = 300 updated **
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_limit_right' = 300 updated **
2020-11-22 23:30|[easygopigo3.py.__init__]Simulated EasyGoPiGo3 instatiated
2020-11-22 23:30|[easygopigo3.py.init_distance_sensor]sim.easygopigo3.init_distance_sensor(port=I2C) called
2020-11-22 23:30|[easy_distance_sensor.py.__init__]sim.di_sensors.EasyDistanceSensor object instantiated
2020-11-22 23:30|[distance_sensor.py.__init__]Initializing sim.di_sensor.distance_sensor.DistanceSensor() object
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'rangeSensor_mm' = 914.4 updated **
2020-11-22 23:30|[easygopigo3.py.set_robot_constants]sim.easygopigo3.set_robot_constants(66.6,116.6) called
2020-11-22 23:30|[easygopigo3.py.save_robot_constants]sim.easygopigo3.save_robot_constants() called
2020-11-22 23:30|[easygopigo3.py.load_robot_constants]sim.easygopigo3.load_robot_constants() called
2020-11-22 23:30|[easygopigo3.py.set_robot_constants]sim.easygopigo3.set_robot_constants(66.6,116.6) called
2020-11-22 23:30|[easygopigo3.py.set_speed]sim.easygopigo3.set_speed(150) called
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_limit_left' = 150 updated **
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_limit_right' = 150 updated **
2020-11-22 23:30|[easygopigo3.py.get_speed]sim.easygopigo3.get_speed() called
2020-11-22 23:30|[easygopigo3.py.reset_speed]sim.easygopigo3.reset_speed() called
2020-11-22 23:30|[easygopigo3.py.set_speed]sim.easygopigo3.set_speed(300) called
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_limit_left' = 300 updated **
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_limit_right' = 300 updated **
2020-11-22 23:30|[easygopigo3.py.get_speed]sim.easygopigo3.get_speed() called
2020-11-22 23:30|[easygopigo3.py.forward]sim.easygopigo3.forward() called
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_dps_left' = 1000 updated **
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_dps_right' = 1000 updated **
2020-11-22 23:30|[easygopigo3.py.stop]sim.easygopigo3.stop() called
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_dps_left' = 0 updated **
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'motor_dps_right' = 0 updated **
2020-11-22 23:30|[easygopigo3.py.drive_cm]sim.easygopigo3.drive_cm(10) called
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'rangeSensor_mm' = 814.4 updated **
2020-11-22 23:30|[easygopigo3.py.drive_inches]sim.easygopigo3.drive_cm(-4.0) called
2020-11-22 23:30|[easygopigo3.py.drive_cm]sim.easygopigo3.drive_cm(-10.16) called
2020-11-22 23:30|[simDataJson.py.saveData]** simData 'rangeSensor_mm' = 916.0 updated **
```

This is the test program:

```
#!/usr/bin/env python3


# Uncomment import of sim_easygopigo3 or easygopigo3 as appropriate
import sim.easygopigo3 as easygopigo3
# import easygopigo3
from time import sleep
import traceback

def testEachMethod(egpg):

    print("Log: set_robot_constants(66.4)")
    egpg.set_robot_constants(66.6, 116.6)

    print("Log: save_robot_constants()")
    egpg.save_robot_constants()

    print("Log: load_robot_constants()")
    egpg.load_robot_constants()

    print("Log: volt() returns {}v".format(egpg.volt()))

    print("Log: set_speed(150)")
    egpg.set_speed(150)

    print("Log: get_speed() returns {} DPS".format(egpg.get_speed()))

    print("Log: reset_speed()")
    egpg.reset_speed()
    print("Log: get_speed() after reset returns {} DPS".format(egpg.get_speed()))

    print("Log: forward() for 2 seconds")
    egpg.forward()

    sleep(2)

    print("Log: stop()")
    egpg.stop()

    print("Log: egpg.ds.read_mm() returned {} mm".format(egpg.ds.read_mm()))

    print("Log: drive_cm(10.16)")
    egpg.drive_cm(10)

    print("Log: egpg.ds.read_mm() returned {} mm".format(egpg.ds.read_mm()))
    print("Log: egpg.ds.read_inches() returned {} inches".format(egpg.ds.read_inches()))

    print("Log: drive_inches(-4.0)")
    egpg.drive_inches(-4.0)

    print("Log: egpg.ds.read_inches() returned {} inches".format(egpg.ds.read_inches()))


def main():

    print("Log: Starting myRobot.py main()")

    try:
        print("Log: Instantiate EasyGoPiGo3 object")
        egpg = easygopigo3.EasyGoPiGo3(use_mutex=True)
        print("Log: Instantiate distance sensor object")
        egpg.ds = egpg.init_distance_sensor()
    except Exception as e:
        print("Log: {}".format(str(e)))
        exit(1)

    try:
        testEachMethod(egpg)
    except Exception as e:
        print("Log: {}".format(str(e)))
        traceback.print_exc()
        exit(1)

    print("Log: End myRobot.py main()")



if __name__ == "__main__":
    main()
```
The simulator lives in a folder named ‘sim’ in the folder with the user program to test:
```
$ls -1
myRobot.py
sim
sim.log
```

Note: it isn’t simulating movement over time - would have to launch a subprocess for that and I didn’t really want to get that tricky.

Just an idea if someone wanted to flesh out a simulator for remote code testing prior to getting access to a bot.


