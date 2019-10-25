import data_viz
import gzip
import sys
import os
import argparse
import time
sys.path.append('hash_table')
from hash_table import hash_functions
from hash_table import hash_tables


# parse arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description='The right way to pass parameters.',
        prog='plot_gtex.py')

    # require file name as one of the inputs
    parser.add_argument('--output_file',
                        type=str,
                        help='Name of the output plot',
                        required=True)

    # require group type as one of the inputs
    parser.add_argument('--group_type',
                        type=str,
                        help='The group type. e.g. SMTS',
                        required=True)

    # require gene as one of the inputs
    parser.add_argument('--gene',
                        type=str,
                        help='Target gene. e.g. ACTA2',
                        required=True)

    # require meta file as one of the inputs
    parser.add_argument('--sample_attributes',
                        type=str,
                        help='A txt file containing meta data',
                        required=True)

    # require gene data as one of the inputs
    parser.add_argument('--gene_reads',
                        type=str,
                        help='Database of genes',
                        required=True)

    return parser.parse_args()


def linear_search(key, L):
    """ return index with matched key
    """
    for i in range(len(L)):
        if key == L[i]:
            return i
    return -1


def linear_search_all_hits(key, L):
    """ Gives indices not values
    """
    hit = []
    for i in range(len(L)):
        if key == L[i]:
            hit.append(i)
    return hit


def binary_search(key, L):
    """ [content, index]
    search content and return index
    """
    lo = 0
    hi = len(L) - 1
    while (lo <= hi):
        mid = (hi + lo) // 2

        if key == L[mid][0]:
            return L[mid][1]

        if (key < L[mid][0]):
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


def parse_meta(group, file):
    """ save meta data to samples and target_group
    """
    metadata_header = None
    target_group = []
    ht = hash_tables.LinearProbe(1000000, hash_functions.h_rolling)
    for l in open(file):
        sample_info = l.rstrip().split('\t')

        if metadata_header is None:
            metadata_header = sample_info
            continue

        sample_idx = linear_search('SAMPID', metadata_header)
        target_idx = linear_search(group, metadata_header)
        if (target_idx == -1):
            return None, target_group
        key = sample_info[target_idx]
        value = sample_info[sample_idx]
        search = ht.search(key)
        if (search is None):
            ht.add(key, [value])
            target_group.append(key)
        else:
            search.append(value)
    return ht, target_group


def main():
    # get argument by arg parser
    args = parse_args()
    # check if it is a valid file name
    if not os.access(args.output_file, os.W_OK):
        try:
            open(args.output_file, 'w').close()
            os.unlink(args.output_file)
        except OSError:
            print('Invalid output file name')
            sys.exit(1)
    if (not os.path.exists(args.sample_attributes)):
        print('Cannot find meta file')
        sys.exit(1)
    if (not os.path.exists(args.gene_reads)):
        print('Cannot find meta file')
        sys.exit(1)

    target_gene_name = args.gene
    meta_map, target_group = parse_meta(args.group_type,
                                        args.sample_attributes)
    target_group.sort()

    if (meta_map is None):
        print('Cannot find group_type')
        sys.exit(1)

    # necessary header
    version = None
    dim = None
    rna_header = None
    for l in gzip.open(args.gene_reads, 'rt'):

        if version is None:
            version = l
            continue

        if dim is None:
            dim = l
            continue

        if rna_header is None:
            rna_header = l.rstrip().split('\t')
            description_idx = linear_search('Description', rna_header)
            continue

        rna_counts = l.rstrip().split('\t')

        if description_idx == -1:
            print('Gene not found in header')
            sys.exit(1)

        if rna_counts[description_idx] == target_gene_name:
            par_array = []
            rna_map = hash_tables.LinearProbe(
                1000000, hash_functions.h_rolling)
            for i in range(description_idx + 1, len(rna_header)):
                rna_map.add(rna_header[i], int(rna_counts[i]))
            # search_loop_start = time.time()
            for attr in target_group:
                attr_counts = []
                meta_find = meta_map.search(attr)
                if meta_find is None:
                    continue
                for sample_name in meta_find:
                    count = rna_map.search(sample_name)
                    if count is None:
                        continue
                    attr_counts.append(count)
                par_array.append(attr_counts)
            # search_loop_end = time.time()
            # print(search_loop_end - search_loop_start)
            data_viz.boxplot(par_array, target_group, args.group_type,
                             'Gene read counts', target_gene_name,
                             args.output_file)
            sys.exit(0)

    sys.exit(0)


if __name__ == '__main__':
    main()
