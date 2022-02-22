import os
files = os.listdir("/Volumes/Data-Storage-HDD-1-4TB/VideoData/Youtube")
webms = []
for file in files:
    if ".webm" in file:
        webms.append(file)
print(f"There are {len(webms)} webms in this folder")
import moviepy.editor as me
import shutil
i = 0
for file in files:
    print(f"-----------------{i}/{len(webms)}---------------------")
    i = i+1
    try:
        print("Running for file - ",file)
        if ".webm" in file:
            print("Got the webm file - ",file)
            if os.path.exists("/Volumes/Expansion/WAVS/"+file.replace(".webm","")):
                if len(os.listdir("/Volumes/Expansion/WAVS/"+file.replace(".webm",""))) < 2:
                    clip = me.VideoFileClip(os.path.join("/Volumes/Data-Storage-HDD-1-4TB/VideoData/Youtube", file))
                    clip.audio.write_audiofile("/Volumes/Expansion/WAVS/"+file.replace(".webm","")+"/"+file.replace(".webm",".wav"))
                    shutil.copy(os.path.join("/Volumes/Data-Storage-HDD-1-4TB/VideoData/Youtube/",file.replace(".webm",".en.vtt")), "/Volumes/Expansion/WAVS/"+file.replace(".webm","")+"/")
                    print(f'This folder {"/Volumes/Expansion/WAVS/"+file.replace(".webm","")+"/"} has {len(os.listdir("/Volumes/Expansion/WAVS/"+file.replace(".webm","")+"/"))} files')
                else:
                    print("There are 2 files.")
            else:
                os.mkdir("/Volumes/Expansion/WAVS/"+file.replace(".webm",""))
                clip = me.VideoFileClip(os.path.join("/Volumes/Data-Storage-HDD-1-4TB/VideoData/Youtube", file))
                clip.audio.write_audiofile("/Volumes/Expansion/WAVS/"+file.replace(".webm","")+"/"+file.replace(".webm",".wav"))
                shutil.copy(os.path.join("/Volumes/Data-Storage-HDD-1-4TB/VideoData/Youtube/",file.replace(".webm",".en.vtt")), "/Volumes/Expansion/WAVS/"+file.replace(".webm","")+"/")
                print(f'This folder {"/Volumes/Expansion/WAVS/"+file.replace(".webm","")+"/"} has {len(os.listdir("/Volumes/Expansion/WAVS/"+file.replace(".webm","")+"/"))} files')
    except:
        pass