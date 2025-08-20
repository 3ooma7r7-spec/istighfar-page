from instabot import Bot
import os

# إنشاء البوت
bot = Bot()
bot.login(username=os.environ.get("IG_USERNAME"), password=os.environ.get("IG_PASSWORD"))

# حفظ آخر صورة تم نشرها
posted_file = "posted_index.txt"
if os.path.exists(posted_file):
    with open(posted_file, "r") as f:
        last_index = int(f.read())
else:
    last_index = 0

# قراءة الصور من فولدر posts بصيغة JPG
images = sorted([f"posts/{f}" for f in os.listdir("posts") if f.endswith(".jpg")])

# اختيار الصورة التالية للنشر
image_to_post = images[last_index % len(images)]

# نشر بوست + ستوري
bot.upload_photo(image_to_post, caption="أضف تعليقك هنا")
bot.upload_story_photo(image_to_post)

# تحديث رقم الصورة المنشورة
with open(posted_file, "w") as f:
    f.writ
