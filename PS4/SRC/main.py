from KnowledgeBase import KnowledgeBase
from Clause import Clause
from Literal import Literal
import glob
import os
import argparse

INPUT_DIR = './INPUT'
OUTPUT_DIR = './OUTPUT'

def get_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", default = INPUT_DIR, help="input dir")
    parser.add_argument("--output", default = OUTPUT_DIR, help="output dir")

    return parser.parse_args()

def main(args):
    input_dir = args.input
    output_dir = args.output

    inputs = glob.glob(input_dir + './*.txt')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for idx, input_file in enumerate(inputs):
        if '\\' in input_file:
            src = input_file.split('\\')[-1]
        else:
            src = input_file.split('/')[-1]
        
        file = open(input_file, 'r')
        KB = KnowledgeBase()
        # alpha = Clause.parseClause(file.readline())
        alpha = file.readline()
        numClauses = file.readline()
        clauses = file.readlines()
        KB.buildKnowledgeBase(alpha, clauses)
        file.close()

        entail, newClauses = KB.PL_Resolution()

        des = os.path.join(output_dir, src.replace('input', 'output'))
        file = open(des, 'w')
        for clauses in newClauses:
            file.write('{}\n'.format(len(clauses)))
            for clause in clauses:
                file.write('{}\n'.format(clause))
        if entail == True:
            file.write('YES')
        else:
            file.write('NO')
        file.close()

if __name__ == '__main__':
    args = get_parser()
    main(args)