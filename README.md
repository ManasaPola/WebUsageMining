# Web Usage Mining
This project helps us to observe and analyze interesting patterns in web usage data using Data Mining Techniques.
+ We have taken NASA July 1995 Server data.


#### Configuration Setup
1. Python
2. MongoDB
3. JavaDriver
4. Hadoop (Pseudo-Distributed Mode)
5. MongoDb Connector for Hadoop
6. Pig Scripts
7. Pig JAR
8. R
9. Tableau

Below instructions helps you setup and get started with this project.
1. Run the file preprocess.py to convert raw data logs into required format.
2. Import data into mongodb using the command "mongoimport --db logs --collection accesslogs --type csv --headerline --file 'julydata.csv'"
3. Installation & Running pig scripts
	* Install hadoop and Java
	* Download apache pig latest stable release from apache mirrors site
	* verify the path is correct for JAVA_HOME, Pig_HOME, PATH in bashrc file
	* After successfully installing execute pig script using "pig count.pig" command which has instructions to load data from MongoDB using Mongo Loader, Tokenize collection imported, Group by and count, Store Output on HDFS.
	* Now you can find the wordcount in the folder named /wordcount/tId
4. Run aprioriAlgo.R to run the apriori algorithm on the dataset and this Extracts frequently co-accessed pages within a single request.
5. Run usersessions.py file to identify the user sessions.
6. Run aprioriAlgoMethod2 to run second approach of apriori and to extract co-accessed web links.
7. Run clustering.py to cluster the url's and this also includes constructing page co-occurence matrix and Path similarity matrix.
8. We have used tableau to visualize the interesting patterns.


Acknowledgements:
We would like to express our thanks to Professor Dr. Hasan Davulcu for giving us guidance and opportunity to work on this project.

References:
1. Srivastava, Jaideep, et al. "Web usage mining: Discovery and applications of usage patterns from web data." ACM SIGKDD Explorations Newsletter 1.2 (2000): 12-23.
2. Asadi, Tawfiq & Obaid, Ahmed. (2016). "An efficient web usage mining algorithm based on log file data." 92. 215-224.
3. Savio, Marc Nipuna Dominic, "Predicting User's Future Requests Using Frequent Patterns" (2016). Master's Projects. 501. http://scholarworks.sjsu.edu/etd_projects/501.
4. Mobasher, Bamshad, Robert Cooley, and Jaideep Srivastava. "Automatic personalization based on web usage mining." Communications of the ACM 43.8 (2000): 142-151.
5. http://www.sthda.com/english/wiki/descriptive-statistics-and-graphics#check-your-data
6. https://onlinehelp.tableau.com/current/desktopdeploy/en-us/desktop_deploy_download_and_install.htm
7. https://www.r-bloggers.com/log-file-analysis-with-r/
8. http://eecs.csuohio.edu/~sschung/cis612/CIS612_PDF_Presentation_NASA_Halley_Orogvany.pdf

Team Members:
* Manasa Pola
* Sravya Balagala
* Himaja Tirumalasetti
* Vaishali Kankanala
* Neeharika Dasari
