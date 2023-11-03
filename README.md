# Automatic-Speech-Summarization-of-Mixed-Arabic-English-Speech
  - Due to the nature of our lives nowadays, and due to the fact that time has become more and more precious, many people don’t have time to hear a full audio, audio of two hours for example, to just find out where they are interested in the content of this audio. And here is where our project comes to life to solve this problem, by summarizing a full audio into a few lines of text.

  - This Repository is a demo where we deploy our machine learning models, which include a model speech recognition for mixed Arabic-English speech, a translation, and a summarization model. In this Project we used flask framework to create the demo as a web application.
  
# Video:
[Watch the demo video](https://www.linkedin.com/posts/hadeer-mamdooh-204522171_details-of-project-activity-7019034056910643200-WfL6?utm_source=share&utm_medium=member_android)

# Getting Started
## To run the demo, walk with the following steps:
    1- Clone this repository to your local machine, by typing this command in CMD or Terminal: `git clone https://github.com/ahmed-0egy/Automatic-Speech-Summarization-of-Mixed-Arabic-English-Speech`
    2- You will need to download the summarization model from this link (https://drive.google.com/file/d/1pq8jGLnwRrDZAmI4yjhjGWQxfkbH4b0x/view?usp=share_link), and put it inside this directory: `.\static\assets\models\summarization`
    3- Install the required packages, you can use the following command in CMD or Terminal:     `pip install requirements.txt`
    4- Run the flask applicaion by running (app.py), you can use the following command in CMD or Terminal:    `flask run`
    5- Now from cmd copy the url that shows up, and paste it in your browser
  ### Notes
  - Note that on github the model.pt file may not exist, you don't need to worry about that since if it doesn't exist it will be downloaded automatically, once you run the application.<br>
  - Also note that it may take sometime to run the application, that's totally OK, since the model.pt file is large and may take sometime to be loaded.<br>
  - Finally note that if you don't have GPU and you are running on CPU this will take much time to execute since these models require parallel copmuting power.

# Machine Learning & Deep Learning work 
  - You can find the work of machine learning on this repository, where you will find the full machine learning pipeline that was followed to gain the models.
https://github.com/hadeer98/Automatic-Speech-Summarization-of-Mixed-Arabic-English-Speech/blob/aa21104da0019bfa9fe14fceb87b1d985e40c259/Rouge.ipynb
# Project Structure
## The project has the following file structure:
. <br>
├── Static <br> 
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; └── assets <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── models <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── summarization <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── pytorch_model.bin <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── transcription <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── medium.pt <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── uploads <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; └── js <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── script.js <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; └── styles <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── scss <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── photon-ai-dekstop-1440.css <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── photon-ai-dekstop-1440.css <br>
├── templates <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── base.html <br>
│&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;└── index.html <br>
├── app.py <br>
├── speech.py <br>
├── summarization.py <br>
└── requirements.txt


# Describtion about the Demo:
 This demo provides the use with an interface that allows him to different tasks. In fact some of these tasks depend on other ones, however the demo allows the user to do any of these tasks without worrying about details, these tasks are:

    1- Speech Recognition: This task will return you the transcription of the mixed Arabic-English Audio into English text.
    2- English Title: This task will return you a short English description about the audio, which you can use as an English title for the audio.
    3- English Title: This task will return you a short Arabic description about the audio, which you can use as an Arabic title for the audio.
    4- English Summarization: This task will summarize the full mixed Arabic-English audio, into few lines of English text.
    5- Arabic Summarization: This task will summarize the full mixed Arabic-English audio, into few lines of Arabic text.
    
 All you need to do is to run the app and open the browser, and don't worry you will know what to do once you are there. The interface is very simple.

 # Website Appearance:
 ![image](https://user-images.githubusercontent.com/55872010/221389154-1571637a-66a2-449e-ab03-4a8d6965c26d.png)
 ![image](https://user-images.githubusercontent.com/55872010/221389165-767dc922-19b2-4eed-a89e-6b834aba3222.png)
 ![image](https://user-images.githubusercontent.com/55872010/221389184-e0a73309-6f57-4903-9a29-bffb997edbab.png)
 ![image](https://user-images.githubusercontent.com/55872010/221389209-1ef2cffa-39d2-4556-9ae7-7f5f0253f68d.png)
 ![image](https://user-images.githubusercontent.com/55872010/221389227-c2d6fa25-d82e-4676-963c-d75f26737be2.png)
 ![image](https://user-images.githubusercontent.com/55872010/221389245-e6345d86-e39d-4ada-8fbd-f50e20d6b0d4.png)
 
#  Contributions
Contributions to "Automatic Speech Summarization of Mixed Arabic-English Speech" are welcome and encouraged! However, please note that this project is licensed under the GNU General Public License v3.0, which means that any contributions must also be licensed under the same terms.

By contributing to this project, you agree to license your contributions under the GNU General Public License v3.0. This means that your contributions may be used, modified, and distributed by anyone under the same terms as the original project.

If you would like to contribute to this project, please follow these guidelines:

    1- Fork the repository.
    2- Make your changes in a new branch.
    3- Test your changes thoroughly.
    4- Submit a pull request.
Thank you for considering contributing to this project!

# Conclusion
    1- We implemented pretrained language models, which were based upon the transformer architecture for 
    the task of summarization. We concluded after tuning facebook/bart provided best results as 54.4% 
    rouge1. So, we chose it as a champion model.
    2- In the future,we are focusing on building more robust models,aim to fine-tune the pre-trained models of different  datasets and examine if the performance is improved.also, We would also like to expand the use case of our summarization task to more general long document summarization.
    3- also we may extend the idea from speech to summarize the video.
