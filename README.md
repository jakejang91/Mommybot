# Mommybot

Our team developed a system called Mommybot, it is a system using jetson nano to manage user's sleeping hours. 
The system was developed for the final proejct of our coursework, which is "KSE 624" from KAIST. 
For Mommybot, it took about 4 weeks to develop the system. 

# Introduction
These days, more and more people are suffering from sleep deprivation. There are many reports saying that sleep deprivation will give negative effects on health. 
According to Korea Gallup REport in 2017, sleep deprivation will increase risk of cardiovascular disease 8 times, risk of diabetes 5 times, risk of dementia 5 times, etc.
Also according to National Helath Insurance Service in South Korea, the number of patients with sleeping disorders increased from 2014 to 2018 fastly. Our team speculates that this trends continued in 2020. 

Due to the advance of technology such as introduction of mobile phones, and computers, this trend continued and will be in the future. Although people are sleeping less due to their hard working styles with a belif in good human nature, our team bet that most people are sleeping less because they got distracted by cell phones or internet. Especially this is a major prolbme for many people who needs to go to specific places such as school or jobs at the certain time in the morning. According to National Sleep Foundation, the minimum required sleeping hours is at least 6 unless you are older than 65 years old. In other words, from Monday to Friday (unless you go to work on Saturday), you need to sleep at elast 30 hours for 5 days. 
To fix this problem, our team thought that what many people need is mom. Mom who cares about your health, who tells you to go to bed, who wakes you up in the morning. 
With this ideation of mom, our team developed Mommybot. 

Mommybot's main function is divided into three: Record time events, Monitors your bed, Actions. each funciton will be explained after the requirement. 



# Requirement setting
## Hardware Components
JetBot

