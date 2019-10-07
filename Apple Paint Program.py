#Johnny Fung

import pygame
from pygame import *
from random import *

#-------------------------------- Get File Name ------------------------------------

def getName():
    ans = ""
    arialFont = font.SysFont("Helvetica", 20, "bold")
    back = screen.copy()
    textArea = Rect(845,232,147,25)
    
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode
                    
        txtPic = arialFont.render(ans, True, (255,255,255))
        draw.rect(screen,(103,148,225),textArea)
        draw.rect(screen,(32,99,215),textArea,2)
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans
font.init()
#----------------------------------Screen Setup-------------------------------------
screen=display.set_mode((1000,730))
pygame.display.set_caption("Johnny's Apple Themed Paint Program")
background = image.load("images/background.png") 
screen.blit(background,(0,0))
canvasRect=Rect(378,94,406,541)
draw.rect(screen,(255,255,255),canvasRect,0)
palette1 = image.load("images/background/colorchart.png")
screen.blit(palette1,(193,555))
palette1Rect = Rect(193,555,101,150)
palette2 = image.load("images/background/colorwheel.png")
screen.blit(palette2,(18,558))
colourindicator = image.load("images/background/indicatorempty.png")
pencilTool = image.load("images/tools/penciloff.jpg") 
pencilRect =  Rect(63,117,46,38)
pencilonRect = image.load("images/tools/pencilon.jpg")
pencilselectedRect = image.load("images/tools/pencilselected.jpg")
eraserTool = image.load("images/tools/eraseroff.jpg") 
eraserRect =  Rect(63,175,46,38)
eraseronRect = image.load("images/tools/eraseron.jpg")
eraserselectedRect = image.load("images/tools/eraserselected.jpg")
spraycanTool = image.load("images/tools/spraycanoff.jpg") 
spraycanRect =  Rect(63,233,46,38)
spraycanonRect = image.load("images/tools/spraycanon.jpg")
spraycanselectedRect = image.load("images/tools/spraycanselected.jpg")
brushTool = image.load("images/tools/brushoff.jpg") 
brushRect =  Rect(63,289,46,38)
brushonRect = image.load("images/tools/brushon.jpg")
brushselectedRect = image.load("images/tools/brushselected.jpg")
eyedropperTool = image.load("images/tools/eyedropperoff.jpg") 
eyedropperRect =  Rect(63,345,46,37)
eyedropperonRect = image.load("images/tools/eyedropperon.jpg")
eyedropperselectedRect = image.load("images/tools/eyedropperselected.jpg")
fillTool = image.load("images/tools/filloff.jpg") 
fillRect = Rect(126,118,46,38)
fillonRect = image.load("images/tools/fillon.jpg")
fillselectedRect = image.load("images/tools/fillselected.jpg")
drawlineTool = image.load("images/tools/drawlineoff.jpg") 
drawlineRect = Rect(63,402,44,36)
drawlineonRect = image.load("images/tools/drawlineon.jpg")
drawlineselectedRect = image.load("images/tools/drawlineselected.jpg")
drawrectTool = image.load("images/tools/drawrectoff.jpg") 
drawrectRect = Rect(63,462,21,32)
drawrectonRect = image.load("images/tools/drawrecton.jpg")
drawrectselectedRect = image.load("images/tools/drawrectselected.jpg")
drawrectfilledTool = image.load("images/tools/drawrectfilledoff.jpg") 
drawrectfilledRect = Rect(87,462,21,32)
drawrectfilledonRect = image.load("images/tools/drawrectfilledon.jpg")
drawrectfilledselectedRect = image.load("images/tools/drawrectfilledselected.jpg")
drawellipseTool = image.load("images/tools/draweclipseoff.jpg") 
drawellipseRect = Rect(63,516,21,32)
drawellipseonRect = image.load("images/tools/draweclipseon.jpg")
drawellipseselectedRect = image.load("images/tools/draweclipseselected.jpg")
drawellipsefilledTool = image.load("images/tools/draweclipsefilledoff.jpg") 
drawellipsefilledRect = Rect(87,516,21,32)
drawellipsefilledonRect = image.load("images/tools/draweclipsefilledon.jpg")
drawellipsefilledselectedRect = image.load("images/tools/draweclipsefilledselected.jpg")
stampTool = image.load("images/tools/stampoff.jpg") 
stampRect = Rect(222,118,50,39)
stamponRect = image.load("images/tools/stampon.jpg")
stampselectedRect = image.load("images/tools/stampselected.jpg")
landscape1tool = image.load("images/tools/landscape 1 tool.png")
landscape1Rect = Rect(199,437,38,51)
landscape1onRect = image.load("images/tools/landscape 1 toolon.png")
landscape2tool = image.load("images/tools/landscape 2 tool.png")
landscape2Rect = Rect(257,437,38,51)
landscape2onRect = image.load("images/tools/landscape 2 toolon.png")
landscape3Tool = image.load("images/tools/landscape 3 tool.png")
landscape3Rect = Rect(199,498,38,51)
landscape3onRect = image.load("images/tools/landscape 3 toolon.png")
landscape4tool = image.load("images/tools/landscape 4 tool.png")
landscape4Rect = Rect(257,498,38,51)
landscape4onRect = image.load("images/tools/landscape 4 toolon.png")
appstoreTool = image.load("images/tools/appstore tool.png")
appstoreRect = Rect(199,165,38,38)
appstoreonRect = image.load("images/tools/appstore toolon.png")
cameraTool = image.load("images/tools/camera tool.png")
cameraRect = Rect(257,166,38,38)
cameraonRect = image.load("images/tools/camera toolon.png")
facebookTool = image.load("images/tools/facebook tool.png")
facebookRect = Rect(199,209,38,38)
facebookonRect = image.load("images/tools/facebook toolon.png")
notesTool = image.load("images/tools/notes tool.png")
notesRect = Rect(257,210,38,38)
notesonRect = image.load("images/tools/notes toolon.png")
safariTool = image.load("images/tools/safari tool.png")
safariRect = Rect(199,254,38,38)
safarionRect = image.load("images/tools/safari toolon.png")
settingsTool = image.load("images/tools/settings tool.png")
settingsRect = Rect(257,254,38,38)
settingsonRect = image.load("images/tools/settings toolon.png")
stocksTool = image.load("images/tools/stocks tool.png")
stocksRect = Rect(199,300,38,38)
stocksonRect = image.load("images/tools/stocks toolon.png")
youtubeTool = image.load("images/tools/youtube tool.png")
youtubeRect = Rect(257,299,38,38)
youtubeonRect = image.load("images/tools/youtube toolon.png")
ipodTool = image.load("images/tools/ipod tool.png")
ipodRect = Rect(257,343,38,38)
ipodonRect = image.load("images/tools/ipod toolon.png")
weatherTool = image.load("images/tools/weather tool.png")
weatherRect = Rect(199,344,38,38)
weatheronRect = image.load("images/tools/weather toolon.png")
mailTool = image.load("images/tools/mail tool.png")
mailRect = Rect(199,391,38,38)
mailonRect = image.load("images/tools/mail toolon.png")
cydiaTool = image.load("images/tools/cydia tool.png")
cydiaRect = Rect(257,390,38,38)
cydiaonRect = image.load("images/tools/cydia toolon.png")
landscape1toolSELECTED = image.load("images/tools/landscape 1 toolSELECTED.png")
landscape2toolSELECTED = image.load("images/tools/landscape 2 toolSELECTED.png")
landscape3toolSELECTED = image.load("images/tools/landscape 3 toolSELECTED.png")
landscape4toolSELECTED = image.load("images/tools/landscape 4 toolSELECTED.png")
appstoreToolSELECTED = image.load("images/tools/appstore toolSELECTED.png")
cameraToolSELECTED = image.load("images/tools/camera toolSELECTED.png")
facebookToolSELECTED = image.load("images/tools/facebook toolSELECTED.png")
notesToolSELECTED = image.load("images/tools/notes toolSELECTED.png")
safariToolSELECTED = image.load("images/tools/safari toolSELECTED.png")
settingsToolSELECTED = image.load("images/tools/settings toolSELECTED.png")
stocksToolSELECTED = image.load("images/tools/stocks toolSELECTED.png")
youtubeToolSELECTED = image.load("images/tools/youtube toolSELECTED.png")
ipodToolSELECTED = image.load("images/tools/ipod toolSELECTED.png")
weatherToolSELECTED = image.load("images/tools/weather toolSELECTED.png")
mailToolSELECTED = image.load("images/tools/mail toolSELECTED.png")
cydiaToolSELECTED = image.load("images/tools/cydia toolSELECTED.png")
saveTool = image.load("images/tools/save.png")
screen.blit(saveTool,(860,35))
saveRect = Rect(860,35,116,73)
savetoolon = image.load("images/tools/saveON.png")
savetoolselected = image.load("images/tools/saveSELECTED.png")
loadTool = image.load("images/tools/load.png")
screen.blit(loadTool,(860,108))
loadRect = Rect(860,108,116,73)
loadtoolon = image.load("images/tools/loadON.png")
loadtoolselected = image.load("images/tools/loadSELECTED.png")
undoTool = image.load("images/tools/undo.png")
screen.blit(undoTool,(846,184))
undoRect = Rect(846,188,70,45)
undotoolon = image.load("images/tools/undoON.png")
undotoolselected = image.load("images/tools/undoSELECTED.png")
redoTool = image.load("images/tools/redo.png")
screen.blit(redoTool,(921,184))
redoRect = Rect(921,188,70,45)
redotoolon = image.load("images/tools/redoON.png")
redotoolselected = image.load("images/tools/redoSELECTED.png")
clearTool = image.load("images/tools/clear.png")
screen.blit(clearTool,(860,254))
clearRect = Rect(860,254,116,73)
cleartoolon = image.load("images/tools/clearON.png")
cleartoolselected = image.load("images/tools/clearSELECTED.png")
descblocker = image.load("images/descriptions/description blocker.png")
pencildesc = image.load("images/descriptions/pencil.png")
brushdesc = image.load("images/descriptions/brush.png")
ellipsefilleddesc = image.load("images/descriptions/ellipse filled.png")
ellipsedesc = image.load("images/descriptions/ellipse.png")
eraserdesc = image.load("images/descriptions/eraser.png")
eyedropperdesc = image.load("images/descriptions/eyedropper.png")
filldesc = image.load("images/descriptions/fill.png")
floodfilldesc = image.load("images/descriptions/flood fill.png")
linedesc = image.load("images/descriptions/line.png")
rectfilleddesc = image.load("images/descriptions/rect filled.png")
rectdesc = image.load("images/descriptions/rect.png")
scrolldesc = image.load("images/descriptions/scroll.png")
stampdesc = image.load("images/descriptions/stamp.png")
spraydesc = image.load("images/descriptions/spray.png")
savedesc = image.load("images/descriptions/save.png")
loaddesc = image.load("images/descriptions/load.png")

