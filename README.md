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

