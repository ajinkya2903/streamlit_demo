# streamlit_demo

Added Dockerfile to the project. It will run on port 8051


For building docker container : 
$ docker image build -t streamlit:app .


For running after build : 
$ docker container run -p 8501:8501 -d streamlit:app