#------------------------------------Stamp Images-------------------------------
landscape1 = image.load("images/stamps/landscape 1.png")
landscape2 = image.load("images/stamps/landscape 2.png")
landscape3 = image.load("images/stamps/landscape 3.png")
landscape4 = image.load("images/stamps/landscape 4.png")
appstore = image.load("images/stamps/appstore.png")
camera = image.load("images/stamps/camera.png")
cydia = image.load("images/stamps/cydia.png")
facebook = image.load("images/stamps/facebook.png")
ipod = image.load("images/stamps/ipod.png")
mail = image.load("images/stamps/mail.png")
notes = image.load("images/stamps/notes.png")
safari = image.load("images/stamps/safari.png")
settings = image.load("images/stamps/settings.png")
stocks = image.load("images/stamps/stocks.png")
weather = image.load("images/stamps/weather.png")
youtube = image.load("images/stamps/youtube.png")
stampblocker = image.load("images/stamp blocker.png")

testRect=Rect(132,472,40,40)
#--------------------------------------Music-------------------------------------
init()
mixer.music.load("sounds/MacStartUp.mp3")
mixer.music.play()

tools="pencil"
stamp=[]
undolist=[]
redolist=[]
scroll=True
colour=(0,0,0)
size=1
#gets the width of the image
cw = appstore.get_width()
ch = appstore.get_height()
mx=0
my=0
mb1=0
mb=0
running = True
#appends the copied pictures into a list
undolist.append(screen.subsurface(canvasRect).copy())

