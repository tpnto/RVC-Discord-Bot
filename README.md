<div align="center">

<h1>Retrieval-Based-Voice-Conversion-Bot</h1>
A Discord bot with the capabilities of processing audio/video through RVC<br><br>
</div>



https://github.com/tpnto/RVC-Discord-Bot/assets/122957904/5a770a53-4a16-4a10-bb9a-84a25a2914e8



# Summary
This Discord bot has the following features:
+ Ability to generate Text-To-Speech like outputs.
+ Ability to generate audio using Open AI's API and Edge-tts.
+ Ability to process audio and video files through RVC.

# Getting Started
In order to host this bot you are going to have to use **Python 3.10.0**, otherwise it won't work. 
[You can download it by clicking here!](https://www.python.org/downloads/release/python-3100/)

In order to convert video files you will need to have [FFmpeg](https://ffmpeg.org/download.html) in the directory you are currently working on.
You will also need [yt-dlp](https://github.com/yt-dlp/yt-dlp/releases).

You are also going to need these two files in your directory:

+ [rmvpe.pt](https://huggingface.co/lj1995/VoiceConversionWebUI/blob/main/rmvpe.pt)

+ [hubert_base.pt](https://huggingface.co/lj1995/VoiceConversionWebUI/blob/main/hubert_base.pt)

In the folder you are using for this bot, go ahead and make an environment using Python 3.10.0:
```bash
Python -m venv env
```
Then we are going to activate it using the terminal: 
```bash
.\env\Scripts\Activate.bat
```
After you are done setting up the environment, you are going to have to install PyTorch here's the link for it, [PyTorch](https://pytorch.org/get-started/locally/)
# Requirements
After PyTorch is done installing, you are going to run these two commands:
``` bash
pip install -e git+https://github.com/JarodMica/rvc.git#egg=rvc\
```
``` bash
pip install -e git+https://github.com/tpnto/rvc-tts-pipeline.git@rvc-output-name#egg=rvc-tts-pipe
```
Once these two are done installing, we are going to have to install the rest of the packages you need, in order to install them you simply run this command:
``` bash
pip install -r requirements.txt
```

If you have followed these steps, you should be able to run this bot locally!
