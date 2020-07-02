# Mommybot

Our team developed a system called Mommybot, it is a system using jetson nano to manage user's sleeping hours. 
The system was developed for the final proejct of our coursework, which is "KSE 624" from KAIST institute. 
For Mommybot, it took about 4 weeks to develop the system. 

# Introduction
These days, more and more people are suffering from sleep deprivation. There are many reports saying that sleep deprivation will give negative effects on health. 
According to Korea Gallup REport in 2017, sleep deprivation will increase risk of cardiovascular disease 8 times, risk of diabetes 5 times, risk of dementia 5 times, etc.
Also according to National Helath Insurance Service in South Korea, the number of patients with sleeping disorders increased from 2014 to 2018 fastly. Our team speculates that this trends continued in 2020. 

Due to the advance of technology such as introduction of mobile phones, and computers, this trend continued and will be in the future. Although people are sleeping less due to their hard working styles with a belif in good human nature, our team bet that most people are sleeping less because they got distracted by cell phones or internet. Especially this is a major prolbme for many people who needs to go to specific places such as school or jobs at the certain time in the morning. According to National Sleep Foundation, the minimum required sleeping hours is at least 6 unless you are older than 65 years old. In other words, from Monday to Friday (unless you go to work on Saturday), you need to sleep at elast 30 hours for 5 days. 
To fix this problem, our team thought that what many people need is mom. Mom who cares about your health, who tells you to go to bed, who wakes you up in the morning. 
With this ideation of mom, our team developed Mommybot. 

Mommybot's main function is divided into three: Record time events, Monitors your bed, Actions. each funciton will be explained after the requirement. 


#Requirement setting








# Record Time event:
Our team classified everyday's time hours into five different classes. 
Each classes will be recorded on Mommybot with two differet sensors & speaker device. 
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

### tip 
Our code named 'Training_model.ipynb' will shows steps in creating pre-trained model, which is 'mode_model2.h5. 
When you are replicating our code, you can use 'Training_model.ipynb' to take photos of three different status.

# Actions
Mommybot gives three different actions, which are
### 1. "Go to bed"

![KakaoTalk_20200629_183154639_02](https://user-images.githubusercontent.com/32156141/86339854-0a74e680-bc8f-11ea-91ed-67a3d05bec28.gif)


### 2. "Go to Sleep"

![KakaoTalk_20200629_183154639](https://user-images.githubusercontent.com/32156141/86339936-2a0c0f00-bc8f-11ea-9f8c-70a40ea1fbc6.gif)

### 3. "Wake up"

![KakaoTalk_20200629_183154639_01](https://user-images.githubusercontent.com/32156141/86340134-6fc8d780-bc8f-11ea-9077-324ea844654f.gif)

