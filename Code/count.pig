REGISTER /Users/sravya/Downloads/hadoop-3.1.2/share/hadoop/common/mongo-java-driver-2.10.1.jar 
REGISTER /Users/sravya/Downloads/hadoop-3.1.2/share/hadoop/common/mongo-hadoop-core-1.3.0.jar 
REGISTER /Users/sravya/Downloads/hadoop-3.1.2/share/hadoop/common/mongo-hadoop-pig-1.1.0.jar 

raw = LOAD 'mongodb://localhost:27017/logs.accesslogs' USING com.mongodb.hadoop.pig.MongoLoader('topLevelDomain:chararray');

words = FOREACH raw GENERATE FLATTEN (TOKENIZE(topLevelDomain)) as word;
grouped = GROUP words BY word;
wordcount = FOREACH grouped GENERATE group, COUNT(words);

STORE wordcount into '/wordcount/tId';
