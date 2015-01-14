return if not $('body').hasClass('project-search')


_get = (name) ->
	# Retrieve the value of a GET parameter
	(new RegExp("[?&]#{name}=([^&$]*)").exec(location.search) or [0, null])[1]

# Pin images
PIN_USER = "#{STATIC_URL}styl/glyphs/user-location.png"

# Cache some elements for better performance
form = $('#search-results form')[0]
main_header = $('#main-header')
main_footer = $('#main-footer')
search_results = $('#search-results ul')
window_ = $(window)


class ProjectSearch

	constructor: (user_lat, user_lng) ->
		center = new google.maps.LatLng(user_lat, user_lng)

		# Create and render the Google Maps widget
		@map_parent = $('#map')
		map_canvas = $('<div/>')[0]
		@map_parent.append(map_canvas)
		@map = map = new google.maps.Map map_canvas, center: center

		# Mark the user into it
		@user_marker = new google.maps.Marker
			map: map,
			position: center,
			icon: PIN_USER,

		# Mark projects' locations
		@results_markers = results_markers = []
		results_bounds = new google.maps.LatLngBounds
		search_results.children('.project').each ->
			marker = new google.maps.Marker
				map: map,
				position: new google.maps.LatLng(
					+@getAttribute('data-lat'), +@getAttribute('data-lng'))
			results_markers.push marker
			results_bounds.extend marker.getPosition()

		# Zoom the map to wrap all search results
		@map.fitBounds results_bounds

		# Initialize a geocode autocomplete on the search form
		autocomplete = new google.maps.places.Autocomplete form.q,
			types: ['geocode'],

		# Fill latitude and longitude fields with geocode from the autocomplete
		google.maps.event.addListener autocomplete, 'place_changed', ->
			location = autocomplete.getPlace().geometry.location
			form.lat.value = location.lat()
			form.lng.value = location.lng()

		# Fill latitude and longitude fields with geocode
		$(form).on 'submit', (e) ->
			if @lat.value and @lng.value
				return

			e.preventDefault()  # Stop the submit

			geocoder = new google.maps.Geocoder()
			geocoder.geocode address: @q.value, (results, status) =>
				if status != google.maps.GeocoderStatus.OK
					alert('Endereço não encontrado: ' + status)
					return

				location = results[0].geometry.location
				@lat.value = location.lat()
				@lng.value = location.lng()
				@submit()

		# Lock the map into the screen viewport
		@lock_viewport()
		window_.on 'scroll', => @lock_viewport()

	lock_viewport: ->
		scroll_bottom = window_.scrollTop() + window_.height()
		footer_top = main_footer[0].offsetTop
		@map_parent.css
			top: main_header.height(),
			bottom: Math.max(scroll_bottom - footer_top, 0),


# Initialize ProjectSearch with geo coords from URL
new ProjectSearch +_get('lat'), +_get('lng')
