import os,pytube,time
from prog import double_bar_example

link=input("Enter full Youtube link to video \n")
yt=pytube.YouTube(str(link)) # create object
# obtain streams which are progressive and of extension mp4
st=yt.streams.filter(progressive=True,file_extension='mp4').all()
print('Available files on the url in mp4 format')
s=1
for i in st:
    print(str(s)+" "+yt.title+" in "+i.resolution+"\n")
    s+=1

res=input('Select desired resolution\n')
st=st[int(res)-1] # chose the desired resolution video

try:
    #downloading the video
    print('Initializing')
    double_bar_example()
    print('Downloading...')

    start_time=time.time()
    st.download(os.path.dirname(os.path.abspath(__file__)))# download to the following path
    duration=time.time()-start_time

    print('Download Completed in'+duration+'seconds\n' + yt.title + ' has been downloaded\n')
except:
    print("Some Error!")

print('View thumbnail at '+yt.thumbnail_url)
# to view captions,
#print(  yt.captions.all() )
#caption=yt.captions.get_by_language_code('en')
#print(caption.getenrate_str_captions())
