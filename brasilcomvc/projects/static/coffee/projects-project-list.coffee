return if not $('body').hasClass('project-list')

search_form = $('#project_search')[0]

# Initialize a geocode autocomplete on the search form
autocomplete = new google.maps.places.Autocomplete search_form.q,
	types: ['geocode'],

# Fill latitude and longitude fields with geocode from the autocomplete
google.maps.event.addListener autocomplete, 'place_changed', ->
	location = autocomplete.getPlace().geometry.location
	search_form.lat.value = location.lat()
	search_form.lng.value = location.lng()

# Geocode on submit
$(search_form).submit( (e) ->
	if search_form.lat.value != "" && search_form.lng.value != ""
		return true

	address = $("input[name=q]", this).val()
	geocoder = new google.maps.Geocoder()

	geocoder.geocode( { 'address': address }, (results, status) ->
		if status == google.maps.GeocoderStatus.OK
			location = results[0].geometry.location
			search_form.lat.value = location.lat()
			search_form.lng.value = location.lng()
			search_form.submit()
		else
			alert('Endereço não encontrado: ' + status)
	)
	return false
)
