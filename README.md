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
* argparse
* os
* sys
* math
* pycodestyle
* numpy
* random
* unittest
* matplotlib

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

## Profiling and Benchmarking

### Results of cProfile

### Results of Time command
* linear version
  * command: `/usr/bin/time -f '%e\t%M' python3 plot_gtex.py --gene_reads GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz --sample_attributes GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt --gene ACTA2 --group_type SMTS --output_file test1.png`
  * result: **14.32 sec** and **74804 KB**
