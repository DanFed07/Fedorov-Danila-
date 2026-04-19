from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import News, Article, Comment
from .forms import RegisterForm, LoginForm, CommentForm, NewsForm, ArticleForm


def index(request):
    latest_news = News.objects.all()[:3]
    top_articles = Article.objects.all().order_by('-views_count')[:10]
    return render(request, 'blog/index.html', {
        'latest_news': latest_news,
        'top_articles': top_articles,
    })


def article_list(request):
    articles = Article.objects.all().order_by('-created_date')
    search_query = request.GET.get('search', '')
    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )
    paginator = Paginator(articles, 12)
    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request, 'blog/article.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.views_count += 1
    article.save()
    comments = article.comments.filter(is_approved=True)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            messages.success(request, 'Комментарий добавлен!')
            return redirect('blog:article_detail', article_id=article.id)
    else:
        form = CommentForm()

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })


def news_list(request):
    news_queryset = News.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        news_queryset = news_queryset.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query)
        )

    sort_order = request.GET.get('sort', 'desc')
    if sort_order == 'asc':
        news_queryset = news_queryset.order_by('published_date')
    else:
        news_queryset = news_queryset.order_by('-published_date')

    main_news = news_queryset.filter(is_main=True).first()
    other_news = news_queryset.exclude(id=main_news.id if main_news else None)

    return render(request, 'blog/news.html', {
        'news_large': main_news,
        'news_small_top': other_news.first(),
        'news_small_bottom': other_news[1] if len(other_news) > 1 else None,
        'news_wide': other_news[2] if len(other_news) > 2 else None,
        'all_news': other_news[3:] if len(other_news) > 3 else [],
        'search_query': search_query,
        'sort_order': sort_order,
    })


def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    comments = news.comments.filter(is_approved=True)

    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news = news
            comment.author = request.user
            comment.save()
            messages.success(request, 'Комментарий добавлен!')
            return redirect('blog:news_detail', news_id=news.id)
    else:
        form = CommentForm()

    return render(request, 'blog/news_detail.html', {
        'news': news,
        'comments': comments,
        'form': form,
    })


def about(request):
    return render(request, 'blog/about.html')


def connection(request):
    return render(request, 'blog/connection.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['name']
            user.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна!')
            return redirect('blog:index')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegisterForm()
    return render(request, 'blog/sign.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {user.username}!')
                return redirect('blog:index')
            else:
                messages.error(request, 'Неверные данные')
    else:
        form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы')
    return redirect('blog:index')


@login_required
def profile(request):
    user_comments = Comment.objects.filter(author=request.user)
    user_articles = Article.objects.filter(author=request.user)
    return render(request, 'blog/profile.html', {
        'user_comments': user_comments,
        'user_articles': user_articles,
    })


def is_staff_or_admin(user):
    return user.is_authenticated and (user.is_staff or user.is_superuser)


# ============ НОВОСТИ (только для персонала) ============
@user_passes_test(is_staff_or_admin)
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            messages.success(request, 'Новость создана!')
            return redirect('blog:news_detail', news_id=news.id)
    else:
        form = NewsForm()
    return render(request, 'blog/news_form.html', {'form': form, 'title': 'Создать новость'})


@user_passes_test(is_staff_or_admin)
def edit_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            messages.success(request, 'Новость обновлена!')
            return redirect('blog:news_detail', news_id=news.id)
    else:
        form = NewsForm(instance=news)
    return render(request, 'blog/news_form.html', {'form': form, 'title': 'Редактировать новость'})


@user_passes_test(is_staff_or_admin)
def delete_news(request, news_id):
    news = get_object_or_404(News, id=news_id)
    if request.method == 'POST':
        news.delete()
        messages.success(request, 'Новость удалена!')
        return redirect('blog:news_list')
    return render(request, 'blog/news_confirm_delete.html', {'news': news})


# ============ СТАТЬИ (для всех авторизованных пользователей) ============
@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, 'Статья успешно создана!')
            return redirect('blog:article_detail', article_id=article.id)
    else:
        form = ArticleForm()
    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Создать статью'})


@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    # Проверяем, что пользователь - автор статьи или админ
    if request.user != article.author and not request.user.is_staff:
        messages.error(request, 'Вы не можете редактировать эту статью')
        return redirect('blog:article_detail', article_id=article.id)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статья обновлена!')
            return redirect('blog:article_detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Редактировать статью'})


# ============ ПОИСК ============
def search(request):
    query = request.GET.get('q', '')
    news_results = News.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    article_results = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'blog/search_results.html', {
        'query': query,
        'news_results': news_results,
        'article_results': article_results,
    })