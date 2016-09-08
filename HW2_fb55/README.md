# PUI2016 HW 2.

## Write scripts to stream real-time bus data from MTA through the MTA Bus Time interface. In order to access this data, you must first request an API key from MTA. 

This homework is based on assignments by Prof. Vo, who is a specialist in transportation and databases, and who you will meet later in the semester. 

  1. Visit MTA Bus Time for Developers at the [MTA Developers Tools](http://bustime.mta.info/wiki/Developers/Index)
  2. Click on the “Go here” link to fill in your information and request an API. You should be
  receiving an email from MTA within an hour (most of the time within only a few minutes).
  3. The key should be in the form of xxxxx-xxxxx-xxxxx-xxxxx-xxxxx. Please keep this key only to yourself as it would be your authorization token for MTA access and will be in this assignment. 


## Submission Info:
### You can work in groups, and you are encouraged to. Create a HW2\_\<netID> directory in your PUI2016\_\<netID> repository. Include a README.md that briefly summarizes the scope of the homework, and states who you worked with and what you specifically worked on.  Submit Assignment 1 and Assignment 2 by pushing them into your PUI2016\_\<netID>/HW2\_\<netID>  repository. Keep in mind that we will look for possible cases of plagiarism, and if the code is the same as that of people that you did not work with (there are automated ways to look for plagiarism in code) *you will be penalized*. 

  
MTA is using the SIRI (Service Interface for Real Time Information) API to serve their data in both XML and JSON format. I want you to use JSON for its increasing popularity in data access API over the web, and because it is a very natural format in Python, since it maps identically to a Python _dictionary_. 
Information on the vehicle monitoring stream is available [here](http://bustime.mta.info/wiki/Developers/SIRIVehicleMonitoring)
For example, using your key, you can retrieve all vehicle information for a bus line, e.g. B52, by
accessing the following [URL](http://api.prod.obanyc.com/api/siri/vehiclemonitoring.json?key=YOUR_KEY&VehicleMonitoringDetailLevel=calls&LineRef=B52)

### IMPORTANT NOTE:
The BusTime API server strictly enforces users to issue only 1 request per 30
seconds. Please do not constantly download or fetching data from the API in
shorter periods. It is a good idea to download a copy of the response to your
local machine for testing purposes. Also make sure to open it in an editor to
familiarize yourself with all the fields of the response.


# Assignment 1:  tracking each vehicle for a line

Write a Python script (not a notebook this time, so that you can experiment with writing code that takes line inputs) to retrieve and report information about active
vehicle for a bus line. 

__The final hand-in should be a single Python file, named
show_bus_locations\_\<netID>.py that takes exactly 2 arguments in the following format:__
```
python show_bus_locations.py <MTA_KEY> <BUS_LINE>
```

For example \<BUS_LINE> could be B52:

```
python show_bus_locations.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx B52
```
The above command has to fetch data from the MTA website through the SIRI API using the
provided key and return information on all available vehicles for the bus line \<BUS_LINE> (e.g. B52). 

__Your program
should output the following to the console:__ 
- the bus name, 
- the number of vehicles
- their current position

###SAMPLE OUTPUT:
```
Bus Line : B52
Number of Active Buses : 5
Bus 0 is at latitude 40.687241 and longitude -73.941661
Bus 1 is at latitude 40.690822 and longitude -73.920759
Bus 2 is at latitude 40.688363 and longitude -73.979563
Bus 3 is at latitude 40.688282 and longitude -73.979356
Bus 4 is at latitude 40.686839 and longitude -73.964694
```


# Assignment 2: next stop information

Write a Python script that displays information on the
next stop location of all busses of a given line. For example, whether the bus is approaching a stop, or is 1 stop
away from it. All the information is already included in the response JSON: your code needs to pull the current JSON file from the MTA API (as before) and parse it to find it. 
Have this script *output the data to a CSV file*. 
For buses that do not have this information,
please output “N/A” in the stop information fields. 

__The final hand-in should be a single Python
file, named get_bus_info\_\<netID>.py that takes 3 arguments in the following format:__

```
python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx <BUS_LINE> <BUS_LINE>.csv
```
__and output to a CSV file named \<BUS_LINE>.csv__:

```
Latitude,Longitude,Stop Name,Stop Status
40.755489,-73.987347,7 AV/W 41 ST,at stop
40.775657,-73.982036,BROADWAY/W 69 ST,approaching
40.808332,-73.944979,MALCOLM X BL/W 127 ST,approaching
40.764998,-73.980416,N/A,N/A
40.804702,-73.947620,MALCOLM X BL/W 122 ST,< 1 stop away
40.776950,-73.981983,AMSTERDAM AV/W 72 ST,< 1 stop away
40.737650,-73.996626,AV OF THE AMERICAS/W 18 ST,< 1 stop away
```

Hint:

- The stop information are included in the “OnwardCalls” field nested somewhere in the
JSON file.

Notes:

- Your program will be tested against the grader API key with different bus lines. Please
make sure that your Python scripts can read arguments from the command line.
- The bus line name is case-sensitive, aka. B52 is not the same as b52
- You can assume that your Python script will be run using the most recent Anaconda
distribution. If you use any additional Python packages that are not included in Anaconda,
please specify them in your README.md when you turn in your github repository.
- When the OnwardCalls field is empty, you must output “N/A” as values for both the “Stop
Name” and “Stop Status” fields.
