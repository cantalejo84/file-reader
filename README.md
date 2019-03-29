# file-reader

Command line tool to parse and analyze data, it has two execution mode.
+ **Batch mode**: Parse and analyze data in batch mode from a static file. (1. Parse the data with a time_init, time_end)
+ **Streaming mode**: Parse and analyze data in streaming from a live file. (2. Unlimited Input Parser)

### Requirements

+ Python 3.6.X

### Install

You only need to download the source code.

##  Use

## Batch mode

In this mode, the tool need a input data with the following format:<br/>

`<unix_timestamp> <foo> <bar>`

(Henceforth, we will use "foo" and "bar" to refer to the second and third columns)

**Data input example:<br/>**
```
1565647204351 Aadvik Matina
1565647205599 Keimy Dmetri
1565647212986 Tyreonna Rehgan
```

**Output:<br/>**
This mode returns a csv file with the records of type "foo" that refer to a given "bar" type,  in a given period.
The output file is in the "outputs" folder, with the next file format:
```
batch_out_<unix_init_time>_<unix_end_time>_<host_introduced>_<timestamp AAAMMDDHHMMSS>.csv
```

<br/>When you launch this mode it´s mandatory introduce four arguments.
+ <path_data_input>: file path, we recommend saving the input data in the folder 'resources' inside file-reader
+ <unix_init_time>: Period init
+ <unix_end_time>: Period end
+ \<bar> field type

**Execution example:**

`python3 file-reader/checker.py file-reader/resources/input.txt 1111 1113 Rehgan`

**Data input errors treatment:<br/>**

If any of the records of the input data is not correct, the tool will not stop de process, instead, it will create a new error file with the wrong records, withe the following format (in the outputs folder):
```
error_batch_out_<unix_init_time>_<uniz_end_time>_<host_introduced>_<timestamp AAAMMDDHHMMSS>.csv
```

## Streaming mode

In this mode the tool need a input data format like batch mode. This mode returns three file ouputs, every hour (config with 2 minute for test) 
+ (PROC1)Output csv file with the records of type "foo" that refer to a given "bar" (configurable) type, during the last hour.<br/>  
File format:<br/> 
```
stream_out_proc1_<host_introduced>_<timestamp AAAMMDDHHMMSS>.csv
```

+ (PROC2)Output csv file with "bar" type records that are referenced by records of a given "foo" (configurable) type,during the last hour.<br/>  
File format:<br/> 
```
stream_out_proc2_<host_introduced>_<timestamp AAAMMDDHHMMSS>.csv
```

+ (PROC3)Output file with "bar" type (separated by semicolons) that generate most references, during the last hour.<br/>
File Format:<br/>
```
stream_out_proc3_<timestamp AAAMMDDHHMMSS>.csv
```

When you launch this mode is mandatory introduce three arguments.
+ <path_data_input>: file path, it is recommend saving the input data in the folder 'resources' inside file-reader
+ \<hostname1>: For PROC1 outputs
+ \<hostname2>: For PROC2 outputs


**Execution example:**

`python3 file-reader/stream_checker.py file-reader/resources/input.txt 1111 1113 Rehgan`

##  Test

For test the tool, exists a example data in the resources folder.(outputs in "resources folder"")<br/>
Example:<br/>

**Test Batch mode:**
```
# Inside the file-reader folder
python3 batch_checker.py test/input-file-10000.txt 1565654627030 1565666186976 Sanjaya
```

**Test Streaming mode:**
```
# Inside the file-reader folder
python3 stream_checker.py test/input-file-10000.txt Sanjaya Manar
```
IMPORTANT: The streaming mode never end, it runs continuously. For check the process of new data you can append data to input file with other open console. (to terminate Ctrl+C)<br/>
For example:
```
# Indicative proposal:
f=open('~/file-reader/test/input-file-10000.txt','a')
f.write('\n1565733598999 alberto Sanjaya')
f.close

```

##  Performance considerations


This tool is robust and resilient, the goal is optimize memory and cpu, for this, i try to store the minimum possible data in memory, in order to avoid memory overflow. It has been designed to work with very large input data, for this reason, unfortunately the processing time is penalized.<br/>

Enjoy! and Happy coding :-) 