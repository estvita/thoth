from django.shortcuts import redirect, render, get_object_or_404

from thoth.bitrix.models import AppInstance, Line, Connector
import thoth.bitrix.utils as bitrix_utils

from .models import OlxApp, OlxUser
from thoth.decorators import login_message_required

@login_message_required(code="olx")
def olx_accounts(request):
    connector_service = "olx"
    connector = Connector.objects.filter(service=connector_service).first()
    olx_accounts = OlxUser.objects.filter(owner=request.user)
    instances = AppInstance.objects.filter(owner=request.user, app__connectors=connector)
    olx_lines = Line.objects.filter(connector=connector, owner=request.user)

    olx_apps = OlxApp.objects.all()

    if request.method == "POST":
        action = request.POST.get("action")

        if action == "connect":
            olx_app_id = request.POST.get("olx_app")
            olx_app = OlxApp.objects.get(id=olx_app_id)
            return render(request, "olx/redirect_page.html", {"auth_link": olx_app.authorization_link})
        else:
            olx_id = request.POST.get("olx_id")
            line_id = request.POST.get("line_id")
            olx_user = get_object_or_404(OlxUser, id=olx_id, owner=request.user)

            bitrix_utils.connect_line(request, line_id, olx_user, connector, "olx-accounts")

    return render(request, "olx/accounts.html", 
        {
            "olx_accounts": olx_accounts,
            "olx_apps": olx_apps,
            "instances": instances,
            "olx_lines": olx_lines,
        }
    )