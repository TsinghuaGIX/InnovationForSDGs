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
2. After add a label to the UI, the toolbox will show tools for the label.
3. Use the tools to update the label's color.
4. Run the project. 

<h2 id="example2"> Example 2: Jumping Frog</h2>

1. Add images to the project.
2. Implement the logic of update the image path.
3. Sync the images to CoreS3 by run the project in Wi-Fi mode.
4. Run the project.

<h2 id="example3"> Example 3: Sensor Reader</h2>

1. Connect the sensor use Port B.
2. Add the `Light Unit` in the Resource Panel.
3. Use the tool in toolbox to read the sensor value.
4. Run the project.

<h2 id="example4"> Example 4: Rainblow LED</h2>

1. Connect the LED with Port B.
2. Add the `RGB unit` in the Resource Panel.
3. Implement HSV to RGB algorithm with Python.
4. Convert python code to UIFlow Block.
5. Add the new block to the project.
6. Implement the function to update LED colors.
7. Implement the loop block.
8. Upload the python file to the device.
9. Run the Project.

## Reference
[1] [Core S3 Development Kit Written by Adam Bryant](https://m5stack.oss-cn-shenzhen.aliyuncs.com/resource/docs/products/core/CoreS3/CoreS3%20Development%20Kit-compressed%20(1).pdf)

[2] [Quick Start Guide for UIFlow Web IDE](https://docs.m5stack.com/en/uiflow2/uiflow_web)

[3] [M5CoreS3 firmware burning and program pushing](https://docs.m5stack.com/en/uiflow2/m5cores3/program)

[4] [MicroPython documentation and references](https://uiflow-micropython.readthedocs.io/en/latest/)



