from django.shortcuts import redirect, render
from lists.models import Item


def home_page(request):
    if request.method == "POST":
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/")

    items = Item.objects.all()
    return render(request, "home.html", {"items": items})


# def new_list(request):
#     nulist = List.objects.create()
#     Item.objects.create(text=request.POST["item_text"], list=nulist)
#     return redirect(f"/lists/{nulist.id}/")


# def view_list(request, list_id):
#     our_list = List.objects.get(id=list_id)
#     return render(request, "list.html", {"list": our_list})


# def add_item(request, list_id):
#     our_list = List.objects.get(id=list_id)
#     Item.objects.create(text=request.POST["item_text"], list=our_list)
#     return redirect(f"/lists/{our_list.id}/")
