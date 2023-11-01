import torch

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
task = 'SHS27k'
mode = 'random'
description = "" + task + "_" + mode + ""

ppi_path = "dataset/" + task + "/protein.actions." + task + ".STRING.txt"
pseq_path = "dataset/" + task + "/protein." + task + ".sequences.dictionary.tsv"

split_new = "True"
split_mode = mode
train_valid_index_path = "dataset_split/" + task + "_split/" + mode + ".txt"

use_lr_scheduler = "True"
save_path = "save_model/"
graph_only_train = "False"

Protein_Max_Length = 512
learning_rate = 0.001
batch_size = 1024
epochs = 500
