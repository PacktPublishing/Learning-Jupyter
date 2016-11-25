

```javascript
const stats = require("stats-analysis");

var arr = [98, 98.6, 98.4, 98.8, 200, 120, 98.5];

//standard deviation 
var my_stddev = stats.stdev(arr).toFixed(2);
 
//mean 
var my_mean = stats.mean(arr).toFixed(2);
 
//median 
var my_median = stats.median(arr);
 
//median absolute deviation 
var my_mad = stats.MAD(arr);
 
// Outlier detection. Returns indexes of outliers 
var my_outliers = stats.indexOfOutliers(arr);
 
// Remove the outliers 
var my_without_outliers = stats.filterOutliers(arr);

//display our stats
console.log("Raw data is ", arr);
console.log("Standard Deviation is ", my_stddev);
console.log("Mean is ", my_mean);
console.log("Median is ", my_median);
console.log("Median Abs Deviation is " + my_mad);
console.log("The outliers of the data set are ", my_outliers);
console.log("The data set without outliers is ", my_without_outliers);


```

    Raw data is  [ 98, 98.6, 98.4, 98.8, 200, 120, 98.5 ]
    Standard Deviation is  35.07
    Mean is  116.04
    Median is  98.6
    Median Abs Deviation is 0.20000000000000284
    The outliers of the data set are  [ 4, 5, 6 ]
    The data set without outliers is  [ 98, 98.6, 98.4, 98.8 ]





    undefined


