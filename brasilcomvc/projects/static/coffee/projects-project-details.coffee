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

# Build and render the sidebar
sidebar = $('<section class="page-content sidebar"/>')
sidebar.append $('.page-title').clone()
sidebar.append $('.apply').clone()
sidebar.append $('#extra-info').clone()
$('#main-content').prepend sidebar

# Handle scrolling x map
map_parent = $('#map')
sidebar_bottom = null
$(window).on 'scroll', ->
	sidebar_bottom or= sidebar[0].offsetTop + sidebar.height()
	wh = $(window).height()
	map_top = wh - ($(document).scrollTop() + wh - map_parent.offset().top)
	if sidebar_bottom > map_top
		sidebar.css bottom: wh - map_top
	else
		sidebar.css bottom: ''


### Project location map ###
project_location = new google.maps.LatLng PROJECT_LAT, PROJECT_LNG
map_canvas = $('<div/>')[0]
map_parent.append map_canvas
map = new google.maps.Map map_canvas,
	center: project_location
	disableDefaultUI: true
	scrollwheel: false
	zoom: 13
	zoomControl: true
	zoomControlOptions:
		position: google.maps.ControlPosition.LEFT_CENTER
project_marker = new google.maps.Marker
	map: map
	position: project_location
	title: PROJECT_NAME
