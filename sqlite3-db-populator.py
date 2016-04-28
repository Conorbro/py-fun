import sqlite3
import os

def insert_picture(conn, picture_file, ref_file, painting_id):
    photo = open(picture_file, 'rb')
    ref = open(ref_file, 'rb')
    ablob = photo.read()
    bblob = ref.read()
    pic = sqlite3.Binary(ablob)
    ref = sqlite3.Binary(bblob)
    base=os.path.basename(picture_file)
    afile, ext = os.path.splitext(base)
    conn.execute("INSERT INTO artwork (Reference, Photo, Title, Id) \
          VALUES (?, ?, ?, ?)", [ref, pic, 'test', painting_id]);
    conn.commit()

photoPath = 'droid/'
refPath = 'references/'

refImages = os.listdir(refPath)
testImages = os.listdir(photoPath)

refImages.remove('.DS_Store')
testImages.remove('.DS_Store')

conn = sqlite3.connect('demo_artwork.db')
print "Opened database successfully";
i = 1
for images in testImages:
    photo_file = photoPath + testImages[i-1]
    ref_file = refPath + refImages[i-1]
    insert_picture(conn, photo_file, ref_file, i)
    i += 1

print "Records created successfully";
conn.close()
