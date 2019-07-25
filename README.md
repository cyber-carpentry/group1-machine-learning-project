### Group Members
* Natalie Chin
* Kaiwen Chen
* Ekincan Ufuktepe

### Description of Deliverables and Hands-on Instructions
1) Reproducibility of both datasets and models

`$ docker pull <image>`

2) Reusability of neural network models 

3) Reusability of datasets

4) Reusability of datasets and models


### Description of files
In mnist directory:
* build_model.py: sets up a basic model based on Keras MNIST data <br>
** note: increasing the number of epochs to 20 increases the accuracy to 0.9963
* sample_output.txt: provides sample output information for the basic model

In Fashion-MNIST directory:
* build_model_fashionmnist.py: sets up a basic model for analyzing fashion MNIST data set
* item_viz.png: visualizes classification of different clothing categories; way to check if the basic set-up is working
* sample_output_fashionmnist.txt: provides sample output information for the basic fashion model 

### How to modify the files for reusability:
1) To improve either model:
- change the number of epochs in line X

2) To use the model for different data:
- change the input data; change size of training and test data sets based (as needed)
