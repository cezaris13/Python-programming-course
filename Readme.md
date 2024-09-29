# Python course in Eötvös loránd university in spring semester 2023
## Installation
```bash
make init

make run # To see the temperature data in terminal

make run_gui # To see the temperature data in graphical mode

make test
```

## Objective

- Develop a Python-based IoT device simulator
- Implement basic data analytics and processing
- Create an eye-catching monitoring dashboard to display sensor data and analytics results
- Use Python data structures, classes, OOP objects, instance and class variables, OOP methods, pip, staticmethods, files & standard library, exception handling, modules, and packages

## Steps
- Create a `Sensor` class that simulates the behavior of a real-world sensor.
- Implement a `DataProcessor` class that processes and performs basic analytics on the sensor data.
- Create a `Communication` class that simulates communication with a central server.
- Build a Device class that brings together the `Sensor`, `DataProcessor`, and `Communication` classes to simulate a complete IoT device.
- Implement exception handling in the Device class for potential errors.
- Create a `Dashboard` class that displays the collected sensor data and analytics results.
- Organize your code into modules and packages to improve its maintainability and readability.
- Write tests to verify the functionality of the IoT device simulator.

More about this task can be read [here](/Assignment%201.pdf)

## Images
![image](/images/temperature_terminal.png)
*Simple terminal based data visualization*

![image](/images/temperature_graphs.png)
*Graphical mode of the iot device simulator*
