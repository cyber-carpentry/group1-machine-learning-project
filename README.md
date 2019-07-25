#### Reproducibility and Reusability of Machine Learning with MNIST & Fashion-MNIST Datasets

### Group Members
* Natalie Chin
* Kaiwen Chen
* Ekincan Ufuktepe


### Description of files
In mnist directory:
* build_model.py: sets up a basic model based on Keras MNIST data <br>
** note: increasing the number of epochs to 20 increases the accuracy to 0.9963
* sample_output.txt: provides sample output information for the basic model

In Fashion-MNIST directory:
* build_model_fashionmnist.py: sets up a basic model for analyzing fashion MNIST data set
* item_viz.png: visualizes classification of different clothing categories; way to check if the basic set-up is working
* sample_output_fashionmnist.txt: provides sample output information for the basic fashion model 


### Description of Deliverables and Hands-on Instructions
 
In this project, we aimed at improving the reproducibility and reusability of neural network models using MNIST and Fashion-MNIST datasets. In terms of reproducibility, it aims at improving the automatization of model training using existing datasets, established neural network architecture, and fixed machine learning parameters. In terms of reusability, it provides several options, including reusing the generated model with different datasets, reusing datasets with different neural network models. All of these deliverables have been published as DockerHub images and can be easily used simply by running a DockerHub container. 
  
1) Reproducibility of both datasets and models

The reproducibility of 

   `$ docker pull <image>`
  
   `$ docker run -it <image>`

2) Reusability of neural network models 
  
   `$ docker pull <image>`
  
   `$ docker run -it <image>`
  
3) Reusability of datasets
  
   `$ `
  
4) Reusability of datasets and models
  
   `$ docker pull <image>`
  
   `$ docker run -it <image>`
  

### How to modify the files for reusability:
1) To improve either model:
- change the number of epochs in line X

2) To use the model for different data:
- change the input data; change size of training and test data sets based (as needed)
