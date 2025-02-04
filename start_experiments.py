from elliot.run import run_experiment
import argparse

parser = argparse.ArgumentParser(description="Run sample main.")
parser.add_argument('--dataset', type=str, default='yelp-2018')
parser.add_argument('--model', type=str, default='simgcl')
args = parser.parse_args()

run_experiment(f"config_files/{args.model}_{args.dataset}.yml")
