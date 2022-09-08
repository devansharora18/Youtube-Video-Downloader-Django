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

	title = yt.title
	author = yt.author
	length = str(yt.length//60) + ' minutes'
	if length == 0:
		length = str(yt.length) + ' seconds'

	thumbnail = yt.thumbnail_url
	print(thumbnail)

	res = list(dict.fromkeys(res))

	return render(request, 'download.html', {
		'res': res,
		'title': title,
		'author': author,
		'length': length,
		'thumbnail': thumbnail,
	})