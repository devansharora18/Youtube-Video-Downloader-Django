from django.shortcuts import render
from pytube import YouTube
import os

# Create your views here.

def ytd(request):
	return render(request, 'ytd.html')

def download_page(request):
	global url
	url = request.GET.get('url')

	yt = YouTube(url)

	streams = yt.streams.all()

	res = []
	ores = []
	for i in streams:
		onlyres = i.resolution

		if i.includes_audio_track == True:
			string = str(i.resolution) + ' audio only ' + str(i.filesize_approx // 1048576) + 'mb'
		else:
			string = str(i.resolution) + ' video ' + str(i.filesize_approx // 1048576) + 'mb'
		res.append(string)
		ores.append(onlyres)
	
	try:
		for j in range(len(res)):
			if 'None' in res[j]:
				res.pop(j)

	except:
		pass

	title = yt.title
	author = yt.author
	length = str(yt.length//60) + ' minutes'
	if length == 0:
		length = str(yt.length) + ' seconds'

	thumbnail = yt.thumbnail_url
	print(thumbnail)


	res = list(dict.fromkeys(res))

	return render(request, 'download.html', {
		'onlyres': ores,
		'res': res,
		'title': title,
		'author': author,
		'length': length,
		'thumbnail': thumbnail,
	})

def success(request, res):
	global url

	homedir = os.path.expanduser("~")

	dirs = homedir + '/Downloads'

	yt = YouTube(url)

	if request.method == 'POST':
		yt.streams.get_by_resolution(res).download(dirs)
		return render(request, 'success.html')

	else:
		return render(request, 'error.html')