# Brad D. Messner
# SDT300 Samples
# Sample Descriptive Statistics

import statistics
import numpy as np

myData = [45,32,11,98,65,85,44,32,85,7,88,44]

print("Count is:  ", len(myData))
print("Mean is:   ", statistics.mean(myData))
print("Median is: ", statistics.median(myData))
print("Mode is:   ", statistics.mode(myData))
print("Min is:    ", min(myData))
print("Max is:    ", max(myData))
print("Range is:  ", max(myData)-min(myData))
print("St Dev is: ", statistics.stdev(myData))
print("Variance:  ", statistics.variance(myData))
print("Lower Q:   ", np.percentile(myData, 25))
print("Upper Q:   ", np.percentile(myData, 75))
print("Inter Q R: ", np.percentile(myData, 75) - np.percentile(myData, 25))
