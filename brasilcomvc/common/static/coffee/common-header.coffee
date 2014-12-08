$(document).on 'click', (e) ->
	in_nav = !!$(e.target).closest('#main-header .main-nav').length
	$(document.body).toggleClass 'header-focus', in_nav
