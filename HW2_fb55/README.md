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
seconds. Please do not constantly download or fetch data from the API in
shorter periods. It is a good idea to download a copy of the response to your
local machine for testing purposes. Also make sure to open it in an editor to
familiarize yourself with all the fields of the response.


# Assignment 1:  tracking vehicles for a chosen bus-line

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

### Grading:

All or nothing at all: 
- 100% of the points if the TA can run the code with his/her MTA key and get a correctly formatted output.

The TAs will do minimal inspection of your code if it does not work. If the issue is not immediately obvious you will not get points for this assignment. 

Working code but wrong output format (but correct content) will earn 50% of the points.

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


### GRADING: 
All or nothing at all: 
- 100% of the points if the TA can run the code with his/her MTA key and get a correctly formatted output.

The TAs will do minimal inspection of your code if it does not work. If the issue is not immediately obvious you will not get points for this assignment. 

Working code but wrong output format  (but correct content) will earn 50% of the points.

# Assignment 3: Read CSV files with pandas

Work on [compute](https://github.com/fedhere/PUI2016_fb55/blob/master/computationalResources.md). Choose a [dataset within the CUSP data facility (DF)](https://datahub.cusp.nyu.edu/dataset) that is available in CSV format (look at the format labels in the list of datasets). Chose one that has _at least_ 2 __numerical value__ columns. __DO NOT DOWNLOAD IT__: you must access it throught compute directly from the DF!! The data location may be stated in the description of the dataset, which you access by clicking the dataset, and may be stated in full in full under __Cusp Location__ (e.g. /gws/open/NYCOpenData/nycopendata/data/5b3a-rs48), or sometimes indicated by the __Data ID__	(e.g. uedp-fegm), in which case the first part of the path /gws/open/NYCOpenData/nycopendata/data/ is implicit.

1. Set an environmental variable DFDATA that points to the data facility location /gws/open/NYCOpenData/nycopendata/data/.

Write a Jupyter Notebook on compute. This will require you to use the JupyterHub ([instructions here](https://datahub.cusp.nyu.edu/documents/guides/Jupyter_Notebook_from_your_browser_Mac.pdf) ). Write a notebook that:

2. Use pandas to read in the CSV file from the DF as a dataframe. The CSV file must have at least 2 numerical value columns.
3. Display the top few rows of the DF in your notebook. This table __must be rendered__.
4. Remove all but 2 _numerical values_ columns of your choice (you can use the drop method in the dataframe) 
5. Display the reducted dataframe. This table __must be rendered__.
6. Plot the columns one against the other in a scatter plot (usual rules for plotting apply, see [Grading Guidelines](https://github.com/fedhere/PUI2016_fb55/blob/master/README.md) and the [instruction notebooks for HW1 Extra Credit](https://github.com/fedhere/PUI2016_fb55/blob/master/HW1_fb55/HW1_3_fb55.ipynb), part 3, for more detailed hints on how to display your rendered plots. The plot __must be rendered__.
7. Repeat the steps above 1-6 with a CSV file that contains _a date/time column and a numerical value_. Plot the numerical value against the date/time (hint: make sure your tick labels are readable. you can use they keyword rot in the df.plot() method, as for example df.plot(....., rot=90) to rotate the tick labels by 90 degrees.


### GRADING: 
You must use the envuronmental variable.

Your notebook must display
- the data tables for the unreducted datasets (first few columns)
- the data tables for the reducted datasets (first few columns)
- the plots for each dataframe, with usual rules for plotting applying: visible and readable axes, title, legend, caption. 