while running:
    if scroll==True:
        screen.blit(scrolldesc,(844,324))
    for evt in event.get():
        if evt.type == QUIT:
            running=False
        if evt.type == MOUSEBUTTONDOWN:
            screenback = screen.copy()
            #copies the canvas
            canvascopy=screen.subsurface(canvasRect).copy()
            mx2,my2=evt.pos
            start=evt.pos
            scroll=False
            if evt.button == 1:
                if undoRect.collidepoint(mx,my) and len(undolist) > 1:
                    #when you click the undo button, it adds a new frame to the list
                    redolist.append(undolist[-1])
                    undolist = undolist[:-1]
                    screen.blit(undolist[-1],(378,94))    
                if redoRect.collidepoint(mx,my) and len(redolist) > 0:
                    undolist.append(redolist[-1])
                    redolist = redolist[:-1]
                    screen.blit(undolist[-1],(378,94))
            if evt.button == 4:
               size+=1
            if evt.button == 5:
                size-=1
            if size <=1:
                size=1
            if size >=20:
                size=20
               
        if evt.type == MOUSEBUTTONUP:
            screenback = screen.copy()
            screen.blit(screenback, (0,0))
            if evt.button == 1:
                if canvasRect.collidepoint(mx,my) and evt.button == 1: 
                    undolist.append(screen.subsurface(canvasRect).copy())
        if evt.type == KEYDOWN:
            scroll=False
                    
    mx1=mx
    my1=my
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    mb1=mb
    #used for brush sizes
    length = (((mx1-mx)**2+(my1-my)** 2))**0.5

