import tkinter as tk
import tkinter.ttk as ttk
from tktooltip import ToolTip
from CTkMessagebox import CTkMessagebox
import customtkinter
from tkinter import filedialog as fd
import os

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):

    def importFunction(self, file=""):

        def importToggle(self, contains, toggle, line):
            if(contains in line):
                if("true," in line):
                    toggle.select()
                else:
                    toggle.deselect()

        def importValue(self, contains, entry, line):
            if(contains in line):
                if(len(entry.get()) > 0):
                    entry.delete(0, tk.END)
                temp = line.split()
                temp2 = temp[1].split(',')
                entry.insert(0, temp2[0])

        try:
            #filename = fd.askopenfilename(title="Choose config file", filetypes=(("JSON File", "*.json"),))
            if os.path.exists(file):
                filename = file
            else:
                filename = os.path.dirname(__file__) + '/../config/config.json'
            importFile = open(filename, 'r')
            Lines = importFile.readlines()
            for line in Lines:
                importToggle(self, "globalToggle", self.globalToggle, line)
                importToggle(self, "weaponClassToggle", self.classToggle, line)
                # importToggle(self, "individualWeaponToggle", self.weaponToggle, line)
                importToggle(self, "hiddenBonusRecoilToggle", self.hiddenBonusToggle, line)
                importToggle(self, "recoilCrank", self.recoilCrankToggle, line)

                importValue(self, "globalVerticalRecoil", self.gVerticalRecoilEntry, line)
                importValue(self, "globalHorizontalRecoil", self.gHorizontalRecoilEntry, line)
                importValue(self, "globalConvergence", self.gConvergenceEntry, line)
                importValue(self, "globalDispersion", self.gDispersionEntry, line)
                importValue(self, "globalCameraRecoil", self.gCameraRecoilEntry, line)
                importValue(self, "globalCameraSnap", self.gCameraSnapEntry, line)

                importValue(self, "aimPunch", self.aimPunchEntry, line)
                importValue(self, "recoilDamping", self.recoilDampingEntry, line)
                importValue(self, "recoilHandDamping", self.recoilHandDampingEntry, line)
                importValue(self, "aimProceduralIntensity", self.aimProceduralIntensityEntry, line)

                importValue(self, "pistolVerticalRecoil", self.pistolVerticalRecoilEntry, line)
                importValue(self, "pistolHorizontalRecoil", self.pistolHorizontalRecoilEntry, line)
                importValue(self, "pistolConvergence", self.pistolConvergenceEntry, line)
                importValue(self, "pistolDispersion", self.pistolDispersionEntry, line)
                importValue(self, "pistolCameraRecoil", self.pistolCameraRecoilEntry, line)
                importValue(self, "pistolCameraSnap", self.pistolCameraSnapEntry, line)

                importValue(self, "smgVerticalRecoil", self.smgVerticalRecoilEntry, line)
                importValue(self, "smgHorizontalRecoil", self.smgHorizontalRecoilEntry, line)
                importValue(self, "smgConvergence", self.smgConvergenceEntry, line)
                importValue(self, "smgDispersion", self.smgDispersionEntry, line)
                importValue(self, "smgCameraRecoil", self.smgCameraRecoilEntry, line)
                importValue(self, "smgCameraSnap", self.smgCameraSnapEntry, line)

                importValue(self, "shotgunVerticalRecoil", self.shotgunVerticalRecoilEntry, line)
                importValue(self, "shotgunHorizontalRecoil", self.shotgunHorizontalRecoilEntry, line)
                importValue(self, "shotgunConvergence", self.shotgunConvergenceEntry, line)
                importValue(self, "shotgunDispersion", self.shotgunDispersionEntry, line)
                importValue(self, "shotgunCameraRecoil", self.shotgunCameraRecoilEntry, line)
                importValue(self, "shotgunCameraSnap", self.shotgunCameraSnapEntry, line)

                importValue(self, "carbineVerticalRecoil", self.acVerticalRecoilEntry, line)
                importValue(self, "carbineHorizontalRecoil", self.acHorizontalRecoilEntry, line)
                importValue(self, "carbineConvergence", self.acConvergenceEntry, line)
                importValue(self, "carbineDispersion", self.acDispersionEntry, line)
                importValue(self, "carbineCameraRecoil", self.acCameraRecoilEntry, line)
                importValue(self, "carbineCameraSnap", self.acCameraSnapEntry, line)

                importValue(self, "rifleVerticalRecoil", self.arVerticalRecoilEntry, line)
                importValue(self, "rifleHorizontalRecoil", self.arHorizontalRecoilEntry, line)
                importValue(self, "rifleConvergence", self.arConvergenceEntry, line)
                importValue(self, "rifleDispersion", self.arDispersionEntry, line)
                importValue(self, "rifleCameraRecoil", self.arCameraRecoilEntry, line)
                importValue(self, "rifleCameraSnap", self.arCameraSnapEntry, line)

                importValue(self, "mgVerticalRecoil", self.lmgVerticalRecoilEntry, line)
                importValue(self, "mgHorizontalRecoil", self.lmgHorizontalRecoilEntry, line)
                importValue(self, "mgConvergence", self.lmgConvergenceEntry, line)
                importValue(self, "mgDispersion", self.lmgDispersionEntry, line)
                importValue(self, "mgCameraRecoil", self.lmgCameraRecoilEntry, line)
                importValue(self, "mgCameraSnap", self.lmgCameraSnapEntry, line)

                importValue(self, "marksmanVerticalRecoil", self.mkVerticalRecoilEntry, line)
                importValue(self, "marksmanHorizontalRecoil", self.mkHorizontalRecoilEntry, line)
                importValue(self, "marksmanConvergence", self.mkConvergenceEntry, line)
                importValue(self, "marksmanDispersion", self.mkDispersionEntry, line)
                importValue(self, "marksmanCameraRecoil", self.mkCameraRecoilEntry, line)
                importValue(self, "marksmanCameraSnap", self.mkCameraSnapEntry, line)

                importValue(self, "sniperVerticalRecoil", self.sniperVerticalRecoilEntry, line)
                importValue(self, "sniperHorizontalRecoil", self.sniperHorizontalRecoilEntry, line)
                importValue(self, "sniperConvergence", self.sniperConvergenceEntry, line)
                importValue(self, "sniperDispersion", self.sniperDispersionEntry, line)
                importValue(self, "sniperCameraRecoil", self.sniperCameraRecoilEntry, line)
                importValue(self, "sniperCameraSnap", self.sniperCameraSnapEntry, line)

                importFile.close()

            CTkMessagebox(title="Import", icon="check", message="Successfully imported from: " + filename)


        except FileNotFoundError:
            print("File not found!")
            msg = CTkMessagebox(title="Import", icon="cancel", message="Could not open: " + filename + "\n\nWould you like to create a new file instead?", option_1="No", option_2="Yes")
            if msg.get() == "Yes":
                try:
                    open(filename, "x")
                    self.defaultFunction()
                    CTkMessagebox(title="Import", icon="check", message="File created! Please click export again to save changes!")
                except FileExistsError:
                    CTkMessagebox(title="Import", icon="cancel", message="File already exists? Stop messing me around.")

        self.savedPath = filename


    def exportFunction(self, path=""):
        if not path == "":
            filename = path + '/config.json'
            response = "Yes"
        else:
            filename = os.path.dirname(__file__) + '/../config/config.json'
            msg = CTkMessagebox(title="Export", message="Are you sure you want to export current settings?", icon="question", option_1="No", option_2="Yes")
            response = msg.get()

        if response == "Yes":
            try:
                exportFile = open(filename, 'w')
                exportFile.write('{\n\n')
                if(self.globalToggle.get() == 0):
                    exportFile.write('\t"globalToggle": false,\n')
                else:
                    exportFile.write('\t"globalToggle": true,\n')
                if(self.classToggle.get() == 0):
                    exportFile.write('\t"weaponClassToggle": false,\n')
                else:
                    exportFile.write('\t"weaponClassToggle": true,\n')

                exportFile.write('\t"individualWeaponToggle": false,\n') # <--- Temporary

                if(self.hiddenBonusToggle.get() == 0):
                    exportFile.write('\t"hiddenBonusRecoilToggle": false,\n')
                else:
                    exportFile.write('\t"hiddenBonusRecoilToggle": true,\n')

                if(self.recoilCrankToggle.get() == 0):
                    exportFile.write('\t"recoilCrank": false,\n')
                else:
                    exportFile.write('\t"recoilCrank": true,\n\n')

                exportFile.write('\t"globalVerticalRecoil": ' + str(self.gVerticalRecoilEntry.get()) + ',\n')
                exportFile.write('\t"globalHorizontalRecoil": ' + str(self.gHorizontalRecoilEntry.get()) + ',\n')
                exportFile.write('\t"globalConvergence": ' + str(self.gConvergenceEntry.get()) + ',\n')
                exportFile.write('\t"globalDispersion": ' + str(self.gDispersionEntry.get()) + ',\n')
                exportFile.write('\t"globalCameraRecoil": ' + str(self.gCameraRecoilEntry.get()) + ',\n')
                exportFile.write('\t"globalCameraSnap": ' + str(self.gCameraSnapEntry.get()) + ',\n\n')

                exportFile.write('\t"aimPunch": ' + str(self.aimPunchEntry.get()) + ',\n')
                exportFile.write('\t"recoilDamping": ' + str(self.recoilDampingEntry.get()) + ',\n')
                exportFile.write('\t"recoilHandDamping": ' + str(self.recoilHandDampingEntry.get()) + ',\n')
                exportFile.write('\t"aimProceduralIntensity": ' + str(self.aimProceduralIntensityEntry.get()) + ',\n\n')

                exportFile.write('\t"pistolVerticalRecoil": ' + str(self.pistolVerticalRecoilEntry.get()) + ',\n')
                exportFile.write('\t"pistolHorizontalRecoil": ' + str(self.pistolHorizontalRecoilEntry.get()) + ',\n')
                exportFile.write('\t"pistolConvergence": ' + str(self.pistolConvergenceEntry.get()) + ',\n')
                exportFile.write('\t"pistolDispersion": ' + str(self.pistolDispersionEntry.get()) + ',\n')
                exportFile.write('\t"pistolCameraRecoil": ' + str(self.pistolCameraRecoilEntry.get()) + ',\n')
                exportFile.write('\t"pistolCameraSnap": ' + str(self.pistolCameraSnapEntry.get()) + ',\n\n')

                exportFile.write('\t"smgVerticalRecoil": ' + str(self.smgVerticalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"smgHorizontalRecoil": ' + str(self.smgHorizontalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"smgConvergence": ' + str(self.smgConvergenceEntry.get() + ',\n'))
                exportFile.write('\t"smgDispersion": ' + str(self.smgDispersionEntry.get() + ',\n'))
                exportFile.write('\t"smgCameraRecoil": ' + str(self.smgCameraRecoilEntry.get() + ',\n'))
                exportFile.write('\t"smgCameraSnap": ' + str(self.smgCameraSnapEntry.get() + ',\n\n'))

                exportFile.write('\t"shotgunVerticalRecoil": ' + str(self.shotgunVerticalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"shotgunHorizontalRecoil": ' + str(self.shotgunHorizontalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"shotgunConvergence": ' + str(self.shotgunConvergenceEntry.get() + ',\n'))
                exportFile.write('\t"shotgunDispersion": ' + str(self.shotgunDispersionEntry.get() + ',\n'))
                exportFile.write('\t"shotgunCameraRecoil": ' + str(self.shotgunCameraRecoilEntry.get() + ',\n'))
                exportFile.write('\t"shotgunCameraSnap": ' + str(self.shotgunCameraSnapEntry.get() + ',\n\n'))

                exportFile.write('\t"carbineVerticalRecoil": ' + str(self.acVerticalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"carbineHorizontalRecoil": ' + str(self.acHorizontalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"carbineConvergence": ' + str(self.acConvergenceEntry.get() + ',\n'))
                exportFile.write('\t"carbineDispersion": ' + str(self.acDispersionEntry.get() + ',\n'))
                exportFile.write('\t"carbineCameraRecoil": ' + str(self.acCameraRecoilEntry.get() + ',\n'))
                exportFile.write('\t"carbineCameraSnap": ' + str(self.acCameraSnapEntry.get() + ',\n\n'))

                exportFile.write('\t"rifleVerticalRecoil": ' + str(self.arVerticalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"rifleHorizontalRecoil": ' + str(self.arHorizontalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"rifleConvergence": ' + str(self.arConvergenceEntry.get() + ',\n'))
                exportFile.write('\t"rifleDispersion": ' + str(self.arDispersionEntry.get() + ',\n'))
                exportFile.write('\t"rifleCameraRecoil": ' + str(self.arCameraRecoilEntry.get() + ',\n'))
                exportFile.write('\t"rifleCameraSnap": ' + str(self.arCameraSnapEntry.get() + ',\n\n'))

                exportFile.write('\t"mgVerticalRecoil": ' + str(self.lmgVerticalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"mgHorizontalRecoil": ' + str(self.lmgHorizontalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"mgConvergence": ' + str(self.lmgConvergenceEntry.get() + ',\n'))
                exportFile.write('\t"mgDispersion": ' + str(self.lmgDispersionEntry.get() + ',\n'))
                exportFile.write('\t"mgCameraRecoil": ' + str(self.lmgCameraRecoilEntry.get() + ',\n'))
                exportFile.write('\t"mgCameraSnap": ' + str(self.lmgCameraSnapEntry.get() + ',\n\n'))

                exportFile.write('\t"marksmanVerticalRecoil": ' + str(self.mkVerticalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"marksmanHorizontalRecoil": ' + str(self.mkHorizontalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"marksmanConvergence": ' + str(self.mkConvergenceEntry.get() + ',\n'))
                exportFile.write('\t"marksmanDispersion": ' + str(self.mkDispersionEntry.get() + ',\n'))
                exportFile.write('\t"marksmanCameraRecoil": ' + str(self.mkCameraRecoilEntry.get() + ',\n'))
                exportFile.write('\t"marksmanCameraSnap": ' + str(self.mkCameraSnapEntry.get() + ',\n\n'))

                exportFile.write('\t"sniperVerticalRecoil": ' + str(self.sniperVerticalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"sniperHorizontalRecoil": ' + str(self.sniperHorizontalRecoilEntry.get() + ',\n'))
                exportFile.write('\t"sniperConvergence": ' + str(self.sniperConvergenceEntry.get() + ',\n'))
                exportFile.write('\t"sniperDispersion": ' + str(self.sniperDispersionEntry.get() + ',\n'))
                exportFile.write('\t"sniperCameraRecoil": ' + str(self.sniperCameraRecoilEntry.get() + ',\n'))
                exportFile.write('\t"sniperCameraSnap": ' + str(self.sniperCameraSnapEntry.get() + ',\n\n'))

                exportFile.write('\t"RecoilXIntensityByPoseX": 1,\n')
                exportFile.write('\t"RecoilXIntensityByPoseY": 1,\n')
                exportFile.write('\t"RecoilXIntensityByPoseZ": 1,\n')
                exportFile.write('\t"RecoilYIntensityByPoseX": 1,\n')
                exportFile.write('\t"RecoilYIntensityByPoseY": 1,\n')
                exportFile.write('\t"RecoilYIntensityByPoseZ": 1,\n')
                exportFile.write('\t"RecoilZIntensityByPoseX": 1,\n')
                exportFile.write('\t"RecoilZIntensityByPoseY": 1,\n')
                exportFile.write('\t"RecoilZIntensityByPoseZ": 1,\n')
                exportFile.write('\t"ProceduralIntensityByPoseX": 1,\n')
                exportFile.write('\t"ProceduralIntensityByPoseY": 1,\n')
                exportFile.write('\t"ProceduralIntensityByPoseZ": 1\n')
                exportFile.write('}')
                exportFile.close()
                CTkMessagebox(title="Export", icon="check", message="Successfully exported to: " + filename)

            except FileNotFoundError:
                msg = CTkMessagebox(title="Export", icon="cancel", message="Could not export to: " + filename)

    def defaultFunction(self):

        def changeValue(entry, value):
            if(len(entry.get()) > 0):
                    entry.delete(0, tk.END)
            entry.insert(0, value)

        msg = CTkMessagebox(title="Defaults", icon="question", message="Are you sure you want to reset all values back to their defaults?", option_1="No", option_2="Yes")

        if msg.get() == "Yes":
            self.globalToggle.select()
            self.classToggle.deselect()
            self.hiddenBonusToggle.select()
            self.recoilCrankToggle.deselect()
            for table in self.allValues:
                for entry in table:
                    changeValue(entry, 1)

    def findPresets(self):
        newPath = os.path.dirname(__file__) + '/../presets/'
        presetList = next(os.walk(newPath))[1]
        return presetList;

    def loadPreset(self):
        curPreset = self.presetCombobox.get()
        configFile = os.path.dirname(__file__) + '/../presets/' + curPreset + "/config.json"
        self.importFunction(configFile)

    def savePreset(self):
        curPreset = self.presetCombobox.get()
        pathPreset = os.path.dirname(__file__) + '/../presets/' + curPreset
        if not os.path.exists(pathPreset):
            try:
                os.mkdir(pathPreset)
            except FileExistsError:
                print("Directory already exists!")
        self.presetCombobox.configure(values=self.findPresets())
        self.exportFunction(pathPreset)

    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("Recoil Config Editor")
        self.savedPath = ""
        self.buttonFont = customtkinter.CTkFont(family="Roboto", size=14)
        self.toolTipFont = customtkinter.CTkFont(family="Roboto", size=12)

        # Tab View

        self.tabview = customtkinter.CTkTabview(master=self)
        self.tabview.pack(padx=10, pady=10, fill="both", expand=True)
        self.toggleTab = self.tabview.add("Toggles")
        self.globalsTab = self.tabview.add("Main Globals")
        self.advTab = self.tabview.add("Advanced Globals")
        self.classTab = self.tabview.add("Weapon Class Values")
        # self.weaponTab = self.tabview.add("Specific Weapon Values")

        # Buttons

        self.importButton = customtkinter.CTkButton(
            master=self, font=self.buttonFont, text="Import", width=100, height=30, command=self.importFunction)
        self.importButton.pack(padx=10, pady=10, side="left")
        self.exportButton = customtkinter.CTkButton(
            master=self, font=self.buttonFont, text="Export", width=100, height=30, command=self.exportFunction)
        self.exportButton.pack(padx=10, pady=10, side="left")
        self.defaultButton = customtkinter.CTkButton(
            master=self, font=self.buttonFont, text="Defaults", width=100, height=30, command=self.defaultFunction)
        self.defaultButton.pack(padx=10, pady=10, side="left")
        self.presetCombobox = customtkinter.CTkComboBox(
            master=self, font=self.buttonFont, values=self.findPresets(), width=150, height=30)
        self.presetCombobox.pack(padx=10, pady=10, side="left")
        self.loadPresetButton = customtkinter.CTkButton(
            master=self, font=self.buttonFont, text="Load Preset", width=100, height=30, command=self.loadPreset)
        self.loadPresetButton.pack(padx=10, pady=10, side="left")
        self.savePresetButton = customtkinter.CTkButton(
            master=self, font=self.buttonFont, text="Save Preset", width=100, height=30, command=self.savePreset)
        self.savePresetButton.pack(padx=10, pady=10, side="left")

        # Toggle Tab
        self.globalToggle = customtkinter.CTkSwitch(
            master=self.toggleTab, text="Global Toggle", font=self.buttonFont)
        self.globalToggle.grid(padx=10, pady=10, column=0, row=0, sticky="w")
        ToolTip(self.globalToggle, msg="Toggle on if you want to set every weapon's recoil.", delay=0.5, parent_kwargs={"bg": "black", "padx": 1, "pady": 1},
        fg="#ffffff", bg="#1c1c1c", padx=10, pady=10, font=self.toolTipFont)
        self.globalToggle.select()

        self.classToggle = customtkinter.CTkSwitch(
            master=self.toggleTab, text="Weapon Class Toggle", font=self.buttonFont)
        self.classToggle.grid(padx=10, pady=10, column=0, row=1, sticky="w")
        ToolTip(self.classToggle, msg="Toggle on if you want to set class-wide recoil.", delay=0.5, parent_kwargs={"bg": "black", "padx": 1, "pady": 1},
        fg="#ffffff", bg="#1c1c1c", padx=10, pady=10, font=self.toolTipFont)

        # self.weaponToggle = customtkinter.CTkSwitch(
        #     master=self.toggleTab, text="Individual Weapon Toggle", font=self.buttonFont)
        # self.weaponToggle.grid(padx=10, pady=10, column=0, row=2, sticky="w")
        # ToolTip(self.weaponToggle, msg="Toggle on if you want to set specific weapons recoil.", delay=0.5, parent_kwargs={"bg": "black", "padx": 1, "pady": 1},
        # fg="#ffffff", bg="#1c1c1c", padx=10, pady=10, font=self.toolTipFont)

        self.hiddenBonusToggle = customtkinter.CTkSwitch(
            master=self.toggleTab, text="Hidden Recoil Bonus Toggle", font=self.buttonFont)
        self.hiddenBonusToggle.grid(padx=10, pady=10, column=0, row=3, sticky="w")
        ToolTip(self.hiddenBonusToggle, msg="Tarkov has a hidden recoil value added to all guns that won't show in game. Toggling this on will turn that back on.", delay=0.5, parent_kwargs={"bg": "black", "padx": 1, "pady": 1},
        fg="#ffffff", bg="#1c1c1c", padx=10, pady=10, font=self.toolTipFont)

        self.recoilCrankToggle = customtkinter.CTkSwitch(
            master=self.toggleTab, text="Recoil Crank", font=self.buttonFont)
        self.recoilCrankToggle.grid(padx=10, pady=10, column=0, row=4, sticky="w")

        # Global Values

        self.gVerticalRecoilLabel = customtkinter.CTkLabel(
            master=self.globalsTab, text="Vertical Recoil", font=self.buttonFont)
        self.gVerticalRecoilLabel.grid(padx=10, pady=10, column=0, row=0)
        self.gVerticalRecoilEntry = customtkinter.CTkEntry(
            master=self.globalsTab)
        self.gVerticalRecoilEntry.grid(padx=10, pady=10, column=1, row=0)

        self.gHorizontalRecoilLabel = customtkinter.CTkLabel(
            master=self.globalsTab, text="Horizontal Recoil", font=self.buttonFont)
        self.gHorizontalRecoilLabel.grid(padx=10, pady=10, column=0, row=1)
        self.gHorizontalRecoilEntry = customtkinter.CTkEntry(
            master=self.globalsTab)
        self.gHorizontalRecoilEntry.grid(padx=10, pady=10, column=1, row=1)

        self.gConvergenceLabel = customtkinter.CTkLabel(
            master=self.globalsTab, text="Convergence", font=self.buttonFont)
        self.gConvergenceLabel.grid(padx=10, pady=10, column=0, row=2)
        self.gConvergenceEntry = customtkinter.CTkEntry(
            master=self.globalsTab)
        self.gConvergenceEntry.grid(padx=10, pady=10, column=1, row=2)

        self.gDispersionLabel = customtkinter.CTkLabel(
            master=self.globalsTab, text="Dispersion", font=self.buttonFont)
        self.gDispersionLabel.grid(padx=10, pady=10, column=0, row=3)
        self.gDispersionEntry = customtkinter.CTkEntry(
            master=self.globalsTab)
        self.gDispersionEntry.grid(padx=10, pady=10, column=1, row=3)

        self.gCameraRecoilLabel = customtkinter.CTkLabel(
            master=self.globalsTab, text="Camera Recoil", font=self.buttonFont)
        self.gCameraRecoilLabel.grid(padx=10, pady=10, column=0, row=4)
        self.gCameraRecoilEntry = customtkinter.CTkEntry(
            master=self.globalsTab)
        self.gCameraRecoilEntry.grid(padx=10, pady=10, column=1, row=4)

        self.gCameraSnapLabel = customtkinter.CTkLabel(
            master=self.globalsTab, text="Camera Snap", font=self.buttonFont)
        self.gCameraSnapLabel.grid(padx=10, pady=10, column=0, row=5)
        self.gCameraSnapEntry = customtkinter.CTkEntry(
            master=self.globalsTab)
        self.gCameraSnapEntry.grid(padx=10, pady=10, column=1, row=5)

        # Advanced Globals

        self.aimPunchLabel = customtkinter.CTkLabel(
            master=self.advTab, text="Aim Punch", font=self.buttonFont)
        self.aimPunchLabel.grid(padx=10, pady=10, column=0, row=0)
        self.aimPunchEntry = customtkinter.CTkEntry(
            master=self.advTab)
        self.aimPunchEntry.grid(padx=10, pady=10, column=1, row=0)

        self.recoilDampingLabel = customtkinter.CTkLabel(
            master=self.advTab, text="Recoil Damping", font=self.buttonFont)
        self.recoilDampingLabel.grid(padx=10, pady=10, column=0, row=1)
        self.recoilDampingEntry = customtkinter.CTkEntry(
            master=self.advTab)
        self.recoilDampingEntry.grid(padx=10, pady=10, column=1, row=1)

        self.recoilHandDampingLabel = customtkinter.CTkLabel(
            master=self.advTab, text="Recoil Hand Damping", font=self.buttonFont)
        self.recoilHandDampingLabel.grid(padx=10, pady=10, column=0, row=2)
        self.recoilHandDampingEntry = customtkinter.CTkEntry(
            master=self.advTab)
        self.recoilHandDampingEntry.grid(padx=10, pady=10, column=1, row=2)

        self.aimProceduralIntensityLabel = customtkinter.CTkLabel(
            master=self.advTab, text="ADS Aim Sway", font=self.buttonFont)
        self.aimProceduralIntensityLabel.grid(padx=10, pady=10, column=0, row=3)
        self.aimProceduralIntensityEntry = customtkinter.CTkEntry(
            master=self.advTab)
        self.aimProceduralIntensityEntry.grid(padx=10, pady=10, column=1, row=3)

        # Class Weapons Tabs

        self.weaponClassTab = customtkinter.CTkTabview(master=self.classTab)
        self.weaponClassTab.pack(padx=10, pady=10, fill="both", expand=True)
        self.pistolTab = self.weaponClassTab.add("Pistols")
        self.smgTab = self.weaponClassTab.add("SMGs")
        self.shotgunTab = self.weaponClassTab.add("Shotguns")
        self.assaultCarbineTab = self.weaponClassTab.add("Assault Carbines")
        self.assaultRifleTab = self.weaponClassTab.add("Assault Rifles")
        self.lmgTab = self.weaponClassTab.add("Machine Guns")
        self.marksmanTab = self.weaponClassTab.add("Marksman Rifles")
        self.sniperTab = self.weaponClassTab.add("Sniper Rifles")

        # Pistol Tab

        self.pistolVerticalRecoilLabel = customtkinter.CTkLabel(
            master=self.pistolTab, text="Vertical Recoil", font=self.buttonFont)
        self.pistolVerticalRecoilLabel.grid(padx=10, pady=10, column=0, row=0)
        self.pistolVerticalRecoilEntry = customtkinter.CTkEntry(
            master=self.pistolTab)
        self.pistolVerticalRecoilEntry.grid(padx=10, pady=10, column=1, row=0)
        self.pistolHorizontalRecoilLabel = customtkinter.CTkLabel(
            master=self.pistolTab, text="Horizontal Recoil", font=self.buttonFont)
        self.pistolHorizontalRecoilLabel.grid(padx=10, pady=10, column=0, row=1)
        self.pistolHorizontalRecoilEntry = customtkinter.CTkEntry(
            master=self.pistolTab)
        self.pistolHorizontalRecoilEntry.grid(padx=10, pady=10, column=1, row=1)
        self.pistolConvergenceLabel = customtkinter.CTkLabel(
            master=self.pistolTab, text="Convergence", font=self.buttonFont)
        self.pistolConvergenceLabel.grid(padx=10, pady=10, column=0, row=2)
        self.pistolConvergenceEntry = customtkinter.CTkEntry(
            master=self.pistolTab)
        self.pistolConvergenceEntry.grid(padx=10, pady=10, column=1, row=2)
        self.pistolDispersionLabel = customtkinter.CTkLabel(
            master=self.pistolTab, text="Dispersion", font=self.buttonFont)
        self.pistolDispersionLabel.grid(padx=10, pady=10, column=0, row=3)
        self.pistolDispersionEntry = customtkinter.CTkEntry(
            master=self.pistolTab)
        self.pistolDispersionEntry.grid(padx=10, pady=10, column=1, row=3)
        self.pistolCameraRecoilLabel = customtkinter.CTkLabel(
            master=self.pistolTab, text="Camera Recoil", font=self.buttonFont)
        self.pistolCameraRecoilLabel.grid(padx=10, pady=10, column=0, row=4)
        self.pistolCameraRecoilEntry = customtkinter.CTkEntry(
            master=self.pistolTab)
        self.pistolCameraRecoilEntry.grid(padx=10, pady=10, column=1, row=4)
        self.pistolCameraSnapLabel = customtkinter.CTkLabel(
            master=self.pistolTab, text="Camera Snap", font=self.buttonFont)
        self.pistolCameraSnapLabel.grid(padx=10, pady=10, column=0, row=5)
        self.pistolCameraSnapEntry = customtkinter.CTkEntry(
            master=self.pistolTab)
        self.pistolCameraSnapEntry.grid(padx=10, pady=10, column=1, row=5)

        # SMG Tab

        self.smgVerticalRecoilLabel = customtkinter.CTkLabel(
            master=self.smgTab, text="Vertical Recoil", font=self.buttonFont)
        self.smgVerticalRecoilLabel.grid(padx=10, pady=10, column=0, row=0)
        self.smgVerticalRecoilEntry = customtkinter.CTkEntry(
            master=self.smgTab)
        self.smgVerticalRecoilEntry.grid(padx=10, pady=10, column=1, row=0)
        self.smgHorizontalRecoilLabel = customtkinter.CTkLabel(
            master=self.smgTab, text="Horizontal Recoil", font=self.buttonFont)
        self.smgHorizontalRecoilLabel.grid(padx=10, pady=10, column=0, row=1)
        self.smgHorizontalRecoilEntry = customtkinter.CTkEntry(
            master=self.smgTab)
        self.smgHorizontalRecoilEntry.grid(padx=10, pady=10, column=1, row=1)
        self.smgConvergenceLabel = customtkinter.CTkLabel(
            master=self.smgTab, text="Convergence", font=self.buttonFont)
        self.smgConvergenceLabel.grid(padx=10, pady=10, column=0, row=2)
        self.smgConvergenceEntry = customtkinter.CTkEntry(
            master=self.smgTab)
        self.smgConvergenceEntry.grid(padx=10, pady=10, column=1, row=2)
        self.smgDispersionLabel = customtkinter.CTkLabel(
            master=self.smgTab, text="Dispersion", font=self.buttonFont)
        self.smgDispersionLabel.grid(padx=10, pady=10, column=0, row=3)
        self.smgDispersionEntry = customtkinter.CTkEntry(
            master=self.smgTab)
        self.smgDispersionEntry.grid(padx=10, pady=10, column=1, row=3)
        self.smgCameraRecoilLabel = customtkinter.CTkLabel(
            master=self.smgTab, text="Camera Recoil", font=self.buttonFont)
        self.smgCameraRecoilLabel.grid(padx=10, pady=10, column=0, row=4)
        self.smgCameraRecoilEntry = customtkinter.CTkEntry(
            master=self.smgTab)
        self.smgCameraRecoilEntry.grid(padx=10, pady=10, column=1, row=4)
        self.smgCameraSnapLabel = customtkinter.CTkLabel(
            master=self.smgTab, text="Camera Snap", font=self.buttonFont)
        self.smgCameraSnapLabel.grid(padx=10, pady=10, column=0, row=5)
        self.smgCameraSnapEntry = customtkinter.CTkEntry(
            master=self.smgTab)
        self.smgCameraSnapEntry.grid(padx=10, pady=10, column=1, row=5)

        # Shotgun Tab

        self.shotgunVerticalRecoilLabel = customtkinter.CTkLabel(
            master=self.shotgunTab, text="Vertical Recoil", font=self.buttonFont)
        self.shotgunVerticalRecoilLabel.grid(padx=10, pady=10, column=0, row=0)
        self.shotgunVerticalRecoilEntry = customtkinter.CTkEntry(
            master=self.shotgunTab)
        self.shotgunVerticalRecoilEntry.grid(padx=10, pady=10, column=1, row=0)
        self.shotgunHorizontalRecoilLabel = customtkinter.CTkLabel(
            master=self.shotgunTab, text="Horizontal Recoil", font=self.buttonFont)
        self.shotgunHorizontalRecoilLabel.grid(padx=10, pady=10, column=0, row=1)
        self.shotgunHorizontalRecoilEntry = customtkinter.CTkEntry(
            master=self.shotgunTab)
        self.shotgunHorizontalRecoilEntry.grid(padx=10, pady=10, column=1, row=1)
        self.shotgunConvergenceLabel = customtkinter.CTkLabel(
            master=self.shotgunTab, text="Convergence", font=self.buttonFont)
        self.shotgunConvergenceLabel.grid(padx=10, pady=10, column=0, row=2)
        self.shotgunConvergenceEntry = customtkinter.CTkEntry(
            master=self.shotgunTab)
        self.shotgunConvergenceEntry.grid(padx=10, pady=10, column=1, row=2)
        self.shotgunDispersionLabel = customtkinter.CTkLabel(
            master=self.shotgunTab, text="Dispersion", font=self.buttonFont)
        self.shotgunDispersionLabel.grid(padx=10, pady=10, column=0, row=3)
        self.shotgunDispersionEntry = customtkinter.CTkEntry(
            master=self.shotgunTab)
        self.shotgunDispersionEntry.grid(padx=10, pady=10, column=1, row=3)
        self.shotgunCameraRecoilLabel = customtkinter.CTkLabel(
            master=self.shotgunTab, text="Camera Recoil", font=self.buttonFont)
        self.shotgunCameraRecoilLabel.grid(padx=10, pady=10, column=0, row=4)
        self.shotgunCameraRecoilEntry = customtkinter.CTkEntry(
            master=self.shotgunTab)
        self.shotgunCameraRecoilEntry.grid(padx=10, pady=10, column=1, row=4)
        self.shotgunCameraSnapLabel = customtkinter.CTkLabel(
            master=self.shotgunTab, text="Camera Snap", font=self.buttonFont)
        self.shotgunCameraSnapLabel.grid(padx=10, pady=10, column=0, row=5)
        self.shotgunCameraSnapEntry = customtkinter.CTkEntry(
            master=self.shotgunTab)
        self.shotgunCameraSnapEntry.grid(padx=10, pady=10, column=1, row=5)

        # Assault Carbines

        self.acVerticalRecoilLabel = customtkinter.CTkLabel(
            master=self.assaultCarbineTab, text="Vertical Recoil", font=self.buttonFont)
        self.acVerticalRecoilLabel.grid(padx=10, pady=10, column=0, row=0)
        self.acVerticalRecoilEntry = customtkinter.CTkEntry(
            master=self.assaultCarbineTab)
        self.acVerticalRecoilEntry.grid(padx=10, pady=10, column=1, row=0)
        self.acHorizontalRecoilLabel = customtkinter.CTkLabel(
            master=self.assaultCarbineTab, text="Horizontal Recoil", font=self.buttonFont)
        self.acHorizontalRecoilLabel.grid(padx=10, pady=10, column=0, row=1)
        self.acHorizontalRecoilEntry = customtkinter.CTkEntry(
            master=self.assaultCarbineTab)
        self.acHorizontalRecoilEntry.grid(padx=10, pady=10, column=1, row=1)
        self.acConvergenceLabel = customtkinter.CTkLabel(
            master=self.assaultCarbineTab, text="Convergence", font=self.buttonFont)
        self.acConvergenceLabel.grid(padx=10, pady=10, column=0, row=2)
        self.acConvergenceEntry = customtkinter.CTkEntry(
            master=self.assaultCarbineTab)
        self.acConvergenceEntry.grid(padx=10, pady=10, column=1, row=2)
        self.acDispersionLabel = customtkinter.CTkLabel(
            master=self.assaultCarbineTab, text="Dispersion", font=self.buttonFont)
        self.acDispersionLabel.grid(padx=10, pady=10, column=0, row=3)
        self.acDispersionEntry = customtkinter.CTkEntry(
            master=self.assaultCarbineTab)
        self.acDispersionEntry.grid(padx=10, pady=10, column=1, row=3)
        self.acCameraRecoilLabel = customtkinter.CTkLabel(
            master=self.assaultCarbineTab, text="Camera Recoil", font=self.buttonFont)
        self.acCameraRecoilLabel.grid(padx=10, pady=10, column=0, row=4)
        self.acCameraRecoilEntry = customtkinter.CTkEntry(
            master=self.assaultCarbineTab)
        self.acCameraRecoilEntry.grid(padx=10, pady=10, column=1, row=4)
        self.acCameraSnapLabel = customtkinter.CTkLabel(
            master=self.assaultCarbineTab, text="Camera Snap", font=self.buttonFont)
        self.acCameraSnapLabel.grid(padx=10, pady=10, column=0, row=5)
        self.acCameraSnapEntry = customtkinter.CTkEntry(
            master=self.assaultCarbineTab)
        self.acCameraSnapEntry.grid(padx=10, pady=10, column=1, row=5)

        # Assault Rifles

        self.arVerticalRecoilLabel = customtkinter.CTkLabel(
            master=self.assaultRifleTab, text="Vertical Recoil", font=self.buttonFont)
        self.arVerticalRecoilLabel.grid(padx=10, pady=10, column=0, row=0)
        self.arVerticalRecoilEntry = customtkinter.CTkEntry(
            master=self.assaultRifleTab)
        self.arVerticalRecoilEntry.grid(padx=10, pady=10, column=1, row=0)
        self.arHorizontalRecoilLabel = customtkinter.CTkLabel(
            master=self.assaultRifleTab, text="Horizontal Recoil", font=self.buttonFont)
        self.arHorizontalRecoilLabel.grid(padx=10, pady=10, column=0, row=1)
        self.arHorizontalRecoilEntry = customtkinter.CTkEntry(
            master=self.assaultRifleTab)
        self.arHorizontalRecoilEntry.grid(padx=10, pady=10, column=1, row=1)
        self.arConvergenceLabel = customtkinter.CTkLabel(
            master=self.assaultRifleTab, text="Convergence", font=self.buttonFont)
        self.arConvergenceLabel.grid(padx=10, pady=10, column=0, row=2)
        self.arConvergenceEntry = customtkinter.CTkEntry(
            master=self.assaultRifleTab)
        self.arConvergenceEntry.grid(padx=10, pady=10, column=1, row=2)
        self.arDispersionLabel = customtkinter.CTkLabel(
            master=self.assaultRifleTab, text="Dispersion", font=self.buttonFont)
        self.arDispersionLabel.grid(padx=10, pady=10, column=0, row=3)
        self.arDispersionEntry = customtkinter.CTkEntry(
            master=self.assaultRifleTab)
        self.arDispersionEntry.grid(padx=10, pady=10, column=1, row=3)
        self.arCameraRecoilLabel = customtkinter.CTkLabel(
            master=self.assaultRifleTab, text="Camera Recoil", font=self.buttonFont)
        self.arCameraRecoilLabel.grid(padx=10, pady=10, column=0, row=4)
        self.arCameraRecoilEntry = customtkinter.CTkEntry(
            master=self.assaultRifleTab)
        self.arCameraRecoilEntry.grid(padx=10, pady=10, column=1, row=4)
        self.arCameraSnapLabel = customtkinter.CTkLabel(
            master=self.assaultRifleTab, text="Camera Snap", font=self.buttonFont)
        self.arCameraSnapLabel.grid(padx=10, pady=10, column=0, row=5)
        self.arCameraSnapEntry = customtkinter.CTkEntry(
            master=self.assaultRifleTab)
        self.arCameraSnapEntry.grid(padx=10, pady=10, column=1, row=5)

        # Machine Guns

        self.lmgVerticalRecoilLabel = customtkinter.CTkLabel(
            master=self.lmgTab, text="Vertical Recoil", font=self.buttonFont)
        self.lmgVerticalRecoilLabel.grid(padx=10, pady=10, column=0, row=0)
        self.lmgVerticalRecoilEntry = customtkinter.CTkEntry(
            master=self.lmgTab)
        self.lmgVerticalRecoilEntry.grid(padx=10, pady=10, column=1, row=0)
        self.lmgHorizontalRecoilLabel = customtkinter.CTkLabel(
            master=self.lmgTab, text="Horizontal Recoil", font=self.buttonFont)
        self.lmgHorizontalRecoilLabel.grid(padx=10, pady=10, column=0, row=1)
        self.lmgHorizontalRecoilEntry = customtkinter.CTkEntry(
            master=self.lmgTab)
        self.lmgHorizontalRecoilEntry.grid(padx=10, pady=10, column=1, row=1)
        self.lmgConvergenceLabel = customtkinter.CTkLabel(
            master=self.lmgTab, text="Convergence", font=self.buttonFont)
        self.lmgConvergenceLabel.grid(padx=10, pady=10, column=0, row=2)
        self.lmgConvergenceEntry = customtkinter.CTkEntry(
            master=self.lmgTab)
        self.lmgConvergenceEntry.grid(padx=10, pady=10, column=1, row=2)
        self.lmgDispersionLabel = customtkinter.CTkLabel(
            master=self.lmgTab, text="Dispersion", font=self.buttonFont)
        self.lmgDispersionLabel.grid(padx=10, pady=10, column=0, row=3)
        self.lmgDispersionEntry = customtkinter.CTkEntry(
            master=self.lmgTab)
        self.lmgDispersionEntry.grid(padx=10, pady=10, column=1, row=3)
        self.lmgCameraRecoilLabel = customtkinter.CTkLabel(
            master=self.lmgTab, text="Camera Recoil", font=self.buttonFont)
        self.lmgCameraRecoilLabel.grid(padx=10, pady=10, column=0, row=4)
        self.lmgCameraRecoilEntry = customtkinter.CTkEntry(
            master=self.lmgTab)
        self.lmgCameraRecoilEntry.grid(padx=10, pady=10, column=1, row=4)
        self.lmgCameraSnapLabel = customtkinter.CTkLabel(
            master=self.lmgTab, text="Camera Snap", font=self.buttonFont)
        self.lmgCameraSnapLabel.grid(padx=10, pady=10, column=0, row=5)
        self.lmgCameraSnapEntry = customtkinter.CTkEntry(
            master=self.lmgTab)
        self.lmgCameraSnapEntry.grid(padx=10, pady=10, column=1, row=5)

        # Marksman Rifles

        self.mkVerticalRecoilLabel = customtkinter.CTkLabel(
            master=self.marksmanTab, text="Vertical Recoil", font=self.buttonFont)
        self.mkVerticalRecoilLabel.grid(padx=10, pady=10, column=0, row=0)
        self.mkVerticalRecoilEntry = customtkinter.CTkEntry(
            master=self.marksmanTab)
        self.mkVerticalRecoilEntry.grid(padx=10, pady=10, column=1, row=0)
        self.mkHorizontalRecoilLabel = customtkinter.CTkLabel(
            master=self.marksmanTab, text="Horizontal Recoil", font=self.buttonFont)
        self.mkHorizontalRecoilLabel.grid(padx=10, pady=10, column=0, row=1)
        self.mkHorizontalRecoilEntry = customtkinter.CTkEntry(
            master=self.marksmanTab)
        self.mkHorizontalRecoilEntry.grid(padx=10, pady=10, column=1, row=1)
        self.mkConvergenceLabel = customtkinter.CTkLabel(
            master=self.marksmanTab, text="Convergence", font=self.buttonFont)
        self.mkConvergenceLabel.grid(padx=10, pady=10, column=0, row=2)
        self.mkConvergenceEntry = customtkinter.CTkEntry(
            master=self.marksmanTab)
        self.mkConvergenceEntry.grid(padx=10, pady=10, column=1, row=2)
        self.mkDispersionLabel = customtkinter.CTkLabel(
            master=self.marksmanTab, text="Dispersion", font=self.buttonFont)
        self.mkDispersionLabel.grid(padx=10, pady=10, column=0, row=3)
        self.mkDispersionEntry = customtkinter.CTkEntry(
            master=self.marksmanTab)
        self.mkDispersionEntry.grid(padx=10, pady=10, column=1, row=3)
        self.mkCameraRecoilLabel = customtkinter.CTkLabel(
            master=self.marksmanTab, text="Camera Recoil", font=self.buttonFont)
        self.mkCameraRecoilLabel.grid(padx=10, pady=10, column=0, row=4)
        self.mkCameraRecoilEntry = customtkinter.CTkEntry(
            master=self.marksmanTab)
        self.mkCameraRecoilEntry.grid(padx=10, pady=10, column=1, row=4)
        self.mkCameraSnapLabel = customtkinter.CTkLabel(
            master=self.marksmanTab, text="Camera Snap", font=self.buttonFont)
        self.mkCameraSnapLabel.grid(padx=10, pady=10, column=0, row=5)
        self.mkCameraSnapEntry = customtkinter.CTkEntry(
            master=self.marksmanTab)
        self.mkCameraSnapEntry.grid(padx=10, pady=10, column=1, row=5)

        # Sniper Rifles

        self.sniperVerticalRecoilLabel = customtkinter.CTkLabel(
            master=self.sniperTab, text="Vertical Recoil", font=self.buttonFont)
        self.sniperVerticalRecoilLabel.grid(padx=10, pady=10, column=0, row=0)
        self.sniperVerticalRecoilEntry = customtkinter.CTkEntry(
            master=self.sniperTab)
        self.sniperVerticalRecoilEntry.grid(padx=10, pady=10, column=1, row=0)
        self.sniperHorizontalRecoilLabel = customtkinter.CTkLabel(
            master=self.sniperTab, text="Horizontal Recoil", font=self.buttonFont)
        self.sniperHorizontalRecoilLabel.grid(padx=10, pady=10, column=0, row=1)
        self.sniperHorizontalRecoilEntry = customtkinter.CTkEntry(
            master=self.sniperTab)
        self.sniperHorizontalRecoilEntry.grid(padx=10, pady=10, column=1, row=1)
        self.sniperConvergenceLabel = customtkinter.CTkLabel(
            master=self.sniperTab, text="Convergence", font=self.buttonFont)
        self.sniperConvergenceLabel.grid(padx=10, pady=10, column=0, row=2)
        self.sniperConvergenceEntry = customtkinter.CTkEntry(
            master=self.sniperTab)
        self.sniperConvergenceEntry.grid(padx=10, pady=10, column=1, row=2)
        self.sniperDispersionLabel = customtkinter.CTkLabel(
            master=self.sniperTab, text="Dispersion", font=self.buttonFont)
        self.sniperDispersionLabel.grid(padx=10, pady=10, column=0, row=3)
        self.sniperDispersionEntry = customtkinter.CTkEntry(
            master=self.sniperTab)
        self.sniperDispersionEntry.grid(padx=10, pady=10, column=1, row=3)
        self.sniperCameraRecoilLabel = customtkinter.CTkLabel(
            master=self.sniperTab, text="Camera Recoil", font=self.buttonFont)
        self.sniperCameraRecoilLabel.grid(padx=10, pady=10, column=0, row=4)
        self.sniperCameraRecoilEntry = customtkinter.CTkEntry(
            master=self.sniperTab)
        self.sniperCameraRecoilEntry.grid(padx=10, pady=10, column=1, row=4)
        self.sniperCameraSnapLabel = customtkinter.CTkLabel(
            master=self.sniperTab, text="Camera Snap", font=self.buttonFont)
        self.sniperCameraSnapLabel.grid(padx=10, pady=10, column=0, row=5)
        self.sniperCameraSnapEntry = customtkinter.CTkEntry(
            master=self.sniperTab)
        self.sniperCameraSnapEntry.grid(padx=10, pady=10, column=1, row=5)

        self.mainGlobals = [
            self.gVerticalRecoilEntry,
            self.gHorizontalRecoilEntry,
            self.gConvergenceEntry,
            self.gDispersionEntry,
            self.gCameraRecoilEntry,
            self.gCameraSnapEntry
        ]

        self.advGlobals = [
            self.aimPunchEntry,
            self.recoilDampingEntry,
            self.recoilHandDampingEntry,
            self.aimProceduralIntensityEntry
        ]

        self.pistolValues = [
            self.pistolVerticalRecoilEntry,
            self.pistolHorizontalRecoilEntry,
            self.pistolConvergenceEntry,
            self.pistolDispersionEntry,
            self.pistolCameraRecoilEntry,
            self.pistolCameraSnapEntry
        ]

        self.smgValues = [
            self.smgVerticalRecoilEntry,
            self.smgHorizontalRecoilEntry,
            self.smgConvergenceEntry,
            self.smgDispersionEntry,
            self.smgCameraRecoilEntry,
            self.smgCameraSnapEntry
        ]

        self.shotgunValues = [
            self.shotgunVerticalRecoilEntry,
            self.shotgunHorizontalRecoilEntry,
            self.shotgunConvergenceEntry,
            self.shotgunDispersionEntry,
            self.shotgunCameraRecoilEntry,
            self.shotgunCameraSnapEntry
        ]

        self.acValues = [
            self.acVerticalRecoilEntry,
            self.acHorizontalRecoilEntry,
            self.acConvergenceEntry,
            self.acDispersionEntry,
            self.acCameraRecoilEntry,
            self.acCameraSnapEntry
        ]

        self.arValues = [
            self.arVerticalRecoilEntry,
            self.arHorizontalRecoilEntry,
            self.arConvergenceEntry,
            self.arDispersionEntry,
            self.arCameraRecoilEntry,
            self.arCameraSnapEntry
        ]

        self.lmgValues = [
            self.lmgVerticalRecoilEntry,
            self.lmgHorizontalRecoilEntry,
            self.lmgConvergenceEntry,
            self.lmgDispersionEntry,
            self.lmgCameraRecoilEntry,
            self.lmgCameraSnapEntry
        ]

        self.mkValues = [
            self.mkVerticalRecoilEntry,
            self.mkHorizontalRecoilEntry,
            self.mkConvergenceEntry,
            self.mkDispersionEntry,
            self.mkCameraRecoilEntry,
            self.mkCameraSnapEntry
        ]

        self.sniperValues = [
            self.sniperVerticalRecoilEntry,
            self.sniperHorizontalRecoilEntry,
            self.sniperConvergenceEntry,
            self.sniperDispersionEntry,
            self.sniperCameraRecoilEntry,
            self.sniperCameraSnapEntry
        ]

        self.allValues = [
            self.mainGlobals,
            self.advGlobals,
            self.pistolValues,
            self.smgValues,
            self.shotgunValues,
            self.acValues,
            self.arValues,
            self.lmgValues,
            self.mkValues,
            self.sniperValues
        ]




if __name__ == "__main__":

    app = App()
    app.mainloop()
