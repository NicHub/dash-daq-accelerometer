# Dash DAQ Accelerometer

## Introduction
A dash application which facilitates the controlling of Phidgets 1041_B Accelerometer. [Try out this app](https://dash-gallery.plotly.host/dash-daq-accelerometer) and learn more about this application from our [blog entry](https://www.dashdaq.io/read-data-from-a-phidgets-accelerometer).

### Phidgets accelerometer
The Phidgets Spatial is a 3-axis accelerometer that :
- Track whether an object is moving, and in which direction (x, y, z)
- Detect the presence of nearby movement or vibration
- Track the orientation of a stationary object relative to the earth's gravitational pull

The 1041 device can measure ±8 g's (±78 m/s2) per axis. It could be connected to your computer via USB and programmatically tracked. Phidgets provide resourceful property-related [APIs](https://www.phidgets.com/?view=api) for programmers.

### Dash-daq
[Dash DAQ](http://dash-daq.netlify.com/#about) is a data acquisition and control package built on top of Plotly's [Dash](https://plot.ly/products/dash/). It comprises a robust set of controls that make it simpler to integrate data acquisition and controls into your Dash applications.

## Requirements
We suggest you to create a virtual environment for python3 to run this app. To do so, run:
```
python3 -m virtualenv [your environment name]
```
```
source activate [your environment name]
```

To install all of this app-specific required packages to this environment, simply run:

```
pip install -r requirements.txt
```
## How to use the app
There are two versions of this application. A mock version for the user to play with, without any instruments connected, and a local version, that can be connected to a device.

### Local application 

If you would like to run the __**local version**__, connect the PhidgetSpatial device to your computer using USB cable and run in command line : 
```
python app.py
```
Open the web address in your browser,you will see the control panel of the accelerometer, with your device information displayed at the top. 
The app is ready-to-use. 

![changefail](screenshots/accelerometer.png)

### Mock application
To run __**mock version**__, simply run in command line:

```
python app_mock.py
```

And you will see the following prompt:

![changefail](screenshots/python_appmock.png)

Open the web address in your browser:  

![changefail](screenshots/openport.png)

The control panel of your accelerometer will be displayed. To change to a dark theme layout, click on the toggle switch at the top of the page. 

### Controls
* Connection Toggle: Disconnect and connect to the device, indicator will light up when Dash DAQ is connected to the device.
* Change interval: Adjust acceleration change interval by dragging the sliders, value will be reflected on LED display accordingly.
* Data interval: Adjust acceleration data interval by dragging the sliders, value will be reflected on LED display accordingly.

The measured data detected on x, y and z axes is gathered from the device, and will be displayed on the gauges.


## Resources

### About the Phidgets instruments

Technical details about Phidgets 1041_B could be found in [**Phidget User Guide**](https://www.phidgets.com/?tier=3&catid=10&pcid=8&prodid=1022).

### Dash
Dash abstracts away all of the technologies and protocols required to build an interactive web-based application, and is a simple and effective way to bind a user interface around your Python code. To learn more about Dash, check out our [documentation](https://dash.plot.ly/).
