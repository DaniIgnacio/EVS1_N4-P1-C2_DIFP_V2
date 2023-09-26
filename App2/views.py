from django.shortcuts import render
from django.http import HttpResponse

def app2Vista3(request):
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
                background-color: brown;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Aplicacion 2</h1>
            <p>vista 3</p>
    
            <li>Vista tres creada en la rama 2</li>
            <li>Django</li>
            
        </div>
    </body>
    """
    return HttpResponse(html)


def app2Vista4(request):
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
                background-color: blue;
                display: flex;
                flex-direction: column;
                justify-content: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Aplicacion 2</h1>
            <p>vista 4</p>
    
            <li>Vista cuatro creada en la rama 2</li>
            <li>Django</li>
            
        </div>
    </body>
    """
    return HttpResponse(html)