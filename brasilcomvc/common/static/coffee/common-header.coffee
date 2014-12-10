body = $(document.body)

_prevent_ghost_click = (e) ->
	e.preventDefault()
	setTimeout(
		-> body.off 'touchend', _prevent_ghost_click,
		370)

$(document).on 'touchstart mousedown', (e) ->
	in_nav = !!$(e.target).closest('#main-header .main-nav').length

	if not in_nav and body.hasClass('header-focus')
		e.preventDefault()

	if in_nav and not body.hasClass('header-focus')
		body.on 'touchend', _prevent_ghost_click

	body.toggleClass 'header-focus', in_nav
