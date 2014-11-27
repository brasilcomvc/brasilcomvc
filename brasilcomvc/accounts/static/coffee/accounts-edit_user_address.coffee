if (!$('body.accounts.edit_user_address').length)
	return


###
Filter cities by state selection
###

cities_select = $ '#useraddressform_city select'

# Group options by state
states = {}
for city_el in $ 'option', cities_select
	(states[state_label = city_el.parentNode.label] or= []).push city_el
	current_state = state_label if city_el.selected

# Clear the original <select> from <optgroup>s
cities_select.empty()

# Preset the already selected state, if any
if current_state
	cities_select.append states[current_state]

# Build cities options upon state selection
$('#useraddressform_state select').on 'change', ->
	cities_select.empty()
	cities_select.append states[@options[@selectedIndex].label]
