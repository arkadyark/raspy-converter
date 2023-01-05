import argparse
from pathlib import Path
import importlib

import raspy
import torch

def convert(model_fn):
    model = None
    # Get the layers of the model
    # Determine their weights and make them layers of a transformer
    return model

def main(input_module: str, output_path: Path):
    module = importlib.import_module(input_module)
    model_fn = module.model
    model_fn()
    converted_model = convert(model_fn)
    # torch.save(converted_model)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-module", "-i", type=str)
    parser.add_argument("--output-path", "-o", type=Path)
    args = parser.parse_args()

    main(args.input_module, args.output_path)