#-------------------------When the mouse is not on the tool icon----------------
    screen.blit(pencilTool,(63,118))
    screen.blit(eraserTool,(63,175))
    screen.blit(spraycanTool,(63,233))
    screen.blit(brushTool,(63,289))
    screen.blit(eyedropperTool,(63,345))
    screen.blit(fillTool,(126,118))
    screen.blit(drawlineTool,(63,402))
    screen.blit(drawrectTool,(63,462))
    screen.blit(drawrectfilledTool,(87,462))
    screen.blit(drawellipseTool,(63,516))
    screen.blit(drawellipsefilledTool,(87,516))
    screen.blit(stampTool,(222,118))
    if tools=="stamp":
        screen.blit(landscape1tool,(199,437))
        screen.blit(landscape2tool,(254,437))
        screen.blit(landscape3Tool,(199,498))
        screen.blit(landscape4tool,(257,498))
        screen.blit(appstoreTool,(199,165))
        screen.blit(cameraTool,(257,166))
        screen.blit(facebookTool,(199,209))
        screen.blit(notesTool,(257,210))
        screen.blit(safariTool,(199,254))
        screen.blit(settingsTool,(257,254))
        screen.blit(stocksTool,(199,300))
        screen.blit(youtubeTool,(257,299))
        screen.blit(ipodTool,(257,343))
        screen.blit(weatherTool,(199,344))
        screen.blit(mailTool,(199,391))
        screen.blit(cydiaTool,(257,390))
    screen.blit(saveTool,(860,35))
    screen.blit(loadTool,(860,108))
    screen.blit(undoTool,(846,184))
    screen.blit(redoTool,(921,184))
    screen.blit(clearTool,(860,254))
    if scroll==False:
        screen.blit(descblocker,(837,321))
    
