from django.shortcuts import render
from django.core.paginator import Paginator


MOCK_COURSES = [
    {'id': 1, 'title': 'Python for Beginners', 'category': 'programming',
        'difficulty': 'beginner', 'instructor': 'Ahmed', 'syllabus': 'Variables, Loops, Functions'},
    {'id': 2, 'title': 'Django Mastery', 'category': 'web', 'difficulty': 'advanced',
        'instructor': 'Sara', 'syllabus': 'Models, Views, ORM'},
    {'id': 3, 'title': 'UI/UX Fundamentals', 'category': 'design', 'difficulty': 'intermediate',
        'instructor': 'Nasser', 'syllabus': 'Figma, Wireframes, Prototyping'},
]


def course_list(request):
    courses = MOCK_COURSES

    query = request.GET.get('q', '').strip().lower()
    if query:
        courses = [cours for cours in courses if query in cours['title'].lower()]

    category = request.GET.get('category', '')

    if category == 'None':
        category = ''

    if category:
        courses = [cours for cours in courses if cours['category'] == category]

    paginator = Paginator(courses, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'courses/course_list.html', {
        'page_obj': page_obj, 'query': query, 'category': category
    })


def course_detail(request, id):
    course = None
    for cours in MOCK_COURSES:
        if cours['id'] == id:
            course = cours
            break

    tab = request.GET.get('tab', 'details')

    return render(request, 'courses/course_detail.html', {'course': course, 'tab': tab})
