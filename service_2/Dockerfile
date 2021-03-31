FROM python:3.6
#RUN requirements.txt
WORKDIR Lottery_Project/service_2
COPY . . 
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3","app.py"]
#ENTRYPOINT ["ls"]