![JB3-Assy_16-5](https://user-images.githubusercontent.com/32156141/86363123-5afd3b80-bcb1-11ea-8116-2f7108782878.jpg)

USB-Speakr
Any type of USB speaker is fine. For this Project, we used Vifa City from a brand named Vifa.

![z](https://user-images.githubusercontent.com/32156141/86362819-d4e0f500-bcb0-11ea-9e25-6af9fad99b12.JPG)

Arduino-kit + LCD

![A000066_front_2](https://user-images.githubusercontent.com/32156141/86365326-54bc8e80-bcb4-11ea-99e1-c38139ae5b21.jpg), ![lcd](https://user-images.githubusercontent.com/32156141/86365322-538b6180-bcb4-11ea-8411-173d534126f3.jpg)

note: we sent 9600 singal to Arduino-kit+LCD in order to use display setting using serial library. 



## software setup
Installing several libraries are required. 
### VLC
### Tensorflow
### sklearn
### pyserial
### pandas 


# Environment setting
Mommybot's experiment was taken at a home of one of teammates. Since the system has to record the user sleeping, Mommybot was positioned right in front of bed which could record his face and body easily. 

Where Mommybot was placed.

![20200629_053120](https://user-images.githubusercontent.com/32156141/86396478-f061f500-bcdc-11ea-8f75-e545caa65f25.jpg)


# Record Time event:
Everyday's time hours is divided into five different classes. 
Each classes transition timestamp will be recorded on Mommybot with two differet sensors & speaker device. 
### 1. Working hours
  - Time interval from the moment you left your house until you returned to home & pair bluetooth to Mommybot.
  - Bluetooth connection is requried to record your home arrival.
### 2. Home-Awake
  - Time interval from you paired bluetooth to Mommybot until you go laydown on a bed.
  - Camera is reuqired to see whether you are on bed or not.
### 3. Bed-nosleep
  - Time interval from you laydown on a bed until you fall a sleep.
  - Camera is reuqired to see whehter you are on bed and not sleeping (doing something else).
### 4. Sleeping Period
  - Time interval from you fall a sleep until monrning call wakes you up.
  - Camera is reuqired to see whehter you are on bed and sleeping.
### 5. Morning
  - Time interval from  monring call sound alarmed untill you leave your house.
  - Speaker is reuqired to make sounds from Mommybot, and when the bluetooth connection is off, Mommybot will think you left the house.

This below photo breifly explains the above timelines, and how Mommybot records each time events.
  ![markdown](https://user-images.githubusercontent.com/32156141/86391549-efc56080-bcd4-11ea-902f-fbad5fc97550.JPG)



# Monitors your bed
Mommybot uses pre-trained model, which uses RandomForestRegressor in order to check your bed's current status.
Current status consist of three situation, which are 
### 1. Non
  -No one's on the bed
  
![0f0ff82c-b9c6-11ea-bacc-00044be6afc0](https://user-images.githubusercontent.com/32156141/86339533-ab16d680-bc8e-11ea-961f-cd0d9b1add8b.jpg)

### 2. Not Sleeping
  -you are on bed, but you are not sleeping. Either using phone, or doing something else.
  
![3c32ebca-b9c6-11ea-bacc-00044be6afc0](https://user-images.githubusercontent.com/32156141/86339587-bc5fe300-bc8e-11ea-885c-667e4093cd63.jpg)


### 3. Sleeping
  -you are sleeping. 
  
![0aca43c0-b9c7-11ea-bacc-00044be6afc0](https://user-images.githubusercontent.com/32156141/86339679-d4cffd80-bc8e-11ea-83bc-7bd84e134114.jpg)


For pre-trained model, we took photos each of status for 2000 times, which are 6000 in total. Then we splited data into training and validation to train and validate the model. 
The accuracy was gained about 80%. We believe this was due to the low light condition, which is one of setings that could not be avoided because people sleep in dark condtion. 

### Note 
Our code named 'Training_model.ipynb' will shows steps in creating pre-trained model, which is 'mode_model2.h5. 
When you are replicating our code, you can use 'Training_model.ipynb' to take photos of three different status.

# Time prediction
We used two RandomForestRegressor model on sklearn to predict start time of 'Bed-nosleep' and 'Sleeping Period'. The RandomForestRegressor is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. source: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html For the first model,  "1.Timestamp of Arrival at home", "4.Duration Time of Average Sleep Time of this week", "5.Duration Time of Sleeptime of Yesterday", "6.Day of the week" was used. The second model used one more featrue which is '2.Timestamp of Lie on Bed'

# Actions
## output explaination
Mommybot uses 6 different time variables to generate four different outputs. 
## Time vairables
 1.Timestamp of Arrival at home
 2.Timestamp of Lie on Bed
 3.Timestamp of Start to Sleep
##### Below variables are calculated by above three variables.
 4.Duration Time of Average Sleep Time of this week
 5.Duration Time of Sleeptime of Yesterday
 6.Day of the week

## Outputs (Prediction vs Suggestion)
###  1.Prediction 1 - When will you go to Bed
###  2.Prediction 2 - When Will you go to Sleep
###  3.Suggestion 1 - WHen Should you go to bed
###  4.Suggestion 2 - WHen Should you go to Sleep

The key difference between Prediction and Suggestion is below.

Prediction: Either user's expected going bed time or sleeping time based on time varaibles. 
Prediction varaibles are generated by RandomForestRegressor.
Suggestion: Either user's going bed time or sleeping time in order to accomplish user's preset sleeping goal hours (default value is 6 hours). 
Suggesstion variables are generated by rule.

which variables were used to generate output vairalbes are shown below image.

![outputs](https://user-images.githubusercontent.com/32156141/86393769-7b8cbc00-bcd8-11ea-9c26-bd5c1917cb9d.JPG)


Based on these variables Mommybot gives three different actions, which are
### 1. "Go to bed"

![KakaoTalk_20200629_183154639_02](https://user-images.githubusercontent.com/32156141/86339854-0a74e680-bc8f-11ea-91ed-67a3d05bec28.gif)

The Arduino display blinks and shows user to go to bed, and also form speakr previously recorded voice will be out teling user to go to bed.
### 2. "Go to Sleep"

![KakaoTalk_20200629_183154639](https://user-images.githubusercontent.com/32156141/86339936-2a0c0f00-bc8f-11ea-9f8c-70a40ea1fbc6.gif)

The Arduino display blinks and shows user to go to sleep, and also form speakr previously recorded voice will be out teling user to go to sleep.


### 3. "Wake up"

![KakaoTalk_20200629_183154639_01](https://user-images.githubusercontent.com/32156141/86340134-6fc8d780-bc8f-11ea-9077-324ea844654f.gif)

The Arduino display blinks and shows user to wake up, and also form speakr will turn on the music that is put into Mommybot.
*Any type of Mp3 file can be put into Mommybot, and can be used for the alaram sound.


Each of actions will be applied in three different intervals, which are shown below pictures. 
 
![DASF](https://user-images.githubusercontent.com/32156141/86392329-36678a80-bcd6-11ea-9c90-e1626bbeb83b.JPG)

Each of actions are performed by Mommybot on gennerated outputs shown at output explaination. 
the time intervals are shown at below image.

![outputs](https://user-images.githubusercontent.com/32156141/86394131-08d01080-bcd9-11ea-8744-bcc03c9450ca.JPG)

# Limitation
Moommybot uses camera to take a photo of user to check wheter he is there, not sleeping, or sleeping. With sleeping condition, normal people would sleeping in the dark. Since our model used normal camera that was attached to the Jetson nano kit, the quality of the photo taken at night was very low. Therefore, Whether one is sleeping or not, can not be achieved in some cases. Not only this was the issue, but also what you are wearing at night is also important as well. Since the pre-trained model only used a picture of me wearing yellow t-shirt, if I'm wearing another shirt, there is a high chance that Mommybot would not be able to check the status correctly. 
In order to replicate our model, we recommend that you to use the same experiemntal conditions. 

To show the demo video of Mommybot, our team took a video showing what it does.
link: https://youtu.be/kPztnB4K7dI
