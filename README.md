# py-feeds


Please contact me in case of any issues with starting/using.


How to run web app:

This project consists of the following applications: 
   Frontend - node js and angular 8
   Backend - python 3.6 and aiohttp server 
   
   Application provides github authorization for properly working we should use localtunnels.
   P.s. performance of application might be pure due to using localtunnels! 

Functionality:
    
   After login or registration user may search articles via 
   hacker-news api by keyword.
   Found articles are stored to MySQL database and rendered at user's dashboard
   Articles are fetched on demand not a real time. 
 
How to run application:
  
  Locally
  fe url: http://localhost:4200
  
  Docker
  fe url: http://192.168.99.100:4200 (by default if docker ip, your might be different please check, docker info)
  for windows docker it the same as locally
 
  Locally
  be url: http://localhost:8080
  be url: https://pyfeed.localtunnel.me
  
  Docker
  be url: http://192.168.99.100:8080
  or windows docker it the same as locally
  
  be url: https://pyfeed.localtunnel.me
  

   1) Docker-compose
      
      Download application and you should have docker more about https://docs.docker.com/docker-for-windows/install/
   
      ```docker-compose up --build```
      
      Do only once (if's not started automatically)
      ```connect to 192.168.99.100:3306 (or localhost:3306 for windows) -u root -p root and run sql/ddl_script.sql```
      
      P.s. Sometimes you can encounter with some connection problem, please make sure that tunnel is working
        https://pyfeed.localtunnel.me - tunnel is needed for getting request from github.
        Please attach to docker with command ```docker exec -it <container_name> /bin/bash```
        ```<container_name>``` has to be py-feeds_web_1 
        and run the following command ```lt --port 8080 --subdomain pyfeed```
        double check properties.yaml or docker-properties.yaml for BE
        and also environment.ts and prod.environment.ts for FE
        That there are proper subdomain name.
   
   2) Locally
      
      Linux
      ```sudo apt install nodejs```
      ```sudo apt install npm```
      
      Windows\MacOS
      ```https://nodejs.org/en/download/```
      
      Downloads local tunnel
      ```npm install -g localtunnel```
      
      it's needed for getting callback from github api
      run for back-end ```lt --port 8080 --subdomain pyfeed```
      
      run ```npm instal```
      run front-end ```server ng serve --open --host 0.0.0.0 --port 4200```
      in case of error ```ng is not resolved``` run ``` npm install -g @angular/cli```
      
      run backed-end server ```python app/main.py -c config/properties.yaml```
      
      in case of issue ```ModuleNotFoundError: No module named 'app'```
      run from root folder ```set PYTHONPATH=.``` or ```export PYTHONPATH=.```
 
      download ```mysql 5.7-8.0```
      open sql folder and run ```ddl_script.sql```
      
      For github authorization I have created my OAuth app pyfeeds.
      https://github.com/settings/connections/applications/5ea9a5cd8777ed7145bf
    
 
