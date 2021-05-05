from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post
import requests
import json
import xmltodict as xmltodict
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def index(request):
    url = "https://api.flyallover.com/api/sitemap/sitemap.xml/support?WSDL"

    response = requests.get(url)

    decoded_response = response.content.decode('utf-8')
    response_json = json.loads(json.dumps(xmltodict.parse(decoded_response)))
    location_urls = response_json['urlset']['url']
    context = {
        'locations': location_urls
    }

    return render(request, 'index.html', context)

def getPosts(request):
    pass
    all_posts = Post.objects.all()
    response = """<?xml version="1.0"?>

                   <soap:Envelope
                   xmlns:soap="http://www.w3.org/2003/05/soap-envelope/"
                   soap:encodingStyle="http://www.w3.org/2003/05/soap-encoding">

                   <soap:Body>
                     <m:GetPostsResponse>
                """

    for post in all_posts:
        response += post.serialize()

    response += """   </m:GetPostsResponse>
                    </soap:Body>
                   </soap:Envelope> 
                """
    soup = BeautifulSoup(response, "xml")
    return HttpResponse(soup, content_type='text/xml')