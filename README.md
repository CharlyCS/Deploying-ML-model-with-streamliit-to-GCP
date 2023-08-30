# API_Gcloud_Streamlit
This project involves generating an SVM model and deploying it using Streamlit and Google Cloud. The SVM model will provide crop recommendations based on soil and environmental characteristics.

##  1. Model training
We trained the SVM model using next code: https://github.com/CharlyCS/Quality-prediction-in-minerals-python-
You can find it in my github account, too.

##  2. Local Server Production 

To set up the local server environment, follow these steps:

    $   conda create -n ApiCrop
    $   conda activate ApiCrop
    $   conda install python=3.7
    $   pip install -r requirements.txt
    $   streamlit run app.py
    
##  3.  Remote Server Production
For remote server deployment:

    *   Create a Google Cloud account and project.
    *   Install Google Cloud SDK (https://cloud.google.com/sdk/docs/install).
    *   Execute the following commands in the terminal:
    
    $ gcloud init
    $ gcloud app deploy app.yaml --project "Nombre del proyecto"
    
    
  ![Screenshot](https://github.com/DavidReveloLuna/API_Gcloud_Streamlit/blob/master/assets/Screenshot.png)

## Acknowledgments

[Praneeth Kandula](https://medium.com/analytics-vidhya/deploying-streamlit-apps-to-google-app-engine-in-5-simple-steps-5e2e2bd5b172)

[DavidReveloLuna](https://github.com/DavidReveloLuna/API_Gcloud_Streamlit/tree/master)