#------Used to give the user feedback as to the mouse being on which stamp--------

    if landscape1Rect.collidepoint(mx,my):
        screen.blit(landscape1onRect,(199,437))
    if landscape2Rect.collidepoint(mx,my):
        screen.blit(landscape2onRect,(257,437))
    if landscape3Rect.collidepoint(mx,my):
        screen.blit(landscape3onRect,(199,498))        
    if landscape4Rect.collidepoint(mx,my):
        screen.blit(landscape4onRect,(257,498))    
    if appstoreRect.collidepoint(mx,my):
        screen.blit(appstoreonRect,(199,165))
    if cameraRect.collidepoint(mx,my):
        screen.blit(cameraonRect,(257,166))
    if facebookRect.collidepoint(mx,my):
        screen.blit(facebookonRect,(199,209))
    if notesRect.collidepoint(mx,my):
        screen.blit(notesonRect,(257,210))
    if safariRect.collidepoint(mx,my):
        screen.blit(safarionRect,(199,254))
    if settingsRect.collidepoint(mx,my):
        screen.blit(settingsonRect,(257,254))
    if stocksRect.collidepoint(mx,my):
        screen.blit(stocksonRect,(199,300))       
    if youtubeRect.collidepoint(mx,my):
        screen.blit(youtubeonRect,(257,299))
    if ipodRect.collidepoint(mx,my):
        screen.blit(ipodonRect,(257,343))
    if weatherRect.collidepoint(mx,my):
        screen.blit(weatheronRect,(199,344))
    if mailRect.collidepoint(mx,my):
        screen.blit(mailonRect,(199,391))
    if cydiaRect.collidepoint(mx,my):
        screen.blit(cydiaonRect,(257,390))
    if clearRect.collidepoint(mx,my):   
        screen.blit(cleartoolon,(860,254))

#------------------------------------Colour branch--------------------------------

    if mb[0]==1:
        if palette1Rect.collidepoint(mx,my):
            colour = screen.get_at((mx,my))            
        if ((89-mx)**2+(629-my)**2)**0.5 <= 70:
            colour = screen.get_at((mx,my))            
        draw.rect(screen,colour,(851,551,149,153))
        screen.blit(colourindicator,(850,550))

#--------------------------------------Save - Load ---------------------------------

    if saveRect.collidepoint(mx,my):
        screen.blit(savetoolon,(860,35))
        if mb[0]==1:
            screen.blit(savetoolselected,(860,35))
            screen.blit(savedesc,(844,324))
            filename=getName()
            image.save(screen.subsurface(canvasRect),filename+".png")
    if loadRect.collidepoint(mx,my):
        screen.blit(loadtoolon,(860,108))
        if mb[0]==1:
            screen.blit(loadtoolselected,(860,108))
            screen.blit(loaddesc,(844,324))
            filename=getName()
            loadpic=image.load(filename)
            screen.blit(loadpic,(378,94,406,541))

#--------------------------------------Undo - Redo ---------------------------------            

    if undoRect.collidepoint(mx,my):
        screen.blit(undotoolon,(846,184))
        if mb[0]==1:
            screen.blit(undotoolselected,(846,184))
    if redoRect.collidepoint(mx,my):
        screen.blit(redotoolon,(921,184))
        if mb[0]==1:
            screen.blit(redotoolselected,(921,184))
            
