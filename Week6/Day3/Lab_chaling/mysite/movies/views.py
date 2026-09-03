from django.shortcuts import render

# Create your views here.
movies = [
    {
        "id": 1,
        "title": "The Odyssey",
        "year": 2026,
        "rating": 9.9,
        "image": "im1.jpg",
        "description": "After the Trojan War, Odysseus faces a dangerous voyage back to Ithaca, meeting creatures like the Cyclops Polyphemus, Sirens, and Calypso along the way."
    },
    {
        "id": 2,
        "title": "Fight Club",
        "year": 1999,
        "rating": 9.3,
        "image": "im2.jpg",
        "description": "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more."
    },
    {
        "id": 3,
        "title": "F1",
        "year": 2025,
        "rating": 8.5,
        "image": "im3.jpg",
        "description": "A Formula One driver comes out of retirement to mentor and team up with a younger driver."
    },
    {
        "id": 4,
        "title": "The Fast and the Furious: Tokyo Drift",
        "year": 2006,
        "rating": 9.0,
        "image": "im4.jpg",
        "description": "A teenager becomes a major competitor in the world of drift racing after moving in with his father in Tokyo."
    },
    {
        "id": 5,
        "title": "The Conjuring",
        "year": 2013,
        "rating": 7.5,
        "image": "im5.jpg",
        "description": "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence in their farmhouse."
    }
]


def movie_list(request):
    return render(request, "movies/movie_list.html", {"movies": movies})


def movie_detail(request, movie_id):
    movie = next((movie for movie in movies if movie["id"] == movie_id), None)

    return render(request, "movies/movie_detail.html", {"movie": movie})
