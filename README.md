## Vision based teleoperation

### Abstract 

In this project, I have compared gesture-based methods with gamepad controllers for teleoperating mobile robots in third person view. The comparison study is based on the quantitative and qualitative data obtained from the study conducted during the class of Human Robot Interaction at Worcester Polytechnic Institute in the Fall of 2022. The study consisted of class students teleoperating a turtle bot (model burger) in a customized gazebo world consisting of a start point and an endpoint. I examine qualitative and quantitative metrics to effectively compare the above two methods. The results showed that the hand gesture-based controlling method showed promising results in competing with the gamepad controller. Hand gesture-based method was shown appreciation by the participants. However, the gamepad remained to be a superior method when comparing quantitative metrics for the two. I discuss the shortcomings of the hand-gesture method, modifications and potential use cases for it.

### Design 

The platform for conducting the study included an Asus laptop with the following configurations;
Hardware:
        ◦ Asus ZenBook Ultrabook Intel Core i5-8250U CPU @ 1.60GHz × 8 running Ubuntu 20.04, 8 GB RAM
        ◦ DualShock 4 Controller
The software configurations were as follows;
Software:
        ◦ ROS 1 Noetic
        ◦ Gazebo Simulator 11
Programming languages:
        ◦ Python 3+ & C++

The study consisted of participants teleoperating a turtle bot in a Gazebo simulation. Standard turtle bot ROS 3 packages were deployed to bring up a turtle bot in an empty gazebo world. The empty world was modified to contain an end goal and a few obstacles. The end goal was represented by a large unmissable red cube. The participants were asked to drive the turtle bot into the red cube through two the two teleoperating methods mentioned in section 3. The figure below shows the obstacle course that the users had to complete.

The start and end goal positions stayed constant during the entire course of the study for all the users. Time to reach the goal was stored in two different files, one for each teleoperating method. The RQT graph of the ROS system can be seen below. The “time tracker” node is responsible for tracking time taken to reach the goal point.

For the dual shock 4 controller, the ps4_joystick and ps_controller nodes take care of receiving inputs from the controller and sending twist commands to the turtle bot.

Similarly, for the hand gesture-based controller, the gesture_controller node is responsible for estimating hand pose and sending twist commands to the turtle bot in gazebo.

Each user was given some time to play around with controlling methods to get the hang of. They were subsequently timed for their task performance.
For quantitative data, the participants were timed in their task of teleoperating the turtle bot to the goal point, a node was coded in python that recorded time taken to move the robot from the start position to the goal position.

For qualitative data, a link to a Likert form was placed near the study platform in the form of a QR. Participants were made to fill it up post study. The questions in the form can be seen below in Figure 8;


### Study analysis

A total of 8 participants showed up for the user evaluation studies. 4 of these were from the HRI class and the rest were friends / associates. Each participant is a student at WPI. 7 of them were male while 1 of them was female. While this wasn’t ideal, there was not enough time to pursue more participants. Adding to the information, it was observed that all the participants were in their 20s. During testing, it was observed that velocities above 0.4 m/s for the turtlebot resulted in extremely unpredictable behavior of the robot. This wasn’t ideal for testing a new teleops method. Hence, the velocity commands were capped at 0.4 m/s.
Figure 10 below shows the distribution of the task completion time for each method. From the chart, it can be inferred easily that the dual shock 4 controller was the fastest method for teleoperating turtle bot out of the two.
