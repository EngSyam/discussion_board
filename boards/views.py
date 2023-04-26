from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
# Create your views here.
from  .models import Board
from  .models import Topic,Post

def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})
    """
    boards_names = []
    for board in boards :
        boards_names.append(board.name)
        boards_names.append(board.description)
    response_html = '<br>'.join(boards_names)
    return HttpResponse(response_html)
    """

def about(request):
    return HttpResponse(request,'yes')

def board_topics(request,board_id):
    #try:
    #    board = Board.objects.get(pk=board_id)
    #    print(board)
    #except Board.DoesNotExist:
    #    raise Http404
    board = get_object_or_404(Board,pk=board_id)
    topics = board.topics.all()
    return render(request,'topics.html',{'board':board,'topics':topics})

def new_topic(request,board_id):
    board = get_object_or_404(Board,pk=board_id)
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user    = User.objects.first()

        topic = Topic.objects.create(
            subject    = subject,
            board      = board,
            created_by = user
        )

        post = Post.objects.create(
            message    = message,
            topic      = topic,
            created_by = user
        )
        return redirect('board_topics', board_id=board.pk)
    return render(request,'new_topic.html',{'board':board})