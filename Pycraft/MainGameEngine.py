from numpy import unsignedinteger


if not __name__ == "__main__":
    print("Started <Pycraft_MainGameEngine>")
    class CreateEngine:
        def __init__(self):
            try:
                import pygame # self mod (module) (module name) (subsection of module) (name references)
                self.mod_Pygame__ = pygame
                import os
                self.mod_OS__ = os
                import sys
                self.mod_Sys__ = sys
                import random
                self.mod_Random__ = random
                import time
                self.mod_Time__ = time
                import pygame.locals
                self.mod_Pygame_locals_ = pygame.locals
                import psutil
                self.mod_Psutil__ = psutil
                from tkinter import messagebox
                self.mod_Tkinter_messagebox_ = messagebox
                import OpenGL.GL
                self.mod_OpenGL_GL_ = OpenGL.GL
                import OpenGL.GLU
                self.mod_OpenGL_GLU_ = OpenGL.GLU
                import OpenGL.GLUT
                self.mod_OpenGL_GLUT_ = OpenGL.GLUT
                import numpy
                self.mod_Numpy__ = numpy
                import ctypes
                self.mod_Ctypes__ = ctypes
                
                self.mod_Pygame__.init()
                
                self.base_folder = os.path.dirname(__file__)
            except Exception as error:
                print(error)
                try:
                    import tkinter as tk
                    root = tk.Tk()
                    root.withdraw()
                    self.mod_Tkinter_messagebox_.showerror("Startup Fail", "Missing required modules")
                    quit()
                except:
                    try:
                        self.mod_Pygame__.quit()
                        sys.exit("Thank you for playing")
                    except:
                        quit()


        def Play(self):
            try:
                realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
                SecondaryFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
                LoadingFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                LoadingTextFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)

                self.Display.fill(self.BackgroundCol)

                self.mod_Pygame__.mixer.Channel(2).fadeout(2000)

                PycraftTitle = MainTitleFont.render("Pycraft", self.aa, self.FontCol)
                TitleWidth = PycraftTitle.get_width()
                self.Display.blit(PycraftTitle, ((realWidth-TitleWidth)/2, 0))

                LoadingTitle = SecondaryFont.render("Loading", self.aa, self.FontCol)
                self.Display.blit(LoadingTitle, (((realWidth-TitleWidth)/2)+55, 50))

                self.mod_Pygame__.draw.lines(self.Display, (self.ShapeCol), self.aa, [(100, realHeight-100), (realWidth-100, realHeight-100)], 3)

                DisplayMessage = LoadingFont.render("Initiating...", self.aa, self.FontCol)
                DisplayMessageWidth = DisplayMessage.get_width()
                self.Display.blit(DisplayMessage, ((realWidth-DisplayMessageWidth)/2, realHeight-120))

                TextFontRendered = LoadingTextFont.render(f"Loading...", self.aa, self.FontCol)
                TextFontRenderedWidth = TextFontRendered.get_width()
                self.Display.blit(TextFontRendered, ((realWidth-TextFontRenderedWidth)/2, realHeight-100))

                self.mod_Pygame__.display.flip()

                self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Loading")

                text = self.mod_TextUtils__.GenerateText.LoadQuickText(self)
                TextFontRendered = LoadingTextFont.render(f"{text}", self.aa, self.FontCol)
                self.Display.blit(TextFontRendered, (600, 160))
                self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_WAIT)
                self.base_folder = self.mod_OS__.path.dirname(__file__)
                realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                LineScaleFact = realWidth/1280
                LoadingPercent = 0
                line = []
                LoadingPercent += 90+((75/7)*LineScaleFact)
                MainTitleFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 60)
                SecondaryFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 35)
                LoadingTextFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                LoadingFont = self.mod_Pygame__.font.Font(self.mod_OS__.path.join(self.base_folder, ("Fonts\\Book Antiqua.ttf")), 15)
                line.append((LoadingPercent, realHeight-100))
                LoadingPercent += 100+((75/7)*LineScaleFact)
                aFPS = 0
                iteration = 1
                line.append((LoadingPercent, realHeight-100))
                self.mod_Pygame__.draw.lines(self.Display, (30, 30, 30), self.aa, [(95, 620), (1200, 620)], 3)
                self.mod_Pygame__.draw.lines(self.Display, (153, 153, 153), self.aa, line)
                Init = LoadingFont.render("Initiating", self.aa, self.FontCol)
                TextFontRendered = LoadingTextFont.render(f"{text}", self.aa, self.FontCol)
                self.Display.blit(TextFontRendered, (600, 160))
                self.Display.blit(Init, (100, 640))
                self.mod_Pygame__.display.flip()
                Jump = False
                JumpID = 0 
                CubeNum = 10 
                FOV = 70 
                MouseUnlock = False 
                max_distance = 0 
                z = 0 
                run = 0 
                y = -10 
                z = 1 
                x = 0 
                cube_dict = {}
                repeater = True
                camera_x = 0
                camera_y = 0
                camera_z = 0

                LoadingPercent += 100+((75/7)*LineScaleFact)
                self.mod_DisplayUtils__.DisplayUtils.GenerateLoadDisplay(self, LoadingFont, text, "Loading", LoadingPercent, True, MainTitleFont, SecondaryFont, LoadingTextFont, line)

                self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Playing")

                MouseUnlock = True
                Sun_pos_x, Sun_pos_y, Sun_pos_z = 0, 10, -20
                LoadingPercent += 100+((75/7)*LineScaleFact)
                self.mod_DisplayUtils__.DisplayUtils.GenerateLoadDisplay(self, LoadingFont, text, "Loaded Image Resources", LoadingPercent, True, MainTitleFont, SecondaryFont, LoadingTextFont, line)

                counter = 0
                rotationvectX, rotationvectY = 0, 0

                LoadingPercent += 100+((75/7)*LineScaleFact)
                self.mod_DisplayUtils__.DisplayUtils.GenerateLoadDisplay(self, LoadingFont, text, "Beginning Resource Loading | 0% complete", LoadingPercent, True, MainTitleFont, SecondaryFont, LoadingTextFont, line)
                if self.Load3D == True:
                    percent = 0
                    self.Map = self.mod_Pywavefront__.Wavefront(self.mod_OS__.path.join(self.base_folder, ("Resources\\G3_Resources\\Map\\map.obj")), create_materials=True, collect_faces=True) 
                    self.MapVerts = self.mod_Numpy__.array(self.Map.vertices)
                    self.Map_box = (self.MapVerts[0], self.MapVerts[0])
                    counterFORvertex = 0
                    for vertex in self.MapVerts:
                        counterFORvertex += 1
                        counterFORvertex = self.mod_ModelMathsUtil__.ComputeMapPoints.LoadingMapData(self, vertex, counterFORvertex)
                        
                        LoadingPercentForEfficiency = (100/13224)*counterFORvertex
                        if int(LoadingPercentForEfficiency) == percent:
                            if percent <= 100:
                                percent += 1

                            LoadingPercent += (2.6448*2)*LineScaleFact
                            COMPLETIONpercent = (100/13224)*counterFORvertex
                            self.mod_DisplayUtils__.DisplayUtils.GenerateLoadDisplay(self, LoadingFont, text, f"Started Resource Loading | Map: {int(COMPLETIONpercent)}% complete", LoadingPercent, False, MainTitleFont, SecondaryFont, LoadingTextFont, line)
                            for event in self.mod_Pygame__.event.get():
                                if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):
                                    return None, "Undefined"
                            self.clock.tick(self.FPS)

                    Map_size = [self.Map_box[1][i]-self.Map_box[0][i] for i in range(3)]
                    max_Map_size = max(Map_size)
                    Map_size = self.G3Dscale 
                    self.Map_scale = [Map_size/max_Map_size for i in range(3)]
                    self.Map_trans = [-(self.Map_box[1][i]+self.Map_box[0][i])/2 for i in range(3)]

                    map_vertices = []
                    for mesh in self.Map.mesh_list: 
                        for face in mesh.faces: 
                            for vertex_i in face: 
                                Data = self.Map.vertices[vertex_i]
                                for k in range(len(Data)):
                                    map_vertices.append(Data[k])
                
                self.mod_DisplayUtils__.DisplayUtils.GenerateLoadDisplay(self, LoadingFont, text, "Resource Loading | Loaded Map", LoadingPercent, True, MainTitleFont, SecondaryFont, LoadingTextFont, line)
                self.mod_Time__.sleep(2)

                self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Playing")

                LoadingPercent += 100+((75/7)*LineScaleFact)
                self.mod_DisplayUtils__.DisplayUtils.GenerateLoadDisplay(self, LoadingFont, text, "Resource Loading | Loaded Map", LoadingPercent, True, MainTitleFont, SecondaryFont, LoadingTextFont, line)
                run = 0
                self.mod_Pygame__.event.get()
                self.mod_Pygame__.mouse.set_pos((realWidth/2), (realHeight/2))
                Total_move_x, Total_move_y, Total_move_z = 0, 0, 0
                self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Playing")
                WKeyPressed, AKeyPressed, SKeyPressed, DKeyPressed = False, False, False, False
                stop = False
                stop1 = False
                counterForWeather = 2
                weather = self.mod_Random__.randint(0, 2)
                
                LoadingPercent = realWidth-105
                self.mod_DisplayUtils__.DisplayUtils.GenerateLoadDisplay(self, LoadingFont, text, "Finished Resource Loading; Rendering", LoadingPercent, True, MainTitleFont, SecondaryFont, LoadingTextFont, line)
                Message = self.mod_DisplayUtils__.DisplayUtils.SetOPENGLdisplay(self)
                if not Message == None:
                    return Message, "Undefined"

                Message = self.mod_SkyBoxUtil__.SkyBox.LoadSkyBox(self)
                if not Message == None:
                    return Message, "Undefined"
                Message = self.mod_MapTextureUtil__.MapTexture.LoadMapTexture(self)
                if not Message == None:
                    return Message, "Undefined"
                
                self.mod_OpenGL_GLU_.gluPerspective(FOV, (realWidth/realHeight), 1, 8000000)
                firstRUN = 0
                self.mod_Pygame__.mouse.set_pos((realWidth/2), (realHeight/2))

                prev_camera_x = camera_x
                prev_camera_y = camera_y
                prev_camera_z = camera_z

                self.X = camera_x
                self.Y = camera_y
                self.Z = camera_z

                prev_collisions = 0

                collisions = [False, 0]

                WkeydownTimer = 0
                AkeydownTimer = 0
                SkeydownTimer = 0
                DkeydownTimer = 0

                self.mod_OpenGL_GL_.glShadeModel(self.mod_OpenGL_GL_.GL_SMOOTH)
                self.mod_OpenGL_GL_.glMatrixMode(self.mod_OpenGL_GL_.GL_MODELVIEW)
                if self.aa == True:
                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_MULTISAMPLE)
                elif self.aa == False:
                    self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_MULTISAMPLE)
                self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_FRAMEBUFFER_SRGB)
                self.mod_Pygame__.mouse.set_cursor(self.mod_Pygame__.SYSTEM_CURSOR_CROSSHAIR)
                FullscreenX, FullscreenY = self.mod_Pyautogui__.size()

                #dima 2021-10-25 BEGIN
                mapVBOVertsId = self.mod_OpenGL_GL_.glGenBuffers(1)
                vertsArr = self.mod_Numpy__.array(self.Map.vertices, 'f')
                self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, mapVBOVertsId)
                self.mod_OpenGL_GL_.glBufferData(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, vertsArr.nbytes, vertsArr.data, self.mod_OpenGL_GL_.GL_STATIC_DRAW)
                self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, 0)

                mapVBOMeshInds = []
                for mesh in self.Map.mesh_list: 
                    mapVBOIndsId = self.mod_OpenGL_GL_.glGenBuffers(1)
                    facesArr = self.mod_Numpy__.array(mesh.faces, 'i')
                    #f = open("123.txt", "a")
                    #f.write('\n'.join(str(e) for e in mesh.faces)+'meshend\n')
                    #f.close()

                    mapVBOMeshInds.append([mapVBOIndsId, facesArr.size])
                    self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, mapVBOIndsId)
                    self.mod_OpenGL_GL_.glBufferData(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, facesArr.nbytes, facesArr.data, self.mod_OpenGL_GL_.GL_STATIC_DRAW)
                    self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, 0)
                #dima 2021-10-25 END


                while True:
                    eFPS = self.clock.get_fps()
                    aFPS += eFPS
                    iteration += 1
                    firstRUN += 1
                    mX, mY = self.mod_Pygame__.mouse.get_pos()
                    x = self.mod_OpenGL_GL_.glGetDoublev(self.mod_OpenGL_GL_.GL_MODELVIEW_MATRIX)
                    camera_x = x[3][0]
                    camera_y = (x[3][1]-71407.406)
                    camera_z = (x[3][2]+2)
                    run += 1
                    counter += 1
                    realWidth, realHeight = self.mod_Pygame__.display.get_window_size()
                    
                    if self.mod_Pygame__.mixer.get_busy() == False:
                        self.mod_SoundUtils__.PlaySound.PlayAmbientSound(self)

                    for event in self.mod_Pygame__.event.get():
                        if event.type == self.mod_Pygame__.QUIT or (event.type == self.mod_Pygame__.KEYDOWN and event.key == self.mod_Pygame__.K_ESCAPE):
                            self.CurrentlyPlaying = None
                            self.LoadMusic = True
                            return None, "Undefined"
                        if event.type == self.mod_Pygame__.KEYDOWN:
                            if event.key == self.mod_Pygame__.K_a:
                                AKeyPressed = True
                            if event.key == self.mod_Pygame__.K_d:
                                DKeyPressed = True
                            if event.key == self.mod_Pygame__.K_e:
                                if self.Fullscreen == False:
                                    myScreenshot = self.mod_Pyautogui__.screenshot(region=((0, 0, FullscreenX, FullscreenY)))
                                    myScreenshot.save(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))
                                else:
                                    print("here")
                                    PosX, PosY = self.mod_DisplayUtils__.DisplayUtils.GetDisplayLocation(self)
                                    myScreenshot = self.mod_Pyautogui__.screenshot(region=((PosX, PosY, realWidth, realHeight)))
                                    myScreenshot.save(self.mod_OS__.path.join(self.base_folder, ("Resources\\General_Resources\\PauseIMG.png")))
                                return None, "Inventory"
                            if event.key == self.mod_Pygame__.K_F11:
                                Message = self.mod_DisplayUtils__.DisplayUtils.UpdateOPENGLdisplay(self)
                                self.mod_OpenGL_GLU_.gluPerspective(FOV, (realWidth/realHeight), 1, 8000000)
                                self.mod_OpenGL_GL_.glShadeModel(self.mod_OpenGL_GL_.GL_SMOOTH)
                                self.mod_OpenGL_GL_.glMatrixMode(self.mod_OpenGL_GL_.GL_MODELVIEW)
                                if self.aa == True:
                                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_MULTISAMPLE)
                                elif self.aa == False:
                                    self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_MULTISAMPLE)
                                self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_FRAMEBUFFER_SRGB)
                            if event.key == self.mod_Pygame__.K_r:
                                return None, "MapGUI"
                            if event.key == self.mod_Pygame__.K_w:
                                WKeyPressed = True
                            if event.key == self.mod_Pygame__.K_s:
                                SKeyPressed = True
                            if event.key == self.mod_Pygame__.K_SPACE and Jump == False: 
                                Jump = True
                            if event.key == self.mod_Pygame__.K_l:
                                if MouseUnlock == True:
                                    MouseUnlock = False
                                elif MouseUnlock == False:
                                    MouseUnlock = True
                            if event.key == self.mod_Pygame__.K_q:
                                self.mod_TkinterUtils__.TkinterInfo.CreateTkinterWindow(self)
                                self.mod_Pygame__.mouse.set_pos((realWidth/2), (realHeight/2))
                        if event.type == self.mod_Pygame__.KEYUP:
                            if event.key == self.mod_Pygame__.K_w:
                                WKeyPressed = False
                            if event.key == self.mod_Pygame__.K_a:
                                AKeyPressed = False
                            if event.key == self.mod_Pygame__.K_s:
                                SKeyPressed = False
                            if event.key == self.mod_Pygame__.K_d:
                                DKeyPressed = False
                        
                        if event.type == self.mod_Pygame__.MOUSEBUTTONDOWN:
                            if event.button == 4:
                                self.mod_OpenGL_GL_.glTranslatef(0, 0, 1)
                            if event.button == 5:
                                self.mod_OpenGL_GL_.glTranslatef(0, 0, -1)

                    if WKeyPressed == True:
                        WkeydownTimer += 1
                        if stop == False:
                            time = eFPS*3
                            stop = True
                        if time >= 0:
                            Total_move_z += 35
                            if WkeydownTimer/(aFPS/iteration) >= ((self.mod_Random__.randint(75, 100))/100):
                                if self.sound == True:
                                    self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                                WkeydownTimer = 0
                        elif time <= 0:
                            if WkeydownTimer/(aFPS/iteration) >= ((self.mod_Random__.randint(40, 50))/100):
                                if self.sound == True:
                                    self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                                WkeydownTimer = 0
                            Total_move_z += 100

                        time -= 1
                    else:
                        stop = False
                        WkeydownTimer = 0

                    if AKeyPressed == True:
                        Total_move_x += -35 
                        AkeydownTimer += 1

                        if AkeydownTimer/(aFPS/iteration) >= ((self.mod_Random__.randint(75, 100))/100):
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                            AkeydownTimer = 0
                    else:
                        AkeydownTimer = 0

                    if SKeyPressed == True:
                        Total_move_z += -35 
                        SkeydownTimer += 1

                        if SkeydownTimer/(aFPS/iteration) >= ((self.mod_Random__.randint(75, 100))/100):
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                            SkeydownTimer = 0
                    else:
                        SkeydownTimer = 0

                    if DKeyPressed == True:
                        Total_move_x += 35 
                        DkeydownTimer += 1

                        if DkeydownTimer/(aFPS/iteration) >= ((self.mod_Random__.randint(75, 100))/100):
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                            DkeydownTimer = 0
                    else:
                        DkeydownTimer = 0

                    
                    if Jump == True:
                        JumpID += 1
                        if JumpID <= 20:
                            JumpID += 1
                            Total_move_y -= 100
                        if JumpID >= 21:
                            JumpID += 1
                            Total_move_y += 100
                        if JumpID >= 40:
                            if self.sound == True:
                                self.mod_SoundUtils__.PlaySound.PlayFootstepsSound(self)
                            Jump = False
                            JumpID = 0

                    if MouseUnlock == True:
                        if mX >= 680:
                            self.mod_OpenGL_GL_.glRotatef(self.cameraANGspeed, 0, 1, 0) 
                            rotationvectX += 0.5
                            
                        if mX <= 600:
                            self.mod_OpenGL_GL_.glRotatef(-self.cameraANGspeed, 0, 1, 0) 
                            rotationvectX += -0.5

                    self.mod_OpenGL_GL_.glClear(self.mod_OpenGL_GL_.GL_COLOR_BUFFER_BIT|self.mod_OpenGL_GL_.GL_DEPTH_BUFFER_BIT)
                    x = self.mod_OpenGL_GL_.glGetDoublev(self.mod_OpenGL_GL_.GL_MODELVIEW_MATRIX)
                    self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_DEPTH_TEST)
                    self.mod_OpenGL_GL_.glPushMatrix()
                    self.mod_OpenGL_GL_.glDepthMask(self.mod_OpenGL_GL_.GL_FALSE)
                    self.mod_OpenGL_GL_.glClear(self.mod_OpenGL_GL_.GL_COLOR_BUFFER_BIT|self.mod_OpenGL_GL_.GL_DEPTH_BUFFER_BIT)
                    self.mod_OpenGL_GL_.glDepthMask(self.mod_OpenGL_GL_.GL_TRUE)
                    self.mod_OpenGL_GL_.glPopMatrix()
                    self.mod_OpenGL_GL_.glPolygonMode(self.mod_OpenGL_GL_.GL_FRONT_AND_BACK, self.mod_OpenGL_GL_.GL_FILL)
                    self.mod_CaptionUtils__.GenerateCaptions.GetNormalCaption(self, "Playing")

                    if camera_x == prev_camera_x and camera_y == prev_camera_y and camera_z == prev_camera_z and not firstRUN == 1:
                        collisions = prev_collisions
                    else:
                        collisions = self.mod_GetWorldCollisions__.GetMapCollisions.GetCollisions(self)
                        prev_camera_x = camera_x
                        prev_camera_y = camera_y
                        prev_camera_z = camera_z
                        prev_collisions = collisions
                    if collisions[0] == False:
                        Total_move_y -= 1
                    elif collisions[0] == True:
                        if collisions[1] < camera_y and collisions[1] < camera_y-1:
                            Total_move_y -= 1
                        elif collisions[1] > camera_y and collisions[1] > camera_y+1:
                            Total_move_y += 1
                    if firstRUN == 1:
                        self.mod_OpenGL_GL_.glTranslatef(0, 50000, 0)
                        prev_camera_x = camera_x
                        prev_camera_y = camera_y
                        prev_camera_z = camera_z
                    else:
                        firstRUN = 2
                    if camera_x >= (1150*self.G3Dscale) or camera_x <= (-1150*self.G3Dscale) or camera_z >= (700*self.G3Dscale) or camera_z <= (-1150*self.G3Dscale):
                        print("World Boarder Reached")
                        
                    self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_DEPTH_TEST)

                    Message = self.mod_SkyBoxUtil__.SkyBox.DrawSkyBox(self)
                    if not Message == None:
                        return Message, "Undefined"

                    self.mod_MapTextureUtil__.MapTexture.DrawMapTexture(self)

                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_DEPTH_TEST)
                    
                    #dima 2021-10-25 BEGIN
                    self.mod_OpenGL_GL_.glPushMatrix() 
                    self.mod_OpenGL_GL_.glScalef(*self.Map_scale) 
                    self.mod_OpenGL_GL_.glTranslatef(*self.Map_trans)          


                    for meshVBO in mapVBOMeshInds: 
                        self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, mapVBOVertsId)
                        self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, meshVBO[0])
                        
                        self.mod_OpenGL_GL_.glVertexPointer(3, self.mod_OpenGL_GL_.GL_FLOAT, vertsArr.itemsize * 3, None);
                        self.mod_OpenGL_GL_.glEnableClientState(self.mod_OpenGL_GL_.GL_VERTEX_ARRAY);

                        self.mod_OpenGL_GL_.glDrawElements(self.mod_OpenGL_GL_.GL_TRIANGLES, meshVBO[1], self.mod_OpenGL_GL_.GL_UNSIGNED_INT, None); 
                        
                        self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ELEMENT_ARRAY_BUFFER, 0)
                        self.mod_OpenGL_GL_.glBindBuffer(self.mod_OpenGL_GL_.GL_ARRAY_BUFFER, 0)
                        
                        self.mod_OpenGL_GL_.glDisableClientState(self.mod_OpenGL_GL_.GL_VERTEX_ARRAY);

                    self.mod_OpenGL_GL_.glPopMatrix()

                    #self.mod_GetWorldVertex__.GetMapVertices.MapModel(self)
                    #dima 2021-10-25 END

                    if stop1 == False:
                        counterForWeather = 1
                        stop1 = True
                    counterForWeather = counterForWeather + self.mod_Random__.randint(0, 10)
                    if counterForWeather/self.FPS >= 300:
                        weather = self.mod_Random__.randint(0, 2)
                        stop1 = False
                    if self.RenderFOG == True and weather == 2: 
                        self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_FOG)
                        self.mod_OpenGL_GL_.glFogfv(self.mod_OpenGL_GL_.GL_FOG_COLOR, (239, 243, 245, 1)) 
                        self.mod_OpenGL_GL_.glFogi(self.mod_OpenGL_GL_.GL_FOG_MODE, self.mod_OpenGL_GL_.GL_LINEAR)
                        self.mod_OpenGL_GL_.glFogf(self.mod_OpenGL_GL_.GL_FOG_START, 160) 
                        self.mod_OpenGL_GL_.glFogf(self.mod_OpenGL_GL_.GL_FOG_END, 3000) 
                        self.mod_OpenGL_GL_.glFogf(self.mod_OpenGL_GL_.GL_FOG_DENSITY, 0) 
                    elif self.RenderFOG == True and weather == 1: 
                        self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_FOG)
                        self.mod_OpenGL_GL_.glFogfv(self.mod_OpenGL_GL_.GL_FOG_COLOR, (115, 145, 165, 1)) 
                        self.mod_OpenGL_GL_.glFogi(self.mod_OpenGL_GL_.GL_FOG_MODE, self.mod_OpenGL_GL_.GL_LINEAR)
                        self.mod_OpenGL_GL_.glFogf(self.mod_OpenGL_GL_.GL_FOG_START, 160) 
                        self.mod_OpenGL_GL_.glFogf(self.mod_OpenGL_GL_.GL_FOG_END, 9000) 
                        self.mod_OpenGL_GL_.glFogf(self.mod_OpenGL_GL_.GL_FOG_DENSITY, 0) 
                    elif self.RenderFOG == True and weather == 0: 
                        self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_FOG)
                        self.mod_OpenGL_GL_.glFogfv(self.mod_OpenGL_GL_.GL_FOG_COLOR, (177, 194, 205, 1)) 
                        self.mod_OpenGL_GL_.glFogi(self.mod_OpenGL_GL_.GL_FOG_MODE, self.mod_OpenGL_GL_.GL_LINEAR)
                        self.mod_OpenGL_GL_.glFogf(self.mod_OpenGL_GL_.GL_FOG_START, 160) 
                        self.mod_OpenGL_GL_.glFogf(self.mod_OpenGL_GL_.GL_FOG_END, 30000) 
                        self.mod_OpenGL_GL_.glFogf(self.mod_OpenGL_GL_.GL_FOG_DENSITY, 0) 
                    elif self.RenderFOG == False:
                        self.mod_OpenGL_GL_.glDisable(self.mod_OpenGL_GL_.GL_FOG)
                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_LIGHTING)
                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_LIGHT0)
                    self.mod_OpenGL_GL_.glLightfv(self.mod_OpenGL_GL_.GL_LIGHT0, self.mod_OpenGL_GL_.GL_POSITION, (Sun_pos_x, Sun_pos_y, Sun_pos_z))
                    self.mod_OpenGL_GL_.glLightfv(self.mod_OpenGL_GL_.GL_LIGHT0, self.mod_OpenGL_GL_.GL_AMBIENT, (1, 0, 1, 1))
                    self.mod_OpenGL_GL_.glLightfv(self.mod_OpenGL_GL_.GL_LIGHT0, self.mod_OpenGL_GL_.GL_DIFFUSE, (1, 0, 1, 1))
                    self.mod_OpenGL_GL_.glLightfv(self.mod_OpenGL_GL_.GL_LIGHT0, self.mod_OpenGL_GL_.GL_SPECULAR, (1, 0, 1, 1))
                    self.mod_OpenGL_GL_.glEnable(self.mod_OpenGL_GL_.GL_COLOR_MATERIAL)
                    self.mod_OpenGL_GL_.glColorMaterial(self.mod_OpenGL_GL_.GL_FRONT_AND_BACK, self.mod_OpenGL_GL_.GL_AMBIENT_AND_DIFFUSE)
                    self.mod_OpenGL_GL_.glMaterial(self.mod_OpenGL_GL_.GL_FRONT_AND_BACK, self.mod_OpenGL_GL_.GL_SPECULAR, (0, 1, 0, 1))
                    self.mod_OpenGL_GL_.glMaterial(self.mod_OpenGL_GL_.GL_FRONT_AND_BACK, self.mod_OpenGL_GL_.GL_EMISSION, (0, 1, 0, 1))

                    self.mod_OpenGL_GL_.glTranslatef(Total_move_x, Total_move_y, Total_move_z)
                    PlayerModel_pos_x, PlayerModel_pos_y, PlayerModel_pos_z = -Total_move_x, -Total_move_y, -Total_move_z
                    Total_move_x, Total_move_y, Total_move_z = 0, 0, 0

                    self.mod_Pygame__.display.flip()
                    self.clock.tick(self.FPS)
            except Exception as Message:
                print(''.join(self.mod_Traceback__.format_exception(None, Message, Message.__traceback__)))
                return Message, "Undefined"
else:
    print("You need to run this as part of Pycraft")
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("Startup Fail", "You need to run this as part of Pycraft, please run the 'main.py' file")
    quit()