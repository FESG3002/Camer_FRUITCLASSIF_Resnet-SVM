import tkinter as tk
import customtkinter as ctk
import Traitementimupdown as tr
from coller4en1 import C4EN1
from coller7en1 import C7EN1
from PIL import Image,ImageTk

# Initialize CustomTkinter
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class FileSelectorApp(ctk.CTk):
    def showframe(self,frame,framecop):        
        frame.grid_forget()
        framecop.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
       
        


    def __init__(self):
        super().__init__()

        # Set window title
        self.title("FuitsRecogniser")

        # Configure window layout
       

        
        self.grid_columnconfigure((2), weight=1)
        self.grid_rowconfigure((0, 1,2), weight=1)
        self.grid_rowconfigure((8), weight=1)
        

        self.branding_frame = ctk.CTkFrame(self )
        self.pub_frame = ctk.CTkFrame(self )
        

        self.sidebar_frame = ctk.CTkFrame(self, width=10, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="FruitRecogniser", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
      
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        
        
         # Create file selection frame
        #self.file_selection_frame = ctk.CTkFrame(self)
        #self.file_selection_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # create tabview

        
        self.branding_frame.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        self.tabview  = ctk.CTkTabview(self.branding_frame)
        self.tabview.grid(row=0, column=0)
        
        self.tabview.add("ModBibliotheque")
        self.tabview.add("ModSansBibliotheque")
        self.tabview.tab("ModBibliotheque").grid_columnconfigure(0, weight=1)
        

         # create a frame for previsualisation of the image ModBibliotheque
        self.file_selection_frameimmod2 = ctk.CTkFrame(self.tabview.tab("ModBibliotheque"))
        self.file_selection_frameimmod2.grid(row=5, column=8, padx=(0,0), pady=(0, 1), sticky="nsew")
        self.logo_label = ctk.CTkLabel(self.tabview.tab("ModBibliotheque"), text="Preview", font=ctk.CTkFont(size=20, weight="bold")).grid(row=4, column=8, padx=(0,100), pady=20, sticky="E")
        # create a frame for previsualisation of the image ModSansBibliotheque
        self.file_selection_frameimmod3 = ctk.CTkFrame(self.tabview.tab("ModSansBibliotheque"))
        self.file_selection_frameimmod3.grid(row=5, column=8, padx=(0,100), pady=(0, 1), sticky="nsew")
        self.logo_label = ctk.CTkLabel(self.tabview.tab("ModSansBibliotheque"), text="Preview", font=ctk.CTkFont(size=20, weight="bold")).grid(row=4, column=8, padx=(0,100), pady=20, sticky="E")

        
       
       
        
        # Create file entry ModBibliotheque branding avec 4 image ModBibliotheque
        
        self.file_entrymod2= ctk.CTkEntry(self.tabview.tab("ModBibliotheque"), placeholder_text="selectioner un image dun fruit a reconaitre", width=500)
        self.file_entrymod2.grid(row=0, column=1, columnspan=2, padx=0, pady=(20, 0), sticky="nsew")
       
        self.im1=Image.open('imdefault.png') 
        # Create file selection button ModBibliotheque
        op4en1=C4EN1()
        self.file_selection_buttonmod2 = ctk.CTkButton(self.tabview.tab("ModBibliotheque"), text="Browse", command=lambda:self.select_file(self.file_entrymod2,self.im1))
        self.file_selection_buttonmod2.grid(row=0, column=8,padx=(20,0), pady=(20, 10))


        # Create status button ModBibliotheque
        self.branding_buttonmod2 = ctk.CTkButton(self.tabview.tab("ModBibliotheque"), text="Branding",command=lambda:op4en1.process_all_img( self.file_entrymod2))
        self.branding_buttonmod2.grid(row=3, column=0, columnspan=3, padx=(0,350), pady=(20, 10), sticky="e")
        self.branding_button2mod2 = ctk.CTkButton(self.tabview.tab("ModBibliotheque"), text="Preview",command=lambda:op4en1.Previsualiser(self.file_selection_frameimmod2))
        self.branding_button2mod2.grid(row=3, column=8, columnspan=3, padx=(20,0), pady=(20, 10))

        # Create file entry ModBibliotheque branding avec 7 image et un frame pour le cte gauche
        

        self.file_entrymod3 = ctk.CTkEntry(self.tabview.tab("ModSansBibliotheque"), placeholder_text="selectioner un image dun fruit a reconaitre", width=500)
        self.file_entrymod3.grid(row=0, column=1, columnspan=2, padx=0, pady=(20, 10), sticky="nsew")
       
       #image du model
        

        # Create file selection button ModSansBibliotheque
        op7en1=C7EN1()
        self.file_selection_buttonmod3 = ctk.CTkButton(self.tabview.tab("ModSansBibliotheque"), text="Browse", command=lambda:self.select_file(self.file_entrymod3,self.im1))
        self.file_selection_buttonmod3.grid(row=0, column=8,padx=(20,0), pady=(20, 10))


        # Create branding button for ModSansBibliotheque
        self.branding_buttonmod3 = ctk.CTkButton(self.tabview.tab("ModSansBibliotheque"), text="Branding",command=lambda:op7en1.process_all_img(self.file_entrymod3))
        self.branding_buttonmod3.grid(row=3, column=0, columnspan=3, padx=(0,350), sticky="e")
        self.labelim=ctk.CTkLabel(self.file_selection_frameimmod3)
        self.branding_button2mod3 = ctk.CTkButton(self.tabview.tab("ModSansBibliotheque"), text="Preview",command=lambda:op7en1.Previsualiser(self.file_selection_frameimmod3))
        self.branding_button2mod3.grid(row=3, column=8, columnspan=3, padx=(20,0), pady=20)

     
              


        self.im1= self.im1.resize((350,350), Image.BILINEAR)
        photo=ImageTk.PhotoImage(self.im1)
        titlelabel = ctk.CTkLabel(self.tabview.tab("ModBibliotheque"), text="IMAGE A PREDIRE", font=ctk.CTkFont(size=20, weight="bold"))
        titlelabel.grid(row=4, column=1, padx=(20,0),pady=10, sticky="nsew")                
        label=ctk.CTkLabel(self.tabview.tab("ModBibliotheque"),image=photo,text='').grid(row=5, column=1,padx=(20,0), rowspan=4, sticky="nsew")
        titlelabel = ctk.CTkLabel(self.tabview.tab("ModBibliotheque"), text=f"Prediction:  ", font=ctk.CTkFont(size=19, weight="bold"))
        titlelabel.grid(row=12, column=1, padx=(20,0),pady=10)   
        im1= Image.open('imp7.jpeg')
        im1 = im1.resize((350,350), Image.BILINEAR)
        photo=ImageTk.PhotoImage(im1)
        titlelabel = ctk.CTkLabel(self.tabview.tab("ModSansBibliotheque"), text="IMAGE A PREDIRE", font=ctk.CTkFont(size=20, weight="bold"))
        titlelabel.grid(row=4, column=1, padx=(20,0),pady=10, sticky="nsew")                
        label=ctk.CTkLabel(self.tabview.tab("ModSansBibliotheque"),image=photo,text='').grid(row=5, column=1,padx=(20,0), rowspan=4, sticky="nsew")


        ###deux bouton du side men
        
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame,text='Reconaisance',command=lambda:self.showframe(self.pub_frame,self.branding_frame))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)




 
    def select_file(self,label,image):
        # Ouvrir une boîte de dialogue de sélection de fichier
        self.fichier = ctk.filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])

        # Afficher le chemin du fichier sélectionné
        if self.fichier:
            label.insert(0,self.fichier)
            image=Image.open(self.fichier) 
        else:
            label.insert(0,"Accune image selectioner")



    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)



if __name__ == "__main__":
    app = FileSelectorApp()
    app.mainloop()
