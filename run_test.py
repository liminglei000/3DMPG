import os

def run_func(description, ppi_path, pseq_path,
            index_path, gnn_model, test_all):
    os.system("python gnn_test.py \
            --description={} \
            --ppi_path={} \
            --pseq_path={} \
            --index_path={} \
            --gnn_model={} \
            --test_all={} \
            ".format(description, ppi_path, pseq_path, index_path, gnn_model, test_all))

if __name__ == "__main__":
    description = "test"
    task = 'SHS27K'
    mode = 'random'
    test_all = "True"

    ppi_path = "dataset/" + task + "/protein.actions." + task + ".STRING.txt"
    pseq_path = "dataset/" + task + "/protein." + task + ".sequences.dictionary.tsv"
    index_path = "dataset_split/" + task + "_split/" + mode + ".txt"
    gnn_model = "save_model/gnn_model_train.ckpt"

    run_func(description, ppi_path, pseq_path, index_path, gnn_model, test_all)
