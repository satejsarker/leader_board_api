


## Leader Board API ###
 Setup environment 

`
prerequisite ->
        
        # python3
        
        # pipenv installed ( if not install : install via "pip install --user pipenv"
        for details follow this link https://pipenv.pypa.io/en/latest/install/#pragmatic-installation-of-pipenv

#### Install all the Dependency: ####
from the root of this project install all the dependency
    `
        run-> 
    pipenv install 
    `
#### Activating pipenv ####

###### Note: All the command will not work unless you activate the environment , make sure you activate the environment before running any command bellow
run 
`
    pipenv shell
`
### RUN the project server ###
run this command after installation
`
    uvicorn main:app --host 0.0.0.0 --port 80
`
### API Documentation ##
All the api documentation will be found  in this URL : `http://0.0.0.0/docs`
    after the running the server 

### Unit Test ###
>RUN unit test by running bellow command from root of this project 
>> `pytest  -rP -vv  -o log_cli=true -rP`