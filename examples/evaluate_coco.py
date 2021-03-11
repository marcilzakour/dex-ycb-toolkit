import argparse
import os

from dex_ycb_toolkit.coco_eval import COCOEvaluator


def parse_args():
  parser = argparse.ArgumentParser(description='Run COCO evaluation.')
  parser.add_argument('--name', help='Dataset name', default=None, type=str)
  parser.add_argument('--res_file',
                      help='Path to result file',
                      default=None,
                      type=str)
  args = parser.parse_args()
  return args


def main():
  args = parse_args()

  if args.name is None and args.res_file is None:
    args.name = 's0_test'
    args.res_file = os.path.join(
        os.path.dirname(__file__), "..", "results",
        "example_results_coco_{}.json".format(args.name))

  coco_eval = COCOEvaluator(args.name)
  coco_eval.evaluate(args.res_file)


if __name__ == '__main__':
  main()
