from django.shortcuts import render

def index(request):
	context = {
		"title": "Portfolio",
		"user": {
            "username": "simongranil",
			"birthday": "2000-10-31T01:30:00.000-05:00",
        },
		"list": [1, 2, 3, 4, 5],
		"sentences": "Lorem ipsum dolor sit amet, consectetur adip"
    }

	return render(request, "pages/portfolio.page.html", context=context)
