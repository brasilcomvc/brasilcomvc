body = $(document.body)

$(document).on 'touchend', (e) ->
	in_nav = !!$(e.target).closest('#main-header .main-nav').length
	if not in_nav and body.hasClass('header-focus')
		e.preventDefault()
	body.toggleClass 'header-focus', in_nav
