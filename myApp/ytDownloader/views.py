from django.shortcuts import render
from pytube import YouTube

# Create your views here.

def ytd(request):
	return render(request, 'ytd.html')

def download_page(request):
	url = request.GET.get('url')

	yt = YouTube(url)

	streams = yt.streams.all()

	res = []
	for i in streams:
		if i.includes_audio_track == True:
			string = f'{i.resolution} audio only'
		else:
			string = f'{i.resolution} video'
		res.append(string)

	res = list(dict.fromkeys(res))

	return render(request, 'download.html', {
		'res': res
	})