# JdeRobot_ROS_Challenge
Usage of ROS2 foxy, Navigation 2 foxy and gazebo
## Challenge Requirements

Part 1: Introduction to ROS2
  a. ‘Hello! ROS2 is fun’
    - Create a new ROS2 workspace
    - Create a ROS2 publisher - subscriber nodes and publish the message ‘Hello! ROS2 is
    fun’
    - Build the package using colcon
    - Use ROS2 run for executable
  b. Launch your robot
    - Choose a ROS2 robot of your choice, install it’s package
    - Visualize the robot’s laser scan data rviz2
Part 2: ROS2 Navigation2
  a. Navigate your turtlebot
  - Install ROS2 Navigation2 and gazebo
  - Perform waypoint navigation with turtlebot robot(or any other robot if you wish to).
  Include at least 3 waypoints in your result video.

## Part 1 Usage guidance
Prerequisite: ROS2, colcon installed

```bash
  git clone https://github.com/ThaiGSeP/JdeRobot_ROS_Challenge.git
  cd JdeRobot_ROS_Challenge
```
Step 2: Include workspace setup.bash into source

```bash
  source ./install/setup.bash
```

Step 3: Build node and executables

```bash
  colcon build
```

Step 4: Run publisher

```bash
  ros2 run hello-ros publisher
```

Step 4: Run publisher

Open another terminal

```bash
  ros2 run hello-ros subscriber
```


## Part 1 Visualise scan data using Rviz (turtle bot)

<img width="1344" alt="Screenshot 2023-04-02 at 16 33 59" src="https://user-images.githubusercontent.com/129572935/229339332-1442384f-5ff3-40e8-9f12-5ee26531365b.png">


## Part 2 Video
  https://youtu.be/3um6l_5CVj0
