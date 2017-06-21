# iSpindel Plugin for CraftBeerPi 3.0

Allows your iSpindel digital hydrometer to send data to CraftBeerPi 3.0, such as the current temperature, gravity readings, and battery level. The plugin allows you to create multiple sensors, each of which is associated with a different data type that the iSpindel is capturing, so that you can use these sensors as you would any other sensor in CraftBeerPi.  You can also use multiple iSpindels for different fermentation chambers at the same time. See below for setup instructions and some screenshots of the configuration options.

## Installation

Click the **System** menu in CraftBeerPi, and then click **Add-On**.  Install the iSpindel plugin by clicking the **Download** button, and when you receive a notification, reboot the Raspberry Pi.

## Configuration

### CraftBeerPi Configuration
1. In CraftBeerPi, click on the **System** menu, and then choose **Hardware Settings**.
2. Click the **Add** button in the Sensor section, and fill out the sensor properties:
    1. **Name**: Give the sensor a name. This is specific to this sensor reading, and does not need to match the iSpindel device name. It can be something like Wort Gravity or iSpindel Temperature.
    2. **Type**: Choose iSpindel.
    3. **iSpindel Name**: This should be set to the iSpindel device name.
    4. **Data Type**: Each iSpindel has many different types of data that it reports, such as Temperature, Gravity, and Battery, so select the one that you are configuring for this particular sensor.
    5. **Tuning Polynomial**: *This field is only required if Data Type is set to Gravity*. Enter the tuning polynomial that is calculated when calibrating your iSpindel. This field determines the calculation that will take the value that the iSpindel has sent and convert it into the desired measurement of gravity. Use the variable `tilt` in your polynomial to represent the iSpindel angle reading. 
    6. **Gravity Units**: *This field is only required if Data Type is set to Gravity*. Based on the calculation in your polynomial, you will have a gravity result in one of several different units, so you can pick the specific unit here so that it will be displayed properly in CraftBeerPi. The plugin does not convert the values into this unit. The choices are SG (Specific Gravity), Brix, and °P (Degrees Plato).
    7. Once you have filled out the sensor fields, click **Add**.
3. Repeat the above steps if you want to additional sensors for the other data types that your iSpindel reports, or if you have more than one iSpindel, you can create sensors for those devices as well.
4. You can now add any of the iSpindel sensors to kettles or fermenters in your brewery, or you can view their data on the dashboard or graph their data with the charts.
