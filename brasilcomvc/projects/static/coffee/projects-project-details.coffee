if (!$('body.projects.project-details').length)
	return


$(document).on 'click', '#main-content figure.img[data-video]', ->
	img = @getElementsByTagName('img')[0]
	player = new YT.Player img.id,
		height: img.offsetHeight,
		width: img.offsetWidth,
		videoId: @getAttribute('data-video').split('v=')[1],
		playerVars:
			autoplay: 1,
			modestbranding: 1,
			theme: 'light',

	# Drop `data-video` attribute
	@removeAttribute 'data-video'
