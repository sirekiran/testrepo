# testrepo
API testing for positive and negative cases of some API end point

This project contains three files

1.tmsandbox_testone.py

Description:
This file will make a call to one API endpoint and will read all the responses for making direct assertions and will fail the test right away even if one assertion got failed.

2.tmsandbox_testtwo.py

Description:
This file will make a call to one API endpoint and will read all the responses.
Once responses are available it will keep on asserting each requirement in try catch blocks and if it got to see any exceptions then it would not fail the test and will still proceed further to check other requirements and the final result would get logged on the console and also on the file by name "report.txt" in one's current directory for reference.

3.tmsandbox_testthree.py

Description:
This file will go with negative validations and logs errors on console and to the file "report.txt" in one's current directory for reference.



To run the files under this project one should have python in their local nodes (Machines/Laptops)

command to execute :

python tmsandbox_testone.py

python tmsandbox_testtwo.py

python tmsandbox_testthree.py



Respective file output's:


python tmsandbox_testone.py

Execution output should be :

All the Assertions are successful



python tmsandbox_testtwo.py

Execution output should be :

All the Assertions verification are successful with catching exceptions




python tmsandbox_testthree.py

Execution output should be :

ERROR:root: seen for Name field assertions since expected is Carbon credits Carbon credits but actual is Carbon credits
ERROR:root: seen for CanRelist field assertions since expected is False while actual is True
ERROR:root: seen for Gallery description since expected subtext is 2x larger image 2x larger image but actual is Good position in category 
2x larger image in desktop site search results
All the Assertions verification are successful with catching exceptions



