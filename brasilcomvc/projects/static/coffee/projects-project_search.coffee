return if not $('body').hasClass('project-search')


search_form = $('#search-results form')[0]


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

# Mark projects' locations
$('.project').each ->
	new google.maps.Marker
		map: map,
		position: new google.maps.LatLng(
			+@getAttribute('data-lat'), +@getAttribute('data-lng'))

# Initialize a geocode autocomplete on the search form
autocomplete = new google.maps.places.Autocomplete search_form.q,
	types: ['geocode'],

# Fill latitude and longitude fields with geocode from the autocomplete
google.maps.event.addListener autocomplete, 'place_changed', ->
	location = autocomplete.getPlace().geometry.location
	search_form.lat.value = location.lat()
	search_form.lng.value = location.lng()
