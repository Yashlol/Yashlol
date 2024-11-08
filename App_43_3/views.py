from django.shortcuts import render
from django.http import HttpResponse

def resume_view(request):
    resume_data = {
        'name': 'Kodali Yash Chowdary',
        'title': 'Software Developer',
        'about': 'Software Developer with 3 years of experience in web development, project management, and data analysis, focused on delivering quality results in fast-paced environments.',
        'email': 'kodaliy28@gmail.com',
        'phone': '546879556',
        
        
        # Additional sections
        'experience': [
            {'position': 'Junior Developer', 'company': 'Tech Solutions Inc.', 'years': '2021-2022'},
            {'position': 'Software Engineer', 'company': 'Innovatech', 'years': '2022-Present'}
        ],
        'skills': ['Python', 'Django', 'JavaScript', 'Project Management'],
        'projects': [
            {'name': 'Portfolio Website', 'description': 'A personal portfolio website built with Django.'},
            {'name': 'E-commerce Platform', 'description': 'An e-commerce platform developed to streamline online sales.'}
        ],
        'education': [
            {'degree': 'B.Tech', 'institution': 'KL University', 'year': '2027'},
            {'degree': 'Certification in Web Development', 'institution': 'KL University', 'year': '2029'}
        ],
        # LinkedIn and GitHub links
        'linkedin': 'https://www.linkedin.com/in/yash-chowdary-888b672b2/',  # replace with your LinkedIn URL
        'github': 'https://github.com/Yashlol'  # replace with your GitHub URL
    }
    return render(request, 'App_43_3/resume.html', resume_data)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Process the form submission here
        
        return HttpResponse("Thank you for your message!")
    
    return render(request, 'App_43_3/contact.html')
