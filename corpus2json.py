import argparse
import glob
import json
import os


def corpus2json(dir, json_out, level):
    if level == 'document':
        labels = os.listdir(dir)
        print('labels: {}'.format(labels))
        for label in labels:
            p = os.path.join(dir, label) + "/*"
            print('p: {}'.format(p))
            files = glob.glob(p)
            print(files)
            for f in files:
                print('processing {}'.format(f))
                filename = os.path.basename(f)
                doc = open(f).read()
                json.dump({'text': doc, 'label': label, 'filename': filename}, json_out)
                json_out.write('\n')
    elif level == 'sentence':
        files =   glob.glob(dir + '/*')
        print('files: {}'.format(files))
        for f in files:
          print('processing {}'.format(f))
          lines = open(f, encoding='utf-8').read().splitlines()
          print('{} has {} lines'.format(f, len(lines)))
          fname = os.path.basename(f)
          for i, line in enumerate(lines):
            json.dump({'text': line, 'label': fname, 'id': i}, json_out)
            json_out.write('\n')
            

parser = argparse.ArgumentParser(description='convert text corpus (directories and files) into a json file.')
parser.add_argument('-i', '--indir', type=str,
                    help='input file.', required=True)
parser.add_argument('-o', '--outfile', type=argparse.FileType(mode='w', encoding='utf-8'),
                    help='out file.', required=True)
parser.add_argument('-l', '--level', type=str,
                    help='out file.', required=True, choices=['sentence', 'document'])


if __name__ == '__main__':
    args = parser.parse_args()
    input = args.indir
    output = args.outfile
    level = args.level
    corpus2json(input, output, level)
    print('done!')
