# PUI2016_solutions


## Technical guidelines

- Make a clone of each student's PUI2016_\<netID> repo. 
- Pull the changes from the repo each week. We can write an automated script and set it to run at dedline time automatically.
- Mark clearly the corrections by adding cells to the notebook for comments and mark how many point the mistake costs, according to the above guidelines. 
- Submit a pull request and make sure that the student merges it. __Not merging the pull request (indicating that the student did not check the homework corrections) within a week will cost 10% of the grade__.



## Grading guidelines 
- Each HW must be turned in as a directory in PUI2016_\<netID>.
- The directory  HW\<hw_number>\_\<netID> must have a README.md which who was in the group that the student worked in and states the student's participation. No penalty if the student declairs not to have had any contribution but to have jut followed and learned. However __missing the README.md, missing the statement about who the student worked with and what they did, or inconsistencies between the statements of students within the group that cannot be easily reconceiled by asking will costs them 10% of the grade__.
- Each assignment turned in as a notebook must have rendered plots with axis labels and captions. __Each missing/non rendered plot, or plot without axes labels or caption will cost 10% of the grade__.
- The notebook must be executables: the TA must downlad the notebook and run it cell by cell without errors. If data are used they must be available to the TA, ideally by loading them online, so that the TA does not need to download large datasets (more details on this will be given in each homework set). The student should use conventional libraries, the use of any unusual library should be justified, and indicated explicitly in the readme, along with links to obtain the library if not available by conda, pip, port, or brew install. __Turning in a notebook that cannot be executed will cost 10% of the grade__.
- If code is used from other resources, e.g. copying a function found online, the resource must be stated, as a citation, in the notebook. **Plagiarism is not allowed (obviously) and severely punished by NYU. Instances of plagiarism will cost the entire homework grade, and may cost failing the class, and may cause expulsion from the program!**
- Adherence to coding style (PEP8) will be encouraged in the first half of the semester, without being penalized. __In the second half of the semester (starting with the midterm) not adhearing to the PEP8 guidelines will cost 5% of the grade per infraction (per type of infraction)__.
- Take points off i proportion of the number of parts in the exercise for each part of the exercise that is done wrong or not done. If the exercise is in 3 parts, take 3 points per piece, if it is 5 take 2 etc. With some discretion: if the mistake is small but the result wrong maybe give partial points. that is a case by case issue and I cannot give more detail at this stage. In some cases you can award partial points for effort.

## Minimal PEP8 requitements:

- Maximum line length: 79 characters. you will not be failed if your lines get to 85 or anything like that, but dont get crazy with the line length

- import packages one at a time:
  ```
  import os
  import sys
  ```
  instead of:

  ```
  import os,sys
  ```
- use descriptive name variables:
  ```
  ridesByZip = ...
  ```
	instead of:
  ```
  rzp = ...
  ```
	or even worse:
	```
	a = ...
	```
	that way we can read your code if needed and understand what you did. That may save 
  you if your code does not run for silly reasons: if we can fix it we may award partial 
  points (if the reason is silly enough)

- use spaces between operators:   
	```
  	a + b
	```
  instead of:
	```
	a+b
  	```
  that way we can read your code if needed and understand what you did. That may save 
  you if your code does not run for silly reasons: if we can fix it we may award partial 
  points (if the reason is silly enough). 
  Naming conventions are generally strictly observed and not observing them will make you a much less strong job candidate for any job that requires conding. https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions
  
- document functions with docstrings as per [PEP257](https://www.python.org/dev/peps/pep-0257/). The docstring is a phrase ending in a period. It starts with """, it prescribes the function or method's effect as a command ("Do this", "Return that"), it describes the arguments, it ends with """ on a separate line.
	```
	def complex(real=0.0, imag=0.0):
    	"""Form a complex number.   

    	Keyword arguments:
    	real -- the real part (default 0.0)
    	imag -- the imaginary part (default 0.0)
    	"""
    	if imag == 0.0 and real == 0.0:
        	return complex_zero
    	...
	```  	
- if you use the try/except syntx name your allowed exceptions:

  	```
  	try: 
  		do_blah()
  	except ValueError, IndexError:        <or wwhatever exceptions you want to allow>
		pass <or whatever you need to do>
   	```
  instead of: 
  	```
   	try: 
    		do_blah()
  	except:
		pass
  	```
- indent by 4 spaces, not by tabs

correct infractions above without taking points off in the first half of the semester, take points off afterwards (5% per infraction, do not count repeated infractions multiple times). 
