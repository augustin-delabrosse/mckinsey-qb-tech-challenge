# Foodix Satelite image analysis tool 🛠:

This tool helps the sales team of Foodix to identify and locate Silos accross the whole globe, thus enabling them to find new potential customers. 
Usecases are to detect Silos and sell them their superior technology, or to identify areas with out any Silos.

## Homepage
General information about the business and about McKinsey

## Check out the website of McKinsey here
📢 https://www.mckinsey.com/

## ______________________

______________________

## Individual Predictions

Upload any of your pictures and check if there is a Silo in it.

## Check your coordinates

Check any coordinates worldwide and see if there are some silos at that given coordination.

## Screenshots
![Screenshots](/demo/screenshot1.jpg?raw=true)
![Screenshots](/demo/screenshot2.jpg?raw=true)
![Screenshots](/demo/screenshot3.jpg?raw=true)


## Requirements
```
streamlit_lottie==0.0.2
streamlit== 1.15.2
requests==2.24.0
Pillow==8.4.0
protobuf~=3.19.0
watchdog==2.1.8
selenium==4.7.2
leafmap==0.14.0
plotly==5.9.0
```

## Model
Please unzip the classification and segmentation models that are in the folder models.  
Leave them in the same folder.  
  
## Run the app
* Terminal
    ```
    # vanilla terminal
    pip install -r requirements.txt
    streamlit run app.py

    # poetry
    poetry add `cat requirements.txt`
    poetry run streamlit run app.py

    # quit
    ctrl-c
    ```
* VSCode
  * Open the repo directory in VSCode
  * Open `1_Homepage.py`
  * Start debugging with F5
  * Stop debugging with Shift-F5

## Authors
🚹
  Zidi Yang: zidi.yang@hec.edu 
  Milos Basic: milos.basic@hec.edu
  Antoine Mellerio: antoine.mellerio@hec.edu
  Camille Epitalon: camille.epitalon@hec.edu
  Augustin de La Brosse: augustin.de-la-brosse@hec.edu
  Michael Liersch: michael.liersch@hec.edu

## Feedback
📥 If you have any feedback, please reach out to us !!!