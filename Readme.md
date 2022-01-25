## HOW TO REPLICATE THE WORK OF RAKUEN ?

- Create a folder containing the files abstracts.txt, train.csv, test.csv, coauthorship.edgelist, submission.csv, author_papers.txt  (these files are available on [\field{\*\fldinst{HYPERLINK "https://www.kaggle.com/c/inf554-2021/data"}}{\fldrslt 
https://www.kaggle.com/c/inf554-2021/data]). The folder can be the one which contains the notebook.\

- Run the file preprocess_abstracts to create a new file abstracts_bar.csv and store that file with the others\

- Make sure to have installed pandas, scikit-learn, seaborn, matplotlib, networkx and TensorFlow Otherwise you will have to use pip install [name]

- Open the notebook and follow the following steps :
	- Run  General import 
	- Run Data retrieval (make sure to change all the file paths if necessary)
	- You can either choose to run word_embeddings or TF-IDF (Make sure to adapt the dimension to the capacity of the RAM.)
	- Run Addition with graph features 
	-  In the part Models, you can choose which model you want to run, DNN(Multi-layer perceptron), XGBoost, CATBoost
	- Finally, run submit,  make sure to change final_model into the model of your choice, and to change the name of the file you wish to save your predictions into.
	- You're done, you can try to submit the predictions on the kaggle platform [https://www.kaggle.com/c/inf554-2021].
