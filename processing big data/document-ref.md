Introduction to Apache Spark
Today’s world runs on data, generating Terabytes of data every single day. Conventional systems are turning outdated overnight, with big data systems becoming a necessity. While we can argue that most organizations do not deal with data of that magnitude, there lies a growing need for better data management that allows the organization to scale global standards quickly.

SQL tables are being replaced by NoSQL or Graph databases. Pandas and Numpy data frames are now becoming parts of Big Data Frameworks. Hadoop, Spark, and Hive are becoming a necessity for the Industry. One of the most commonly used, and highly recommended Big Data Framework is Apache Spark. Before we understand Apache Spark, it is important we go through a few basic systems.

What is MapReduce?
MapReduce is a programming model that is used to work with large datasets that support parallel processing. It is important to note that there are some use cases, where parallel processing does not work, and in such cases, neither Map Reduce nor Apache Spark is helpful.

MapReduce is one of the main components in the Hadoop ecosystem as well as in Spark. It is designed to support parallel processing of huge amounts of data by splitting the work into independent tasks working with smaller datasets. MapReduce takes the entire dataset from the user, splits it into smaller tasks (MAP), and assigns them to worker nodes. Once all the worker nodes complete each of their independent tasks successfully, the results from the independent activities are aggregated(REDUCE) and return as a single result corresponding to the entire dataset. Usually the Map and Reduce functions are user-defined functions, that solve the business use-case that the code is trying to solve.

MapReduce working. (Image from tutorialspoint.com)
What is Spark?
Apache Spark is a general-purpose cluster computing system. Like MapReduce, it works with a cluster of computers(nodes) to parallel process the working and improve response times. However, unlike MapReduce, Spark clusters have an in-memory nature. In-memory nature is a feature that allows Spark Clusters to cache the data on the nodes, rather than fetching them from the disk every time. Since the data size is huge, the read-write actions, which usually take a long while, are now one-time actions for each node, saving time and increasing processing speed.

The in-memory processing of data is done using Resilient Distributed Datasets(RDD). The user has to specify the operations, and the RDDs perform the distribution of data and execution of the operations in-memory across all nodes.

The Spark Ecosystem is designed in 2 layers — Spark Core and the second layer is a package of libraries and APIs.

The Spark Ecosystem as explained by databricks.com.
Apache spark does not offer cluster management or storage management facilities. Commonly, people use YARN for cluster management and store distributed data on Hadoop File Systems(HDFS) or AWS’s S3 system. Spark also has a compute engine called the SPARK ENGINE, which is responsible for breaking the tasks into smaller ones, scheduling the tasks for parallel processing, providing the data to the clusters, and reporting the faults. It also is the middle management, that interacts with the cluster manager and data managers.

The Apache Spark Core APIs— available in R, SQL, Python, Scala, and Java — were initially used to write data processing logic. These APIs were based on RDDs and lacked a few performance optimizers. However, due to the lack of additional overheads, they also provide the users the maximum level of customization and flexibility to code according to the organization’s requirements.

To overcome the shortcomings of the core APIs and provide more targeted support, the second layer of Apache Spark was introduced, based on the core APIs. The second layer is usually grouped into 4 logical sets of APIs/Libraries:

SparkSQL and Dataframes.
This allows the users to apply SQL commands onto Spark data frames. They are mostly used for structured and semi-structured data.
Streaming.
These APIs are used to deal with continuous incoming unbounded data streams.
Mllib.
This library is used to support all the Machine learning activities that can be deployed over the Spark Frameworks.
GraphX.
It is a library that allows the application of Graph Processing Algorithms onto the available datasets.
Spark vs Hadoop
A frequent question is asked — Why Spark when MapReduce was already a part of Hadoop? Or — What is the advantage of Spark when it is built over the Hadoop Ecosystem? A few key differences between Spark and Hadoop are:

Performance — Hadoop is relatively slow in comparison to Spark, because of the disk operation. Spark is faster and preferred for real-time analytics due to its in-memory nature. Spark is 100 times faster in-memory, and 10 times faster on disk. However, when other resource-demanding services are running, there can be a reduction in the execution times.
Data Processing — Hadoop processes data only in batches ie. sequential step-wise processing. Spark processes data in batch, real-time, and as graphs.
Machine learning — Hadoop uses Mahout for algebraic operation and has scarce ML library support. Spark has a large ML library to build pipelines and perform hyperparameter tuning.
Ease of Use — Hadoop MapReduce has no interactive mode and requires lots of coding. Spark, on the other hand, has a lot of high-level APIs with less coding and interactive modes.
Cost — Hadoop is cheaper because it needs more memory on disk. Spark needs a higher RAM to run in-memory, making it more expensive.
Fault Tolerance — Hadoop is fault-tolerant because it replicates the data across multiple nodes. Spark RDDs are fault-tolerant because of their in-memory nature.
Overall, Hadoop is picked when the system needs to be cheaper, time-independent, and more fault-tolerant. Spark is picked when the algorithm is iterative and requires interactive data processing or machine learning. Spark also has the advantage when the results are expected to be real-time.

Now that a brief introduction is completed to the Spark ecosystem and its apparent advantages, in the future articles, I shall describe the concepts like SparkSQL and PySpark.

webpagelink: https://medium.com/analytics-vidhya/introduction-to-apache-spark-b2d4ff8aacec
