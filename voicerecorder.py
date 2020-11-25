import sound device as sd
import sound file as sf
from tkinter import *
def voice_rec():
fs=48000
duration-5
myrecording=sf.rec(int(duration*fs),samplerate=fs,channeis=2)
sd.wait()

return sf.write('my_Audio_file.flac',myrecording,fs)
master -Tk()
Label(master,text-'Voice Recorder : "').grid(row=0,sticky=W,rowspan=5)
b=button(master,text="Start",command=Voice_rec)
b.grid(row=0,column=2,columnspan=2,rowspan=2,padx=5,pady=5)
mainloop()