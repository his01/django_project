from django.shortcuts import render

def ai_pg(request):
    return render(request, "ai_pg/ai_pg.html")

def ai_tool_guide(request):
    return render(request, 'ai_pg/ai_tool_guide.html')

def ai_sld(request):
    return render(request, 'ai_pg/ai_sld.html')

def ai_pjrv(request):
    return render(request, 'ai_pg/ai_pjrv.html')

