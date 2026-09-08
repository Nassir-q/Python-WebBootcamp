from django.shortcuts import render


courses = [
    {
        "id": 1,
        "name": "python programming",
        "level": "beginner",
        "student_count": 25,
        "description": "Learn Python fundamentals and build simple programs.",
        "image": "python.jpg",
    },
    {
        "id": 2,
        "name": "django development",
        "level": "intermediate",
        "student_count": 0,
        "description": "Build dynamic websites using <strong>Django</strong>.",
        "image": "django.jpg",
    },
    {
        "id": 3,
        "name": "web development",
        "level": "beginner",
        "student_count": 1,
        "description": "Learn HTML, CSS, and modern web development concepts.",
        "image": "web.jpg",
    },
]


def home(request):
    context = {
        "username": "Nasser",
    }

    return render(request, "students/home.html", context)


def course_list(request):
    context = {
        "courses": courses,
    }

    return render(request, "students/courses.html", context)


def course_detail(request, course_id):
    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    context = {
        "course": selected_course,
    }

    return render(request, "students/courses_detail.html", context)
