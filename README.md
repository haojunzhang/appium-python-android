## appium-python-android

### Environment
* Windows 10
* Python 3.6

### Install Node.js (https://nodejs.org/en/download/)
```
node -v
```
### Install JDK (http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)
```
Add environment variable "JAVA_HOME"
value="jdk dir"
```
```
Add environment variable "CLASSPATH"
value="%JAVA_HOME%\lib\tools.jar;%JAVA_HOME%\lib\dt.jar"
```
```
Update environment variable "Path"
add value="%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin"
```
```
java -version
```
### Install AndroidSDK (https://developer.android.com/studio/)
```
Add environment variable "ANDROID_HOME"
value="sdk dir"
```
```
Update environment variable "Path"
add value="sdk dir\platform-tools"
add value="sdk dir\tools"
```
```
adb version
```
### Install Python (https://www.python.org/downloads/)
```
python -V
```
### Install Appium (http://appium.io/)

### Install appium-doctor (https://github.com/appium/appium-doctor)
```
npm install appium-doctor -g
```
### Install Appium-Python-Client (https://github.com/appium/python-client)
```
python setup.py install
```

### Screenshot
![sc1](screenshot/sc1.png)