from dataset import MultiDataset, apply_transform

import config
import argparse
from torch.utils.data import DataLoader


parser = argparse.ArgumentParser(prog='EmRec')
# Dataset
parser.add_argument('-a', dest='all_datasets', action='store_true',
                    help='Use all available datasets')
parser.add_argument('-d', dest='datasets', type=str, nargs='+',
                    help='Datasets to use')
parser.add_argument('--img_size', type=int,
                    help='Every image in the Dataset will be transform to img_size')
parser.add_argument('--transform', type=str, default='default',
                    help='What tranform use for images in Dataset')
# Other
parser.add_argument('-b', '--batch_size', type=int,
                    help='Batch size for training')
parser.add_argument('-j', '--num_workers', type=int, default=4,
                    help='Number of workers')

args = parser.parse_args()


def run_training():
    dataset = MultiDataset(args, transform=apply_transform(args))
    dataloader = DataLoader(dataset, batch_size=args.batch_size, shuffle=True,
                            num_workers=args.num_workers)


if __name__ == '__main__':
    run_training()