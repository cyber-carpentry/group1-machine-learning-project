## Reproducibility and Reusability of Deep Neural Networks with MNIST & Fashion-MNIST Datasets

This project aims to improve the reproducibility and reusability of deep neural network models trained using the MNIST and Fashion-MNIST datasets. In terms of reproducibility, it aims to improve the automatization of model training using existing datasets, established neural network architecture, and fixed machine learning parameters. In terms of reusability, it provides several options, including reusing the generated model with different datasets and reusing datasets with different neural network models. 

This project provides Docker images that have been prepared with all necessary packages installed to build some basic neural network models that are tuned for MNIST and Fashion-MNIST datasets. It will allow anyone to gain some exposure to deep learning models but do not have experience or do not want to spend time with coding and debugging.  Please refer to the instructions below for how to set up these basic models and how to modify them to run with different data sets.

### Group Members
* Natalie Chin
* Kaiwen Chen
* Ekincan Ufuktepe

### Description of Deliverables
 
All of these deliverables have been published as DockerHub images and can be easily used simply by running a DockerHub container. 
  
1) Reproducibility of both datasets and models

   If you want to get the trained model for the classifications of  

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
