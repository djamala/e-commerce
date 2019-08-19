from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.generic import ListView, DetailView, View
from .forms import RegisterForm, LoginForm
from core.models import  Category, Item, Brand, OrderItem, Order


class HomeView(ListView):
    context_object_name = "last_items"
    template_name = "index.html"
    queryset = Item.objects.filter(status=True)[:6]

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(HomeView, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories ou le status egale true
        context['brands'] = Brand.objects.filter(status=True)
        context['categorys'] = Category.objects.filter(status=True)
        return context



class CategoryItemList(ListView):
    model = Item
    template_name = "article.html"
    context_object_name = "items"
    paginate_by = 12

    def get_queryset(self):
        return Item.objects.filter(category__id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(CategoryItemList, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories ou le status egale true
        context['brands'] = Brand.objects.filter(status=True)
        context['categorys'] = Category.objects.filter(status=True)
        return context


class ArticleDetailView(DetailView):
    context_object_name = "item"
    model = Item
    template_name = "product-details.html"

    def get_context_data(self, **kwargs):
        # Nous récupérons le contexte depuis la super-classe
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        # Nous ajoutons la liste des catégories ou le status egale true
        context['categorys'] = Category.objects.filter(status=True)
        context['brands'] = Brand.objects.filter(status=True)
        return context



#add item from cart
@login_required(login_url='/login/', redirect_field_name = 'next')
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            print("This item quantity was updated.")
            return redirect("index")
        else:
            order.items.add(order_item)
            print("This item was added to your cart.")
            return redirect("index")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        print("This item was added to your cart.")
        return redirect("index")



#remove item from cart
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            print("This item was removed from your cart.")
            return redirect("cart-summary-view")
        else:
            print("This item was not in your cart")
            return redirect("article-detail", slug=slug)
    else:
        print("You do not have an active order")
        return redirect("article-detail", slug=slug)



def login(request):
    context = { 'rgfrm':RegisterForm(), 'lgfrm':LoginForm() }
    return render(request, 'login.html', context)

@login_required(login_url='/login/', redirect_field_name = 'next')
def user_log_out(request):
    logout(request)
    redirect("index")



def user_register(request):
    if request.method =='POST':
        rgfrm = RegisterForm(request.POST)

        if rgfrm.is_valid():
            username = rgfrm.cleaned_data['username']
            email = rgfrm.cleaned_data['email']
            password = rgfrm.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            print("Votre compte a été creer avec succéss")

            context = {'rgfrm': RegisterForm(), 'lgfrm': LoginForm}
            return render(request, 'login.html', context)

        else:
            context = {'rgfrm': RegisterForm(), 'lgfrm': LoginForm}
            return render(request, 'login.html', context)

    else:
        context = { 'rgfrm': RegisterForm(), 'lgfrm': LoginForm }
    return render(request, 'login.html', context)



def user_login(request):
    if request.method == 'POST':
        form1 = LoginForm(request.POST)
        if form1.is_valid():
            username = form1.cleaned_data['username']
            password = form1.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
            else:
                print("Username or password invalid !")
                context = {'rgfrm': RegisterForm(), 'lgfrm': LoginForm}
                return render(request, 'login.html', context)
    else:
        context = {'rgfrm': RegisterForm(), 'lgfrm': LoginForm}
    return render(request, 'login.html', context)



class CartSummaryView(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'next'

    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            print("You do not have an active order")
            return redirect("index")


#remove single item from cart
@login_required(login_url='/login/', redirect_field_name = 'next')
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            print("This item quantity was updated.")
            return redirect("cart-summary-view")
        else:
            print("This item was not in your cart")
            return redirect("article-detail", slug=slug)
    else:
        print("You do not have an active order")
        return redirect("article-detail", slug=slug)


#add single item from cart
@login_required(login_url='/login/', redirect_field_name = 'next')
def add_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            print("This item quantity was updated.")
            return redirect("cart-summary-view")
        else:
            order.items.add(order_item)
            print("This item was added to your cart.")
            return redirect("article-detail")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        print("This item was added to your cart.")
        return redirect("article-detail")


def checkout(request):
    return render(request, 'checkout.html')


# @login_required(login_url='/login/', redirect_field_name = 'next')
# def cart(request):
#     return render(request, 'cart.html')



def blog_single(request):
    return render(request, 'blog-single.html')



def blog(request):
    return render(request, 'blog.html')



def page_not_found(request):
    return render(request, '404.html')

def contact_us(request):
    return render(request, 'contact-us.html')



def shop(request):
    return render(request, 'shop.html')



def product_details(request):
    return render(request, 'product-details.html')


