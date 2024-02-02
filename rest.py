from plyer import notification
import time

if __name__=='__main__':
        
    while True:    
        notification.notify(
                title="*****Take rest*****",
                message="Rest is vital for better mental health, increase the dopamine, you fell so good",
                app_icon="C:/Users/Lenovo/Desktop/python.org/notifications.ico",
                timeout=5  
        ) 
        time.sleep(10)