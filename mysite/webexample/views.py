from django.shortcuts import render

def index (request):
    title = request.GET["title"]
    subtitle = request.GET["subtitle"]
    image_url = request.GET["image_url"]
    cards = {"version":"v2","content":{"type": "instagram","messages":[{"type":"cards","elements":[{"title":title,"subtitle":subtitle,"image_url":image_url,"action_url":"https://manychat.com","buttons":[]}],"image_aspect_ratio":"horizontal"}]}}
    data = {'dict': cards}
    return render(request, 'main/index.html', data)

    