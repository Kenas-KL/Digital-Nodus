import hashlib


import requests
import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import (
    Member,
    Reservation, 
    Event,
    SocialProofComment,
    OpenSourceProject, 
    Support,
    LinkGroupDigitalNodus
)


def generer_hash_court(nombre):
    hash_obj = hashlib.sha256(str(nombre).encode())
    return hash_obj.hexdigest()[:8].upper()


def index(request):
    reservations = Member.objects.all()
    social_proof_comments = SocialProofComment.objects.all()
    nbr_open_source_projects = OpenSourceProject.objects.all()
    supports = Support.objects.all()
    events = Event.objects.order_by('created_at')[:5]


    return render(
        request, 
        template_name="index.html",
        context={
            "res_len": len(reservations),
            "members": social_proof_comments,
            "nbr_open_source_projects": len(nbr_open_source_projects),
            "support": supports,
            "events": events
        }
    )

def list_events(request):
    events = Event.objects.all()
    return render(request, context={"events": events}, template_name="list_events.html")

def detail_event(request, pk: int):
    event = Event.objects.get(pk=pk)
    if request.method == "POST":
        names = request.POST.get('all_names')
        email = request.POST.get('email')
        whatsapp_number = str(request.POST.get('whatsapp_number'))
        profession = request.POST.get('profession')
        sex = request.POST.get('sex')

        whatsapp_number = whatsapp_number.strip().replace(" ","")
        participant =  Reservation.objects.filter(event=event, email=email)
        print(participant)
        if participant:
            send_whatsapp_msg(names, whatsapp_number, f"""
                              Ceci est votre ticket 

                              |
                              *SESSION : {event.name}*
                              *ID :  {generer_hash_court(participant[0].pk)}* 
                              |
                              Présente ce ticket en message (capture d'écran) à l'entrée de la session.
            """)

            return render(
                request,          
                context={
                    "participants": Reservation.objects.filter(event=pk),
                    "participant": participant,
                    "event": event}, template_name="success.html")
            
        if names and whatsapp_number and profession and sex :
            participant = Reservation.objects.create(
                event = event,
                all_names=names,
                email=email, 
                whatsapp_number = whatsapp_number,
                profession=profession or "-",
                sex = "M" if sex == "Sexe: Masculin" else "F",
            )

            send_whatsapp_msg(names, whatsapp_number, f"""
                              Ceci est votre ticket 

                              |
                              *SESSION : {event.name}*
                              *ID_TICKET:  {hex(participant.pk)}* 
                              |
                              Présente ce ticket en message (capture d'écran) à l'entrée de la session.
            """)

            return render(
                request,          
                context={
                    "participants": Reservation.objects.filter(event=pk),
                    "participant": participant,
                    "event": event
                }, template_name="success.html")
    reservation_count = event.places_event - Reservation.objects.filter(event=pk).count()
    return render(request, context={"event": event, "rest_reservation":reservation_count}, template_name="detail_event.html")


def send_whatsapp_msg(names, whatsapp_number, msg):
    url = "https://api.ultramsg.com/instance157054/messages/chat"


    if whatsapp_number.startswith("+243"):
        whatsapp_number.removeprefix("+243")
    elif whatsapp_number.startswith("243"):
        whatsapp_number.removeprefix("243")
    elif whatsapp_number.startswith("0"):
        whatsapp_number.removeprefix("0")

    whatsapp_number = whatsapp_number.strip().replace(" ","")

    link_group = LinkGroupDigitalNodus.objects.last()

    payload = json.dumps({
        "token": "aghjscgv5w67s5wz",
        "to": f"+243{whatsapp_number}",
        "body": f"""
        > *{names}* ! \n{msg} 🚀\n Utilisez ce lien pour integrer le groupe de la communauté : {link_group.link}
        """,
        "priority": 1,
        "referenceId": "",
        "msgId": "",
        "mentions": ""
    })
    headers = {
    'Content-Type': 'application/json'
    }
    try:
        requests.request("POST", url, headers=headers, data=payload)
    except:
        pass
    return JsonResponse({"status": "ok"})



def about(request):

    return render(request, template_name="about.html", context={"members": Member.objects.all().count()})

def register(request):
    if request.method == "POST":
        names = request.POST.get('all_names')
        email = request.POST.get('email')
        whatsapp_number = str(request.POST.get('whatsapp_number'))
        profession = request.POST.get('profession')
        sex = request.POST.get('sex')
        institution = request.POST.get('institution')
        reason = request.POST.get('reason')
        
        if names and whatsapp_number and profession and sex and institution :

            Member.objects.create(
                all_names=names,
                email=email, 
                whatsapp_number = whatsapp_number,
                profession=profession,
                sex = "M" if sex == "M" else "F",
                institution = institution,
                reason = reason
            )
            try:
                send_whatsapp_msg(names, whatsapp_number, """
                                  Bienvenue dans la communauté Tech de Kalemie.
                                  Ton inscription a été validée avec succès.
                """)
            except:
                pass
            return JsonResponse({"status": "ok"})
            
    return JsonResponse({"status": "error"}, status=400)


