import data_viz
import gzip
import sys
import os
import argparse


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
    for i in range(len(L)):
        if key == L[i]:
            return i
    return -1


def linear_search_all_hits(key, L):
    """Gives indices not values"""
    hit = []
    for i in range(len(L)):
        if key == L[i]:
            hit.append(i)
    return hit


def binary_serach(key, L):
    lo = -1
    hi = len(L)
    while (hi - lo > 1):
        mid = (hi + lo) // 2

        if key == L[mid][0]:
            return L[mid][1]

        if (key < L[mid][0]):
            hi = mid
        else:
            lo = mid

    return -1


def parse_meta(group, file):
    metadata_header = None
    samples = []
    target_group = []
    for l in open(file):
        sample_info = l.rstrip().split('\t')

        if metadata_header is None:
            metadata_header = sample_info
            continue

        sample_idx = linear_search('SAMPID', metadata_header)
        target_idx = linear_search(group, metadata_header)
        samples.append(sample_info[sample_idx])
        target_group.append(sample_info[target_idx])
    return samples, target_group


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
    samples, target_group = parse_meta(
        args.group_type, args.sample_attributes)

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
            rna_header_plus_index = []
            for i in range(len(rna_header)):
                rna_header_plus_index.append([rna_header[i], i])
            continue

        rna_counts = l.rstrip().split('\t')
        description_idx = linear_search('Description', rna_header)

        if description_idx == -1:
            print('Gene not found in header')
            sys.exit(1)

        if rna_counts[description_idx] == target_gene_name:
            attrs = list(set(target_group))
            attrs.sort()
            par_array = []
            for attr in attrs:
                attr_idxs = linear_search_all_hits(attr, target_group)

                attr_counts = []
                for attr_idx in attr_idxs:
                    rna_header_idx = linear_search(
                        samples[attr_idx], rna_header)
                    if rna_header_idx == -1:
                        continue
                    count = rna_counts[rna_header_idx]
                    attr_counts.append(int(count))
                par_array.append(attr_counts)
            data_viz.boxplot(par_array, attrs, args.group_type,
                             'Gene read counts', target_gene_name,
                             args.output_file)
            sys.exit(0)

    sys.exit(0)


if __name__ == '__main__':
    main()
