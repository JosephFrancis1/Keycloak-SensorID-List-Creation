# Keycloak-SensorID-List-Creation
Python script to take all sensor IDs associated with a project and format them for keycloak group creation

Before executing the python script a csv file containing all sensor IDs for a given project must be downloaded from the metabase
custom query section. This is done by searching for devices and filtering by the desired project.

To run the script type the following into the command line in terminal and execute:
    python sensorID.py 'path to downloaded csvfile'

Copy the entire output and paste it into the permitted_sensors field in keycloak, overwriting existing text.
