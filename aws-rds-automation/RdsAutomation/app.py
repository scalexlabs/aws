from chalice import Chalice,Cron,Response
from os import getenv
import boto3


app = Chalice(app_name='RdsAutomation')
#Getting the environment variables from config.json using getenv-->
region =  getenv('RDS_REGION')
instance_name = getenv('RDS_INSTANCE_NAME')


@app.route('/')
def index():
    return {'version': '1.0.0'}


#Lambda Function to start instace -->
#Will run at 7:00am (Localtime) or 1:30am (UTC) every day
@app.schedule(Cron(30, 01, '?', '*', 'MON-FRI', '*'))
def rds_instance_start(region,instance_name):    
    try:
        RDS = boto3.client('rds',region_name=region)
        responseOne = RDS.start_db_instance(DBInstanceIdentifier=instance_name)
        print('RDS instance has started Successfully')
        print(responseOne)

    except Exception as e:
        print(str(e))

#Lambda Function to stop instace -->       
# Will run at 08:00PM (Localtime) or 15:00pm (UTC) every day
@app.schedule(Cron(00, 15, '?', '*', 'MON-FRI', '*'))
def rds_instance_stop(region,instance_name):
    try:
        RDS = boto3.client('rds',region_name=region)
        responseTwo = RDS.stop_db_instance(DBInstanceIdentifier=instance_name)
        print('RDS instance has stopped Successfully')
        print(responseTwo)
        
    except Exception as e:
        print(str(e)) 

    

