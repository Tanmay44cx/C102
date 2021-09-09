import cv2
import dropbox
import time
import random

start_time=time.time()
print(start_time)
def take_snapshot():
    number=random.randint(0,1000)
    #starting the camera
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #read the frames while the camera is on
        ret,frame=videoCaptureObject.read()
        #save the picture also file name
        image_name="img"+str(number)+".jpg"
        cv2.imwrite(image_name,frame)
        start_time=time.time()
        print(start_time)
        result=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()    
    start_time=time.time()  
    return(image_name)
    

def upload_file(image_name):
    acces_token='R74iuCt-oaEAAAAAAAAAAR45el18-z31qo-PQ424jLkVoBtADG7uhU0c2-qIdk7Y'
    file_name=image_name
    file_from=file_name
    file_to="/images/"+image_name
    dbx=dropbox.Dropbox(acces_token)

    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')
def main():
    while(True):
        if((time.time()-start_time)>=50):
            print("heloo")
            name=take_snapshot()
            upload_file(name)
main()












