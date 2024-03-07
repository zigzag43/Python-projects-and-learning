import cv2
import time
import mediapipe as mp
import pyautogui
hand_dectector=mp.solutions.hands.Hands(max_num_hands=1,
                                        model_complexity=1,
                                        min_detection_confidence=0.5,
                                        min_tracking_confidence=0.5)
drawing=mp.solutions.drawing_utils
drawing_styles= mp.solutions.drawing_styles
mphands=mp.solutions.hands
screen_width,screen_height=pyautogui.size()
cap=cv2.VideoCapture(0)
index_y=0
cTime=0
pTime=0
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    frame_height,frame_width,_= frame.shape
 #====ret is for checking if the frame is sucessfully read or not 
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) #============coooonverting colour==========
    #======process the colour and detect hand========
    output=hand_dectector.process(rgb_frame)
    #========number for hand===========
    hands=output.multi_hand_landmarks
    #==============checking if its working or not================
    if hands:
          for hand in hands:
                drawing.draw_landmarks(frame,hand,mphands.HAND_CONNECTIONS)
                landmarks=hand.landmark
                for id, landmark in enumerate(landmarks):
                      x=int(landmark.x*frame_width)
                      y=int(landmark.y*frame_height)
                      if id==8:
                            cv2.circle(img=frame,center=(x,y), radius=20,color=(0,255,255))
                            index_x = (screen_width / frame_width) * x 
                            index_y = (screen_height / frame_height) * y 
                            pyautogui.moveTo(index_x,index_y)
                      if id==4:
                        cv2.circle(img=frame,center=(x,y), radius=20,color=(0,255,255))
                        thumb_x=screen_width/frame_width*x 
                        thumb_y=screen_height/frame_width*y
                        #=======abs for ddiffreneces  ================
                        print(index_y,thumb_y)
                        if abs(index_y - thumb_y)<40:
                             print("clicked")
                             pyautogui.click()
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime= cTime
    cv2.putText(frame,str(int(fps)),(10,70), cv2.FONT_HERSHEY_COMPLEX,3,(255,0,255),3)
                 

    #==================camera frame====================
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows(
      
)