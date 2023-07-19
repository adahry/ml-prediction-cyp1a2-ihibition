from data_loading import *
from data_preprocessing import *
from gnn import GNN
from training import train
from plot_training import plot_training
from model_evaluation import *

#set seed
torch.manual_seed(42)

#load dataset
df = get_data('cyp1a2_veith')
x_smiles = df['Drug']
y = df['Y']
data_list = create_pytorch_geometric_graph_data_list_from_smiles_and_labels(x_smiles, y)

#spliting data for training
train_size = int(0.7 * len(data_list))
valid_size = int(0.2 * len(data_list))
test_size = len(data_list) - train_size - valid_size
train_dataset, valid_dataset , test_dataset = torch.utils.data.random_split(data_list, [train_size, valid_size ,test_size])


#training the model
model = GNN(data_list[0],32)

#parameters
DATA_LIST = data_list
MODEL = model
LEARNING_RATE = 1e-4
EPOCHS = 30
BATCH_SIZE = 32

train_loss, val_loss = train(train_dataset, valid_dataset, MODEL, LEARNING_RATE, EPOCHS, BATCH_SIZE, print=False)

plot_training(train_loss, val_loss)

#evaluation
result_df = score_dataframe(test_dataset, model)
accuracy(result_df)
plot_conf_matrix(result_df)