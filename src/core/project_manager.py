import requests
from pathlib import Path
import os
import datetime
import json
from utils.const import *

class ProjectManager:
    def __init__(self, ui, mainDirectory):
        super().__init__()
        self.ui = ui
        self.mainDirectory = mainDirectory
        
        self.elements = {}
        self.apiURL = "https://joelalexander.dev/RedstoneAPI/api/"
    
    def newProject(self, packDetails):
        self.packDetails = packDetails
        
        self.installVersion(packDetails["version"])

        self.saveProject()
    
    def saveProject(self):
        self.projectDirectory = self.mainDirectory / 'workspaces' / self.packDetails["namespace"]
        os.makedirs(self.projectDirectory, exist_ok=True)

        with open(self.projectDirectory / 'project.json', 'w') as file:
            data = {
                "app_version": APP_VERSION,
                "metadata": {
                    "last_edited": datetime.datetime.now(datetime.timezone.utc).isoformat()
                },
                "packDetails": self.packDetails
            }
            json.dump(data, file, indent=4)
        
        with open(self.projectDirectory / 'elements.json', 'w') as file:
            json.dump(self.elements, file, indent=4)

        os.makedirs(self.projectDirectory / 'assets', exist_ok=True)

        manifestPath = self.mainDirectory / 'workspaces' / 'manifest.json'

        # If it exists, load Manifest
        if os.path.exists(manifestPath):
            with open(manifestPath, 'r') as f:
                manifest = json.load(f)
        else:
            manifest = {"workspaces": []}
        
        # If not listed, add current workspace
        namespace = self.packDetails["namespace"]
        if namespace not in manifest["workspaces"]:
            manifest["workspaces"].append(namespace)
            with open(manifestPath, 'w') as f:
                json.dump(manifest, f, indent=4)

    def installVersion(self, version):
        pass

    def getVersions(self):
        versionsUrl = self.apiURL + "versions.json"
        response = requests.get(versionsUrl)
        response.raise_for_status()

        return response.json()

if __name__ == '__main__':
    projMan = ProjectManager("")
    versions = projMan.getVersions()
    print(versions)