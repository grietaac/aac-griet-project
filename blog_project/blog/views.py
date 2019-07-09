from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.shortcuts import redirect
from blog.forms import CommentForm
# Create your views here.
def post_list_view(request):
    post_list=Post.objects.all()
    return render(request,'blog/post_list.html',{'post_list':post_list})
def thanks_view(request):
    return render(request,'blog/thanks.html')
def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            csubmit=True
            return redirect('http://127.0.0.1:8000/thanks')

    else:
        form=CommentForm()
    return render(request,'blog/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})
