# Eventminer
Web Services for the Eventminer
##Manual
This manual is tested under Ubuntu 14.04!

##Requirements
* Python 2.7 should be already installed, but make sure with the following command:
```shell
  python2
```

* Install the following package:
```shell
  apt-get install python-virtualenv python-dev
```

### Installation
* Create a new directory for the project
```shell
  mkdir eventminer
```
* Create a Python Virtual Environment with Python 2 and activate it
```shell
  virtualenv eventminer --python=python2
  cd eventminer
  source bin/activate
```
* Clone the repository including submodules
* Note: The submodule are configured for use with SSH, so configure your access to GitHub: https://help.github.com/articles/generating-ssh-keys
```shell
  git clone git@github.com:policycompass/eventminer.git
  cd eventminer
```
* Install the Requirements
```shell
  pip install -r requirements.txt
```

* Start the application
```shell
  python flask_file.py run
```
* Send a POST request to "localhost:5000/extraction" with a body containing JSON.
  For example: 
  
```shell
  { "text" : "The paaring season is normally between May to August."}
```
  Result:
  
  ```shell
  { 
    "extraction_result" : [
      {
        "end_day": "",
        "end_month": "8",
        "end_year": "",
        "event": "The paaring seasion is normally between May to August",
        "event_found": true,
        "event_nr": 1,
        "location": "",
        "rule_name": "Range: Month_to_Month",
        "rule_nr": "9a",
        "start_day": "",
        "start_month": "5",
        "start_year": ""
      }
    ]
  }
```
