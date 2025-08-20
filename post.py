from instabot import Bot
import os

bot = Bot()
bot.login(username=os.environ.get("IG_USERNAME"), password=os.environ.get("IG_PASSWORD"))

posted_file = "posted_index.txt"
if os.path.exists(posted_file):
    with open(posted_file, "r") as f:
        last_index = int(f.read())
else:
    last_index = 0

images = sorted([f for f in os.listdir(".") if f.endswith(".jpg")])
image_to_post = images[last_index % len(images)]

bot.upload_photo(image_to_post, caption="أضف تعليقك هنا")

with open(posted_file, "w") as f:
    f.write(str(last_index + 1))
