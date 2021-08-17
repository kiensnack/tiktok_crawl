import os
import zipfile
dir = '/home/kien/PycharmProjects/tiktok'
allfiles = os.listdir(dir)
#files = [ fname for fname in allfiles if fname.endswith('.mp4')]
#print (files)





for fname in allfiles:
    if fname.endswith('.mp4'):
       jungle_zip = zipfile.ZipFile('/home/kien/PycharmProjects/tiktok/zip_tiktok/'+fname.replace('.mp4', '')+'.zip', 'w')
       jungle_zip.write(fname, compress_type=zipfile.ZIP_DEFLATED)
       jungle_zip.close()