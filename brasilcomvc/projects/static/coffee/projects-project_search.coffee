return if not $('body').hasClass('project-search')


_get = (name) ->
	# Retrieve the value of a GET parameter
	(new RegExp("[?&]#{name}=([^&$]*)").exec(location.search) or [0, null])[1]


# Create a <div> to contain the map
map_canvas = $('<div/>')[0]
$('#map').append(map_canvas)

# Initialize the map widget
map = new google.maps.Map map_canvas,
	center: new google.maps.LatLng(+_get('lat'), +_get('lng')),
	zoom: 13,

# Mark the user location
user_marker = new google.maps.Marker
	map: map,
	position: map.center,
	icon: window._user_location_icon,
