
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import AnonymousPost, PostReport


def home(request):
    if request.method == 'POST':
        message = request.POST.get('message', '').strip()

        if not message:
            messages.error(request, 'Please write your confession first.')
        elif len(message) > 1000:
            messages.error(request, 'Maximum of 1000 characters only.')
        else:
            AnonymousPost.objects.create(
                category='CONFESSION',
                message=message,
                status='PENDING'
            )
            messages.success(
                request,
                'Your confession has been submitted for review!'
            )
            return redirect('home')

    return render(request, 'confessions/home.html')


def community_wall(request):
    posts = AnonymousPost.objects.filter(
        status='APPROVED'
    ).order_by('-created_at')

    return render(request, 'confessions/wall.html', {
        'posts': posts
    })


def report_post(request, post_id):
    post = get_object_or_404(
        AnonymousPost,
        id=post_id,
        status='APPROVED'
    )

    if request.method == 'POST':
        reason = request.POST.get('reason', '').strip()

        allowed_reasons = [
            'Harassment or bullying',
            'Inappropriate content',
            'Personal information',
            'Threats or harmful content',
            'Other'
        ]

        if reason in allowed_reasons:
            PostReport.objects.create(
                post=post,
                reason=reason
            )
            messages.success(
                request,
                'Report submitted. Thank you for helping keep our community safe!'
            )
        else:
            messages.error(request, 'Please select a valid report reason.')

    return redirect('community_wall')
