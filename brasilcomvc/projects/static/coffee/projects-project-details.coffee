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
			rel: 0,
			theme: 'light',

	# Drop `data-video` attribute
	@removeAttribute 'data-video'


### Fixed sidebar ###
# This cannot be just a matter of style because the required elements are not
# wrapped into a single container.
sidebar = $('<section class="page-content sidebar"/>')
sidebar.append $('.page-title').clone()
sidebar.append $('.apply').clone()
sidebar.append $('#extra-info').clone()
$('#main-content').prepend sidebar
