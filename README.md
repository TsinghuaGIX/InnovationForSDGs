<div align="center">

  # Transformative Innovation for SDGs with Visual Programming on M5Stack 
  
</div>

<h3 align="center">
    <a href="https://gix.tsinghua.edu.cn/en/">GIX</a> |
     <a href="https://wangxu.ai/">Slides</a> |
    <a href="#">Gallery</a> 
</h3>

## Table of Contents

1. [Introduction to M5Stack](#Introduction-To-M5Stack)

2. [Visual Programming](#Visual-Programming)

3. [Example 1: Hello World](#example1)

4. [Example 2: Jumping Frog](#example2)

5. [Example 3: Sensor Reader](#example3)

6. [Example 4: Rainbow LED](#example4)

7. [Reference](#Reference)

## Introduction to M5Stack

**M5Stack** refers to Standard `5×5cm` functionally `Stacking` `Modularized` components hardware system.

Now, M5Stack is a leading provider of IoT solutions, committed to providing developers worldwide with convenient and flexible development components and tools. They offer `stackable hardware modules` and user-friendly `graphical programming` platform, as well as customized services, to provide clients in industrial IoT, smart agriculture, smart retail, STEM education, and many other fields with efficient and reliable Quick&Easy IoT Development experience.

The Hardware Library:

| SKU-ID| Modules  | Type | Document |
| ------------- | ------------- |  ------------- | ------------- |
| K128  | CoreS3  | Controller| https://docs.m5stack.com/en/core/CoreS3 |
| K132  | Cardputor  | Controller | https://docs.m5stack.com/en/core/Cardputer |
| U021 | Light Sensor Unit| Sensor | https://docs.m5stack.com/en/unit/LIGHT |
| U010 | Time-of-Flight Distance Ranging Sensor| Sensor | https://docs.m5stack.com/en/unit/TOF |
| U029 | Mini Heart Rate Unit (MAX30100) Pulse Oximeter| Sensor| https://docs.m5stack.com/en/unit/heart |
| U004 | PIR Motion Sensor | Sensor | https://docs.m5stack.com/en/unit/PIR |
| U001­C | ENV III Unit with Temperature Humidity Air Pressure Sensor | Sensor | https://docs.m5stack.com/en/unit/envIII |
| U019 | Earth Moisture Sensor | Sensor | https://docs.m5stack.com/en/unit/earth |
| U104 | CO2L Unit with Temperature and Humidity Sensor | Sensor | https://docs.m5stack.com/en/unit/CO2L |
| U040­B | I2C Hub 1 to 6 Expansion | Hub| https://docs.m5stack.com/en/unit/pahub2 |
| A093 |Digital RGB LED Weatherproof Strip| Output| https://docs.m5stack.com/en/unit/rgb_led_strip |
| A045­B | Neo HEX 37 RGB LED Board | Output | https://docs.m5stack.com/en/unit/neohex |
| U132 | Passive Buzzer | Output | https://docs.m5stack.com/en/unit/buzzer |
| U144 | Mechanical Key Button Unit | Input| https://docs.m5stack.com/en/unit/key |
| SDCS2/64GBCA |SDCard| Storage| - |




## Visual Programming
Visual programming is a way of creating software programs or applications without writing code. Instead, icons, symbols, and flowcharts make such programs. Traditional programming is the process of writing code using a programming language, such as Java, Python, or C++. This method requires a deep understanding of programming concepts and syntax.

* Pros: Easier to learn and use
* Cons: Limitation in customization and flexibility

UIFlow2.0 is a visual programming platform for M5Stack products.

To enable UIFlow2.0, the first is to burn the UIFlow2.0 firmware.

The tutorial for CoreS3 to burn the firmware: https://docs.m5stack.com/en/uiflow2/m5cores3/program

UIFlow2.0 now use the web IDE:https://uiflow2.m5stack.com/

Carefully for the two mode to connect the device with UIFlow2.0: USB mode and Wi-Fi mode.

* USB mode: Fast but may not be compatible.
* Wi-Fi mode: Better compatible with UIFlow but sometimes stupid.

**Final solution** for bugs: 
``reburn UIFlow2.0 firmware``










<h2 id="example1"> Example 1: Hello World </h2>

1. Use UI Editor to add a new `Label`. Change the text of the Label to `Hello World`.
   
   ![image](https://github.com/user-attachments/assets/f6e6bc9b-3d1d-412b-a40d-b39d374d01b7)


2. After add a label to the UI, the toolbox will show tools for the label.

   ![image](https://github.com/user-attachments/assets/d6e3950f-091b-484c-a33a-761cd089b3c8)

   
3. Use the tools to update the label's color.

  <img width="787" alt="image" src="https://github.com/user-attachments/assets/304617d1-90ac-48ee-98ba-93b4dd466705">

   
4. Run the project.
   
![helloworld](https://github.com/user-attachments/assets/d04591bb-31d8-4100-93e0-0df5ea8f0a85)

  


<h2 id="example2"> Example 2: Jumping Frog</h2>

1. Add images to the project.

![image](https://github.com/user-attachments/assets/58ec914f-ec3e-450c-9c74-ae61f381ef2e)

   
2. Implement the logic of update the image path.

<img width="730" alt="image" src="https://github.com/user-attachments/assets/e34d76c7-4c2b-454e-8d8e-5f6257a51e94">

  
3. Sync the images to CoreS3 by run the project in Wi-Fi mode.

![image](https://github.com/user-attachments/assets/f4d34188-8d30-4705-9a6e-72e8225fabb5)
Make sure the device's status is green.
   
4. Run the project.

   ![IMG_6578-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/162bb9e8-37e7-43f6-be15-d7933c6b59dd)


<h2 id="example3"> Example 3: Sensor Reader</h2>

1. Connect the sensor use Port B.
   
   ![IMG_6579](https://github.com/user-attachments/assets/23de658e-48e2-4c89-82f0-67fe19935564)

2. Add the `Light Unit` in the Resource Panel.

<img width="1122" alt="add_light_unit" src="https://github.com/user-attachments/assets/1f4b0c2d-bba5-4f5d-8125-9cb1cd86f2cd">

   
3. Use the tool in toolbox to read the sensor value.

![image](https://github.com/user-attachments/assets/97602f9b-6261-417f-9888-fc7b279a78ca)

   
4. Run the project.

   ![IMG_6580-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/e2741dc1-a8af-4247-a3ea-cacb32f5682a)


<h2 id="example4"> Example 4: Rainblow LED</h2>

1. Connect the LED with Port B.

![IMG_6581](https://github.com/user-attachments/assets/540bf460-6e40-4a4a-abac-7f80ae44f9c0)

   
2. Add the `RGB unit` in the Resource Panel.

<img width="1119" alt="image" src="https://github.com/user-attachments/assets/e828aaaa-6c44-4318-a106-6cb2a20318f4">

   
3. Implement HSV to RGB algorithm with Python.

<img width="1168" alt="image" src="https://github.com/user-attachments/assets/4a3e5ae1-08e5-4820-b611-a5a62beaf445">

   
4. Convert python code to UIFlow Block.

![image](https://github.com/user-attachments/assets/b874e084-a23f-41ba-bb6f-396bb2093964)

   
5. Add the new block to the project.

<img width="1111" alt="image" src="https://github.com/user-attachments/assets/fc282839-68d6-4bc5-b6f7-de8d31fb7ed5">

    
6. Implement the function to update LED colors.

<img width="557" alt="image" src="https://github.com/user-attachments/assets/4cba9c20-e6e6-49c1-b709-b4334094048a">

    
7. Implement the loop block.
   
<img width="475" alt="image" src="https://github.com/user-attachments/assets/233b8e5c-32cb-462f-bb79-5487be44e5b1">

8. Upload the python file to the device.

<img width="673" alt="image" src="https://github.com/user-attachments/assets/f6251629-7ee1-4764-ae8f-1bdfdfffc2eb">

    
9. Run the Project.

    ![IMG_6582-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/ca2d2863-b1f2-481a-a16f-b0a458867c1c)

**Hope all of you have a good time with M5Stack！！！**


## Reference
[1] [Core S3 Development Kit Written by Adam Bryant](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/CoreS3%20Development%20Kit-compressed%20(1).pdf)

[2] [Quick Start Guide for UIFlow Web IDE](https://docs.m5stack.com/en/uiflow2/uiflow_web)

[3] [M5CoreS3 firmware burning and program pushing](https://docs.m5stack.com/en/uiflow2/m5cores3/program)

[4] [MicroPython documentation and references](https://uiflow-micropython.readthedocs.io/en/latest/)



