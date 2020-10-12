# **README.md**
## **Applying Clustering Algorithms to Classify and Forecast Financial Time-Series** 
#### Abstract: https://drive.google.com/file/d/1oYk8XS_9ZE9QTb8XgfzAPTiIGx4-zs4i/view?usp=sharing
#### Project contributions: S&P 500 time-series data cleaning and processing for one year up to 5 min intervals, k-means and k-medoid clustering to classify and forecast S&amp;P 500 time-series, 3 different methods of analysis conducted with silhouette score, Davies-Bouldin Index, and Elbow method

##### Update: I've taken down several files involving key clustering analysis and data pre-processing
##### Please contact me to request them for non-proprietary purposes

##### Study to apply k-means and k-medoid clustering algorithms in the development of portfolio strategies, uses Python in Jupyter Notebook to classify different time-series from the S&P 500, uses EasyLanguage in TradeStation to simulate trading output based upon clustering outcomes

**/ry_sci:**
RY Science Project Design.docx: the project design document

 - 001-generate_price_matrix_csv.py: price data pre-processing python code, read in original data from /data folder, generate a price matrix csv file for each time frequency (daily, 5-min, 30-min).
 - 002-calculate_bestK.py: calculate the best k number for clustering using elbow method and silhouette scores.
 - 003-cluster-KMeans.py: cluster code using kmeans
 - 003-cluster-KMedoid.py: cluster code using k-medoid
 - 004-analyze-KMedoid.py: clustering analysis code
 - README.txt: this file

**/DataExport:** has original stock price csv files zipped, downloaded from tradestation

**/data:** folder has original stock price csv data in three folders, daily, 30-min, and 5-min (not uploaded to google drive); and the pre-processed 5min, 30min, daily stock price data (output from the data pre-processing python code)

**/demo:** demo python codes for different data processing and calculation, prototype code for stock price data manipulation. Files are named in two types of ways as follows:

 - **/demo:** demo-xxxx.py - demo code snippets, has hand-coded demo data such as 2-d, 4-d arrays.
 - **/demo:** mystock-xxxx.py - demo codes using a demo ticker price csv file, read in the demo price data, perform different functions. Python file names tell the function of the demo codes in general.

**/clustering:** folder has documentation of clustering and clustering analysis demo codes

**/py_output:** has three generated csv files, one for each time frequency, i.e., daily, 5-min, 30-min, each has a list of stock tickers listed by clusters

**/TS Documentation:** tradestation documentation

**/ts_output:** Tradestation strategy backtest or forward test results using the py_output for feeding the tickers

	



