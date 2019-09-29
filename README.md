# parallel-arrays-profiling-and-benchmarking
Parallel Arrays, Profiling, and Benchmarking

## Data Sources
* https://github.com/swe4s/lectures/blob/master/data_integration/gtex/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz?raw=true
* https://storage.googleapis.com/gtex_analysis_v8/annotations/GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt

## Continuous Integration Status
![](https://travis-ci.com/cu-swe4s-fall-2019/parallel-arrays-profiling-and-benchmarking-Sayter99.svg?branch=master)

## Installation
To use this package, you need to have [Python3](https://www.python.org/download/releases/3.0/) in your environment. And the used packages are listed below.

### Used Packages
* os
* sys
* math
* time
* numpy
* random
* argparse
* unittest
* matplotlib
* pycodestyle

## Usage
`plot_gtex.py` is the main program for generating boxplots from `GTEX` data.
Examples of using `plot_gtex.py`:
* `python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file test1.png`
* `python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTSD --output_file test2.png`

## Changes in this assignment
* Added both functional tests (`test_plot_gtex.sh`) and unit tests (`test_plot_gtex.py`)
* Completed robust modules and scripts including `data_viz.py` and `plot_gtex.py`
    * completed `linear search` and `binary search` functions to parse `GTEX` data
    * completed `boxplot` to plot multiple boxes from 2D array
* Tested and developed iteratively
* Profiling and benchmarking the programs
* Modified `travis.yaml` to carry out added tests
* Complete the `README.md` with performance analysis

## Profiling and Benchmarking

### Results of cProfile
We can easily compare the total time of each function call in `plot_gtex.binary_search.txt` and `plot_gtex.linear_search.txt`. In `plot_gtex.linear_search.txt`, the most interesting part is the total time of `linear_search` function. It's **17.707** secs, **87.489%** of the total process. So, we absolutely need to improve this method to speed up the whole process. By leveraging the `binary search` algorithm, we amazingly speeded it up a lot. In `plot_gtex.binary_search.txt`, we already reduced the total time of `linear_search` to **0.023** secs with the small overhead (`sort`: **0.001** secs and `binary_search`: **0.068** secs). To conclude, by this simple and basic technique, we do improve the `plot_gtex` considerably. Thus, we can conclude that profiling and complexity analysis play important roles in software engineering.

### Results of Time command
* linear search version
  * command: `/usr/bin/time -f '%e\t%M' python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file test1.png`
  * result: **14.32 sec** and **74804 KB**
* binary search version
  * command: same as linear search version
  * result: **1.39 sec** and **75844 KB**
According to the results, we can roughly calculate the performance improvement of the whole process:
*Improvement percentage = (14.32 - 1.39)/1.39 ~= **930.2158%** increased*

We may also notice that the memory usage is also increased *(75844 - 74804)/74804 = 1.39%*, however, our application, data analysis, is usually run on desktop platform which has a lot of memory capacity. Therefore, it is totally reasonable to choose **900%** speed improvement with sacrificing **1.39%** memory usage.

### Results of time.time() function
In this section, I measured the different parts of each version.

For linear search, I leverage `time.time()` to measure the main loop for generating 2D arrays:
* `main loop`: **12.206398** sec

For binary search, I leverage `time.time()` to measure the extra `sort` and the main loop for generating 2D arrays:
* `sort`: **0.0006568** sec
* `main loop`: **0.8194587** sec

According to the results, we can rougly calculate the performance improvement by utilizing `binary search` by
*Improvement percentage = (12.206398 - (0.8194587 + 0.0006568))/(0.8194587 + 0.0006568) ~= **1388.375%** increased*
