#!/usr/bin/python3
print("content-type: text/html")
print()





import subprocess as sp
import json
import xmltodict
import requests
import random
count =0
#print("Please wait , We are processing.......")
def api_call(RegistrationNumber): #calling RTO's api with car number plate for details
    username=["token04","carapi01", "carapi05", "carapi06", "carapi07", "carapi08", "carapi09", "carapi10", "carapi11", "carapi12", "carapi13", "carapi14", "carapi15", "shivam90", "shivam91", "shivam92", "shivam93", "shivam94", "shivam95", "shivam96", "shivam97", "shivam98", "shivam99", "techtrollers80", "techtrollers81", "techtrollers82", "techtrollers83", "techtrollers84", "techtrollers85", "techtrollers86", "techtrollers87", "techtrollers88", "techtrollers89", "techtrollers99"]
    #username=["shivam15","token04"]
    URL ="https://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber="+RegistrationNumber+"&username="+random.choice(username)
    r = requests.get(url = URL)
    try:
        return(r.json())
    except:
        return(r.text)
s=sp.getstatusoutput("aws s3 cp ./images/task8.jpeg s3://task-8") #Uploading file to s3 with name task8.jpeg
p = 'aws rekognition detect-text   --image "S3Object={Bucket=task-8,Name=task8.jpeg}" ' #recogitiong the text from images using rekognition.
#print("please wait....we are processing")
text = sp.getoutput('aws rekognition detect-text   --image "S3Object={Bucket=task-8,Name=task8.jpeg}" --region ap-south-1')

#outp=str(json.loads(text))
output=json.loads(text)
#print(type(output))
#print(output["TextDetections"][0]["DetectedText"])
#r=range(0,int(len(output["TextDetections"])))
i =0
l= int(len(output["TextDetections"]))
while i <=l:
    if (len(output["TextDetections"][i]["DetectedText"].replace(" ", ""))==10) or (len(output["TextDetections"][i]["DetectedText"].replace(" ", ""))==9):
        out = api_call(output["TextDetections"][i]["DetectedText"].replace(" ", ""))
        print(output["TextDetections"][i]["DetectedText"])
        if ("Out of credit" in str(out)) and (count <=2):
            print("Trying once more....")
            i -=1
            count=count + 1
        elif count >2:
            print("ALL Credit exhausted")
            break
        else:
            data_dict = xmltodict.parse(out)
            json_data = json.dumps(data_dict)
            put=json.loads(json_data)
            main= json.loads(put["Vehicle"]["vehicleJson"][:])
            print("-------------------------------------------------")
            print("-------------------------------------------------")
            print("Description: "+main["Description"])
            print("Owner: "+main["Owner"])
            print("RegistrationYear: "+main["RegistrationYear"])
            print("CarMake: "+main["CarMake"]["CurrentTextValue"])
            print("CarModel: "+main["CarModel"]["CurrentTextValue"])
            print("EngineSize: "+main["EngineSize"]["CurrentTextValue"])
            print("MakeDescription: "+main["MakeDescription"]["CurrentTextValue"])
            print("ModelDescription: "+main["ModelDescription"]["CurrentTextValue"])
            print("VechileIdentificationNumber: "+main["VechileIdentificationNumber"])
            print("EngineNumber: "+main["EngineNumber"])
            print("FuelType: "+main["FuelType"]["CurrentTextValue"])
            print("RegistrationDate: "+main["RegistrationDate"])
            print("VehicleType: "+main["VehicleType"])
            print("Location: "+main["Location"])
            print("VehicleType: "+main["VehicleType"])
            print("-------------------------------------------------")
            print("-------------------------------------------------")
            break
         #print(out)
    i=i+1
    '''count=count +1
         if "Out of credit" in str(out) and count <=3:
               print("trying again.......")
               i=i-1

         else:
               print("ALL credit exhausted")
               break
            if "Out of credit" in str(out) and count <=3:
        print("trying again.......")
        i=i-1
    else:
        print("ALL credit exhausted")
        break'''
sp.getstatusoutput("aws s3 rm s3://task-8 --recursive")
sp.getstatusoutput("rm -rf ./images/* ")


