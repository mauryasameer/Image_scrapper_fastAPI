
# IMAGE CRAWLER DEPLOYMENT USING FAST-API

In this repository I am making an image crawler with the help of selenium and deploying it suing fast-API, I find fast-API helpful in the deployment of the deep learning models because of its async nature, which helps us to get a faster inference.

## APP SETUP
For running the application you have to install the dependencies from the `requirement.txt`

  you can raise an issue if some libraries are not included in the requitement.txt or create a pull request.

I have provided the `chrome driver` but it might not work with your browser version so change it accordingly.

## RUNNING THE APPLICATION
now to run the application we have to use the following command
```
uvicorn app:app 
```

## OUTPUT

the server will be created at the localhost and you can access it by going to 

[127.0.0.1:5000](127.0.0.1:5000)

![video](temp_images/main.gif)
## TO-DO

 - [ ] Make the output page more pleasing
 - [ ] Make the whole application docker deployable
 - [ ] deploy the application
 - [ ] Create better README