#-----------------------------------------Tools----------------------------------
    
    if pencilRect.collidepoint(mx,my):
        screen.blit(pencilonRect,(63,118))
        if mb[0]==1:
            screen.blit(pencilselectedRect,(63,118))
            tools="pencil"
    if tools=="pencil":
        screen.blit(pencilselectedRect,(63,118))
        if scroll==False:
            screen.blit(pencildesc,(844,324))
            #the area within set_clip(AREA) is only affected by the moving mouse        
        screen.set_clip(canvasRect)
        if mb[0]==1:
            draw.line(screen,colour,(mx,my),(mx1,my1),1) 
        screen.set_clip()                

    if eraserRect.collidepoint(mx,my):
        screen.blit(eraseronRect,(63,175))
        if mb[0]==1:
            screen.blit(eraserselectedRect,(63,175))
            tools="eraser"
    if tools=="eraser":
        screen.blit(eraserselectedRect,(63,175))
        screen.blit(eraserdesc,(844,324))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            draw.circle(screen,colour,(mx,my),size/2)
        if mb[0]==1:
            draw.circle(screen,(255,255,255),(mx,my),(size+3))
            draw.line(screen,(255,255,255),(mx1,my1),(mx,my),size+9)
        screen.set_clip()

    if spraycanRect.collidepoint(mx,my):
        screen.blit(spraycanonRect,(63,233))
        if mb[0]==1:
            screen.blit(spraycanselectedRect,(63,233))
            tools="spraycan"
    if tools=="spraycan":
        screen.blit(spraycanselectedRect,(63,233))
        screen.blit(spraydesc,(844,324))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            for i in range(300):
                #a random position 25 pixels away from the mouse position
                randomx=randint(mx-25,mx+25)
                randomy=randint(my-25,my+25)
                #distance formula
                radius=((mx-randomx)**2 + (my-randomy)**2)**.5
                if radius<size+6:
                    #draws circles in random places when you click
                    draw.circle(screen,colour,(randomx,randomy),int(.5))
        screen.set_clip()

    if brushRect.collidepoint(mx,my):
        screen.blit(brushonRect,(63,289))
        if mb[0]==1:
            screen.blit(brushselectedRect,(63,289))
            tools="brush"
    if tools=="brush":
        screen.blit(brushselectedRect,(63,289))
        screen.blit(brushdesc,(844,324))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            draw.circle(screen,colour,(mx,my),size+3)
        if mb[0]==1:
            for i in range(int(length)):
                #radius of the circle
                sx = i*(mx1-mx)/length
                sy = i*(my1-my)/length
                draw.circle(screen,colour,(mx1-int(sx),my1-int(sy)),size+3)           
        screen.set_clip()
        
    if eyedropperRect.collidepoint(mx,my): 
        screen.blit(eyedropperonRect,(63,345))
        if mb[0]==1:
            screen.blit(eyedropperselectedRect,(63,345))
            tools="eyedropper"
    if tools=="eyedropper":
        screen.blit(eyedropperselectedRect,(63,345))
        screen.blit(eyedropperdesc,(844,324))
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            #gets a colour thats on the canvas
            colour = screen.get_at((mx,my))
            draw.rect(screen,colour,(851,551,149,149))
            screen.blit(colourindicator,(850,550))       

    if fillRect.collidepoint(mx,my): 
        screen.blit(fillonRect,(126,118))
        if mb[0]==1:
            screen.blit(fillselectedRect,(126,118))
            tools="fill"
    if tools=="fill":
        screen.blit(fillselectedRect,(126,118))
        screen.blit(filldesc,(844,324))
        screen.set_clip(canvasRect)
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            #draws a rectangle of your specificed, the save coordinates as your canvas
            draw.rect(screen,colour,canvasRect,0)           
        screen.set_clip()

    if drawlineRect.collidepoint(mx,my): 
        screen.blit(drawlineonRect,(63,402))
        if mb[0]==1:
            screen.blit(drawlineselectedRect,(63,402))
            tools="drawline"
    if tools=="drawline":
        screen.blit(drawlineselectedRect,(63,402))
        screen.blit(linedesc,(844,324))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            screen.blit(canvascopy,(378,94))
            #draws a line according to your mouse starting poition and end position
            draw.line(screen,colour,(mx,my),(mx2,my2),size)
        screen.set_clip()

    if drawrectRect.collidepoint(mx,my): 
        screen.blit(drawrectonRect,(63,462))
        if mb[0]==1:
            screen.blit(drawrectselectedRect,(63,462))
            tools="drawrect"
    if tools=="drawrect":
        screen.blit(drawrectselectedRect,(63,462))
        screen.blit(rectdesc,(844,324))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            screen.blit(canvascopy,(378,94))
            #draws 4 different lines each direction to make a rectangle shape
            draw.line(screen,colour,(mx,my),(mx2,my),1)
            draw.line(screen,colour,(mx,my2),(mx,my),1)
            draw.line(screen,colour,(mx2,my2),(mx,my2),1)
            draw.line(screen,colour,(mx2,my2),(mx2,my),1)            
        screen.set_clip()

    if drawrectfilledRect.collidepoint(mx,my): 
        screen.blit(drawrectfilledonRect,(87,462))
        if mb[0]==1:
            screen.blit(drawrectfilledselectedRect,(87,462))
            tools="drawrectfilled"
    if tools=="drawrectfilled":
        screen.blit(drawrectfilledselectedRect,(87,462))
        screen.blit(rectfilleddesc,(844,324))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            #draws a circle on the canvas when the mouse is clicked - to fill in the rectangle
            draw.circle(screen,colour,(mx,my),0)
            screen.blit(canvascopy,(378,94))
            #draws the rectangle shape of the rectangle tool
            draw.rect(screen,colour,(mx2,my2,mx-mx2,my-my2))           
        screen.set_clip()

    if drawellipseRect.collidepoint(mx,my): 
        screen.blit(drawellipseonRect,(63,516))
        if mb[0]==1:
            screen.blit(drawellipseselectedRect,(63,516))
            tools="drawellipse"
    if tools=="drawellipse":
        screen.blit(drawellipseselectedRect,(63,516))
        screen.blit(ellipsedesc,(844,324))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            if abs(mx2-mx)>1 and abs(my2-my)>1:
                x=min(mx2,mx)
                x1=max(mx2,mx)
                y=min(my2,my)
                y1=max(my2,my)
                rx=abs(x1-x)
                ry=abs(y1-y)
                screen.blit(canvascopy,(378,94))
                #makes a ellipse using absolute, maximum and minimum values
                draw.ellipse(screen,colour,(x,y,rx,ry),1)         
        screen.set_clip()

    if drawellipsefilledRect.collidepoint(mx,my): 
        screen.blit(drawellipsefilledonRect,(87,516))
        if mb[0]==1:
            screen.blit(drawellipsefilledselectedRect,(87,516))
            tools="drawellipsefilled"
    if tools=="drawellipsefilled":
        screen.blit(drawellipsefilledselectedRect,(87,516))
        screen.blit(ellipsefilleddesc,(844,324))
        screen.set_clip(canvasRect)
        if mb[0]==1:
            if abs(mx2-mx)>1 and abs(my2-my)>1:
                x=min(mx2,mx)
                x1=max(mx2,mx)
                y=min(my2,my)
                y1=max(my2,my)
                rx=abs(x1-x)
                ry=abs(y1-y)
                screen.blit(canvascopy,(378,94))
                #makes a filled ellipse using absolute, maximum and minimum values
                draw.ellipse(screen,colour,(x,y,rx,ry))           
        screen.set_clip()

    if stampRect.collidepoint(mx,my): 
        screen.blit(stamponRect,(222,118))
        if mb[0]==1:
            screen.blit(stampselectedRect,(222,118))
            tools="stamp"
    if tools=="stamp":
        screen.blit(stampselectedRect,(222,118))
        screen.blit(stampdesc,(844,324))
        if landscape1Rect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(landscape1,(378,94))
            screen.blit(landscape1toolSELECTED,(199,437))
        if landscape2Rect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(landscape2,(378,94))
            screen.blit(landscape2toolSELECTED,(257,437))
        if landscape3Rect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(landscape3,(378,94))
            screen.blit(landscape3toolSELECTED,(199,498))
        if landscape4Rect.collidepoint(mx,my) and mb[0]==1:
            screen.blit(landscape4,(378,94))
            screen.blit(landscape4toolSELECTED,(257,498)) 
        if appstoreRect.collidepoint(mx,my) and mb[0]==1:
            stamp="appstore"
        if stamp=="appstore":
            screen.blit(appstoreToolSELECTED,(199,165))
        if stamp=="appstore" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(appstore,(mx-cw/2,my-ch/2))
            screen.set_clip()
        if cameraRect.collidepoint(mx,my) and mb[0]==1:
            stamp="camera"
        if stamp=="camera":
            screen.blit(cameraToolSELECTED,(257,166))
        if stamp=="camera" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(camera,(mx-cw/2,my-ch/2))
            screen.set_clip()
        if facebookRect.collidepoint(mx,my) and mb[0]==1:
            stamp="facebook"
        if stamp=="facebook":
            screen.blit(facebookToolSELECTED,(199,209))
        if stamp=="facebook" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(facebook,(mx-cw/2,my-ch/2))
            screen.set_clip()
        if notesRect.collidepoint(mx,my) and mb[0]==1:
            stamp="notes"
        if stamp=="notes":
            screen.blit(notesToolSELECTED,(257,210))
        if stamp=="notes" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(notes,(mx-cw/2,my-ch/2))
            screen.set_clip()
        if safariRect.collidepoint(mx,my) and mb[0]==1:
            stamp="safari"
        if stamp=="safari":
            screen.blit(safariToolSELECTED,(199,254))
        if stamp=="safari" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(safari,(mx-cw/2,my-ch/2))
            screen.set_clip()        
        if settingsRect.collidepoint(mx,my) and mb[0]==1:
            stamp="settings"
        if stamp=="settings":
            screen.blit(settingsToolSELECTED,(257,254))
        if stamp=="settings" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(settings,(mx-cw/2,my-ch/2))
            screen.set_clip()
        if stocksRect.collidepoint(mx,my) and mb[0]==1:
            stamp="stocks"
        if stamp=="stocks":
            screen.blit(stocksToolSELECTED,(199,300))
        if stamp=="stocks" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(stocks,(mx-cw/2,my-ch/2))
            screen.set_clip()
        if youtubeRect.collidepoint(mx,my) and mb[0]==1:
            stamp="youtube"
        if stamp=="youtube":
            screen.blit(youtubeToolSELECTED,(257,299))
        if stamp=="youtube" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(youtube,(mx-cw/2,my-ch/2))
            screen.set_clip()        
        if ipodRect.collidepoint(mx,my) and mb[0]==1:
            stamp="ipod"
        if stamp=="ipod":
            screen.blit(ipodToolSELECTED,(257,343))
        if stamp=="ipod" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(ipod,(mx-cw/2,my-ch/2))
            screen.set_clip()
        if weatherRect.collidepoint(mx,my) and mb[0]==1:
            stamp="weather"
        if stamp=="weather":
            screen.blit(weatherToolSELECTED,(199,344))
        if stamp=="weather" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(weather,(mx-cw/2,my-ch/2))
            screen.set_clip()
        if mailRect.collidepoint(mx,my) and mb[0]==1:
            stamp="mail"
        if stamp=="mail":
            screen.blit(mailToolSELECTED,(199,391))
        if stamp=="mail" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(mail,(mx-cw/2,my-ch/2))
            screen.set_clip()
        if cydiaRect.collidepoint(mx,my) and mb[0]==1:
            stamp="cydia"
        if stamp=="cydia":
            screen.blit(cydiaToolSELECTED,(257,390))
        if stamp=="cydia" and canvasRect.collidepoint(mx,my) and mb[0]==1:
            screen.set_clip(canvasRect)
            screen.blit(screenback,(0,0))
            screen.blit(cydia,(mx-cw/2,my-ch/2))
            screen.set_clip()        

    if clearRect.collidepoint(mx,my) and mb[0]==1:
        screen.blit(cleartoolselected,(860,254))
        #draws a white rectangle over the canvas to make a "clear" effect
        draw.rect(screen,(255,255,255),canvasRect,0)
    if tools!="stamp":
        screen.blit(stampblocker,(193,163))

    display.flip()
quit()
