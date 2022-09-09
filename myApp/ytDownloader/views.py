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
	global streams
	streams = yt.streams

	res = []
	ores = []
	for i in streams:
		onlyres = i.resolution

		string = str(i.resolution) + ' ' + str(i.filesize_approx // 1048576) + 'mb'

		res.append(string)
		ores.append(onlyres)
	
	ores = list(dict.fromkeys(ores))

	try:
		for j in range(len(ores)):
			if ores[j] == None:
				ores.pop(j)

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

	#yt = YouTube(url)
	#yt = yt.streams.filter(file_extension='mp4')

	if request.method == 'POST':
		#a,b = res.split()
		streams.filter(res=res).first().download(dirs)
		return render(request, 'success.html')

	else:
		return render(request, 'error.html')