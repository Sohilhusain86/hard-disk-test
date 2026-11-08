import urllib.request
import json
import random

# 20-50 चुनिंदा मोटिवेशनल और इस्लामी अकवाल (बिना जानदार वाली तस्वीरों के साथ)
quotes = [
    {
        "title": "📚 علم کی روشنی اور مطالعہ",
        "message": "علم وہ دولت ہے جو بانٹنے سے بڑھتی ہے۔ آج ہی اپنے نصاب کا کچھ وقت ضرور نکالیں۔",
        "image": "https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?q=80&w=1000&auto=format&fit=crop" # Books library (Non-living)
    },
    {
        "title": "🌟 ذکر و نور کا سفر",
        "message": "دلوں کا سکون اللہ کے ذکر اور نعت پاک کی سماعت میں ہے۔ سکرین کھولیں اور فیض حاصل کریں۔",
        "image": "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?q=80&w=1000&auto=format&fit=crop" # Islamic architecture / Mosque dome (Non-living)
    },
    {
        "title": "📖 درسی کتب اور کامیابی",
        "message": "مستقل مزاجي کامیابی کی کنجی ہے۔ روزانہ فیض الأدب اور نحو الواضح کا مطالعہ جاری رکھیں۔",
        "image": "https://images.unsplash.com/photo-1457369804613-52c61a468e7d?q=80&w=1000&auto=format&fit=crop" # Classic books (Non-living)
    }
]

def send_notification():
    q = random.choice(quotes)
    app_id = "a4d0bc8e-b2ad-484a-ad60-3f68f99bce44"
    # Yahan apni OneSignal REST API Key dalein ya environment se lein
    rest_api_key = "YOUR_REST_API_KEY" 

    payload = {
        "app_id": app_id,
        "included_segments": ["All"],
        "headings": {"en": q["title"]},
        "contents": {"en": q["message"]},
        "big_picture": q["image"],
        "url": "https://hardrisk.vercel.app/"
    }

    req = urllib.request.Request(
        "https://onesignal.com/api/v1/notifications",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": f"Basic {rest_api_key}"
        }
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            print("🚀 Motivational Quote Notification Sent!", resp.read().decode())
    except Exception as e:
        print("❌ Error:", str(e))

if __name__ == "__main__":
    send_notification()
