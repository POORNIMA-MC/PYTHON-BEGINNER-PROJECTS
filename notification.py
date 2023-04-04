import time
from plyer import notification
 
 
if __name__=="main_":
 
        notification.notify(
            title = "DRINK WATER!",
            message=" DRINK WATER!" ,
           
            # displaying time
            timeout=2
)
        # waiting time
        time.sleep(7)