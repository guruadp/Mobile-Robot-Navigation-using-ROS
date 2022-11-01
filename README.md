# Mobile Robot Navigation using ROS

## 1. Project Objectives

1. Build a specific robot model on SolidWorks and export it as URDF.

2. Add LiDAR Sensor on to your robot and show your visualization (LiDAR points) in RViz.

3. Perform teleop and move around in the map in Gazebo.

4. Create a simple publisher and subscriber to move in a straight line or circular loop.

## 2. Installation of Dependencies

To install the ROS - Noetic type the following command in the terminal:

```` 
$ sudo apt install ros-noetic-desktop-full
````
To install the python 3 type the following command in the terminal:

```` 
$ sudo apt-get install python3
````

## 3. Setting up the package

1. Create a workspace folder and create a src folder in it. Clone the repo into your src folder.<br />

3. Go to your catkin_ws by typing the command  ````$ cd <your catkin_ws_name>```` 

4. Place that package in your catkin_ws and build that package<br />

5. Source ROS everytime you open a new terminal or made any changes in the ROS package using the command
````
source devel/setup.bash
````
## 4. Instruction to run RViz to visualize LiDAR

1. Open two terminals and source ROS using the command mentioned above <br />

2. Run the command below to launch the toy car in Gazebo environment
```` 
roslaunch mobile_robot template_launch.launch 
```` 
3. In your other terminal run the command, to launch the teleop controllers
````
rosrun rviz rviz
````

4. Add the RobotModel and Laserscan to visualize the robot & LiDAR in RViz

## 5. Instructions to run the toy car using Teleop

1. Open two terminals and source ROS using the command mentioned above & Run the command below in one of the terminal <br />

```` 
roslaunch mobile_robot template_launch.launch 
```` 
2. In the second terminal run the command below, to launch the teleop controllers
````
rosrun mobile_robot teleop_template.py
````
3. The controls to move the toy car are mentoined in the teleop terminal <br />

## 6. Instructions to run the toy car using Subscriber and Publisher

## ---------- For Straight Line Movement ----------

1. Open three terminals and source ROS in each terminal<br />

2. Run the command below in the first terminal to launch the toy car
```` 
roslaunch mobile_robot template_launch.launch 
```` 
3. In your second terminal run the command, to launch the subscriber 
````
rosrun mobile_robot subscriber_straight_line.py
````
4. In your third terminal run the command, to launch the publisher
````
rosrun mobile_robot publisher_straight_line.py
````

## ---------- For Circular Loop Movement ----------

1. Open three terminals and source ROS using the command mentioned above <br />

2. Run the command below in the first terminal to launch the toy car
```` 
roslaunch mobile_robot template_launch.launch 
```` 
3. In your second terminal run the command, to launch the subscriber 
````
rosrun mobile_robot subscriber_circle.py
````
4. In your third terminal run the command, to launch the publisher
````
rosrun mobile_robot publisher_circle.py
````
