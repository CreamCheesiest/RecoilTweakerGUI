import tkinter as tk
import tkinter.ttk as ttk
from tktooltip import ToolTip
import customtkinter
from tkinter import filedialog as fd

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    
    def importFunction(self):

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
                        print(temp2[0])
                        entry.insert(0, temp2[0])

        try:
            filename = fd.askopenfilename(title="Choose config file", filetypes=(("JSON File", "*.json"),))
            importFile = open(filename, 'r')
            print("Read " + str(importFile))
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
        except FileNotFoundError as err:
            print("File not found!")

        self.savedPath = filename


    def exportFunction(self):
        filename = fd.asksaveasfile(mode='w', title="Export as...", filetypes=(("JSON File", "*.json"),), defaultextension=".json")
        exportFile = open(filename.name, 'w')
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
        exportFile.write('\t"ProceduralIntensityByPoseZ": 1,\n\n')

        exportFile.write('"// ADAR":"//",\n\
      "adarVerticalRecoil": 1,\n\
      "adarHorizontalRecoil": 1,\n\
      "adarConvergence": 1,\n\
      "adarDispersion": 1,\n\
      "adarCameraRecoil": 1,\n\
      "adarCameraSnap": 1,\n\
      \
      "// AK-101":"//",\n\
      "ak101VerticalRecoil": 1,\n\
      "ak101HorizontalRecoil": 1,\n\
      "ak101Convergence": 1,\n\
      "ak101Dispersion": 1,\n\
      "ak101CameraRecoil": 1,\n\
      "ak101CameraSnap": 1,\n\
      \
      "// AK-102":"//",\n\
      "ak102VerticalRecoil": 1,\n\
      "ak102HorizontalRecoil": 1,\n\
      "ak102Convergence": 1,\n\
      "ak102Dispersion": 1,\n\
      "ak102CameraRecoil": 1,\n\
      "ak102CameraSnap": 1,\n\
    \
      "// AK-103":"//",\n\
      "ak103VerticalRecoil": 1,\n\
      "ak103HorizontalRecoil": 1,\n\
      "ak103Convergence": 1,\n\
      "ak103Dispersion": 1,\n\
      "ak103CameraRecoil": 1,\n\
      "ak103CameraSnap": 1,\n\
    \
      "// AK-104":"//",\n\
      "ak104VerticalRecoil": 1,\n\
      "ak104HorizontalRecoil": 1,\n\
      "ak104Convergence": 1,\n\
      "ak104Dispersion": 1,\n\
      "ak104CameraRecoil": 1,\n\
      "ak104CameraSnap": 1,\n\
    \
      "// AK-105":"//",\n\
      "ak105VerticalRecoil": 1,\n\
      "ak105HorizontalRecoil": 1,\n\
      "ak105Convergence": 1,\n\
      "ak105Dispersion": 1,\n\
      "ak105CameraRecoil": 1,\n\
      "ak105CameraSnap": 1,\n\
    \
      "// AK-74":"//",\n\
      "ak74VerticalRecoil": 1,\n\
      "ak74HorizontalRecoil": 1,\n\
      "ak74Convergence": 1,\n\
      "ak74Dispersion": 1,\n\
      "ak74CameraRecoil": 1,\n\
      "ak74CameraSnap": 1,\n\
    \
      "// AK-74M":"//",\n\
      "ak74mVerticalRecoil": 1,\n\
      "ak74mHorizontalRecoil": 1,\n\
      "ak74mConvergence": 1,\n\
      "ak74mDispersion": 1,\n\
      "ak74mCameraRecoil": 1,\n\
      "ak74mCameraSnap": 1,\n\
    \
      "// AK-74N":"//",\n\
      "ak74nVerticalRecoil": 1,\n\
      "ak74nHorizontalRecoil": 1,\n\
      "ak74nConvergence": 1,\n\
      "ak74nDispersion": 1,\n\
      "ak74nCameraRecoil": 1,\n\
      "ak74nCameraSnap": 1,\n\
    \
      "// AKM":"//",\n\
      "akmVerticalRecoil": 1,\n\
      "akmHorizontalRecoil": 1,\n\
      "akmConvergence": 1,\n\
      "akmDispersion": 1,\n\
      "akmCameraRecoil": 1,\n\
      "akmCameraSnap": 1,\n\
    \
      "// AKMN":"//",\n\
      "akmnVerticalRecoil": 1,\n\
      "akmnHorizontalRecoil": 1,\n\
      "akmnConvergence": 1,\n\
      "akmnDispersion": 1,\n\
      "akmnCameraRecoil": 1,\n\
      "akmnCameraSnap": 1,\n\
    \
      "// AKMS":"//",\n\
      "akmsVerticalRecoil": 1,\n\
      "akmsHorizontalRecoil": 1,\n\
      "akmsConvergence": 1,\n\
      "akmsDispersion": 1,\n\
      "akmsCameraRecoil": 1,\n\
      "akmsCameraSnap": 1,\n\
    \
      "// AKMSN":"//",\n\
      "akmsnVerticalRecoil": 1,\n\
      "akmsnHorizontalRecoil": 1,\n\
      "akmsnConvergence": 1,\n\
      "akmsnDispersion": 1,\n\
      "akmsnCameraRecoil": 1,\n\
      "akmsnCameraSnap": 1,\n\
    \
      "// AKS-74":"//",\n\
      "aks74VerticalRecoil": 1,\n\
      "aks74HorizontalRecoil": 1,\n\
      "aks74Convergence": 1,\n\
      "aks74Dispersion": 1,\n\
      "aks74CameraRecoil": 1,\n\
      "aks74CameraSnap": 1,\n\
    \
      "// AKS-74N":"//",\n\
      "aks74nVerticalRecoil": 1,\n\
      "aks74nHorizontalRecoil": 1,\n\
      "aks74nConvergence": 1,\n\
      "aks74nDispersion": 1,\n\
      "aks74nCameraRecoil": 1,\n\
      "aks74nCameraSnap": 1,\n\
    \
      "// AKS-74U":"//",\n\
      "aks74uVerticalRecoil": 1,\n\
      "aks74uHorizontalRecoil": 1,\n\
      "aks74uConvergence": 1,\n\
      "aks74uDispersion": 1,\n\
      "aks74uCameraRecoil": 1,\n\
      "aks74uCameraSnap": 1,\n\
    \
      "// AKS-74UB":"//",\n\
      "aks74ubVerticalRecoil": 1,\n\
      "aks74ubHorizontalRecoil": 1,\n\
      "aks74ubConvergence": 1,\n\
      "aks74ubDispersion": 1,\n\
      "aks74ubCameraRecoil": 1,\n\
      "aks74ubCameraSnap": 1,\n\
    \
      "// AKS-74UN":"//",\n\
      "aks74unVerticalRecoil": 1,\n\
      "aks74unHorizontalRecoil": 1,\n\
      "aks74unConvergence": 1,\n\
      "aks74unDispersion": 1,\n\
      "aks74unCameraRecoil": 1,\n\
      "aks74unCameraSnap": 1,\n\
    \
      "// ASh-12":"//",\n\
      "ashVerticalRecoil": 1,\n\
      "ashHorizontalRecoil": 1,\n\
      "ashConvergence": 1,\n\
      "ashDispersion": 1,\n\
      "ashCameraRecoil": 1,\n\
      "ashCameraSnap": 1,\n\
    \
      "// AUG A1":"//",\n\
      "aug1VerticalRecoil": 1,\n\
      "aug1HorizontalRecoil": 1,\n\
      "aug1Convergence": 1,\n\
      "aug1Dispersion": 1,\n\
      "aug1CameraRecoil": 1,\n\
      "aug1CameraSnap": 1,\n\
    \
      "// AUG A3":"//",\n\
      "aug3VerticalRecoil": 1,\n\
      "aug3HorizontalRecoil": 1,\n\
      "aug3Convergence": 1,\n\
      "aug3Dispersion": 1,\n\
      "aug3CameraRecoil": 1,\n\
      "aug3CameraSnap": 1,\n\
    \
      "// MDR 5.56x45":"//",\n\
      "mdr556VerticalRecoil": 1,\n\
      "mdr556HorizontalRecoil": 1,\n\
      "mdr556Convergence": 1,\n\
      "mdr556Dispersion": 1,\n\
      "mdr556CameraRecoil": 1,\n\
      "mdr556CameraSnap": 1,\n\
    \
      "// MDR 7.62x51":"//",\n\
      "mdr762VerticalRecoil": 1,\n\
      "mdr762HorizontalRecoil": 1,\n\
      "mdr762Convergence": 1,\n\
      "mdr762Dispersion": 1,\n\
      "mdr762CameraRecoil": 1,\n\
      "mdr762CameraSnap": 1,\n\
    \
      "// HK 416A5":"//",\n\
      "hk416VerticalRecoil": 1,\n\
      "hk416HorizontalRecoil": 1,\n\
      "hk416Convergence": 1,\n\
      "hk416Dispersion": 1,\n\
      "hk416CameraRecoil": 1,\n\
      "hk416CameraSnap": 1,\n\
    \
      "// HK G36":"//",\n\
      "g36VerticalRecoil": 1,\n\
      "g36HorizontalRecoil": 1,\n\
      "g36Convergence": 1,\n\
      "g36Dispersion": 1,\n\
      "g36CameraRecoil": 1,\n\
      "g36CameraSnap": 1,\n\
    \
      "// M4A1":"//",\n\
      "m4a1VerticalRecoil": 1,\n\
      "m4a1HorizontalRecoil": 1,\n\
      "m4a1Convergence": 1,\n\
      "m4a1Dispersion": 1,\n\
      "m4a1CameraRecoil": 1,\n\
      "m4a1CameraSnap": 1,\n\
    \
      "// MCX":"//",\n\
      "mcxVerticalRecoil": 1,\n\
      "mcxHorizontalRecoil": 1,\n\
      "mcxConvergence": 1,\n\
      "mcxDispersion": 1,\n\
      "mcxCameraRecoil": 1,\n\
      "mcxCameraSnap": 1,\n\
    \
      "// Mk47":"//",\n\
      "mk47VerticalRecoil": 1,\n\
      "mk47HorizontalRecoil": 1,\n\
      "mk47Convergence": 1,\n\
      "mk47Dispersion": 1,\n\
      "mk47CameraRecoil": 1,\n\
      "mk47CameraSnap": 1,\n\
    \
      "// RD-704":"//",\n\
      "rdVerticalRecoil": 1,\n\
      "rdHorizontalRecoil": 1,\n\
      "rdConvergence": 1,\n\
      "rdDispersion": 1,\n\
      "rdCameraRecoil": 1,\n\
      "rdCameraSnap": 1,\n\
    \
      "// SA-58":"//",\n\
      "sa58VerticalRecoil": 1,\n\
      "sa58HorizontalRecoil": 1,\n\
      "sa58Convergence": 1,\n\
      "sa58Dispersion": 1,\n\
      "sa58CameraRecoil": 1,\n\
      "sa58CameraSnap": 1,\n\
    \
      "// SAG AK":"//",\n\
      "sagakVerticalRecoil": 1,\n\
      "sagakHorizontalRecoil": 1,\n\
      "sagakConvergence": 1,\n\
      "sagakDispersion": 1,\n\
      "sagakCameraRecoil": 1,\n\
      "sagakCameraSnap": 1,\n\
    \
      "// SAG AK Short":"//",\n\
      "sagaksVerticalRecoil": 1,\n\
      "sagaksHorizontalRecoil": 1,\n\
      "sagaksConvergence": 1,\n\
      "sagaksDispersion": 1,\n\
      "sagaksCameraRecoil": 1,\n\
      "sagaksCameraSnap": 1,\n\
    \
      "// SCAR-H":"//",\n\
      "scarhVerticalRecoil": 1,\n\
      "scarhHorizontalRecoil": 1,\n\
      "scarhConvergence": 1,\n\
      "scarhDispersion": 1,\n\
      "scarhCameraRecoil": 1,\n\
      "scarhCameraSnap": 1,\n\
    \
      "// SCAR-L":"//",\n\
      "scarlVerticalRecoil": 1,\n\
      "scarlHorizontalRecoil": 1,\n\
      "scarlConvergence": 1,\n\
      "scarlDispersion": 1,\n\
      "scarlCameraRecoil": 1,\n\
      "scarlCameraSnap": 1,\n\
    \
      "// TX-15 DML":"//",\n\
      "tx15VerticalRecoil": 1,\n\
      "tx15HorizontalRecoil": 1,\n\
      "tx15Convergence": 1,\n\
      "tx15Dispersion": 1,\n\
      "tx15CameraRecoil": 1,\n\
      "tx15CameraSnap": 1,\n\
    \
      "// Vepr AKM/VPO-209":"//",\n\
      "vpo209VerticalRecoil": 1,\n\
      "vpo209HorizontalRecoil": 1,\n\
      "vpo209Convergence": 1,\n\
      "vpo209Dispersion": 1,\n\
      "vpo209CameraRecoil": 1,\n\
      "vpo209CameraSnap": 1,\n\
    \
      "// Vepr KM/VPO-136":"//",\n\
      "vpo136VerticalRecoil": 1,\n\
      "vpo136HorizontalRecoil": 1,\n\
      "vpo136Convergence": 1,\n\
      "vpo136Dispersion": 1,\n\
      "vpo136CameraRecoil": 1,\n\
      "vpo136CameraSnap": 1,\n\
    \
    "// Assault Carbines":"//",\n\
    \
      "// AS VAL":"//",\n\
      "valVerticalRecoil": 1,\n\
      "valHorizontalRecoil": 1,\n\
      "valConvergence": 1,\n\
      "valDispersion": 1,\n\
      "valCameraRecoil": 1,\n\
      "valCameraSnap": 1,\n\
    \
      "// OP-SKS":"//",\n\
      "opsksVerticalRecoil": 1,\n\
      "opsksHorizontalRecoil": 1,\n\
      "opsksConvergence": 1,\n\
      "opsksDispersion": 1,\n\
      "opsksCameraRecoil": 1,\n\
      "opsksCameraSnap": 1,\n\
    \
      "// SKS":"//",\n\
      "sksVerticalRecoil": 1,\n\
      "sksHorizontalRecoil": 1,\n\
      "sksConvergence": 1,\n\
      "sksDispersion": 1,\n\
      "sksCameraRecoil": 1,\n\
      "sksCameraSnap": 1,\n\
    \
      "// Vepr Hunter/VPO-101":"//",\n\
      "vpo101VerticalRecoil": 1,\n\
      "vpo101HorizontalRecoil": 1,\n\
      "vpo101Convergence": 1,\n\
      "vpo101Dispersion": 1,\n\
      "vpo101CameraRecoil": 1,\n\
      "vpo101CameraSnap": 1,\n\
    \
    "// Light Machine Guns (LMG)":"//",\n\
    \
      "// RPK":"//",\n\
      "rpkVerticalRecoil": 1,\n\
      "rpkHorizontalRecoil": 1,\n\
      "rpkConvergence": 1,\n\
      "rpkDispersion": 1,\n\
      "rpkCameraRecoil": 1,\n\
      "rpkCameraSnap": 1,\n\
    \
    "// Submachine Guns (SMG)":"//",\n\
    \
      "// MP5":"//",\n\
      "mp5VerticalRecoil": 1,\n\
      "mp5HorizontalRecoil": 1,\n\
      "mp5Convergence": 1,\n\
      "mp5Dispersion": 1,\n\
      "mp5CameraRecoil": 1,\n\
      "mp5CameraSnap": 1,\n\
    \
      "// MP5K-N":"//",\n\
      "mp5kVerticalRecoil": 1,\n\
      "mp5kHorizontalRecoil": 1,\n\
      "mp5kConvergence": 1,\n\
      "mp5kDispersion": 1,\n\
      "mp5kCameraRecoil": 1,\n\
      "mp5kCameraSnap": 1,\n\
    \
      "// MP7A1":"//",\n\
      "mp7a1VerticalRecoil": 1,\n\
      "mp7a1HorizontalRecoil": 1,\n\
      "mp7a1Convergence": 1,\n\
      "mp7a1Dispersion": 1,\n\
      "mp7a1CameraRecoil": 1,\n\
      "mp7a1CameraSnap": 1,\n\
    \
      "// MP7A2":"//",\n\
      "mp7a2VerticalRecoil": 1,\n\
      "mp7a2HorizontalRecoil": 1,\n\
      "mp7a2Convergence": 1,\n\
      "mp7a2Dispersion": 1,\n\
      "mp7a2CameraRecoil": 1,\n\
      "mp7a2CameraSnap": 1,\n\
    \
      "// MP9":"//",\n\
      "mp9VerticalRecoil": 1,\n\
      "mp9HorizontalRecoil": 1,\n\
      "mp9Convergence": 1,\n\
      "mp9Dispersion": 1,\n\
      "mp9CameraRecoil": 1,\n\
      "mp9CameraSnap": 1,\n\
    \
      "// MP9-N":"//",\n\
      "mp9nVerticalRecoil": 1,\n\
      "mp9nHorizontalRecoil": 1,\n\
      "mp9nConvergence": 1,\n\
      "mp9nDispersion": 1,\n\
      "mp9nCameraRecoil": 1,\n\
      "mp9nCameraSnap": 1,\n\
    \
      "// MPX":"//",\n\
      "mpxVerticalRecoil": 1,\n\
      "mpxHorizontalRecoil": 1,\n\
      "mpxConvergence": 1,\n\
      "mpxDispersion": 1,\n\
      "mpxCameraRecoil": 1,\n\
      "mpxCameraSnap": 1,\n\
    \
      "// P90":"//",\n\
      "p90VerticalRecoil": 1,\n\
      "p90HorizontalRecoil": 1,\n\
      "p90Convergence": 1,\n\
      "p90Dispersion": 1,\n\
      "p90CameraRecoil": 1,\n\
      "p90CameraSnap": 1,\n\
\
      "// PP-19-01 Vityaz-SN":"//",\n\
      "pp19VerticalRecoil": 1,\n\
      "pp19HorizontalRecoil": 1,\n\
      "pp19Convergence": 1,\n\
      "pp19Dispersion": 1,\n\
      "pp19CameraRecoil": 1,\n\
      "pp19CameraSnap": 1,\n\
\
      "// PP-9":"//",\n\
      "pp9VerticalRecoil": 1,\n\
      "pp9HorizontalRecoil": 1,\n\
      "pp9Convergence": 1,\n\
      "pp9Dispersion": 1,\n\
      "pp9CameraRecoil": 1,\n\
      "pp9CameraSnap": 1,\n\
\
      "// PP-91":"//",\n\
      "pp91VerticalRecoil": 1,\n\
      "pp91HorizontalRecoil": 1,\n\
      "pp91Convergence": 1,\n\
      "pp91Dispersion": 1,\n\
      "pp91CameraRecoil": 1,\n\
      "pp91CameraSnap": 1,\n\
\
      "// PP-91-01":"//",\n\
      "pp9101VerticalRecoil": 1,\n\
      "pp9101HorizontalRecoil": 1,\n\
      "pp9101Convergence": 1,\n\
      "pp9101Dispersion": 1,\n\
      "pp9101CameraRecoil": 1,\n\
      "pp9101CameraSnap": 1,\n\
\
      "// PPSH-41":"//",\n\
      "ppshVerticalRecoil": 1,\n\
      "ppshHorizontalRecoil": 1,\n\
      "ppshConvergence": 1,\n\
      "ppshDispersion": 1,\n\
      "ppshCameraRecoil": 1,\n\
      "ppshCameraSnap": 1,\n\
\
      "// Saiga-9":"//",\n\
      "saiga9VerticalRecoil": 1,\n\
      "saiga9HorizontalRecoil": 1,\n\
      "saiga9Convergence": 1,\n\
      "saiga9Dispersion": 1,\n\
      "saiga9CameraRecoil": 1,\n\
      "saiga9CameraSnap": 1,\n\
\
      "// SR-2M":"//",\n\
      "sr2mVerticalRecoil": 1,\n\
      "sr2mHorizontalRecoil": 1,\n\
      "sr2mConvergence": 1,\n\
      "sr2mDispersion": 1,\n\
      "sr2mCameraRecoil": 1,\n\
      "sr2mCameraSnap": 1,\n\
\
      "// STM-9":"//",\n\
      "stmVerticalRecoil": 1,\n\
      "stmHorizontalRecoil": 1,\n\
      "stmConvergence": 1,\n\
      "stmDispersion": 1,\n\
      "stmCameraRecoil": 1,\n\
      "stmCameraSnap": 1,\n\
\
      "// UMP-45":"//",\n\
      "umpVerticalRecoil": 1,\n\
      "umpHorizontalRecoil": 1,\n\
      "umpConvergence": 1,\n\
      "umpDispersion": 1,\n\
      "umpCameraRecoil": 1,\n\
      "umpCameraSnap": 1,\n\
\
      "// Vector .45":"//",\n\
      "vector45VerticalRecoil": 1,\n\
      "vector45HorizontalRecoil": 1,\n\
      "vector45Convergence": 1,\n\
      "vector45Dispersion": 1,\n\
      "vector45CameraRecoil": 1,\n\
      "vector45CameraSnap": 1,\n\
\
      "// Vector 9x19":"//",\n\
      "vector9x19VerticalRecoil": 1,\n\
      "vector9x19HorizontalRecoil": 1,\n\
      "vector9x19Convergence": 1,\n\
      "vector9x19Dispersion": 1,\n\
      "vector9x19CameraRecoil": 1,\n\
      "vector9x19CameraSnap": 1,\n\
\
    "// Shotguns":"//",\n\
\
      "// KS-23M":"//",\n\
      "ksVerticalRecoil": 1,\n\
      "ksHorizontalRecoil": 1,\n\
      "ksConvergence": 1,\n\
      "ksDispersion": 1,\n\
      "ksCameraRecoil": 1,\n\
      "ksCameraSnap": 1,\n\
\
      "// M3 Super 90":"//",\n\
      "m3VerticalRecoil": 1,\n\
      "m3HorizontalRecoil": 1,\n\
      "m3Convergence": 1,\n\
      "m3Dispersion": 1,\n\
      "m3CameraRecoil": 1,\n\
      "m3CameraSnap": 1,\n\
\
      "// M590A1":"//",\n\
      "m590VerticalRecoil": 1,\n\
      "m590HorizontalRecoil": 1,\n\
      "m590Convergence": 1,\n\
      "m590Dispersion": 1,\n\
      "m590CameraRecoil": 1,\n\
      "m590CameraSnap": 1,\n\
\
      "// M870":"//",\n\
      "m870VerticalRecoil": 1,\n\
      "m870HorizontalRecoil": 1,\n\
      "m870Convergence": 1,\n\
      "m870Dispersion": 1,\n\
      "m870CameraRecoil": 1,\n\
      "m870CameraSnap": 1,\n\
\
      "// MP-133":"//",\n\
      "mp133VerticalRecoil": 1,\n\
      "mp133HorizontalRecoil": 1,\n\
      "mp133Convergence": 1,\n\
      "mp133Dispersion": 1,\n\
      "mp133CameraRecoil": 1,\n\
      "mp133CameraSnap": 1,\n\
\
      "// MP-153":"//",\n\
      "mp153VerticalRecoil": 1,\n\
      "mp153HorizontalRecoil": 1,\n\
      "mp153Convergence": 1,\n\
      "mp153Dispersion": 1,\n\
      "mp153CameraRecoil": 1,\n\
      "mp153CameraSnap": 1,\n\
\
      "// MP-155":"//",\n\
      "mp155VerticalRecoil": 1,\n\
      "mp155HorizontalRecoil": 1,\n\
      "mp155Convergence": 1,\n\
      "mp155Dispersion": 1,\n\
      "mp155CameraRecoil": 1,\n\
      "mp155CameraSnap": 1,\n\
\
      "// MP-43-1C":"//",\n\
      "mp43VerticalRecoil": 1,\n\
      "mp43HorizontalRecoil": 1,\n\
      "mp43Convergence": 1,\n\
      "mp43Dispersion": 1,\n\
      "mp43CameraRecoil": 1,\n\
      "mp43CameraSnap": 1,\n\
\
      "// MTs-255-12":"//",\n\
      "mtsVerticalRecoil": 1,\n\
      "mtsHorizontalRecoil": 1,\n\
      "mtsConvergence": 1,\n\
      "mtsDispersion": 1,\n\
      "mtsCameraRecoil": 1,\n\
      "mtsCameraSnap": 1,\n\
\
      "// Saiga-12":"//",\n\
      "saiga12VerticalRecoil": 1,\n\
      "saiga12HorizontalRecoil": 1,\n\
      "saiga12Convergence": 1,\n\
      "saiga12Dispersion": 1,\n\
      "saiga12CameraRecoil": 1,\n\
      "saiga12CameraSnap": 1,\n\
\
      "// TOZ-106":"//",\n\
      "tozVerticalRecoil": 1,\n\
      "tozHorizontalRecoil": 1,\n\
      "tozConvergence": 1,\n\
      "tozDispersion": 1,\n\
      "tozCameraRecoil": 1,\n\
      "tozCameraSnap": 1,\n\
\
    "// Designated Marksman Rifles":"//",\n\
\
      "// HK G28":"//",\n\
      "hkg28VerticalRecoil": 1,\n\
      "hkg28HorizontalRecoil": 1,\n\
      "hkg28Convergence": 1,\n\
      "hkg28Dispersion": 1,\n\
      "hkg28CameraRecoil": 1,\n\
      "hkg28CameraSnap": 1,\n\
\
      "// M1A":"//",\n\
      "m1aVerticalRecoil": 1,\n\
      "m1aHorizontalRecoil": 1,\n\
      "m1aConvergence": 1,\n\
      "m1aDispersion": 1,\n\
      "m1aCameraRecoil": 1,\n\
      "m1aCameraSnap": 1,\n\
\
      "// Mk-18":"//",\n\
      "mk18VerticalRecoil": 1,\n\
      "mk18HorizontalRecoil": 1,\n\
      "mk18Convergence": 1,\n\
      "mk18Dispersion": 1,\n\
      "mk18CameraRecoil": 1,\n\
      "mk18CameraSnap": 1,\n\
\
      "// RFB":"//",\n\
      "rfbVerticalRecoil": 1,\n\
      "rfbHorizontalRecoil": 1,\n\
      "rfbConvergence": 1,\n\
      "rfbDispersion": 1,\n\
      "rfbCameraRecoil": 1,\n\
      "rfbCameraSnap": 1,\n\
\
      "// RSASS":"//",\n\
      "rsassVerticalRecoil": 1,\n\
      "rsassHorizontalRecoil": 1,\n\
      "rsassConvergence": 1,\n\
      "rsassDispersion": 1,\n\
      "rsassCameraRecoil": 1,\n\
      "rsassCameraSnap": 1,\n\
\
      "// SR-25":"//",\n\
      "sr25VerticalRecoil": 1,\n\
      "sr25HorizontalRecoil": 1,\n\
      "sr25Convergence": 1,\n\
      "sr25Dispersion": 1,\n\
      "sr25CameraRecoil": 1,\n\
      "sr25CameraSnap": 1,\n\
\
      "// SVDS":"//",\n\
      "svdsVerticalRecoil": 1,\n\
      "svdsHorizontalRecoil": 1,\n\
      "svdsConvergence": 1,\n\
      "svdsDispersion": 1,\n\
      "svdsCameraRecoil": 1,\n\
      "svdsCameraSnap": 1,\n\
\
      "// VSS Vintorez":"//",\n\
      "vssVerticalRecoil": 1,\n\
      "vssHorizontalRecoil": 1,\n\
      "vssConvergence": 1,\n\
      "vssDispersion": 1,\n\
      "vssCameraRecoil": 1,\n\
      "vssCameraSnap": 1,\n\
\
    "// Sniper Rifles":"//",\n\
\
      "// AXMC":"//",\n\
      "axmcVerticalRecoil": 1,\n\
      "axmcHorizontalRecoil": 1,\n\
      "axmcConvergence": 1,\n\
      "axmcDispersion": 1,\n\
      "axmcCameraRecoil": 1,\n\
      "axmcCameraSnap": 1,\n\
\
      "// DVL-10":"//",\n\
      "dvlVerticalRecoil": 1,\n\
      "dvlHorizontalRecoil": 1,\n\
      "dvlConvergence": 1,\n\
      "dvlDispersion": 1,\n\
      "dvlCameraRecoil": 1,\n\
      "dvlCameraSnap": 1,\n\
\
      "// M700":"//",\n\
      "m700VerticalRecoil": 1,\n\
      "m700HorizontalRecoil": 1,\n\
      "m700Convergence": 1,\n\
      "m700Dispersion": 1,\n\
      "m700CameraRecoil": 1,\n\
      "m700CameraSnap": 1,\n\
\
      "// Mosin (Infantry)":"//",\n\
      "mosiniVerticalRecoil": 1,\n\
      "mosiniHorizontalRecoil": 1,\n\
      "mosiniConvergence": 1,\n\
      "mosiniDispersion": 1,\n\
      "mosiniCameraRecoil": 1,\n\
      "mosiniCameraSnap": 1,\n\
\
      "// Mosin (Sniper)":"//",\n\
      "mosinsVerticalRecoil": 1,\n\
      "mosinsHorizontalRecoil": 1,\n\
      "mosinsConvergence": 1,\n\
      "mosinsDispersion": 1,\n\
      "mosinsCameraRecoil": 1,\n\
      "mosinsCameraSnap": 1,\n\
\
      "// SV-98":"//",\n\
      "sv98VerticalRecoil": 1,\n\
      "sv98HorizontalRecoil": 1,\n\
      "sv98Convergence": 1,\n\
      "sv98Dispersion": 1,\n\
      "sv98CameraRecoil": 1,\n\
      "sv98CameraSnap": 1,\n\
\
      "// T-5000":"//",\n\
      "t5000VerticalRecoil": 1,\n\
      "t5000HorizontalRecoil": 1,\n\
      "t5000Convergence": 1,\n\
      "t5000Dispersion": 1,\n\
      "t5000CameraRecoil": 1,\n\
      "t5000CameraSnap": 1,\n\
\
      "// VPO-215":"//",\n\
      "vpo215VerticalRecoil": 1,\n\
      "vpo215HorizontalRecoil": 1,\n\
      "vpo215Convergence": 1,\n\
      "vpo215Dispersion": 1,\n\
      "vpo215CameraRecoil": 1,\n\
      "vpo215CameraSnap": 1,\n\
\
    "// Pistols":"//",\n\
\
      "// APB":"//",\n\
      "apbVerticalRecoil": 1,\n\
      "apbHorizontalRecoil": 1,\n\
      "apbConvergence": 1,\n\
      "apbDispersion": 1,\n\
      "apbCameraRecoil": 1,\n\
      "apbCameraSnap": 1,\n\
\
      "// APS":"//",\n\
      "apsVerticalRecoil": 1,\n\
      "apsHorizontalRecoil": 1,\n\
      "apsConvergence": 1,\n\
      "apsDispersion": 1,\n\
      "apsCameraRecoil": 1,\n\
      "apsCameraSnap": 1,\n\
\
      "// FN 5-7":"//",\n\
      "fnVerticalRecoil": 1,\n\
      "fnHorizontalRecoil": 1,\n\
      "fnConvergence": 1,\n\
      "fnDispersion": 1,\n\
      "fnCameraRecoil": 1,\n\
      "fnCameraSnap": 1,\n\
\
      "// GLOCK17":"//",\n\
      "glk17VerticalRecoil": 1,\n\
      "glk17HorizontalRecoil": 1,\n\
      "glk17Convergence": 1,\n\
      "glk17Dispersion": 1,\n\
      "glk17CameraRecoil": 1,\n\
      "glk17CameraSnap": 1,\n\
\
      "// GLOCK18C":"//",\n\
      "glk18VerticalRecoil": 1,\n\
      "glk18HorizontalRecoil": 1,\n\
      "glk18Convergence": 1,\n\
      "glk18Dispersion": 1,\n\
      "glk18CameraRecoil": 1,\n\
      "glk18CameraSnap": 1,\n\
\
      "// GLOCK 19X":"//",\n\
      "glk19VerticalRecoil": 1,\n\
      "glk19HorizontalRecoil": 1,\n\
      "glk19Convergence": 1,\n\
      "glk19Dispersion": 1,\n\
      "glk19CameraRecoil": 1,\n\
      "glk19CameraSnap": 1,\n\
\
      "// M1911A1":"//",\n\
      "m1911VerticalRecoil": 1,\n\
      "m1911HorizontalRecoil": 1,\n\
      "m1911Convergence": 1,\n\
      "m1911Dispersion": 1,\n\
      "m1911CameraRecoil": 1,\n\
      "m1911CameraSnap": 1,\n\
\
      "// M45A1":"//",\n\
      "m45a1VerticalRecoil": 1,\n\
      "m45a1HorizontalRecoil": 1,\n\
      "m45a1Convergence": 1,\n\
      "m45a1Dispersion": 1,\n\
      "m45a1CameraRecoil": 1,\n\
      "m45a1CameraSnap": 1,\n\
\
      "// M9A3":"//",\n\
      "m9a3VerticalRecoil": 1,\n\
      "m9a3HorizontalRecoil": 1,\n\
      "m9a3Convergence": 1,\n\
      "m9a3Dispersion": 1,\n\
      "m9a3CameraRecoil": 1,\n\
      "m9a3CameraSnap": 1,\n\
\
      "// MP-443":"//",\n\
      "mp443VerticalRecoil": 1,\n\
      "mp443HorizontalRecoil": 1,\n\
      "mp443Convergence": 1,\n\
      "mp443Dispersion": 1,\n\
      "mp443CameraRecoil": 1,\n\
      "mp443CameraSnap": 1,\n\
\
      "// P226R":"//",\n\
      "p226VerticalRecoil": 1,\n\
      "p226HorizontalRecoil": 1,\n\
      "p226Convergence": 1,\n\
      "p226Dispersion": 1,\n\
      "p226CameraRecoil": 1,\n\
      "p226CameraSnap": 1,\n\
\
      "// PB pistol":"//",\n\
      "pbVerticalRecoil": 1,\n\
      "pbHorizontalRecoil": 1,\n\
      "pbConvergence": 1,\n\
      "pbDispersion": 1,\n\
      "pbCameraRecoil": 1,\n\
      "pbCameraSnap": 1,\n\
\
      "// PL-15":"//",\n\
      "pl15VerticalRecoil": 1,\n\
      "pl15HorizontalRecoil": 1,\n\
      "pl15Convergence": 1,\n\
      "pl15Dispersion": 1,\n\
      "pl15CameraRecoil": 1,\n\
      "pl15CameraSnap": 1,\n\
\
      "// PM pistol":"//",\n\
      "pmVerticalRecoil": 1,\n\
      "pmHorizontalRecoil": 1,\n\
      "pmConvergence": 1,\n\
      "pmDispersion": 1,\n\
      "pmCameraRecoil": 1,\n\
      "pmCameraSnap": 1,\n\
\
      "// PM (t) pistol":"//",\n\
      "pmtVerticalRecoil": 1,\n\
      "pmtHorizontalRecoil": 1,\n\
      "pmtConvergence": 1,\n\
      "pmtDispersion": 1,\n\
      "pmtCameraRecoil": 1,\n\
      "pmtCameraSnap": 1,\n\
\
      "// SR-1MP Gyurza":"//",\n\
      "sr1mpVerticalRecoil": 1,\n\
      "sr1mpHorizontalRecoil": 1,\n\
      "sr1mpConvergence": 1,\n\
      "sr1mpDispersion": 1,\n\
      "sr1mpCameraRecoil": 1,\n\
      "sr1mpCameraSnap": 1,\n\
\
      "// TT pistol":"//",\n\
      "ttVerticalRecoil": 1,\n\
      "ttHorizontalRecoil": 1,\n\
      "ttConvergence": 1,\n\
      "ttDispersion": 1,\n\
      "ttCameraRecoil": 1,\n\
      "ttCameraSnap": 1,\n\
\
      "// TT pistol (gold)":"//",\n\
      "ttgVerticalRecoil": 1,\n\
      "ttgHorizontalRecoil": 1,\n\
      "ttgConvergence": 1,\n\
      "ttgDispersion": 1,\n\
      "ttgCameraRecoil": 1,\n\
      "ttgCameraSnap": 1,\n\
\
      "// USP .45":"//",\n\
      "uspVerticalRecoil": 1,\n\
      "uspHorizontalRecoil": 1,\n\
      "uspConvergence": 1,\n\
      "uspDispersion": 1,\n\
      "uspCameraRecoil": 1,\n\
      "uspCameraSnap": 1,\n\
\
      "// CR 200DS":"//",\n\
      "cr200VerticalRecoil": 1,\n\
      "cr200HorizontalRecoil": 1,\n\
      "cr200Convergence": 1,\n\
      "cr200Dispersion": 1,\n\
      "cr200CameraRecoil": 1,\n\
      "cr200CameraSnap": 1,\n\
\
      "// CR 50DS":"//",\n\
      "cr50VerticalRecoil": 1,\n\
      "cr50HorizontalRecoil": 1,\n\
      "cr50Convergence": 1,\n\
      "cr50Dispersion": 1,\n\
      "cr50CameraRecoil": 1,\n\
      "cr50CameraSnap": 1,\n\
\
      "// RSh-12":"//",\n\
      "rsh12VerticalRecoil": 1,\n\
      "rsh12HorizontalRecoil": 1,\n\
      "rsh12Convergence": 1,\n\
      "rsh12Dispersion": 1,\n\
      "rsh12CameraRecoil": 1,\n\
      "rsh12CameraSnap": 1\n')

        exportFile.write('}')
        exportFile.close()

    


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

        # Toggle Tab
        self.globalToggle = customtkinter.CTkSwitch(
            master=self.toggleTab, text="Global Toggle", font=self.buttonFont)
        self.globalToggle.grid(padx=10, pady=10, column=0, row=0, sticky="w")
        ToolTip(self.globalToggle, msg="Toggle on if you want to set every weapon's recoil.", delay=0.5, parent_kwargs={"bg": "black", "padx": 1, "pady": 1},
        fg="#ffffff", bg="#1c1c1c", padx=10, pady=10, font=self.toolTipFont)

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




if __name__ == "__main__":

    app = App()
    app.mainloop()
