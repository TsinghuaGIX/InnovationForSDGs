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

What does `Setup` Block do?

<h2 id="example2"> Example 2: Jumping Frog</h2>

What does `Loop` Block do?

<h2 id="example3"> Example 3: Sensor Reader</h2>

How to connect `Sensor`?

<h2 id="example4"> Example 4: Rainblow LED</h2>

How to define `function` and add `cutomized module`?

