import os

import click
import numpy as np
from keras.models import load_model

from deeptune.evaluation.eval_mark_I import (calculate_intra_cluster_distances,
                                             generate_embeddings,
                                             load_and_preprocess_image)


@click.group()
def cli():
    pass


@click.command()
@click.argument("model_path")
@click.argument("dataset_path")
def evaluate_model(model_path, dataset_path):
    """Evaluate the model with the given dataset."""
    model = load_model(model_path)
    embeddings, labels = generate_embeddings(model, dataset_path)
    intra_distances = calculate_intra_cluster_distances(embeddings, labels)
    print(f"Intra-Cluster Distances: {intra_distances}")
    print(f"Mean Distance: {np.mean(intra_distances)}")


cli.add_command(evaluate_model)

if __name__ == "__main__":
    cli()
