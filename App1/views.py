from django.shortcuts import render
from django.http import HttpResponse

def app1Vista1(request):
    html = """
    <head>
        <style>
            body, html {
                height: 100%;
                margin: 0;
                color: white;
            }
            .container {
                width: 80%;
                height: 50%;
                margin: auto;
                position: absolute;
                top: 0;
                bottom: 0;
                left: 0;
                right: 0;
                text-align: center;
                background-color: #202060;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Aplicacion 1</h1>
            <p>vista 1</p>
    
            <li>Vista uno creada en la rama 1</li>
            <li>Django</li>
            
        </div>
    </body>
    """
    return HttpResponse(html)


def app1Vista2(request):
    html = """
    <head>
        <style>
            body, html {
                height: 100%;
                margin: 0;
                color: white;
            }
            .container {
                width: 80%;
                height: 50%;
                margin: auto;
                position: absolute;
                top: 0;
                bottom: 0;
                left: 0;
                right: 0;
                text-align: center;
                background-color: black;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Aplicacion 1</h1>
            <p>vista 2</p>
    
            <li>Vista dos creada en la rama 1</li>
            <li>Django</li>
            
        </div>
    </body>
    """
    return HttpResponse(html)
